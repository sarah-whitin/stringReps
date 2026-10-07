"""Standard-library support for pset2-benchmarks.ipynb; no assignment solutions."""

import csv
import hashlib
import json
import platform
import random
import statistics
import sys
import time
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1
FIELDS = [
    "schema_version", "run_id", "participant_id", "method", "workload",
    "n", "k", "pattern", "seed", "sample", "seconds", "return_type",
    "return_items", "return_shallow_bytes", "return_deep_bytes", "status", "error",
]


def deep_size(value):
    """Count reachable built-in containers and contents once per object identity.

    This estimates Python object storage, not peak working memory or serialized size.
    Intended for the assignment's dict, list, set, str, and int return types.
    """
    seen = set()
    pending = [value]
    total = 0
    while pending:
        item = pending.pop()
        if id(item) in seen:
            continue
        seen.add(id(item))
        total += sys.getsizeof(item)
        if isinstance(item, dict):
            pending.extend(item.keys())
            pending.extend(item.values())
        elif isinstance(item, (list, tuple, set, frozenset)):
            pending.extend(item)
    return total


def make_text(n, workload, seed):
    if workload == "random_dna":
        return "".join(random.Random(seed + n).choices("ACGT", k=n))
    if workload == "repeated_a":
        return "A" * n
    raise ValueError(f"Unknown workload: {workload}")


def run_benchmarks(functions, *, participant_id, sizes, repeats=3, k=3,
                   seed=258, slow_seconds=1.0, output_dir="benchmark-results",
                   source_dir="src/pset2"):
    """Save each sample immediately; skip larger cases after a slow call/error.

    slow_seconds is a soft cutoff checked AFTER a call, not a timeout.
    Input generation, output measurement, and file writes are outside timing.
    """
    expected = {"countNucleotides", "patternIndex", "patternCount", "frequentWords"}
    if set(functions) != expected:
        raise ValueError(f"Provide exactly these functions: {sorted(expected)}")
    sizes = list(sizes)
    if (not sizes or any(type(n) is not int or n < k for n in sizes)
            or sizes != sorted(set(sizes)) or type(k) is not int or k < 1
            or type(repeats) is not int or repeats < 1 or slow_seconds <= 0):
        raise ValueError("Use increasing unique integer sizes >= k, k/repeats >= 1, and a positive cutoff.")
    if not str(participant_id).strip():
        raise ValueError("Set a nonempty participant ID (a class alias is fine).")
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    csv_path = destination / f"{run_id}.csv"
    metadata_path = destination / f"{run_id}.json"
    hashes = {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(Path(source_dir).glob("*.py"))
    }
    metadata = {
        "schema_version": SCHEMA_VERSION, "run_id": run_id,
        "participant_id": str(participant_id), "created_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version, "python_implementation": platform.python_implementation(),
        "platform": platform.platform(), "machine": platform.machine(),
        "processor": platform.processor(), "timer": vars(time.get_clock_info("perf_counter")),
        "config": {"sizes": sizes, "repeats": repeats, "k": k, "seed": seed,
                   "slow_seconds": slow_seconds, "workloads": ["random_dna", "repeated_a"]},
        "source_sha256": hashes, "complete": False,
        "size_definition": "sys.getsizeof; deep size counts reachable built-in objects once by identity",
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
    rows = []
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        handle.flush()
        for workload in metadata["config"]["workloads"]:
            stopped = {}
            for n in sizes:
                text = make_text(n, workload, seed)
                pattern = "A" * k
                for name, function in functions.items():
                    base = dict.fromkeys(FIELDS, "")
                    base.update(schema_version=SCHEMA_VERSION, run_id=run_id,
                                participant_id=str(participant_id), method=name, workload=workload,
                                n=n, k=k, pattern=pattern if name in {"patternIndex", "patternCount"} else "",
                                seed=seed)
                    if name in stopped:
                        row = dict(base, status="skipped", error=stopped[name])
                        writer.writerow(row)
                        handle.flush()
                        rows.append(row)
                        continue
                    args = (text,) if name == "countNucleotides" else (text, k if name == "frequentWords" else pattern)
                    for sample in range(1, repeats + 1):
                        row = dict(base, sample=sample)
                        try:
                            start = time.perf_counter()
                            result = function(*args)
                            elapsed = time.perf_counter() - start
                            row.update(seconds=elapsed, return_type=type(result).__name__,
                                       return_items=len(result) if isinstance(result, (dict, list, tuple, set, frozenset, str)) else 1,
                                       return_shallow_bytes=sys.getsizeof(result),
                                       return_deep_bytes=deep_size(result), status="ok")
                            del result
                            if elapsed >= slow_seconds:
                                stopped[name] = f"Earlier call took {elapsed:.3f}s (soft cutoff {slow_seconds}s)."
                        except Exception as exc:
                            row.update(status="error", error=f"{type(exc).__name__}: {exc}")
                            stopped[name] = row["error"]
                        writer.writerow(row)
                        handle.flush()
                        rows.append(row)
                        if name in stopped:
                            break
                    print(f"{workload:12} n={n:>7} {name:18} {row['status']}"
                          + (f" ({row['seconds']:.6f}s)" if row["status"] == "ok" else f": {row['error']}"))
    metadata["complete"] = True
    metadata["successful_samples"] = sum(row["status"] == "ok" for row in rows)
    metadata["error_samples"] = sum(row["status"] == "error" for row in rows)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
    return rows, csv_path, metadata_path


def load_results(directory):
    """Load flat or nested class submissions, validating schema and run identity.

    Duplicate copies of a run are ignored, so rerunning the loader is safe.
    """
    rows, seen_runs = [], set()
    for path in sorted(Path(directory).rglob("*.csv")):
        with path.open(newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != FIELDS:
                raise ValueError(f"{path}: expected the benchmark CSV column schema")
            batch = list(reader)
        if not batch:
            continue
        run_ids = {row["run_id"] for row in batch}
        if len(run_ids) != 1:
            raise ValueError(f"{path}: expected one run per CSV")
        run_id = next(iter(run_ids))
        if run_id in seen_runs:
            continue
        for row in batch:
            if int(row["schema_version"]) != SCHEMA_VERSION:
                raise ValueError(f"{path}: unsupported schema version")
            for field in ["n", "k", "seed"]:
                row[field] = int(row[field])
            if row["status"] == "ok":
                row["seconds"] = float(row["seconds"])
                for field in ["sample", "return_items", "return_shallow_bytes", "return_deep_bytes"]:
                    row[field] = int(row[field])
        rows.extend(batch)
        seen_runs.add(run_id)
    return rows


def summarize(rows):
    groups = defaultdict(list)
    for row in rows:
        if row["status"] == "ok":
            key = tuple(row[field] for field in ["participant_id", "run_id", "method", "workload", "n", "k", "pattern", "seed"])
            groups[key].append(row)
    output = []
    for key, samples in sorted(groups.items()):
        item = dict(zip(["participant_id", "run_id", "method", "workload", "n", "k", "pattern", "seed"], key))
        item.update(samples=len(samples),
                    median_seconds=statistics.median(float(s["seconds"]) for s in samples),
                    min_seconds=min(float(s["seconds"]) for s in samples),
                    max_seconds=max(float(s["seconds"]) for s in samples),
                    median_return_items=statistics.median(int(s["return_items"]) for s in samples),
                    median_return_deep_bytes=statistics.median(int(s["return_deep_bytes"]) for s in samples))
        output.append(item)
    return output


def write_summary(rows, path):
    summary = summarize(rows)
    if not summary:
        print("No successful samples to summarize. Implement the functions and rerun.")
        return summary
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary[0]))
        writer.writeheader()
        writer.writerows(summary)
    print(f"Saved {len(summary)} summary rows to {path}")
    return summary


def plot_results(rows, title="Benchmark results"):
    """One figure per workload/config; keep independent runs as separate lines."""
    import matplotlib.pyplot as plt

    summary = summarize(rows)
    if not summary:
        print("No successful samples to plot.")
        return
    configs = sorted({(r["workload"], r["k"], r["seed"]) for r in summary})
    methods = ["countNucleotides", "patternIndex", "patternCount", "frequentWords"]
    for workload, k, seed in configs:
        fig, axes = plt.subplots(3, 4, figsize=(18, 11), squeeze=False)
        for column, method in enumerate(methods):
            groups = defaultdict(list)
            for row in summary:
                if (row["workload"], row["k"], row["seed"], row["method"]) == (workload, k, seed, method):
                    groups[(row["participant_id"], row["run_id"])].append(row)
            for (participant, run_id), points in sorted(groups.items()):
                points.sort(key=lambda r: r["n"])
                for index, metric in enumerate(["median_seconds", "median_return_deep_bytes", "median_return_items"]):
                    axes[index, column].plot([r["n"] for r in points], [r[metric] for r in points],
                                             marker="o", label=f"{participant} / {run_id[-8:]}")
            axes[0, column].set_title(method)
            for index, ylabel in enumerate(["Median runtime (seconds)", "Returned object (deep bytes)", "Returned items (scalar = 1)"]):
                ax = axes[index, column]
                ax.set_xscale("log")
                if index < 2:
                    ax.set_yscale("log")
                ax.set_xlabel("Input length n")
                ax.set_ylabel(ylabel)
                ax.grid(True, alpha=0.3)
            if groups:
                axes[0, column].legend(fontsize=7)
        fig.suptitle(f"{title}: {workload}, k={k}, seed={seed}")
        fig.tight_layout()
        plt.show()

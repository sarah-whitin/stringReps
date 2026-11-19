# Problem Set 5

Complete the five stubs in `src/pset5/`. Keep the function signatures and
package exports as provided. See the linked Rosalind pages for each problem.

| Problem | Function | File |
| --- | --- | --- |
| [BA3A: String Composition](https://rosalind.info/problems/ba3a/) | `stringComposition(k, text)` | `src/pset5/string_composition.py` |
| [BA3B: String Spelled by a Genome Path](https://rosalind.info/problems/ba3b/) | `stringSpelledByGenomePath(patterns)` | `src/pset5/genome_path.py` |
| [BA3C: Overlap Graph](https://rosalind.info/problems/ba3c/) | `overlapGraph(patterns)` | `src/pset5/overlap_graph.py` |
| [BA3D: De Bruijn Graph from a String](https://rosalind.info/problems/ba3d/) | `deBruijnFromString(k, text)` | `src/pset5/de_bruijn_from_string.py` |
| [BA3E: De Bruijn Graph from k-mers](https://rosalind.info/problems/ba3e/) | `deBruijnFromKmers(patterns)` | `src/pset5/de_bruijn_from_kmers.py` |

Pass `patterns` as a list of strings (in path order for BA3B). Return a list
of k-mers for BA3A, a string for BA3B, and a two-column adjacency list
(`list[list[str]]`) for BA3C–BA3E. Each row is one directed edge
`[source, destination]`; for example, `[["TCT", "CTA"], ["TCT", "CTC"]]`.
Rows may appear in any order. Preserve repeated k-mers in BA3A and repeated
edge rows in BA3D–BA3E.
Return values rather than printing them.

## Setup

With your Python 3.10+ environment activated, run from the repository root:

```sh
python -m pip install -e ./pset-5
```

In a notebook, use `%pip install -e ./pset-5` and restart the kernel.
Then import the functions you need, for example:

```python
from pset5 import stringComposition, overlapGraph
```

# Problem Set 3

This assignment lives in `pset-3/` within your existing `stringReps`
repository, alongside `pset-1/` and `pset-2/`. Use the same repository for
your work; you do not need to create a separate repository.

Implement the four functions below in the assigned order. Each starter function
contains a TODO and raises `NotImplementedError` until you implement it.
Keep the function signatures and package exports as provided.

| Order | Function | File | Rosalind problem |
| --- | --- | --- | --- |
| 1 | `frequencyArray(text, k)` | `src/pset3/frequency_array.py` | [BA1K: Frequency Array](https://rosalind.info/problems/ba1k/) |
| 2 | `transcribeRNA(text)` | `src/pset3/transcribe_rna.py` | [RNA: Transcription](https://rosalind.info/problems/rna/) |
| 3 | `reverseComplement(text)` | `src/pset3/reverse_complement.py` | [BA1C: Reverse Complement](https://rosalind.info/problems/ba1c/) |
| 4 | `findClumps(genome, k, L, t)` | `src/pset3/find_clumps.py` | [BA1E: Clump Finding](https://rosalind.info/problems/ba1e/) |

BA1K extends the k-mer counting from pset-2. RNA and BA1C practice string
transformations, and BA1E combines k-mer counting with windows along a genome.
Refer to the linked pages for the full problem statements.

## Setup

Use Python 3.10 or newer. From the repository root, create and activate a
virtual environment if you do not already have one:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ./pset-3
```

On subsequent visits, activate the environment with `source .venv/bin/activate`.
This package does not require the earlier assignments.

In a notebook opened at the repository root, install with:

```python
%pip install -e ./pset-3
```

Restart the kernel after installation. Import the functions using the package
name `pset3`, rather than running individual source files:

```python
from pset3 import frequencyArray, transcribeRNA, reverseComplement, findClumps
```

## Sample calls and expected results

These calls use the samples from the linked Rosalind pages. They will raise
`NotImplementedError` until you complete the corresponding functions.

```python
frequencyArray("ACGCGGCTCTGAAA", 2)
# Expected: [2, 1, 0, 0, 0, 0, 2, 2, 1, 2, 1, 0, 0, 1, 1, 0]

transcribeRNA("GATGGAACTTGACTACGTAAATT")
# Expected: "GAUGGAACUUGACUACGUAAAUU"

reverseComplement("AAAACCCGGT")
# Expected: "ACCGGGTTTT"

genome = (
    "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGAC"
    "ATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
)
findClumps(genome, 5, 75, 4)
# Expected: {"CGACA", "GAAGA", "AATGT"} (set order may vary)
```

Return Python values from your functions; do not print inside them. For a
Rosalind submission, format the returned value as text:

```python
print(" ".join(map(str, frequencyArray("ACGCGGCTCTGAAA", 2))))
print(transcribeRNA("GATGGAACTTGACTACGTAAATT"))
print(reverseComplement("AAAACCCGGT"))
print(" ".join(sorted(findClumps(genome, 5, 75, 4))))
```

Frequency arrays include all k-mers, including those with count zero, in
lexicographic order using A, C, G, T. Clump results contain distinct k-mers;
their output order is arbitrary. Both counting problems include overlapping
occurrences.

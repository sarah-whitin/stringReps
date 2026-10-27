"""Rosalind BA1K: Generate the Frequency Array of a String."""


def frequencyArray(text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).

    I don't think this is the most efficient way to do it but it will work.
    """
    # find possible kmers, a list with 4^k elements
    seqs = ["A", "C", "G", "T"]

    for i in range(k):
        print(f"spot = {i}")
        for j in range(seqs.__len__()):
            print(f"seq index = {j}")
            print(f"seq to update is: {seqs[j]}")
            for nuc in ["A", "C", "G", "T"]: 
                print(seqs[j] + nuc)
        # seqs = newList
            # for base in ["A", "C", "G", "T"]:
            #     seqs = seqs[j] + base
            
        print()

    # count for each kmer & update frequency table


print(frequencyArray("ACGCGGCTCTGAAA", 2))
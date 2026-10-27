"""Rosalind BA1K: Generate the Frequency Array of a String."""


def frequencyArray(text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).

    I don't think this is the most efficient way to do it but it will work.

    Calls pattern_count, 
    another function in this .py script, 
    because I did not know how to have it referencing the right func in github as well as locally
    """
    # find possible kmers, a list with 4^k elements

    # starting list of k-mers to add to (k-mer of  1)
    seqs = ["A", "C", "G", "T"]
    for i in range(k-1): # for each nucleotide spot in k (k-1 because of our initialization of seqs)
        tempList = [] 
        for j in range(seqs.__len__()): # for each k-mer built so far
            for nuc in ["A", "C", "G", "T"]: # add a nucleotide
                tempList.append(seqs[j] + nuc)
        seqs = tempList.copy()
        tempList = []
    print(seqs)

    freqArray = [] # to be list of ints that correspond by index to our possible k-mers
    for seq in seqs:
        freqArray.append(patternCount(text, seq)) # call previosuly defined pattern count

    return freqArray

def patternCount(text: str, pattern: str) -> int:
    """Return the number of occurrences of pattern in text.

    Matches are case-sensitive and may overlap. Assume pattern is nonempty.
    Return 0 if pattern is longer than text or text is empty.

    Example:
        PatternCount("AAAA", "AA") returns 3.
    """

    count = 0
    for i in range(0, text.__len__()):
        if pattern == text[i:i+pattern.__len__()]:
            count += 1
    return count

# print(frequencyArray("ACGCGGCTCTGAAA", 2))
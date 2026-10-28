"""Rosalind BA1E: Find Patterns Forming Clumps in a String."""


def findClumps(genome: str, k: int, L: int, t: int) -> set[str]:
    """Return distinct k-mers appearing at least t times in any length-L window.

    Count overlapping occurrences fully contained within each window.
    Assume uppercase DNA, 1 <= k <= L <= len(genome), and t >= 1.
    Each qualifying k-mer appears only once in the returned set.

    Not very space efficent - essentially combining frequent_words and pattern_count
    Could also call combo of find_clumbs and frequent_words
    """

    kmerCounts = dict() # initialize dict to store all kmer and their appreance
    for i in range(L-k):
        kmer = genome[i:i+k] # find kmer at each position 
        if kmer in kmerCounts.keys():
            # update kmer count
            kmerCounts.update({kmer: kmerCounts.get(kmer)+1})
        else: 
            # add kmer to dict
            kmerCounts.update({kmer: 1})

    kmersOfT = [] # initalize list of kmers that will be of length t
    for seq in kmerCounts.keys():
        if kmerCounts.get(seq) >= t: # if kmer val is greater than or eqal to t
            kmersOfT.append(seq) # add to list

    return kmersOfT

genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
print(findClumps(genome, 5, 100, 4)) # updated from 75 to 100
            

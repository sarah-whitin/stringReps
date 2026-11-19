def stringSpelledByGenomePath(patterns: list[str]) -> str:
    """Return the string spelled by the ordered genome path (BA3B)."""
    genome = patterns[0] # start genome with full first k-mer
    size = patterns[0].count("") #g4g

    for i in range(patterns.__len__()-1):
        genome = genome + patterns[1+i][size-2:size-1] # add in next nuc one at a time

    return genome

if __name__ == "__main__":
    patterns = ["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]
    print(stringSpelledByGenomePath(patterns))


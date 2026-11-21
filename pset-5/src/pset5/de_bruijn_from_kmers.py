def deBruijnFromKmers(patterns: list[str]) -> list[list[str]]:
    """Return the de Bruijn graph of the k-mers as rows [source, destination] (BA3E).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """

    nodesAndEdges = []
    k = patterns[0].count("")

    # for each kmer
    for kmer in patterns:
        firstK = kmer[0:k-2]# find first 3
        lastK = kmer[1:k]# find last 3
        # we arent checking if firstK already in list because instructiosn above say to preserve duplicates
        nodesAndEdges.append([firstK, lastK])# add to list

    return nodesAndEdges

if __name__ == "__main__":
    patterns = "GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"
    print(deBruijnFromKmers(patterns))
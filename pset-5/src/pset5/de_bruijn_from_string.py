from string_composition import stringComposition

def deBruijnFromString(k: int, text: str) -> list[list[str]]:
    """Return the de Bruijn graph of text as rows [source, destination] (BA3D).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    kmers = stringComposition(k, text)
    # initialize list
    nodesAndEdges = []
    # for each kmer
    for kmer in kmers:
        firstK = kmer[0:k-1]# find first 3
        lastK = kmer[1:k]# find last 3
        # we arent checking if firstK already in list because instructiosn above say to preserve duplicates
        nodesAndEdges.append([firstK, lastK])# add to list

    return nodesAndEdges


if __name__ == "__main__":
    k = 4
    text = "AAGATTCTCTAC"
    print(deBruijnFromString(k, text))
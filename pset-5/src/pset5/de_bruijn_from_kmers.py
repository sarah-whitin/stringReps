def deBruijnFromKmers(patterns: list[str]) -> list[list[str]]:
    """Return the de Bruijn graph of the k-mers as rows [source, destination] (BA3E).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    # initialize list
    nodesAndEdges = []

    # intialize length k
    k = patterns[0].count("")-1

    # for each k-mer, find what matches the list k-1 
    for i in range(patterns.__len__()):
        matches = [patterns[i]] # intialize list
        for j in range(patterns.__len__()):# for each possible match
            if i != j:
                query = patterns[i][1:k]
                answer = patterns[j][0:k-1]
                if query == answer:
                    matches.append(patterns[j])# add to list if there is a match
                    nodesAndEdges.append(matches)# add list to list of list
                    matches = [patterns[i]]#reset list
    return(nodesAndEdges)

if __name__ == "__main__":
    patterns = ["ATGCG", "GCATG", "GCATC", "CATGC", "AGGCA", "GGCAT"]
    print(deBruijnFromKmers(patterns))

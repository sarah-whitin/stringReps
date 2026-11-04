from hamming_distance import hammingDistance

def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
    # find all possible k-mers available
    
    posKmers = 4**k # find how many k-mers possible
    allKmers = []
    for i in range(posKmers):
        allKmers.append("") # list of size of possible kmers which is 4^k

    for i in range(1, k+1): # this is a ridiculous way to do this
        posKmers = posKmers/4 # size of increments we want to add of one letter at a time
        last = 1
        times2Add = 4**(i-1) # how many times we want to go through this increment
        for l in range(0,times2Add):
            for allele in ["A", "G", "C", "T"]:
                groupMax = last + posKmers # last sequence to add letter to
                for j in range(int(last), int(groupMax)):
                    oldString = allKmers[j-1]
                    allKmers[j-1] = oldString + allele
                    last = groupMax # last sequence letter has been added to
    
    counts = dict()
    for kmer in allKmers:
        count = 0
        for i in range(text.__len__()-kmer.__len__()+1): 
            if hammingDistance(kmer, text[i:i+kmer.__len__()]) <= d: # check every pattern length sentence in text
                # add if have at least d mismatches
                count += 1
        counts.update({kmer: count})
        count = 0
    
    counts = {key: v for key, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)} # from geeks 4 geeks
    lowestKmers = set()
    # while value is the lowest
    if len(list(counts.keys())) > 0: # if there is something in our dict
        firstkmer = list(counts.keys())[0]
        for kmer in counts.keys():
            if counts.get(kmer) == counts.get(firstkmer):
                lowestKmers.add(kmer) # add k to set
    else: 
        return lowestKmers
    
    return lowestKmers
    
    

if __name__ == "__main__":
    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT" 
    k = 4
    d = 1
    print(frequentWordsWithMismatches(text, k, d))


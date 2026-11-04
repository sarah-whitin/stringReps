def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
    # find all possible k-mers available
    
    posKmers = k**4 # find how many k-mers possible
    allKmers = []
    for i in range(posKmers):
        allKmers.append("")

    for i in range(1, k+1):
        print(i)
        posKmers = posKmers/4
        last = 1
        times2Add = i**(i-1)
        for k in range(0,times2Add):
            print(times2Add)
            for allele in ["A", "G", "C", "T"]:
                groupMax = last + posKmers
                for j in range(int(last), int(groupMax)):
                    print(f"add {allele} at {j}")
                    last = groupMax
        
                
            

if __name__ == "__main__":
    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT" 
    k = 4
    d = 1
    frequentWordsWithMismatches(text, k, d)


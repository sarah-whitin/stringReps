from hamming_distance import hammingDistance

def approximatePatternMatching(pattern: str, text: str, d: int) -> list[int]:

    positions = []
    
    for i in range(text.__len__()-pattern.__len__()+1): 
        if hammingDistance(pattern, text[i:i+pattern.__len__()]) <= d: # check every pattern length sentence in text
            positions.append(i) # add if have at least d mismatches

    return positions

if __name__ == "__main__":
    pattern = "ATTCTGGA"
    text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
    mismatches = 3
    print(approximatePatternMatching(pattern, text, mismatches))


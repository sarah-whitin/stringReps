def hammingDistance(p: str, q: str) -> int:
   # only works for strings of the same length
    count = 0

    for i in range(p.__len__()): # for every allele
        if p[i] == q[i]: # see if they match
            pass
        else:
            count += 1 # increment count if they don't

    return count

text1 = "GGGCCGTTGGT"
text2 = "GGACCGTTGAC"
print(hammingDistance(text1, text2))
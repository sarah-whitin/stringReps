"""Rosalind BA1C: Find the Reverse Complement of a String."""

def reverseComplement(text: str) -> str:
    """Return the reverse complement of an uppercase DNA string.

    A pairs with T, and C pairs with G. Return the complementary
    nucleotides in reverse order. 

    Will not work if chars W and Z are present. 
    """

    toReplace = ["A", "T", "C", "G"]
    replacement = ["W", "A", "Z", "C"]
    toReplace2 = ["W", "Z"]  # to avoid replacing a nucleotide twice 
    replacement2 = ["T", "G"]

    for i in range(4): # for each nucleotide, replace with unique char
        text = text.replace(toReplace[i], replacement[i]) # makes a new sting everytime, four total new strings
    for i in range(2): # replace W and Z with final replacemenets from original A and Cs
        text = text.replace(toReplace2[i], replacement2[i])
    
    revComp = text[::-1] # reverse the strand

    return revComp

# print(reverseComplement("ATCG"))
"""Rosalind BA1C: Find the Reverse Complement of a String."""

def reverseComplement(text: str) -> str:
    """Return the reverse complement of an uppercase DNA string.

    A pairs with T, and C pairs with G. Return the complementary
    nucleotides in reverse order.
    """

    toReplace = ["A", "T", "C", "G"]
    replacement = ["T", "A", "G", "C"]

    for i in range(4):
        text = text.replace(toReplace[i], replacement[i])
    # does not work because it replaces nucleotides twice
    
    revComp = text[::-1]

    return revComp

print(reverseComplement("ATCG"))
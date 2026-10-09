"""Rosalind BA1C: Find the Reverse Complement of a String."""

def reverseComplement(text: str) -> str:
    """Return the reverse complement of an uppercase DNA string.

    A pairs with T, and C pairs with G. Return the complementary
    nucleotides in reverse order.
    """
    revComp = ""

    for x in reversed(text):
        if x == "A":
            revComp = revComp + "T"
        elif x == "T":
            revComp = revComp + "A"
        elif x == "C":
            revComp = revComp + "G"
        elif x == "G":
            revComp = revComp + "C"
    
    return revComp

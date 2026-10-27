"""Rosalind RNA: Transcribing DNA into RNA."""


def transcribeRNA(text: str) -> str:
    """Return the RNA string corresponding to an uppercase DNA coding strand.

    Replace each T with U, retaining the order of the other nucleotides.
    """
    return(text.replace("T", "U")) #idk if this is cheating, but just know that i know that a string is immutable

print(transcribeRNA("GATGGAACTTGACTACGTAAATT"))

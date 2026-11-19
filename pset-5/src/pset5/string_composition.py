def stringComposition(k: int, text: str) -> list[str]:
    """Return the k-mer composition of text, including repeated k-mers (BA3A).
    Generate the k-mer composition of a string.

    Given: An integer k and a string Text.
    Return: Compositionk(Text) (the k-mers can be provided in any order).   
    """
    comp = set()

    for i in range(0, text.__len__()-k+1):
        word = text[i:i+k]
        comp.add(word)

    return comp # does not return in alphabtical order because feels like an extra step (for now)

if __name__ == "__main__":
    text = "CAATCCAAC"
    k = 5
    print(stringComposition(k, text))
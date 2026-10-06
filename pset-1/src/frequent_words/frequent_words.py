"""Find the most frequent words of a given length in text."""

from pattern_count import PatternCount


def FrequentWords(text: str, k: int) -> set[str]:
    """Return all length-k substrings with the highest occurrence count.

    Count overlapping, case-sensitive matches and include every tie once.
    Assume k is a positive integer. Return an empty set if k exceeds the
    length of text or text is empty.

    Example:
        FrequentWords("ATAT", 2) returns {"AT"}.
        FrequentWords("ATGC", 2) returns {"AT", "TG", "GC"}.

    PatternCount is already imported above. You can call
    PatternCount(text, pattern) directly in your implementation.
    """
    frequentPatterns = set()
    count = dict()

    for i in range(0, text.__len__()-k+1):
        pattern = text[i:i+k]
        if pattern not in count.keys(): # if pattern is not in dictionary:
            # add pattern and it's count
            count.update({pattern: PatternCount(text, pattern)})
    
    # find top int in count
    maxVal = sorted(count.values(), reverse=True)[0]

    # add all patterns with top count to frequentPatterns
    for i in count.keys():
        if maxVal == count.get(i):
            frequentPatterns.add(i)

    return frequentPatterns


def main():

    # rosalins q
    print(FrequentWords("TTGAATAGGTTTGAATAGGTTGCCCACTTAGAACTCCGGAGACTATTCAAGGATCGAAGGATCGAAGGATCGGAGACTATTCAAGGATCGAGAACTCCGGAGACTATTCGAGACTATTCGAGACTATTCAAGGATCGTTGAATAGGTTGCCCACTTAAGGATCGGAGACTATTCAGAACTCCGTTGAATAGGTTGCCCACTTAGAACTCCGGAGACTATTCAGAACTCCGAAGGATCGTTGAATAGGTAAGGATCGAGAACTCCGTTGAATAGGTAAGGATCGTGCCCACTTGAGACTATTCAAGGATCGTTGAATAGGTAGAACTCCGAGAACTCCGTGCCCACTTAAGGATCGAAGGATCGAAGGATCGGAGACTATTCTGCCCACTTTGCCCACTTTTGAATAGGTAGAACTCCGAGAACTCCGTGCCCACTTAGAACTCCGGAGACTATTCAAGGATCGAAGGATCGTGCCCACTTTGCCCACTTAGAACTCCGTTGAATAGGTTTGAATAGGTTGCCCACTTAGAACTCCGAGAACTCCGAGAACTCCGAAGGATCGTGCCCACTTAGAACTCCGTGCCCACTTGAGACTATTCTGCCCACTTTGCCCACTTTTGAATAGGTAAGGATCGAAGGATCGGAGACTATTCAAGGATCGGAGACTATTCTGCCCACTTAGAACTCCGAAGGATCGAAGGATCGTTGAATAGGTAGAACTCCGAAGGATCGGAGACTATTCAAGGATCGAGAACTCCGTTGAATAGGTTTGAATAGGTAAGGATCGGAGACTATTCAGAACTCCGGAGACTATTCGAGACTATTCAAGGATCGTGCCCACTTAAGGATCGAGAACTCCGTTGAATAGGTTGCCCACTTTTGAATAGGTAAGGATCGTGCCCACTTTGCCCACTTAGAACTCCG", 13))
if __name__ == "__main__":
    main()
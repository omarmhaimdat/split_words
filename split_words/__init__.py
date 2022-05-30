"""
Split a text into words.
"""
import os
from math import log

def get_cost_dict(file_path: str) -> dict:
    """
    Builds a cost dictionary for a given corpus.

    Assuming Zipf's law and cost = -math.log(probability).

    :param file_path: Path to the corpus.
    :return: A dictionary where each key is a word and each value is the cost
    of that word.
    """
    with open(file_path, mode="r", encoding="utf8") as f:
        words = f.read().split()
        wordcost = dict((k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))
        maxword = max(len(x) for x in words)
    return wordcost, maxword


wordcost, maxword = get_cost_dict(os.path.join(os.path.dirname(__file__), "corpus.txt"))



def split(text: str) -> str:
    """
    Uses dynamic programming to infer the location of spaces in a string
    without spaces.
    """

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i - maxword) : i]))
        return min(
            (c + wordcost.get(text[i - k - 1 : i], 9e999), k + 1) for k, c in candidates
        )

    # Build the cost array.
    cost = [0]
    for i in range(1, len(text) + 1):
        c, k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    text_length = len(text)
    while text_length > 0:
        c, k = best_match(text_length)
        assert c == cost[text_length]
        out.append(text[text_length - k : text_length])
        text_length -= k

    return " ".join(reversed(out))

print(split("helloworld"))

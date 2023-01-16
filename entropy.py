import collections
from math import log

def create_dict(content):
    """
    content is in bytes
    Creates a dictionnary containing the following associations:
        (integer [ranged between 0 and 255]: frequency in content)
    """
    a = collections.Counter(content)
    total = a.total()
    for k in a.keys():
        a[k] /= total
    return dict(a)


def entropy(probabilities):
    """
    probabilities is a dictionnary where values are the frequency of the
    associated key

    Compute Shannon entropy
    """
    H = 0
    for k in probabilities.keys():
        H += -probabilities[k] * log(probabilities[k])
    return H

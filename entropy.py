from math import log

# collection.counter does exactly that
def create_dict(content):
    """
    content is in bytes
    Creates a dictionnary containing the following associations:
        (integer [ranged between 0 and 255]: frequency in content)
    """
    a = {}
    total = 0
    for elt in content:
        total += 1
        if elt in a.keys():
            a[elt] += 1
        else:
            a[elt] = 1

    for k in a.keys():
        a[k] /= total
    return a


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

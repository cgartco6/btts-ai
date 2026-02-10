from rapidfuzz import fuzz

def fuzzy_find(elements, keyword):
    scored = [(el, fuzz.partial_ratio(el.text, keyword)) for el in elements]
    return max(scored, key=lambda x: x[1])[0]

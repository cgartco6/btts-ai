import numpy as np

def confidence_interval(probs):
    mean = probs.mean()
    std = probs.std()
    return mean, (mean - std, mean + std)

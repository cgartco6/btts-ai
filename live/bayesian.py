def bayesian_update(prior, likelihood):
    posterior = prior * likelihood
    return posterior / (posterior + (1 - prior))

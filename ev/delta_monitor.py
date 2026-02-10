def ev_delta(old_ev, new_ev, threshold=0.05):
    return abs(new_ev - old_ev) >= threshold

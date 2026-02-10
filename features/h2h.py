def h2h_btts(h2h_results):
    if not h2h_results:
        return 0.5
    return sum(h2h_results) / len(h2h_results)

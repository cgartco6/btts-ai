import hashlib

# Stable numeric encoding for cross-league learning
def encode_league(league_name):
    h = hashlib.md5(league_name.encode()).hexdigest()
    return int(h[:6], 16) / 10**6

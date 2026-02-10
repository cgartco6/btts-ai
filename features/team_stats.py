import numpy as np

def team_features(results):
    arr = np.array(results)
    return {
        "avg_scored": arr[:,0].mean(),
        "avg_conceded": arr[:,1].mean(),
        "btts_rate": arr[:,2].mean()
    }

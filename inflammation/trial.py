import numpy as np


class Patient:
    def __init__(self, id, inflammation_scores:list):
        self.id = id
        self.inflammation_scores = inflammation_scores
    def data_mean(self):
        return np.mean(self.inflammation_scores)
    def data_max(self):
        return np.max(self.inflammation_scores)
    def data_min(self):
        return np.min(self.inflammation_scores)

class Trial:
    def __init__(self, id, data:np.array):
        pass
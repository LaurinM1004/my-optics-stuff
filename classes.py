import numpy as np

class Ray:
    def __init__(self, origin, direction):
        self.origin = np.array(origin, dtype=float)
        self.direction = np.array(direction, dtype=float) / np.linalg.norm(direction)
        self.path = [self.origin.copy()]

    def propagate(self, distance):
        self.origin += self.direction * distance
        self.path.append(self.origin.copy())
    

class Lens:
    def __init__(self, origin, R1, R2, thickness, n_lens):
        self.origin = np.array(origin, dtype=float)
        self.R1 = R1
        self.R2 = R2
        self.thickness = thickness
        self.n_lens = n_lens
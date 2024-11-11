class Vector:
    def __init__(self, dimensions):
        self._coords = [0] * dimensions

    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        return self._coords[j]
    
    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors are not of the same dimension")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self._coords == other._coords
    
    def __str__(self):
        return f"<{str(self._coords)[1:-1]}>"
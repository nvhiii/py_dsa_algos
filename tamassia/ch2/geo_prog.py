from progression import Progression

class GeometricProgression(Progression):
    def __init__(self, base, start=1):
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        self._current *= self._base

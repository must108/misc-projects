
class FeatureFlag:
    def __init__(self):
        self.flags = {}

    def create(self, key, val) -> bool:
        if key not in self.flags:
            self.flags[key] = val
            return True
        else:
            return False
        
    def fetch(self, key) -> bool | None:
        if key in self.flags:
            return self.flags[key]
        else:
            return None
    
    def update(self, key) -> bool:
        if key in self.flags:
            self.flags[key] = not self.flags[key]
            return True
        else:
            return False



class KV:
    def __init__(self, window, k):
        self.h = {}
        self.time = 0
        self.window = k
        self.max = k
        self.cur = 0

    def tick(self):
        self.time += 1

    def put(self, key, value):
        self.h[key] = value
        return True
    
    def get(self, key):
        if key in self.h:
            return self.h[key]
        else:
            return None
        
    def delete(self, key):
        if key in self.h:
            del self.h[key]
            return True
        else:
            return False
from collections import deque

class JobQueue:
    def __init__(self):
        self.queue = deque()
        self.id = 0

    def submit(self, job):
        id = self.id
        self.queue.append((id, job))
        self.id += 1
        return id

    def fetch(self):
        if self.queue:
            return self.queue.popleft()

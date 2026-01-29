class LPCMemory:
    def __init__(self):
        self.history = []

    def record(self, state, action):
        self.history.append((state, action))

    def last_state(self):
        return self.history[-1] if self.history else None

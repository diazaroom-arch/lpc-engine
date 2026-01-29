from lpc.config import WORLD_STATES

class LPCWorld:
    def __init__(self):
        self.state = "STABLE"

    def update(self, avg_energy):
        for state, threshold in WORLD_STATES.items():
            if avg_energy >= threshold:
                self.state = state
                return


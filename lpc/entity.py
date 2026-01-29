import uuid
from lpc.config import ACTION_COST, INIT_ENERGY, MAX_WEAR

class LPCEntity:
    def __init__(self, traits, memory):
        self.id = str(uuid.uuid4())[:4]
        self.energy = INIT_ENERGY
        self.wear = 0
        self.age = 0
        self.traits = traits
        self.memory = memory
        self.alive = True
        self.last_action = None

    def act(self, action, pressure):
        cost = ACTION_COST[action]
        self.energy += cost["energy"] + pressure
        self.wear += cost["wear"]
        self.last_action = action
        self.age += 1

        if self.energy <= 0 or self.wear >= MAX_WEAR:
            self.alive = False

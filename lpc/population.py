from lpc_entity import LPCEntity
from lpc_traits import generate_traits
from lpc_memory import LPCMemory
from config import REPRODUCTION_THRESHOLD, REPRODUCTION_COST

class LPCPopulation:
    def __init__(self, size):
        self.entities = [
            LPCEntity(generate_traits(), LPCMemory())
            for _ in range(size)
        ]

    def living(self):
        return [e for e in self.entities if e.alive]

    def reproduce(self):
        newborns = []
        for e in self.living():
            if e.energy >= REPRODUCTION_THRESHOLD and e.traits["fertility"] > 0.7:
                e.energy -= REPRODUCTION_COST
                newborns.append(
                    LPCEntity(generate_traits(), LPCMemory())
                )
        self.entities.extend(newborns)

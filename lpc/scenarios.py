from config import SCENARIO_PRESSURE

def pressure(world_state, cycle):
    base = SCENARIO_PRESSURE[world_state]

    if cycle > 40:
        base -= 2
    if cycle > 80:
        base -= 3

    return base


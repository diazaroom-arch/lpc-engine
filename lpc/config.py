INIT_ENERGY = 70
MAX_WEAR = 100

ACTION_COST = {
    "REST": {"energy": +8, "wear": +1},
    "EXPLORE": {"energy": +2, "wear": +4},
    "EXERT": {"energy": -4, "wear": +8},
}

REPRODUCTION_THRESHOLD = 85
REPRODUCTION_COST = 20

WORLD_STATES = {
    "GROWTH": 90,
    "STABLE": 65,
    "CRISIS": 40,
    "COLLAPSE": 0
}

SCENARIO_PRESSURE = {
    "GROWTH": 0,
    "STABLE": -1,
    "CRISIS": -4,
    "COLLAPSE": -8
}

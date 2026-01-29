import random

def decide_action(entity, world_state):
    e, w = entity.energy, entity.wear

    if e < 30 or w > 80:
        return "REST"

    if world_state == "CRISIS":
        return "EXPLORE" if random.random() < entity.traits["curiosity"] else "REST"

    if world_state == "COLLAPSE":
        return "REST"

    if random.random() < entity.traits["risk"]:
        return "EXERT"

    return "EXPLORE"

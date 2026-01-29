import random

def generate_traits():
    return {
        "risk": random.uniform(0.1, 1.0),
        "resilience": random.uniform(0.5, 1.2),
        "curiosity": random.uniform(0.3, 1.0),
        "fertility": random.random()
    }

def compute(population):
    alive = population.living()
    if not alive:
        return {"alive": 0, "avg_energy": 0}

    avg_energy = sum(e.energy for e in alive) / len(alive)
    return {"alive": len(alive), "avg_energy": round(avg_energy, 2)}


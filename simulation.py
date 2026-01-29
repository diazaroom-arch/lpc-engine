# simulation.py
from lpc_decision import decide_action
from lpc_metrics import compute
from lpc_scenarios import pressure


class LPCSimulation:
    def __init__(self, population, world, max_cycles=24):
        self.population = population
        self.world = world
        self.max_cycles = max_cycles
        self.snapshots = []  # historial CORE (neutro)
        self.world_history = {}

    def run(self, visualizer=None):
        for cycle in range(1, self.max_cycles + 1):

            metrics = compute(self.population)
            self.world.update(metrics["avg_energy"])
            p = pressure(self.world.state, cycle)

            self.world_history[cycle] = self.world.state

            print(f"\n🔁 CICLO {cycle} | WORLD: {self.world.state}")

            cycle_snapshots = []

            for e in self.population.living():
                action = decide_action(e, self.world.state)
                e.act(action, p)

                print(
                    f"Entity-{e.id} | Act:{action} | "
                    f"E:{round(e.energy,1)} | W:{round(e.wear,1)}"
                )

                snapshot = {
                    "id": e.id,
                    "age": e.age,
                    "energy": round(e.energy, 2),
                    "wear": round(e.wear, 2),
                    "action": action,
                    "alive": e.alive,
                    "cycle": cycle
                }

                self.snapshots.append(snapshot)
                cycle_snapshots.append(snapshot)

            self.population.reproduce()

            print("📊 METRICS", metrics)

            # 🔹 VISUALIZACIÓN BULCS POR CICLO
            if visualizer:
                visualizer.render_cycle(cycle, cycle_snapshots, self.world.state)

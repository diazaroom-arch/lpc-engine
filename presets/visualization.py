from presets.presets import PRESETS

class LPCVisualizer:
    def __init__(self, preset_name="CORE"):
        if preset_name not in PRESETS:
            raise ValueError(f"Preset '{preset_name}' no existe")

        self.preset = PRESETS[preset_name]

    def render_cycle(self, cycle, snapshots, world_state):
        metrics = self.preset["metrics"]
        actions = self.preset["actions"]

        print(f"\n🔁 VISUALIZACIÓN BUSINESS UNIT LIFE CYCLE (ciclo {cycle})")

        for s in snapshots:
            print({
                "id": s["id"],
                metrics["energy"]: s["energy"],
                metrics["wear"]: s["wear"],
                metrics["age"]: s["age"],
                "decision": actions.get(s["action"]),
                metrics["alive"]: s["alive"],
                "cycle": cycle
            })

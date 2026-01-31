from lpc.population import LPCPopulation
from lpc.world import LPCWorld
from simulation import LPCSimulation
from presets.visualization import LPCVisualizer


if __name__ == "__main__":

    population = LPCPopulation(size=10)
    world = LPCWorld()

    visualizer = LPCVisualizer(preset_name="BUSINESS_UNIT")

    sim = LPCSimulation(
        population=population,
        world=world,
        max_cycles=24
    )


    sim.run(visualizer=visualizer)
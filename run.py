from lpc_population import LPCPopulation
from lpc_world import LPCWorld
from simulation import LPCSimulation
from lpc_visualization import LPCVisualizer


if __name__ == "__main__":

    population = LPCPopulation(size=10)
    world = LPCWorld()

    visualizer = LPCVisualizer(preset_name="BUSINESS_UNIT")

    sim = LPCSimulation(
        population=population,
        world=world,
        max_cycles=24
    )

    # 👇 El visualizador se inyecta en la simulación
    sim.run(visualizer=visualizer)
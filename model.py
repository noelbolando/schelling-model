"""
This file contains all the Schelling model classes.
"""

from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import SingleGrid

from agents import SchellingAgent

class Schelling(Model):
    """Model class for the Schelling segregation model."""

    def __init__(
            self,
            height: int=20,
            width: int=20,
            density: float=0.8,
            minority_pc: float=0.5,
            homophily: float=0.4,
            radius: int=1,
            seed=None
    ):
        """Create a new Schelling model.
        
        Args:
            width: width of the grid
            height: height of the grid
            density: initial chance for a cell to be populated (0-1)
            minority_pc: chance for an agent to be in a minority class (0-1)
            homophily: minimum number of similiar neighbors needed for happiness
            radius: search radius for checking neighbor similarity
            seed: seed for reproducibility
        """
        super().__init__(seed=seed)

        # Model parameters
        self.height = height
        self.width = width
        self.density = density
        self.minority_pc = minority_pc
        self.homophily = homophily
        self.radius = radius
        
        # Initalize the grid
        self.grid = SingleGrid(width, height, torus=True)

        # Track happiness
        self.happy = 0

        # Set up the data collection
        self.datacollector = DataCollector(
            model_reporters={
                "happy": "happy",
                "pct_happy": lambda m: (m.happy / len(m.agents)) * 100
                if len(m.agents) > 0
                else 0,
                "population": lambda m: len(m.agents),
                "minority_pc": lambda m: (
                    sum(1 for agent in m.agents if agent.type == 1) / len(m.agents) * 100
                    if len(m.agents) > 0
                    else 0
                ),
            },
            agent_reporters={"agent_type": "type"},
        )

        # Create agents and place them on the grid
        for _, pos in self.grid.coord_iter():
            if self.random.random() < self.density:
                agent_type = 1 if self.random.random() < minority_pc else 0
                agent = SchellingAgent(self, agent_type)
                self.grid.place_agent(agent, pos)
        
        # Collect initial state
        self.datacollector.collect(self)

    def step(self):
        """Run one step of the model."""
        self.happy = 0 # Reset the number of happy agents
        self.agents.shuffle_do("step") # Activate all agents in random pairs
        self.datacollector.collect(self) # Collect data
        self.running = self.happy < len(self.agents) # Continue until everyone is happy

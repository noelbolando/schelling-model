"""
This file contains all the Schelling agent classes needed.
"""

from mesa import Agent

class SchellingAgent(Agent):
    """Schelling segregation agent class."""

    def __init__(self, model, agent_type: int) -> None:
        """
        Create a new Schelling Agent.
        Args:
            model: the model instance that the agent belongs to.
            agent_type: indicator for agent's type (minority = 1, majority = 0)
        """
        super().__init__(model)
        self.type = agent_type

    def step(self) -> None:
        """Determine if the agent is happy and move the agent if necessary."""
        neighbors = self.model.grid.get_neighbors(
            self.pos, 
            moore=True, 
            radius=self.model.radius
        )

        # Count the number of similiar neighbors
        similar_neighbors = len([n for n in neighbors if n.type == self.type])

        # Calculate the fraction of similiar neighbors
        if (valid_neighbors := len(neighbors)) > 0:
            similarity_fraction = similar_neighbors / valid_neighbors
        else:
            # If there are no neighbors, the similarity fraction is 0
            similarity_fraction = 0.0
        
        # Move the agent is it is unhappy
        if similarity_fraction < self.model.homophily:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1

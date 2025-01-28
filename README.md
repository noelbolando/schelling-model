# The Schelling Segregation Model #

## Project Description ##
This is a classic agent-based model, demonstrating how minimal preference for similar neighbors can lead to high levels of segregation within 2D landscapes.

I developed this project to help me understand the underlying favorability in agents obtaining similar neighbors.

A quick note on this model: this model looks at segregation but does NOT include outside factors that place pressure on agents to segregation. For example, it does not operate with the consideration of Jim Crow Laws in the US. However, this model demonstrates that mild simililar-neighbor preferences could and do lead to highly segregated societies via de facto segregation.

From a game-theory perspective, this model demonstrates how agents strive to maximize their utilities or influence by relocating to positions with the highest fraction of neighboring agents from the same group.

## How it Works ##

The model itself consists of agents on a square grid where each grid cell can contain a maximum of 1 agent. Agents are distinguished by colors: red and blue. They are happy if a certain number of their neighbors are of the same color, and unhappy otherwise. Unhappy agents will pick a random empty cell to move to each step, until they are happy. The models runs indefinitely until there are no unhappy agents.

What does an agent need to be happy? Three similiar neighbors. This means that the agents could be happy even with a majority of their neighbors being a different color. Regardless, the model usually leads to a high level of segregation when most agents end up with little-to-no neighbors of a different color.

## References ##

[This](https://mesa.readthedocs.io/stable/examples/basic/schelling.html) documentation was very helpful in developing this model.

[This Article](https://www.stat.berkeley.edu/~aldous/157/Papers/Schelling_Seg_Models.pdf) outlines the dynamic modeling of segreation and is a great read into the theory behind this model. 

Like always, [Wikipedia](https://en.wikipedia.org/wiki/Schelling%27s_model_of_segregation) has some helpful overview of Schelling's model of segregation too.


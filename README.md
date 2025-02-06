# The Schelling Segregation (Eco-Chamber) Model #

## Project Description ##

This is a classic agent-based model, demonstrating how minimal preference for similar neighbors can lead to high levels of segregation within 2D landscapes. The underlying principle of this model is the notion of homophily: the tendency of people to form social bonds with others who are similar to them.

High degrees of homophily can lead to the formation of echo-chambers wherein populations are observed to interact with information scoped to the relativistic homophilic landscape of their environment. This leads me to surmise that, when an individual agent is in an echo-chamber, it doesn't know what it doesn't know due to the nature of highly-localized environments supporting the interaction and spread of homophilic information. I also theorize that this mechanism also supresses the interaction and spread of non-homophilic information.

TL;DR - I developed this project to help me understand the underlying nature of echo-chamber evolution.

A quick note on this model: this model looks at how nearest-neighbor favorability results in the formation of echo-chambers. Classically, this model considers segregation as a result of this simulation but given the ever-evolving digital world that we find ourselves in, I thought it more appropriate to consider the effects of this model through the scope of an echo-chamber. This model does NOT include outside factors that place pressure on agents to segregation. However, this model demonstrates that mild similar-neighbor preferences could and do lead to highly segregated societies.

From a game-theory perspective, this model demonstrates how agents strive to maximize their utilities or influence by relocating to positions with the highest fraction of neighboring agents from the same group.

## Project Details ##

As you'll see, there are three files in this repo:

1. 'agents.py': this file defines the properties of agents.
2. 'app.py': using Solara, this file defines an interactive visualization tool so that users can toggle different agent properties to see how segregation drives the evolution of echo-chambers.
3. 'model.py': this file defines the model itself and sets initial values for the properties of agents. 

## How it Works ##

The model itself consists of agents on a square grid where each grid cell can contain a maximum of 1 agent. Agents are distinguished by colors: red and blue. They are happy if a certain number of their neighbors are of the same color, and unhappy otherwise. Unhappy agents will pick a random empty cell to move to each step, until they are happy. The models runs indefinitely until there are no unhappy agents.

What does an agent need to be happy? Three similiar neighbors. This means that the agents could be happy even with a majority of their neighbors being a different color. Regardless, the model usually leads to a high level of segregation when most agents end up with little-to-no neighbors of a different color.


## References ##

[This](https://mesa.readthedocs.io/stable/examples/basic/schelling.html) documentation was very helpful in developing this model.

[This Article](https://www.stat.berkeley.edu/~aldous/157/Papers/Schelling_Seg_Models.pdf) outlines the dynamic modeling of segreation and is a great read into the theory behind this model. 

Like always, [Wikipedia](https://en.wikipedia.org/wiki/Schelling%27s_model_of_segregation) has some helpful overview of Schelling's model of segregation too.


""""
This file instantiates a web page for the Schelling model using Solara.
This creates an interface for the model and displays some cool graphs.

To initialize the app:
    solara run app.py
"""

from mesa.visualization import Slider, SolaraViz, make_plot_component, make_space_component
import solara

from model import Schelling

def get_happy_agents(model):
    """Display a text count of how many happy agents there are."""
    return solara.Markdown(f"**Happy agents: {model.happy}**")

def agent_portrayal(agent):
    """Define how the agents are diplayed."""
    return{"color": "tab:orange" if agent.type == 0 else "tab:blue"}

"""Define how the parameters will be displayed."""
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed"
    },
    "density": Slider(
        label="Agent Density",
        value=0.8,
        min=0.1,
        max=1.0,
        step=0.1
    ),
    "minority_pc": Slider(
        label="Fraction Minority",
        value=0.2,
        min=0.0,
        max=1.0,
        step=0.05
    ),
    "homophily": Slider(
        label="Homophily",
        value=0.4,
        min=0.0,
        max=1.0,
        step=0.125
    ),
    "width": 20,
    "height": 20
}

model1 = Schelling()

HappyPlot = make_plot_component({"happy": "tab:green"})

page = SolaraViz(
    model1,
    components = [
        make_space_component(agent_portrayal),
        HappyPlot,
        get_happy_agents
    ],
    model_params=model_params
)

page

from globals import runtime_context, MODEL, model_dict, func_write
from models import AgentBasedModel

from behave import *
from mesa.space import *

@when(u'the model has a single-agent per cell grid sized by width {width:S} and height {height:S}') 
def step_impl(context, width, height):
  MODEL.grid = SingleGrid(width=int(width), height=int(height), torus=False)
  model_dict_update = {
    "the model's grid" : MODEL.grid,
    "the empty cells in the grid" : MODEL.grid.empties,
    "the grid's coordinates" : MODEL.grid.coord_iter(), 
  }
  assert isinstance(MODEL, AgentBasedModel) and isinstance(MODEL.grid, SingleGrid)
  
@when(u'the model has a single-agent per cell grid sized by width {width} and height {height:S} as torus') 
def step_impl(context, width, height):
  MODEL.grid = SingleGrid(width=int(width), height=int(height), torus=True)
  assert isinstance(MODEL, AgentBasedModel) and isinstance(MODEL.grid, SingleGrid)

@when(u'the model has a multi-agent per cell grid sized by width {width:S} and height {height:S}')
def step_impl(context, width, height):
  MODEL.grid = MultiGrid(width=int(width), height=int(height), torus=False)
  assert isinstance(MODEL, AgentBasedModel) and isinstance(MODEL.grid, MultiGrid)
 
@when(u'the model has a single-agent per cell hexagonal grid sized by width {width:S} and height {height:S}')
def step_impl(context, width, height):
  MODEL.grid = HexSingleGrid(width=int(width), height=int(height), torus=False)
  assert isinstance(MODEL, AgentBasedModel) and isinstance(MODEL.grid, HexSingleGrid)
  
@when(u'the model has a single-agent per cell hexagonal grid sized by width {width:S} and height {height:S} as torus')
def step_impl(context, width, height):
  MODEL.grid = HexSingleGrid(width=int(width), height=int(height), torus=True)
  assert isinstance(MODEL, AgentBasedModel) and isinstance(MODEL.grid, HexSingleGrid)
  
@when(u'the model has a multi-agent per cell hexagonal grid sized by width {width:S} and height {height:S}')
def step_impl(context, width, height):
  MODEL.grid = HexMultiGrid(width=int(width), height=int(height), torus=False)
  assert isinstance(MODEL, AgentBasedModel) and isinstance(MODEL.grid, HexMultiGrid)
  
@when(u'the model has a multi-agent per cell hexagonal grid sized by width {width:S} and height {height:S} as torus')
def step_impl(context, width, height):
  MODEL.grid = HexMultiGrid(width=int(width), height=int(height), torus=True)
  assert isinstance(MODEL, AgentBasedModel) and isinstance(MODEL.grid, HexMultiGrid)

@when(u'{num_agents:S} {agent_name:S} agents are placed in empty grid cells')
@when(u'{num_agents:S} {agent_name:S} agents are placed in empty cells')
@when(u'{num_agents:S} {agent_name:S} agents are placed on empty tiles')
def step_impl(context, num_agents, agent_name):
  num_agents = int(num_agents)
  num_on_grid = 0
  for agent in MODEL.agents:
    if isinstance(agent, getattr(runtime_context, agent_name)):
      MODEL.grid.move_to_empty(agent) 
      num_on_grid += 1
    if (num_on_grid == num_agents):
      break
  
  assert (num_agents == num_on_grid) \
    and (MODEL.grid.empties() < MODEL.grid.width * MODEL.grid.height)
 
  
import globals
from models import AgentBasedModel

from behave import *
from mesa.space import *

@when(u'the model has a single-agent per cell grid sized by width {width:S} and height {height:S}') 
def step_impl(context, width, height):
  globals.MODEL.grid = SingleGrid(width=int(width), height=int(height), torus=False)
  dict_update = {
    "the model's grid" : globals.MODEL.grid,
    "the empty cells in the grid" : globals.MODEL.grid.empties,
    "iteration over all the grid's coordinates" : globals.MODEL.grid.coord_iter(), 
    "empty cells exist": globals.MODEL.grid.exists_empty_cells()
  }
  for row in range(height):
    for col in range(width):
      dict_update[f"iteration over the agent's neighborhood at ({row}, {col})"] = globals.MODEL.grid.iter_neighborhood(pos=(row, col), moore=False)
      dict_update[f"iteration over the agent's moore neighborhood at ({row}, {col})"] = globals.MODEL.grid.iter_neighborhood(pos=(row, col), moore=True)
      dict_update[f"the agent's neighborhood at ({row}, {col})"] = globals.MODEL.grid.get_neighborhood(pos=(row, col))
      dict_update[f"the agent's moore neighborhood at ({row}, {col})"] = globals.MODEL.grid.get_neighborhood(pos=(row, col), moore=True)
      dict_update[f"iteration of the agent's neighbors at ({row}, {col})"] = globals.MODEL.grid.iter_neighbors(pos=(row, col))
      dict_update[f"iteration of the agent's moore neighbors at ({row}, {col})"] = globals.MODEL.grid.iter_neighbors(pos=(row, col), moore=True)
      dict_update[f"the agent's neighbors at ({row}, {col})"] = globals.MODEL.grid.get_neighbors(pos=(row, col))
      dict_update[f"the agent's moore neighbors at ({row}, {col})"] = globals.MODEL.grid.get_neighbors(pos=(row, col), moore=True)
      dict_update[f"the list of all cell contents at ({row}, {col})"] = globals.MODEL.grid.get_cell_list_contents(cell_list=(row, col))
      dict_update[f"the cell at ({row}, {col}) is empty"] = globals.MODEL.grid.is_cell_empty(pos=(row, col))
  globals.model_dict.update(dict_update)
  globals.func_write.update(dict_update)
      
  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ and isinstance(globals.MODEL.grid, SingleGrid)
  
@when(u'the model has a single-agent per cell grid sized by width {width} and height {height:S} as torus') 
def step_impl(context, width, height):
  globals.MODEL.grid = SingleGrid(width=int(width), height=int(height), torus=True)
  dict_update = {
    "the model's grid" : globals.MODEL.grid,
    "the empty cells in the grid" : globals.MODEL.grid.empties,
    "iteration over all the grid's coordinates" : globals.MODEL.grid.coord_iter(), 
    "empty cells exist": globals.MODEL.grid.exists_empty_cells()
  }
  for row in range(height):
    for col in range(width):
      dict_update[f"the iteration over the agent's neighborhood at ({row}, {col})"] = globals.MODEL.grid.iter_neighborhood(pos=(row, col))
      dict_update[f"the iteration over the agent's moore neighborhood at ({row}, {col})"] = globals.MODEL.grid.iter_neighborhood(pos=(row, col), moore=True)
      dict_update[f"the agent's neighborhood at ({row}, {col})"] = globals.MODEL.grid.get_neighborhood(pos=(row, col))
      dict_update[f"the agent's moore neighborhood at ({row}, {col})"] = globals.MODEL.grid.get_neighborhood(pos=(row, col), moore=True)
      dict_update[f"the iteration of the agent's neighbors at ({row}, {col})"] = globals.MODEL.grid.iter_neighbors(pos=(row, col))
      dict_update[f"the iteration of the agent's moore neighbors at ({row}, {col})"] = globals.MODEL.grid.iter_neighbors(pos=(row, col), moore=True)
      dict_update[f"the agent's neighbors at ({row}, {col})"] = globals.MODEL.grid.get_neighbors(pos=(row, col))
      dict_update[f"the agent's moore neighbors at ({row}, {col})"] = globals.MODEL.grid.get_neighbors(pos=(row, col), moore=True)
      dict_update[f"the list of all cell contents at ({row}, {col})"] = globals.MODEL.grid.get_cell_list_contents(cell_list=(row, col))
      dict_update[f"the cell at ({row}, {col}) is empty"] = globals.MODEL.grid.is_cell_empty(pos=(row, col))
  globals.model_dict.update(dict_update)
  globals.func_write.update(dict_update)
  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ and isinstance(globals.MODEL.grid, SingleGrid)

@then(u'{num_agents:S} {agent_name:S} agents are placed in empty grid cells')
@then(u'{num_agents:S} {agent_name:S} agents are placed in empty cells')
@then(u'{num_agents:S} {agent_name:S} agents are placed on empty tiles')
def step_impl(context, num_agents, agent_name):
  num_agents = int(num_agents)
  num_on_grid = 0
  for agent in globals.MODEL.agents:
    if type(agent).__name__ == getattr(globals.runtime_context, agent_name).__name__:
      globals.MODEL.grid.move_to_empty(agent) 
      num_on_grid += 1
    if (num_on_grid == num_agents):
      break
  
  assert (num_agents == num_on_grid) \
    and (len(globals.MODEL.grid.empties) < globals.MODEL.grid.width * globals.MODEL.grid.height)
 
#------- TO MUCH COMPLEXITY WITH DIFFERENT TYPES OF GRIDS, IMPLEMENTED LATER TBD ----------
#@when(u'the model has a multi-agent per cell grid sized by width {width:S} and height {height:S}')
#def step_impl(context, width, height):
#  globals.MODEL.grid = MultiGrid(width=int(width), height=int(height), torus=False)
#  globals.MODEL.get_single_grid_data = get_single_agent_grid_data
#  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ and isinstance(globals.MODEL.grid, MultiGrid)
# 
#@when(u'the model has a single-agent per cell hexagonal grid sized by width {width:S} and height {height:S}')
#def step_impl(context, width, height):
#  globals.MODEL.grid = HexSingleGrid(width=int(width), height=int(height), torus=False)
#  globals.MODEL.get_single_grid_data = get_single_agent_grid_data
#  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ and isinstance(globals.MODEL.grid, HexSingleGrid)
#  
#@when(u'the model has a single-agent per cell hexagonal grid sized by width {width:S} and height {height:S} as torus')
#def step_impl(context, width, height):
#  globals.MODEL.grid = HexSingleGrid(width=int(width), height=int(height), torus=True)
#  globals.MODEL.get_single_grid_data = get_single_agent_grid_data
#  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ and isinstance(globals.MODEL.grid, HexSingleGrid)
  
#@when(u'the model has a multi-agent per cell hexagonal grid sized by width {width:S} and height {height:S}')
#def step_impl(context, width, height):
#  globals.MODEL.grid = HexMultiGrid(width=int(width), height=int(height), torus=False)
#  globals.MODEL.get_single_grid_data = get_single_agent_grid_data
#  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ and isinstance(globals.MODEL.grid, HexMultiGrid)
#  
#@when(u'the model has a multi-agent per cell hexagonal grid sized by width {width:S} and height {height:S} as torus')
#def step_impl(context, width, height):
#  globals.MODEL.grid = HexMultiGrid(width=int(width), height=int(height), torus=True)
#  globals.MODEL.get_single_grid_data = get_single_agent_grid_data
#  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ and isinstance(globals.MODEL.grid, HexMultiGrid) 
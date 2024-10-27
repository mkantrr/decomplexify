#globals.py
from features.models import AgentBasedModel

def indent(indent):
  indent[0] = indent[0] + '  '
  return [indent[0], indent[1] + 1]

def deindent(indent):
  indent[0] = indent[0][:-2]
  return [indent[0], indent[1] - 1]

class Context:
  """Object for storing context"""
  def __init__(self):
    pass 
  
def init():
  global MODEL
  MODEL = AgentBasedModel()
  global runtime_context
  runtime_context = Context()
 
  global operator_dict
  operator_dict = {
    "=" : "==",
    "equals" : "==",
    "does not equal" : "!=",
    "is less than" : "<",
    "is greater than" : ">",
    "is less than or equal to": "<=",
    "is greater than or equal to": ">="
  } 
  
  global model_dict_write
  model_dict_write = {
    "the model's grid" : "MODEL.grid", 
    "the empty cells in the grid" : "MODEL.grid.empties()", 
    "the grid's coordinates" : "MODEL.grid.coord_iter()", 
    "the agent's current position" : "self.pos", 
    "" : "", 
    "" : "", 
    "" : "", 
    "" : "", 
    "" : "", 
    "" : "", 
    "" : "", 
  }
  global model_dict
  model_dict = dict()
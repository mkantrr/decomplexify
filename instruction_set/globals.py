#globals.py
from features.models import AgentBasedModel

def indent(indent):
  indent[0] = indent[0] + '  '
  return [indent[0], indent[1] + 1]

def deindent(indent):
  indent[0] = indent[0][:-2]
  return [indent[0], indent[1] - 1]

# --------------- BEGIN COMMON STEP ROUTINE ---------------------
def step(self):
  self.schedule.step()
  self.datacollector.collect()
  
def step_no_data(self):
  self.schedule.step()

  
# --------------- END COMMON STEP ROUTINE -----------------------

class Context:
  """Object for storing context"""
  def __init__(self):
    pass 
  
def init():
  global MODEL
  MODEL = AgentBasedModel()
  global runtime_context
  runtime_context = Context()
  runtime_context.agent_number = 0
 
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
  
  global agent_dict
  agent_dict = dict()
  
  global func_write
  func_write = dict()
  
  global model_dict
  model_dict = dict()
  
  global data_dict
  data_dict = dict()
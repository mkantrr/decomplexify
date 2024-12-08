from inspect import isclass
from importlib import reload
import uuid

import globals
import agent_classes

from behave import *
from mesa.time import *

@given(u'a {agent_name:S} agent')
@given(u'an {agent_name:S} agent')
def step_impl(context, agent_name):
  context.indent = [str(), 0]
  agent_file = open('agent_classes.py', 'a')
  agent_file.write(context.indent[0] + "class {agent_name}(Agent):\n".format(
    agent_name=agent_name
  ))
  context.indent = globals.indent(context.indent)
  agent_file.write(context.indent[0] + "def __init__(self, unique_id):\n") 
  context.indent = globals.indent(context.indent)
  agent_file.write(context.indent[0] + "super().__init__(unique_id, globals.MODEL)\n")
  agent_file.close()
  reload(agent_classes)
  setattr(globals.runtime_context, agent_name, getattr(__import__('agent_classes'), agent_name))
  context.indent = [str(), 0]
  globals.agent_dict.update({getattr(globals.runtime_context, agent_name).__name__: globals.runtime_context.agent_number})
  globals.runtime_context.agent_number += 1
  assert hasattr(globals.runtime_context, agent_name) and isclass(getattr(globals.runtime_context, agent_name))

@then(u'put {num_agents:S} {agent_name:S} agents in the model')
def step_impl(context, num_agents, agent_name):
  globals.MODEL.N = int(num_agents)
  for i in range(int(num_agents)):
    agent = getattr(globals.runtime_context, agent_name)(uuid.uuid4().int)
    globals.func_write.update({"the agent's position": agent.pos})
    globals.MODEL.schedule.add(agent) 
    
  num_in_model = 0
  for agent in globals.MODEL.agents:
    if getattr(globals.runtime_context, agent_name).__name__ == agent.__class__.__name__:
      num_in_model += 1
  assert num_in_model == int(num_agents)
  
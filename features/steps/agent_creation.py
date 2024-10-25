from inspect import isclass
import uuid
import logging

from globals import indent, deindent, runtime_context, MODEL

from behave import *
from mesa.time import *

@given(u'a {agent_name:S} agent')
def step_impl(context, agent_name):
  context.indent = str()
  agent_file = open('agent_classes.py', 'a')
  agent_file.write(context.indent + "class {agent_name}(Agent):\n".format(
    agent_name=agent_name
  ))
  context.indent = indent(context.indent)
  agent_file.write(context.indent + "def __init__(self, unique_id, model):\n") 
  context.indent = indent(context.indent)
  agent_file.write(context.indent + "super().__init__(unique_id, model)\n")
  agent_file.close()
  setattr(runtime_context, agent_name, getattr(__import__('agent_classes'), agent_name))
  assert hasattr(runtime_context, agent_name) and isclass(getattr(runtime_context, agent_name))
  context.indent = deindent(context.indent)
  context.indent = deindent(context.indent)

@then('put {num_agents} {agent_name} agents in the model')
def step_impl(context, num_agents, agent_name):
  MODEL.N = int(num_agents)
  for i in range(int(num_agents)):
    agent = getattr(runtime_context, agent_name)(uuid.uuid4().int, MODEL)
    MODEL.schedule.add(agent) 
    
  num_in_model = 0
  for agent in MODEL.agents:
    if isinstance(agent, getattr(runtime_context, agent_name)):
      num_in_model += 1
  assert num_in_model == int(num_agents)
  
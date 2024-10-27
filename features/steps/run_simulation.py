from inspect import isclass

from models import AgentBasedModel
from globals import indent, deindent, runtime_context, MODEL

from behave import *

@given(u'a model and a {agent_name:S} agent')
def step_impl(context, agent_name):
  MODEL = AgentBasedModel()
  
  context.indent = str()
  agent_file = open('agent_classes.py', 'a')
  agent_file.write(context.indent + "class {agent_name}(Agent):\n".format(
    agent_name=agent_name
  ))
  context.indent = indent(context.indent)
  agent_file.write(context.indent + "def __init__(self, unique_id, model):\n") 
  context.indent = indent(context.indent)
  agent_file.write(context.indent + "global MODEL\n") 
  agent_file.write(context.indent + "super().__init__(unique_id, MODEL)\n")
  agent_file.close()
  setattr(runtime_context, agent_name, getattr(__import__('agent_classes'), agent_name))
  assert hasattr(runtime_context, agent_name) and isclass(getattr(runtime_context, agent_name))
  context.indent = deindent(context.indent)
  context.indent = deindent(context.indent)
  
  assert MODEL is not None and \
    (hasattr(runtime_context, agent_name) and isclass(getattr(runtime_context, agent_name)))
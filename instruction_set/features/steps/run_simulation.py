from inspect import isclass

from models import AgentBasedModel
import globals

from behave import *

@given(u'a model and a {agent_name:S} agent')
def step_impl(context, agent_name):
  MODEL = AgentBasedModel()
  
  context.indent = str()
  agent_file = open('agent_classes.py', 'a')
  agent_file.write(context.indent + "class {agent_name}(Agent):\n".format(
    agent_name=agent_name
  ))
  context.indent = globals.indent(context.indent)
  agent_file.write(context.indent + "def __init__(self, unique_id, model):\n") 
  context.indent = globals.indent(context.indent)
  agent_file.write(context.indent + "super().__init__(unique_id, globals.MODEL)\n")
  agent_file.close()
  setattr(globals.runtime_context, agent_name, getattr(__import__('agent_classes'), agent_name))
  context.indent = globals.deindent(context.indent)
  context.indent = globals.deindent(context.indent)
  
  globals.agent_dict.update({getattr(globals.runtime_context, agent_name).__name__: globals.runtime_context.agent_number})
  globals.runtime_context.agent_number += 1
  
  assert MODEL is not None and \
    (hasattr(globals.runtime_context, agent_name) and isclass(getattr(globals.runtime_context, agent_name)))
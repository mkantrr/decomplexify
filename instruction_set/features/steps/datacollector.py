import globals
from models import AgentBasedModel

from types import MethodType

from behave import *
from mesa.datacollection import *

@when(u'the model collects data on the attribute {variable:S}') 
@when(u'the model collects data on the variable {variable:S}') 
@when(u'the model collects data on the model attribute {variable:S}') 
@when(u'the model collects data on the model variable {variable:S}') 
def step_impl(context, variable):
    
  if (hasattr(globals.runtime_context, 'model_reporters')):
    if (hasattr(globals.MODEL, variable)):
      model_reporters = {f'{variable}': f'{variable}'}
      globals.runtime_context.model_reporters.update(model_reporters)
    elif (hasattr(globals.runtime_context, variable)):
      setattr(globals.MODEL, variable, getattr(globals.runtime_context, variable))
      model_reporters = {f'{variable}': f'{variable}'}
      globals.runtime_context.model_reporters.update(model_reporters)
  else:
    if (hasattr(globals.MODEL, variable)):
      globals.runtime_context.model_reporters = {f'{variable}': f'{variable}'}
    elif (hasattr(globals.runtime_context, variable)):
      setattr(globals.MODEL, variable, getattr(globals.runtime_context, variable))
      globals.runtime_context.model_reporters = {f'{variable}': f'{variable}'}
      
  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ \
    and globals.runtime_context.model_reporters is not {}
    
@when(u'the model collects data on the routine {func_name:S}') 
@when(u'the model collects data on the model routine {func_name:S}') 
def step_impl(context, func_name):
    
  if (hasattr(globals.runtime_context, 'model_reporters')):
    if (hasattr(globals.MODEL, func_name)):
      model_reporters = {f'{func_name}': getattr(globals.MODEL, func_name)}
      globals.runtime_context.model_reporters.update(model_reporters)
    elif (hasattr(globals.runtime_context, func_name)):
      model_reporters = {f'{func_name}': getattr(globals.runtime_context, func_name)}
      globals.runtime_context.model_reporters.update(model_reporters)
  else:
    if (hasattr(globals.MODEL, func_name)):
      globals.runtime_context.model_reporters = {f'{func_name}': getattr(globals.MODEL, func_name)}
    elif (hasattr(globals.runtime_context, func_name)):
      globals.runtime_context.model_reporters = {f'{func_name}': getattr(globals.runtime_context, func_name)}
  
  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ \
    and globals.runtime_context.model_reporters is not {}
    
@when(u'the model collects data on the routines {func_names:S}') 
@when(u'the model collects data on the model routines {func_names:S}') 
def step_impl(context, func_names):
  if (func_names.find(', ') == -1):
    func_names = func_names.split(',') 
  else:
    func_names = func_names.split(', ') 
  for func_name in func_names:
    if (hasattr(globals.runtime_context, 'model_reporters')):
      if (hasattr(globals.MODEL, func_name)):
        model_reporters = {f'{func_name}': getattr(globals.MODEL, func_name)}
        globals.runtime_context.model_reporters.update(model_reporters)
      elif (hasattr(globals.runtime_context, func_name)):
        model_reporters = {f'{func_name}': getattr(globals.runtime_context, func_name)}
        globals.runtime_context.model_reporters.update(model_reporters)
    else:
      if (hasattr(globals.MODEL, func_name)):
        globals.runtime_context.model_reporters = {f'{func_name}': getattr(globals.MODEL, func_name)}
      elif (hasattr(globals.runtime_context, func_name)):
        globals.runtime_context.model_reporters = {f'{func_name}': getattr(globals.runtime_context, func_name)}
      
  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ \
    and globals.runtime_context.model_reporters is not {}
    
@when(u'the model collects data on the {agent_name:S} agent attribute {variable:S}') 
@when(u'the model collects data on the {agent_name:S} agent variable {variable:S}') 
def step_impl(context, agent_name, variable):
    
  if (hasattr(globals.runtime_context, 'agent_reporters')):
    if (hasattr(globals.runtime_context, agent_name)):
      if (hasattr(getattr(globals.runtime_context, agent_name), variable)):
        agent_reporters = {f'{variable}': f'{variable}'}
        globals.runtime_context.agent_reporters.update(agent_reporters)
  else:
    if (hasattr(globals.runtime_context, agent_name)):
      if (hasattr(getattr(globals.runtime_context, agent_name), variable)):
        globals.runtime_context.agent_reporters = {f'{variable}': f'{variable}'}
      
  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ \
    and globals.runtime_context.agent_reporters is not {}
    
@when(u'the model collects data on the {agent_name:S} agent routine {func_name:S}') 
def step_impl(context, agent_name, func_name):
  
  if (hasattr(globals.runtime_context, 'agent_reporters')):
    if (hasattr(globals.runtime_context, agent_name)):
      if (hasattr(getattr(globals.runtime_context, agent_name), func_name)):
        agent_reporters = {f'{func_name}': getattr(getattr(globals.runtime_context, agent_name), func_name)}
        globals.runtime_context.agent_reporters.update(agent_reporters)
  else:
    if (hasattr(globals.runtime_context, agent_name)):
      if (hasattr(getattr(globals.runtime_context, agent_name), func_name)):
        globals.runtime_context.agent_reporters = {f'{func_name}': getattr(getattr(globals.runtime_context, agent_name), func_name)}
    
  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ \
    and globals.runtime_context.agent_reporters is not {}
    
@when(u'the model collects data on the {agent_name:S} agent routines {func_names:S}') 
def step_impl(context, agent_name, func_names):
  if (func_names.find(', ') == -1):
    func_names = func_names.split(',') 
  else:
    func_names = func_names.split(', ') 
  for func_name in func_names:
    if (hasattr(globals.runtime_context, 'agent_reporters')):
      if (hasattr(globals.runtime_context, agent_name)):
        if (hasattr(getattr(globals.runtime_context, agent_name), func_name)):
          agent_reporters = {f'{func_name}': getattr(getattr(globals.runtime_context, agent_name), func_name)}
          globals.runtime_context.agent_reporters.update(agent_reporters)
    else:
      if (hasattr(globals.runtime_context, agent_name)):
        if (hasattr(getattr(globals.runtime_context, agent_name), func_name)):
          globals.runtime_context.agent_reporters = {f'{func_name}': getattr(getattr(globals.runtime_context, agent_name), func_name)}
      
  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ \
    and globals.runtime_context.agent_reporters is not {}
    
@then (u'collect the data')
@then (u'collect the model data')
def step_impl(context):
  globals.MODEL.datacollector = DataCollector(
    model_reporters=globals.runtime_context.model_reporters, 
    agent_reporters=globals.runtime_context.agent_reporters)  
  
  setattr(globals.MODEL, "step",
    MethodType(globals.step, globals.MODEL))
  
  assert type(globals.MODEL).__name__ == AgentBasedModel.__name__ \
    and isinstance(globals.MODEL.datacollector, DataCollector) \
    and hasattr(globals.MODEL, 'step')
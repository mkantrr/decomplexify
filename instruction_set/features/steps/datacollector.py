from globals import step, runtime_context, MODEL
from models import AgentBasedModel

from types import MethodType

from behave import *
from mesa.datacollection import *

@when(u'the model collects data on the attribute {variable:S}') 
@when(u'the model collects data on the variable {variable:S}') 
@when(u'the model collects data on the model attribute {variable:S}') 
@when(u'the model collects data on the model variable {variable:S}') 
def step_impl(context, variable):
    
  if (hasattr(runtime_context, 'model_reporters')):
    if (hasattr(MODEL, variable)):
      model_reporters = {'{variable}'.format(variable): '{variable}'.format(variable)}
      runtime_context.model_reporters.update(model_reporters)
    elif (hasattr(runtime_context, variable)):
      setattr(MODEL, variable, getattr(runtime_context, variable))
      model_reporters = {'{variable}'.format(variable): '{variable}'.format(variable)}
      runtime_context.model_reporters.update(model_reporters)
  else:
    if (hasattr(MODEL, variable)):
      runtime_context.model_reporters = {'{variable}'.format(variable): '{variable}'.format(variable)}
    elif (hasattr(runtime_context, variable)):
      setattr(MODEL, variable, getattr(runtime_context, variable))
      runtime_context.model_reporters = {'{variable}'.format(variable): '{variable}'.format(variable)}
      
  assert isinstance(MODEL, AgentBasedModel) \
    and runtime_context.model_reporters is not {}
    
@when(u'the model collects data on the routine {func_name:S}') 
@when(u'the model collects data on the model routine {func_name:S}') 
def step_impl(context, func_name):
    
  if (hasattr(runtime_context, 'model_reporters')):
    if (hasattr(MODEL, func_name)):
      model_reporters = {'{func_name}'.format(func_name): getattr(MODEL, func_name)}
      runtime_context.model_reporters.update(model_reporters)
    elif (hasattr(runtime_context, func_name)):
      model_reporters = {'{func_name}'.format(func_name): getattr(runtime_context, func_name)}
      runtime_context.model_reporters.update(model_reporters)
  else:
    if (hasattr(MODEL, func_name)):
      runtime_context.model_reporters = {'{func_name}'.format(func_name): getattr(MODEL, func_name)}
    elif (hasattr(runtime_context, func_name)):
      runtime_context.model_reporters = {'{func_name}'.format(func_name): getattr(runtime_context, func_name)}
  
  assert isinstance(MODEL, AgentBasedModel) \
    and runtime_context.model_reporters is not {}
    
@when(u'the model collects data on the routines {func_names:S}') 
@when(u'the model collects data on the model routines {func_names:S}') 
def step_impl(context, func_names):
  if (func_names.find(', ') == -1):
    func_names = func_names.split(',') 
  else:
    func_names = func_names.split(', ') 
  for func_name in func_names:
    if (hasattr(runtime_context, 'model_reporters')):
      if (hasattr(MODEL, func_name)):
        model_reporters = {'{func_name}'.format(func_name): getattr(MODEL, func_name)}
        runtime_context.model_reporters.update(model_reporters)
      elif (hasattr(runtime_context, func_name)):
        model_reporters = {'{func_name}'.format(func_name): getattr(runtime_context, func_name)}
        runtime_context.model_reporters.update(model_reporters)
    else:
      if (hasattr(MODEL, func_name)):
        runtime_context.model_reporters = {'{func_name}'.format(func_name): getattr(MODEL, func_name)}
      elif (hasattr(runtime_context, func_name)):
        runtime_context.model_reporters = {'{func_name}'.format(func_name): getattr(runtime_context, func_name)}
      
  assert isinstance(MODEL, AgentBasedModel) \
    and runtime_context.model_reporters is not {}
    
@when(u'the model collects data on the {agent_name:S} agent attribute {variable:S}') 
@when(u'the model collects data on the {agent_name:S} agent variable {variable:S}') 
def step_impl(context, agent_name, variable):
    
  if (hasattr(runtime_context, 'agent_reporters')):
    if (hasattr(runtime_context, agent_name)):
      if (hasattr(getattr(runtime_context, agent_name), variable)):
        agent_reporters = {'{variable}'.format(variable): '{variable}'.format(variable)}
        runtime_context.agent_reporters.update(agent_reporters)
  else:
    if (hasattr(runtime_context, agent_name)):
      if (hasattr(getattr(runtime_context, agent_name), variable)):
        runtime_context.agent_reporters = {'{variable}'.format(variable): '{variable}'.format(variable)}
      
  assert isinstance(MODEL, AgentBasedModel) \
    and runtime_context.agent_reporters is not {}
    
@when(u'the model collects data on the {agent_name:S} agent routine {func_name:S}') 
def step_impl(context, agent_name, func_name):
  
  if (hasattr(runtime_context, 'agent_reporters')):
    if (hasattr(runtime_context, agent_name)):
      if (hasattr(getattr(runtime_context, agent_name), func_name)):
        agent_reporters = {'{func_name}'.format(func_name): getattr(getattr(runtime_context, agent_name), func_name)}
        runtime_context.agent_reporters.update(agent_reporters)
  else:
    if (hasattr(runtime_context, agent_name)):
      if (hasattr(getattr(runtime_context, agent_name), func_name)):
        runtime_context.agent_reporters = {'{func_name}'.format(func_name): getattr(getattr(runtime_context, agent_name), func_name)}
    
  assert isinstance(MODEL, AgentBasedModel) \
    and runtime_context.agent_reporters is not {}
    
@when(u'the model collects data on the {agent_name:S} agent routines {func_names:S}') 
def step_impl(context, agent_name, func_names):
  if (func_names.find(', ') == -1):
    func_names = func_names.split(',') 
  else:
    func_names = func_names.split(', ') 
  for func_name in func_names:
    if (hasattr(runtime_context, 'agent_reporters')):
      if (hasattr(runtime_context, agent_name)):
        if (hasattr(getattr(runtime_context, agent_name), func_name)):
          agent_reporters = {'{func_name}'.format(func_name): getattr(getattr(runtime_context, agent_name), func_name)}
          runtime_context.agent_reporters.update(agent_reporters)
    else:
      if (hasattr(getattr(runtime_context, agent_name), func_name)):
        runtime_context.agent_reporters = {'{func_name}'.format(func_name): getattr(getattr(runtime_context, agent_name), func_name)}
      
  assert isinstance(MODEL, AgentBasedModel) \
    and runtime_context.agent_reporters is not {}
    
@then (u'collect the data')
@then (u'collect the model data')
def step_impl(context):
  MODEL.datacollector = DataCollector(
    model_reporters=runtime_context.model_reporters, 
    agent_reporters=runtime_context.agent_reporters)  
  
  setattr(MODEL, "step",
    MethodType(step))
  
  assert isinstance(MODEL, AgentBasedModel) \
    and isinstance(MODEL.datacollector, DataCollector) \
    and hasattr(MODEL, 'step')
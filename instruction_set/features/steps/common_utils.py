import globals

from behave import *
from mesa.space import *

@when(u'the attribute {variable:S} is {value:S}')
@when(u'the variable {variable:S} is {value:S}')
@when(u'the attribute {variable:S}={value:S}')
@when(u'the variable {variable:S}={value:S}')
@when(u'the attribute {variable:S} = {value:S}')
@when(u'the variable {variable:S} = {value:S}')
@when(u'the attribute {variable:S} equals {value:S}')
@when(u'the variable {variable:S} equals {value:S}')
def step_impl(context, variable, value):
  if (hasattr(globals.runtime_context, value)):
    setattr(globals.runtime_context, variable, getattr(globals.runtime_context, value))
  else:
    setattr(globals.runtime_context, variable, value)
  assert hasattr(globals.runtime_context, variable)
  
@when(u'the attribute {variable:S} is the result of routine {func_name:S}')
@when(u'the variable {variable:S} is the result of routine {func_name:S}')
@when(u'the attribute {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the variable {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the attribute {variable:S} equals the result of routine {func_name:S}')
@when(u'the variable {variable:S} equals the result of routine {func_name:S}')
def step_impl(context, variable, func_name):
  if (hasattr(globals.runtime_context, func_name)):
    setattr(globals.runtime_context, variable, getattr(globals.runtime_context, func_name)())
  assert hasattr(globals.runtime_context, variable)
  
@when(u'the attribute {variable:S} is the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the variable {variable:S} is the result of routine {func_name:S} with variable {parameter:S}' )
@when(u'the attribute {variable:S} is equal to the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the variable {variable:S} is equal to the result of routine {func_name:S} with variable {parameter:S}')
@when(u'the attribute {variable:S} equals the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the variable {variable:S} equals the result of routine {func_name:S} with variable {parameter:S}')
def step_impl(context, variable, func_name, parameter):
  if (hasattr(globals.runtime_context, func_name)):
    if (hasattr(globals.runtime_context, parameter)):
      setattr(globals.runtime_context, variable, getattr(globals.runtime_context, func_name)(getattr(globals.runtime_context, parameter)))
  assert hasattr(globals.runtime_context, variable)
  
@when(u'the attribute {variable:S} is the result of routine {func_name:S} with attributes {parameters:S}')
@when(u'the variable {variable:S} is the result of routine {func_name:S} with variables {parameters:S}' )
@when(u'the attribute {variable:S} is equal to the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the variable {variable:S} is equal to the result of routine {func_name:S} with variables {parameter:S}')
@when(u'the attribute {variable:S} equals the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the variable {variable:S} equals the result of routine {func_name:S} with variables {parameter:S}')
def step_impl(context, variable, func_name, parameters):
  parameters_list = parameters.split(',')
  if (hasattr(globals.runtime_context, func_name)):
      for parameter in parameters_list:
        if (hasattr(globals.runtime_context, parameter)):
          parameter = getattr(globals.runtime_context, parameter) 
      setattr(globals.runtime_context, variable, getattr(globals.runtime_context, func_name)(*parameters_list))
  assert hasattr(globals.runtime_context, variable)
  
@when(u'the model attribute {variable:S} is {value:S}')
@when(u'the model variable {variable:S} is {value:S}')
@when(u'the model attribute {variable:S}={value:S}')
@when(u'the model variable {variable:S}={value:S}')
@when(u'the model attribute {variable:S} = {value:S}')
@when(u'the model variable {variable:S} = {value:S}')
@when(u'the model attribute {variable:S} equals {value:S}')
@when(u'the model variable {variable:S} equals {value:S}')
def step_impl(context, variable, value):
  if (hasattr(globals.MODEL, value)):
    setattr(globals.MODEL, variable, getattr(globals.MODEL, value))
  elif (hasattr(globals.runtime_context, value)):
    setattr(globals.MODEL, variable, getattr(globals.runtime_context, value))
  elif (value in globals.model_dict.keys()):
    setattr(globals.MODEL, variable, globals.model_dict[value])
  else:
    setattr(globals.MODEL, variable, value)
  assert hasattr(globals.MODEL, variable)
  
@when(u'the model attribute {variable:S} is the result of routine {func_name:S}')
@when(u'the model variable {variable:S} is the result of routine {func_name:S}')
@when(u'the model attribute {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the model variable {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the model attribute {variable:S} equals the result of routine {func_name:S}')
@when(u'the model variable {variable:S} equals the result of routine {func_name:S}')
def step_impl(context, variable, func_name):
  if (hasattr(globals.MODEL, func_name)):
    setattr(globals.MODEL, variable, getattr(globals.MODEL, func_name)())
  elif (hasattr(globals.runtime_context, func_name)):
    setattr(globals.MODEL, variable, getattr(globals.runtime_context, func_name)())
  assert hasattr(globals.MODEL, variable)
  
@when(u'the model attribute {variable:S} is the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the model variable {variable:S} is the result of routine {func_name:S} with variable {parameter:S}' )
@when(u'the model attribute {variable:S} is equal to the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the model variable {variable:S} is equal to the result of routine {func_name:S} with variable {parameter:S}')
@when(u'the model attribute {variable:S} equals the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the model variable {variable:S} equals the result of routine {func_name:S} with variable {parameter:S}')
def step_impl(context, variable, func_name, parameter):
  if (hasattr(globals.MODEL, func_name)):
    if (hasattr(globals.MODEL, parameter)):
      setattr(globals.MODEL, variable, getattr(globals.MODEL, func_name)(getattr(globals.MODEL, parameter)))
    elif (hasattr(globals.runtime_context, parameter)):
      setattr(globals.MODEL, variable, getattr(globals.MODEL, func_name)(getattr(globals.runtime_context, parameter)))
      
  elif (hasattr(globals.runtime_context, func_name)):
    if (hasattr(globals.MODEL, parameter)):
      setattr(globals.MODEL, variable, getattr(globals.runtime_context, func_name)(getattr(globals.MODEL, parameter)))
    elif (hasattr(globals.runtime_context, parameter)):
      setattr(globals.MODEL, variable, getattr(globals.runtime_context, func_name)(getattr(globals.runtime_context, parameter)))
      
  assert hasattr(globals.runtime_context, variable)
  
@when(u'the model attribute {variable:S} is the result of routine {func_name:S} with attributes {parameters:S}')
@when(u'the model variable {variable:S} is the result of routine {func_name:S} with variables {parameters:S}' )
@when(u'the model attribute {variable:S} is equal to the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the model variable {variable:S} is equal to the result of routine {func_name:S} with variables {parameter:S}')
@when(u'the model attribute {variable:S} equals the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the model variable {variable:S} equals the result of routine {func_name:S} with variables {parameter:S}')
def step_impl(context, variable, func_name, parameters):
  parameters_list = parameters.split(',')
  
  if (hasattr(globals.MODEL, func_name)):
    for parameter in parameters_list:
      if (hasattr(globals.MODEL, parameter)):
        parameter = getattr(globals.MODEL, parameter) 
      elif (hasattr(globals.runtime_context, parameter)):
        parameter = getattr(globals.runtime_context, parameter)
    setattr(globals.MODEL, variable, getattr(globals.MODEL, func_name)(*parameters_list))
    
  elif (hasattr(globals.runtime_context, func_name)):
    for parameter in parameters_list:
      if (hasattr(globals.MODEL, parameter)):
        parameter = getattr(globals.MODEL, parameter) 
      elif (hasattr(globals.runtime_context, parameter)):
        parameter = getattr(globals.runtime_context, parameter)
    setattr(globals.MODEL, variable, getattr(globals.runtime_context, func_name)(*parameters_list))
    
  assert hasattr(globals.runtime_context, variable)
  
@when(u'the {agent_name:S} agent attribute {variable:S} is {value:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is {value:S}')
@when(u'the {agent_name:S} agent attribute {variable:S}={value:S}')
@when(u'the {agent_name:S} agent variable {variable:S}={value:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} = {value:S}')
@when(u'the {agent_name:S} agent variable {variable:S} = {value:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} equals {value:S}')
@when(u'the {agent_name:S} agent variable {variable:S} equals {value:S}')
def step_impl(context, agent_name, variable, value):
  if (hasattr(globals.runtime_context, agent_name)):
    agent_obj = getattr(globals.runtime_context, agent_name)
    
    if (hasattr(agent_obj, value)):
      setattr(agent_obj, variable, getattr(agent_obj, value))
    elif (hasattr(globals.MODEL, value)):
      setattr(agent_obj, variable, getattr(globals.MODEL, value))
    elif (hasattr(globals.runtime_context, value)):
      setattr(agent_obj, variable, getattr(globals.runtime_context, value))
    elif (value in globals.model_dict.keys()):
     setattr(globals.MODEL, variable, globals.model_dict[value])
    else:
      setattr(agent_obj, variable, value)
      
    setattr(globals.runtime_context, agent_name, agent_obj)
    
  check_agent_obj = getattr(globals.runtime_context, agent_name)
  assert hasattr(globals.runtime_context, agent_name) and hasattr(check_agent_obj, variable)
  
@when(u'the {agent_name:S} agent attribute {variable:S} is the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} equals the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent variable {variable:S} equals the result of routine {func_name:S}')
def step_impl(context, agent_name, variable, func_name):
  if (hasattr(globals.runtime_context, agent_name)):
    agent_obj = getattr(globals.runtime_context, agent_name)
    if (hasattr(agent_obj, func_name)):
      setattr(agent_obj, variable, getattr(agent_obj, func_name)())
    elif (hasattr(globals.MODEL, func_name)):
      setattr(agent_obj, variable, getattr(globals.MODEL, func_name)())
    elif (hasattr(globals.runtime_context, func_name)):
      setattr(agent_obj, variable, getattr(globals.runtime_context, func_name)())
    setattr(globals.runtime_context, agent_name, agent_obj)
      
  check_agent_obj = getattr(globals.runtime_context, agent_name)
  assert hasattr(globals.runtime_context, agent_name) and hasattr(check_agent_obj, variable)
  
@when(u'the {agent_name:S} agent attribute {variable:S} is the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is the result of routine {func_name:S} with variable {parameter:S}' )
@when(u'the {agent_name:S} agent attribute {variable:S} is equal to the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is equal to the result of routine {func_name:S} with variable {parameter:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} equals the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} equals the result of routine {func_name:S} with variable {parameter:S}')
def step_impl(context, agent_name, variable, func_name, parameter):
  if (hasattr(globals.runtime_context, agent_name)):
    agent_obj = getattr(globals.runtime_context, agent_name)
    
    if (hasattr(agent_obj, func_name)):
      if (hasattr(agent_obj, parameter)):
        setattr(agent_obj, variable, getattr(agent_obj, func_name)(getattr(agent_obj, parameter)))
      elif (hasattr(globals.MODEL, parameter)):
        setattr(agent_obj, variable, getattr(agent_obj, func_name)(getattr(globals.MODEL, parameter)))
      elif (hasattr(globals.runtime_context, parameter)):
        setattr(agent_obj, variable, getattr(agent_obj, func_name)(getattr(globals.runtime_context, parameter)))
        
    elif (hasattr(globals.MODEL, func_name)):
      if (hasattr(agent_obj, parameter)):
        setattr(agent_obj, variable, getattr(globals.MODEL, func_name)(getattr(agent_obj, parameter)))
      elif (hasattr(globals.MODEL, parameter)):
        setattr(agent_obj, variable, getattr(globals.MODEL, func_name)(getattr(globals.MODEL, parameter)))
      elif (hasattr(globals.runtime_context, parameter)):
        setattr(agent_obj, variable, getattr(globals.MODEL, func_name)(getattr(globals.runtime_context, parameter)))
        
    elif (hasattr(globals.runtime_context, func_name)):
      if (hasattr(agent_obj, parameter)):
        setattr(agent_obj, variable, getattr(globals.runtime_context, func_name)(getattr(agent_obj, parameter)))
      elif (hasattr(globals.MODEL, parameter)):
        setattr(agent_obj, variable, getattr(globals.runtime_context, func_name)(getattr(globals.MODEL, parameter)))
      elif (hasattr(globals.runtime_context, parameter)):
        setattr(agent_obj, variable, getattr(globals.runtime_context, func_name)(getattr(globals.runtime_context, parameter)))
        
    setattr(globals.runtime_context, agent_name, agent_obj)
        
  check_agent_obj = getattr(globals.runtime_context, agent_name)
  assert hasattr(globals.runtime_context, agent_name) and hasattr(check_agent_obj, variable)
  
@when(u'the {agent_name:S} agent attribute {variable:S} is the result of routine {func_name:S} with attributes {parameters:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is the result of routine {func_name:S} with variables {parameters:S}' )
@when(u'the {agent_name:S} agent attribute {variable:S} is equal to the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is equal to the result of routine {func_name:S} with variables {parameter:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} equals the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} equals the result of routine {func_name:S} with variables {parameter:S}')
def step_impl(context, agent_name, variable, func_name, parameters):
  parameters_list = parameters.split(',')
  if (hasattr(globals.runtime_context, agent_name)):
    agent_obj = getattr(globals.runtime_context, agent_name)
    
    if (hasattr(agent_obj, func_name)):
      for parameter in parameters_list: 
        if (hasattr(agent_obj, parameter)):
          parameter = getattr(agent_obj, parameter)
        elif (hasattr(globals.MODEL, parameter)):
          parameter = getattr(globals.MODEL, parameter)
        elif (hasattr(globals.runtime_context, parameter)):
          parameter = getattr(globals.runtime_context, parameter)
      setattr(agent_obj, variable, getattr(agent_obj, func_name)(*parameters_list))
      
    elif (hasattr(globals.MODEL, func_name)):
      for parameter in parameters_list: 
        if (hasattr(agent_obj, parameter)):
          parameter = getattr(agent_obj, parameter)
        elif (hasattr(globals.MODEL, parameter)):
          parameter = getattr(globals.MODEL, parameter)
        elif (hasattr(globals.runtime_context, parameter)):
          parameter = getattr(globals.runtime_context, parameter)
      setattr(agent_obj, variable, getattr(globals.MODEL, func_name)(*parameters_list))
        
    elif (hasattr(globals.runtime_context, func_name)):
      for parameter in parameters_list: 
        if (hasattr(agent_obj, parameter)):
          parameter = getattr(agent_obj, parameter)
        elif (hasattr(globals.MODEL, parameter)):
          parameter = getattr(globals.MODEL, parameter)
        elif (hasattr(globals.runtime_context, parameter)):
          parameter = getattr(globals.runtime_context, parameter)
      setattr(agent_obj, variable, getattr(globals.runtime_context, func_name)(*parameters_list))
      
    setattr(globals.runtime_context, agent_name, agent_obj)
        
  check_agent_obj = getattr(globals.runtime_context, agent_name)
  assert hasattr(globals.runtime_context, agent_name) and hasattr(check_agent_obj, variable)
  
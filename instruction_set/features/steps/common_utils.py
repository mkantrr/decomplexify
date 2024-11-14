from globals import MODEL, runtime_context, model_dict

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
  if (hasattr(runtime_context, value)):
    setattr(runtime_context, variable, getattr(runtime_context, value))
  else:
    setattr(runtime_context, variable, value)
  assert hasattr(runtime_context, variable)
  
@when(u'the attribute {variable:S} is the result of routine {func_name:S}')
@when(u'the variable {variable:S} is the result of routine {func_name:S}')
@when(u'the attribute {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the variable {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the attribute {variable:S} equals the result of routine {func_name:S}')
@when(u'the variable {variable:S} equals the result of routine {func_name:S}')
def step_impl(context, variable, func_name):
  if (hasattr(runtime_context, func_name)):
    setattr(runtime_context, variable, getattr(runtime_context, func_name)())
  assert hasattr(runtime_context, variable)
  
@when(u'the attribute {variable:S} is the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the variable {variable:S} is the result of routine {func_name:S} with variable {parameter:S}' )
@when(u'the attribute {variable:S} is equal to the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the variable {variable:S} is equal to the result of routine {func_name:S} with variable {parameter:S}')
@when(u'the attribute {variable:S} equals the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the variable {variable:S} equals the result of routine {func_name:S} with variable {parameter:S}')
def step_impl(context, variable, func_name, parameter):
  if (hasattr(runtime_context, func_name)):
    if (hasattr(runtime_context, parameter)):
      setattr(runtime_context, variable, getattr(runtime_context, func_name)(getattr(runtime_context, parameter)))
  assert hasattr(runtime_context, variable)
  
@when(u'the attribute {variable:S} is the result of routine {func_name:S} with attributes {parameters:S}')
@when(u'the variable {variable:S} is the result of routine {func_name:S} with variables {parameters:S}' )
@when(u'the attribute {variable:S} is equal to the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the variable {variable:S} is equal to the result of routine {func_name:S} with variables {parameter:S}')
@when(u'the attribute {variable:S} equals the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the variable {variable:S} equals the result of routine {func_name:S} with variables {parameter:S}')
def step_impl(context, variable, func_name, parameters):
  parameters_list = parameters.split(',')
  if (hasattr(runtime_context, func_name)):
      for parameter in parameters_list:
        if (hasattr(runtime_context, parameter)):
          parameter = getattr(runtime_context, parameter) 
      setattr(runtime_context, variable, getattr(runtime_context, func_name)(*parameters_list))
  assert hasattr(runtime_context, variable)
  
@when(u'the model attribute {variable:S} is {value:S}')
@when(u'the model variable {variable:S} is {value:S}')
@when(u'the model attribute {variable:S}={value:S}')
@when(u'the model variable {variable:S}={value:S}')
@when(u'the model attribute {variable:S} = {value:S}')
@when(u'the model variable {variable:S} = {value:S}')
@when(u'the model attribute {variable:S} equals {value:S}')
@when(u'the model variable {variable:S} equals {value:S}')
def step_impl(context, variable, value):
  if (hasattr(MODEL, value)):
    setattr(MODEL, variable, getattr(MODEL, value))
  elif (hasattr(runtime_context, value)):
    setattr(MODEL, variable, getattr(runtime_context, value))
  elif (value in model_dict.keys()):
    setattr(MODEL, variable, model_dict[value])
  else:
    setattr(MODEL, variable, value)
  assert hasattr(MODEL, variable)
  
@when(u'the model attribute {variable:S} is the result of routine {func_name:S}')
@when(u'the model variable {variable:S} is the result of routine {func_name:S}')
@when(u'the model attribute {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the model variable {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the model attribute {variable:S} equals the result of routine {func_name:S}')
@when(u'the model variable {variable:S} equals the result of routine {func_name:S}')
def step_impl(context, variable, func_name):
  if (hasattr(MODEL, func_name)):
    setattr(MODEL, variable, getattr(MODEL, func_name)())
  elif (hasattr(runtime_context, func_name)):
    setattr(MODEL, variable, getattr(runtime_context, func_name)())
  assert hasattr(MODEL, variable)
  
@when(u'the model attribute {variable:S} is the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the model variable {variable:S} is the result of routine {func_name:S} with variable {parameter:S}' )
@when(u'the model attribute {variable:S} is equal to the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the model variable {variable:S} is equal to the result of routine {func_name:S} with variable {parameter:S}')
@when(u'the model attribute {variable:S} equals the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the model variable {variable:S} equals the result of routine {func_name:S} with variable {parameter:S}')
def step_impl(context, variable, func_name, parameter):
  if (hasattr(MODEL, func_name)):
    if (hasattr(MODEL, parameter)):
      setattr(MODEL, variable, getattr(MODEL, func_name)(getattr(MODEL, parameter)))
    elif (hasattr(runtime_context, parameter)):
      setattr(MODEL, variable, getattr(MODEL, func_name)(getattr(runtime_context, parameter)))
      
  elif (hasattr(runtime_context, func_name)):
    if (hasattr(MODEL, parameter)):
      setattr(MODEL, variable, getattr(runtime_context, func_name)(getattr(MODEL, parameter)))
    elif (hasattr(runtime_context, parameter)):
      setattr(MODEL, variable, getattr(runtime_context, func_name)(getattr(runtime_context, parameter)))
      
  assert hasattr(runtime_context, variable)
  
@when(u'the model attribute {variable:S} is the result of routine {func_name:S} with attributes {parameters:S}')
@when(u'the model variable {variable:S} is the result of routine {func_name:S} with variables {parameters:S}' )
@when(u'the model attribute {variable:S} is equal to the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the model variable {variable:S} is equal to the result of routine {func_name:S} with variables {parameter:S}')
@when(u'the model attribute {variable:S} equals the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the model variable {variable:S} equals the result of routine {func_name:S} with variables {parameter:S}')
def step_impl(context, variable, func_name, parameters):
  parameters_list = parameters.split(',')
  
  if (hasattr(MODEL, func_name)):
    for parameter in parameters_list:
      if (hasattr(MODEL, parameter)):
        parameter = getattr(MODEL, parameter) 
      elif (hasattr(runtime_context, parameter)):
        parameter = getattr(runtime_context, parameter)
    setattr(MODEL, variable, getattr(MODEL, func_name)(*parameters_list))
    
  elif (hasattr(runtime_context, func_name)):
    for parameter in parameters_list:
      if (hasattr(MODEL, parameter)):
        parameter = getattr(MODEL, parameter) 
      elif (hasattr(runtime_context, parameter)):
        parameter = getattr(runtime_context, parameter)
    setattr(MODEL, variable, getattr(runtime_context, func_name)(*parameters_list))
    
  assert hasattr(runtime_context, variable)
  
@when(u'the {agent_name:S} agent attribute {variable:S} is {value:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is {value:S}')
@when(u'the {agent_name:S} agent attribute {variable:S}={value:S}')
@when(u'the {agent_name:S} agent variable {variable:S}={value:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} = {value:S}')
@when(u'the {agent_name:S} agent variable {variable:S} = {value:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} equals {value:S}')
@when(u'the {agent_name:S} agent variable {variable:S} equals {value:S}')
def step_impl(context, agent_name, variable, value):
  if (hasattr(runtime_context, agent_name)):
    agent_obj = getattr(runtime_context, agent_name)
    
    if (hasattr(agent_obj, value)):
      setattr(agent_obj, variable, getattr(agent_obj, value))
    elif (hasattr(MODEL, value)):
      setattr(agent_obj, variable, getattr(MODEL, value))
    elif (hasattr(runtime_context, value)):
      setattr(agent_obj, variable, getattr(runtime_context, value))
    elif (value in model_dict.keys()):
     setattr(MODEL, variable, model_dict[value])
    else:
      setattr(agent_obj, variable, value)
      
    setattr(runtime_context, agent_name, agent_obj)
    
  check_agent_obj = getattr(runtime_context, agent_name)
  assert hasattr(runtime_context, agent_name) and hasattr(check_agent_obj, variable)
  
@when(u'the {agent_name:S} agent attribute {variable:S} is the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is equal to the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} equals the result of routine {func_name:S}')
@when(u'the {agent_name:S} agent variable {variable:S} equals the result of routine {func_name:S}')
def step_impl(context, agent_name, variable, func_name):
  if (hasattr(runtime_context, agent_name)):
    agent_obj = getattr(runtime_context, agent_name)
    if (hasattr(agent_obj, func_name)):
      setattr(agent_obj, variable, getattr(agent_obj, func_name)())
    elif (hasattr(MODEL, func_name)):
      setattr(agent_obj, variable, getattr(MODEL, func_name)())
    elif (hasattr(runtime_context, func_name)):
      setattr(agent_obj, variable, getattr(runtime_context, func_name)())
    setattr(runtime_context, agent_name, agent_obj)
      
  check_agent_obj = getattr(runtime_context, agent_name)
  assert hasattr(runtime_context, agent_name) and hasattr(check_agent_obj, variable)
  
@when(u'the {agent_name:S} agent attribute {variable:S} is the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is the result of routine {func_name:S} with variable {parameter:S}' )
@when(u'the {agent_name:S} agent attribute {variable:S} is equal to the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is equal to the result of routine {func_name:S} with variable {parameter:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} equals the result of routine {func_name:S} with attribute {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} equals the result of routine {func_name:S} with variable {parameter:S}')
def step_impl(context, agent_name, variable, func_name, parameter):
  if (hasattr(runtime_context, agent_name)):
    agent_obj = getattr(runtime_context, agent_name)
    
    if (hasattr(agent_obj, func_name)):
      if (hasattr(agent_obj, parameter)):
        setattr(agent_obj, variable, getattr(agent_obj, func_name)(getattr(agent_obj, parameter)))
      elif (hasattr(MODEL, parameter)):
        setattr(agent_obj, variable, getattr(agent_obj, func_name)(getattr(MODEL, parameter)))
      elif (hasattr(runtime_context, parameter)):
        setattr(agent_obj, variable, getattr(agent_obj, func_name)(getattr(runtime_context, parameter)))
        
    elif (hasattr(MODEL, func_name)):
      if (hasattr(agent_obj, parameter)):
        setattr(agent_obj, variable, getattr(MODEL, func_name)(getattr(agent_obj, parameter)))
      elif (hasattr(MODEL, parameter)):
        setattr(agent_obj, variable, getattr(MODEL, func_name)(getattr(MODEL, parameter)))
      elif (hasattr(runtime_context, parameter)):
        setattr(agent_obj, variable, getattr(MODEL, func_name)(getattr(runtime_context, parameter)))
        
    elif (hasattr(runtime_context, func_name)):
      if (hasattr(agent_obj, parameter)):
        setattr(agent_obj, variable, getattr(runtime_context, func_name)(getattr(agent_obj, parameter)))
      elif (hasattr(MODEL, parameter)):
        setattr(agent_obj, variable, getattr(runtime_context, func_name)(getattr(MODEL, parameter)))
      elif (hasattr(runtime_context, parameter)):
        setattr(agent_obj, variable, getattr(runtime_context, func_name)(getattr(runtime_context, parameter)))
        
    setattr(runtime_context, agent_name, agent_obj)
        
  check_agent_obj = getattr(runtime_context, agent_name)
  assert hasattr(runtime_context, agent_name) and hasattr(check_agent_obj, variable)
  
@when(u'the {agent_name:S} agent attribute {variable:S} is the result of routine {func_name:S} with attributes {parameters:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is the result of routine {func_name:S} with variables {parameters:S}' )
@when(u'the {agent_name:S} agent attribute {variable:S} is equal to the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} is equal to the result of routine {func_name:S} with variables {parameter:S}')
@when(u'the {agent_name:S} agent attribute {variable:S} equals the result of routine {func_name:S} with attributes {parameter:S}')
@when(u'the {agent_name:S} agent variable {variable:S} equals the result of routine {func_name:S} with variables {parameter:S}')
def step_impl(context, agent_name, variable, func_name, parameters):
  parameters_list = parameters.split(',')
  if (hasattr(runtime_context, agent_name)):
    agent_obj = getattr(runtime_context, agent_name)
    
    if (hasattr(agent_obj, func_name)):
      for parameter in parameters_list: 
        if (hasattr(agent_obj, parameter)):
          parameter = getattr(agent_obj, parameter)
        elif (hasattr(MODEL, parameter)):
          parameter = getattr(MODEL, parameter)
        elif (hasattr(runtime_context, parameter)):
          parameter = getattr(runtime_context, parameter)
      setattr(agent_obj, variable, getattr(agent_obj, func_name)(*parameters_list))
      
    elif (hasattr(MODEL, func_name)):
      for parameter in parameters_list: 
        if (hasattr(agent_obj, parameter)):
          parameter = getattr(agent_obj, parameter)
        elif (hasattr(MODEL, parameter)):
          parameter = getattr(MODEL, parameter)
        elif (hasattr(runtime_context, parameter)):
          parameter = getattr(runtime_context, parameter)
      setattr(agent_obj, variable, getattr(MODEL, func_name)(*parameters_list))
        
    elif (hasattr(runtime_context, func_name)):
      for parameter in parameters_list: 
        if (hasattr(agent_obj, parameter)):
          parameter = getattr(agent_obj, parameter)
        elif (hasattr(MODEL, parameter)):
          parameter = getattr(MODEL, parameter)
        elif (hasattr(runtime_context, parameter)):
          parameter = getattr(runtime_context, parameter)
      setattr(agent_obj, variable, getattr(runtime_context, func_name)(*parameters_list))
      
    setattr(runtime_context, agent_name, agent_obj)
        
  check_agent_obj = getattr(runtime_context, agent_name)
  assert hasattr(runtime_context, agent_name) and hasattr(check_agent_obj, variable)
  
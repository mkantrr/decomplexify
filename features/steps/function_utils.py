from importlib import reload
from types import MethodType

from globals import indent, deindent, MODEL, runtime_context, model_dict_write, operator_dict
import generated_functions
import agent_classes
from behave import *

# -------------- BEGIN REGULAR ROUTINES --------------------
@given(u'a routine called {func_name:S}')
@given(u'a routine called {func_name:S}')
def step_impl(context, func_name):
  context.indent = [str(), 0]
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + "def {func_name}():\n".format(
      func_name=func_name
  ))
  func_file.close()
  context.indent = indent(context.indent)
  context.prev_indent = context.indent

@given(u'a routine called {func_name:S} with attribute {parameter:S}')
@given(u'a routine called {func_name:S} with variable {parameter:S}')
def step_impl(context, func_name, parameter):
  context.indent = str()
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + "def {func_name}({parameter}):\n".format(
      func_name=func_name,
      parameter=parameter
  ))
  func_file.close()
  context.indent = indent(context.indent)
  context.prev_indent = context.indent
  
@given(u'a routine called {func_name:S} with attributes {parameters:S}')
@given(u'a routine called {func_name:S} with variables {parameters:S}')
def step_impl(context, func_name, parameters):
  context.indent = [str(), 0]
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + "def {func_name}({parameters}):\n".format(
      func_name=func_name,
      parameters=parameters
  ))
  func_file.close()
  context.indent = indent(context.indent)
  context.prev_indent = context.indent
  
@when(u'it has an attribute {variable:S} that is {value:S}')
@when(u'it has a variable {variable:S} that is {value:S}')
@when(u'it has an attribute {variable:S}={value:S}')
@when(u'it has a variable {variable:S}={value:S}')
@when(u'it has an attribute {variable:S} = {value:S}')
@when(u'it has a variable {variable:S} = {value:S}')
@when(u'it has an attribute {variable:S} equal to {value:S}')
@when(u'it has a variable {variable:S} equal to {value:S}')
def step_impl(context, variable, value):
  if (value in model_dict_write.keys()):
    value = model_dict_write[value]
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + '{variable} = {value}\n'.format(
    variable=variable,
    value=value
  ))
  func_file.close()
  if (context.indent != context.prev_indent):
    context.indent = context.prev_indent
    
@when('something needs to be done for all things in {item}')
def step_impl(context, item):
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + 'for thing in {value}:\n'.format(
    value=model_dict_write[item]
  ))
  func_file.close()
  context.prev_indent = context.indent
  context.indent = indent(context.indent)
  
@when(u'the condition {item1:S} {operator:S} {item2:S} is met')
def step_impl(context, item1, operator, item2):
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + 'if ({item1} {operator} {item2}):\n'.format(
    item1=item1,
    operator=operator_dict[operator],
    item2=item2
  ))
  func_file.close()
  context.prev_indent = context.indent
  context.indent = indent(context.indent)
  
@when(u'the condition {item1:S} {operator:S} {item2:S} is not met')
def step_impl(context, item1, operator, item2):
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + 'if not ({item1} {operator} {item2}):\n'.format(
    item1=item1,
    operator=operator_dict[operator],
    item2=item2
  ))
  func_file.close()
  context.prev_indent = context.indent
  context.indent = indent(context.indent) 
  
@when(u'it is true that {condition}')
def step_impl(context, condition):
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + 'if ({condition}):\n'.format(
    condition=model_dict_write[condition]
  ))
  func_file.close()
  context.prev_indent = context.indent
  context.indent = indent(context.indent) 
  
@when(u'it is not true that {condition}')
def step_impl(context, condition):
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + 'if not ({condition}):\n'.format(
    condition=model_dict_write[condition]
  ))
  func_file.close()
  context.prev_indent = context.indent
  context.indent = indent(context.indent) 
  
@when(u'the previous condition is no longer considered')
def step_impl(context):
  context.prev_indent = context.indent
  context.indent = deindent(context.indent)


@when('the result of {func_name} is {expression}')
@when('the result of {func_name} equals {expression}')
@when('{func_name} results in {expression}')
@when('{func_name} returns {expression}')
@when('{func_name} yields {expression}')
def step_impl(context, func_name, expression):
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + 'return {expression}\n'.format(expression=expression))
  func_file.close()
  if (context.indent != context.prev_indent):
    context.indent = context.prev_indent
    
@then('routine {func_name} is finished')
@then('the routine {func_name} is finished')
def step_impl(context, func_name):
  context.indent = [str(), 0]
  context.prev_indent = context.indent
  reload(generated_functions)
  setattr(runtime_context, func_name, getattr(__import__('generated_functions'), func_name))
  assert hasattr(runtime_context, func_name) and callable(getattr(runtime_context, func_name))

# --------------- END REGULAR ROUTINES ---------------------

# --------------- BEGIN MODEL ROUTINES ---------------------
@given(u'a model routine called {func_name:S}')
@given(u'a model routine called {func_name:S}')
def step_impl(context, func_name):
  context.indent = [str(), 0]
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + "def {func_name}(self: AgentBasedModel):\n".format(
      func_name=func_name
  ))
  context.indent = indent(context.indent)
  context.prev_indent = context.indent
  func_file.write(context.indent[0] + "global MODEL\n")
  func_file.close()

@given(u'a model routine called {func_name:S} with attribute {parameter:S}')
@given(u'a model routine called {func_name:S} with variable {parameter:S}')
def step_impl(context, func_name, parameter):
  
  context.indent = [str(), 0]
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + "def {func_name}(self: AgentBasedModel, {parameter}):\n".format(
      func_name=func_name,
      parameter=parameter
  ))
  context.indent = indent(context.indent)
  context.prev_indent = context.indent
  func_file.write(context.indent[0] + "global MODEL\n")
  func_file.close()
  
@given(u'a model routine called {func_name:S} with attributes {parameters:S}')
@given(u'a model routine called {func_name:S} with variables {parameters:S}')
def step_impl(context, func_name, parameters):
  context.indent = [str(), 0]
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + "def {func_name}(self: AgentBasedModel, {parameters}):\n".format(
      func_name=func_name,
      parameters=parameters
  ))
  context.indent = indent(context.indent)
  context.prev_indent = context.indent
  func_file.write(context.indent[0] + "global MODEL\n")
  func_file.close()
  
@when(u'it has an attribute {variable:S} that is the model attribute {value:S}')
@when(u'it has a variable {variable:S} that is model variable {value:S}')
@when(u'it has an attribute {variable:S} equal to the model attribute {value:S}')
@when(u'it has a variable {variable:S} equal to the model variable {value:S}')
def step_impl(context, variable, value):
  if (hasattr(MODEL, value)):
    func_file = open('generated_functions.py', 'a')
    func_file.write(context.indent[0] + '{variable} = self.model.{value}\n'.format(
      variable=variable,
      value=value
  ))
  func_file.close()
  if (context.indent != context.prev_indent):
    context.indent = context.prev_indent
  
@then('model routine {func_name} is finished')
@then('the model routine {func_name} is finished')
def step_impl(context, func_name):
  context.indent = [str(), 0]
  context.prev_indent = context.indent
  reload(generated_functions)
  setattr(MODEL, func_name, 
          MethodType(getattr(__import__('generated_functions'), func_name), MODEL))
  assert hasattr(MODEL, func_name) and callable(getattr(MODEL, func_name))

  
# ---------------- END MODEL ROUTINES ----------------------

# --------------- BEGIN AGENT ROUTINES ---------------------
@given(u'a {agent_name} agent routine called {func_name:S}')
@given(u'an {agent_name} agent routine called {func_name:S}')
def step_impl(context, agent_name, func_name):
  context.indent = [str(), 0]
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + "def {func_name}(self):\n".format(
      func_name=func_name
  ))
  context.indent = indent(context.indent)
  context.prev_indent = context.indent
  func_file.write(context.indent[0] + "global MODEL\n")
  func_file.close()

@given(u'a {agent_name} agent routine called {func_name:S} with attribute {parameter:S}')
@given(u'a {agent_name} agent routine called {func_name:S} with variable {parameter:S}')
@given(u'an {agent_name} agent routine called {func_name:S} with attribute {parameter:S}')
@given(u'an {agent_name} agent routine called {func_name:S} with variable {parameter:S}')
def step_impl(context, agent_name, func_name, parameter):
  context.indent = [str(), 0]
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + "def {func_name}(self, {parameter}):\n".format(
      func_name=func_name,
      parameter=parameter
  ))
  context.indent = indent(context.indent)
  context.prev_indent = context.indent
  func_file.write(context.indent[0] + "global MODEL\n")
  func_file.close()
  
@given(u'a {agent_name} agent routine called {func_name:S} with attributes {parameters:S}')
@given(u'a {agent_name} agent routine called {func_name:S} with variables {parameters:S}')
@given(u'an {agent_name} agent routine called {func_name:S} with attributes {parameters:S}')
@given(u'an {agent_name} agent routine called {func_name:S} with variables {parameters:S}')
def step_impl(context, agent_name, func_name, parameters):
  context.indent = [str(), 0]
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent[0] + "def {func_name}(self, {parameters}):\n".format(
      func_name=func_name,
      parameters=parameters
  ))
  context.indent = indent(context.indent)
  context.prev_indent = context.indent
  func_file.write(context.indent[0] + "global MODEL\n")
  func_file.close()
  
@when(u'it has an attribute {variable:S} that is the {agent_name:S} agent attribute {value:S}')
@when(u'it has a variable {variable:S} that is the {agent_name:S} agent variable {value:S}')
@when(u'it has an attribute {variable:S} equal to the {agent_name:S} agent attribute {value:S}')
@when(u'it has a variable {variable:S} equal to the {agent_name:S} agent variable {value:S}')
def step_impl(context, variable, agent_name, value):
  if (hasattr(getattr(runtime_context, agent_name), value)):
    func_file = open('generated_functions.py', 'a')
    func_file.write(context.indent[0] + '{variable} = self.{value}\n'.format(
      variable=variable,
      value=value
  ))
  func_file.close()
  if (context.indent != context.prev_indent):
    context.indent = context.prev_indent
  
@then(u'the {agent_name:S} agent routine {func_name:S} is finished')
@then(u'{agent_name:S} agent routine {func_name:S} is finished')
def step_impl(context, agent_name, func_name):
  context.indent = [str(), 0]
  context.prev_indent = context.indent
  reload(generated_functions)
  reload(agent_classes)
  setattr(getattr(runtime_context, agent_name), func_name,
    MethodType(
      getattr(__import__('generated_functions'), func_name), 
      getattr(__import__('agent_classes'), agent_name)))
  
  assert hasattr(getattr(runtime_context, agent_name), func_name) and \
    callable(getattr(getattr(runtime_context, agent_name), func_name))
  
# ---------------- END AGENT ROUTINES ----------------------
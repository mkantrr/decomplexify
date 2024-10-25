from globals import runtime_context

from behave import *

def indent(indent):
  indent = indent + '  '
  return indent

def deindent(indent):
  indent = indent[:-2]
  return indent

@given(u'a routine called {func_name:S}')
@given(u'a routine called {func_name:S}')
def step_impl(context, func_name):
  context.indent = str()
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent + "def {func_name}():\n".format(
      func_name=func_name
  ))
  func_file.close()
  context.indent = indent(context.indent)

@given(u'a routine called {func_name:S} with attribute {parameter:S}')
@given(u'a routine called {func_name:S} with variable {parameter:S}')
def step_impl(context, func_name, parameter):
  context.indent = str()
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent + "def {func_name}({parameter}):\n".format(
      func_name=func_name,
      parameter=parameter
  ))
  func_file.close()
  context.indent = indent(context.indent)
  
@given(u'a routine called {func_name:S} with attributes {parameters:S}')
@given(u'a routine called {func_name:S} with variables {parameters:S}')
def step_impl(context, func_name, parameters):
  context.indent = str()
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent + "def {func_name}({parameters}):\n".format(
      func_name=func_name,
      parameters=parameters
  ))
  func_file.close()
  context.indent = indent(context.indent)
  
@when('it has a attribute {variable} that is {value}')
@when('it has a variable {variable} that is {value}')
@when('it has a attribute {variable}={value}')
@when('it has a variable {variable}={value}')
@when('it has a attribute {variable} = {value}')
@when('it has a variable {variable} = {value}')
@when('it has a attribute {variable} equal to {value}')
@when('it has a variable {variable} equal to {value}')
def step_impl(context, variable, value):
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent + '{variable} = {value}\n'.format(
    variable=variable,
    value=value
  ))
  func_file.close()

@then('the result of {func_name} is {expression}')
@then('the result of {func_name} equals {expression}')
@then('{func_name} results in {expression}')
@then('{func_name} returns {expression}')
@then('{func_name} yields {expression}')
def step_impl(context, func_name, expression):
  func_file = open('generated_functions.py', 'a')
  func_file.write(context.indent + 'return {expression}\n'.format(expression=expression))
  func_file.close()
  setattr(runtime_context, func_name, getattr(__import__('generated_functions'), func_name))
  assert hasattr(runtime_context, func_name) and callable(getattr(runtime_context, func_name))
  
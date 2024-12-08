from types import MethodType

import globals

from behave import *
from mesa.time import *

@when('the agents are activated one at a time') 
def step_impl(context):
  globals.MODEL.schedule = BaseScheduler(globals.MODEL)
  
  setattr(globals.MODEL, "step",
    MethodType(globals.step_no_data, globals.MODEL))
  
  assert hasattr(globals.MODEL, "step") and isinstance(globals.MODEL.schedule, BaseScheduler)
  
@when('the agents are activated in random order')
def step_impl(context):
  globals.MODEL.schedule = RandomActivation(globals.MODEL)
  
  setattr(globals.MODEL, "step",
    MethodType(globals.step_no_data, globals.MODEL))

  assert hasattr(globals.MODEL, "step") and isinstance(globals.MODEL.schedule, RandomActivation)
 
@when('the agents are activated in simultaneous order')
def step_impl(context):
  globals.MODEL.schedule = SimultaneousActivation(globals.MODEL)
  
  setattr(globals.MODEL, "step",
    MethodType(globals.step_no_data, globals.MODEL))

  assert hasattr(globals.MODEL, "step") and isinstance(globals.MODEL.schedule, SimultaneousActivation)
 
# ------ FUNCTIONALITY TOO COMPLEX FOR CURRENT VERSION OF DECOMPLEXIFY ----- 
#@when('the agents are activated in order of stages')
#def step_impl(context):
#  globals.MODEL.schedule = StagedActivation(globals.MODEL)
#  
#  setattr(globals.MODEL, "step",
#    MethodType(globals.step_no_data, globals.MODEL))
#
#  assert hasattr(globals.MODEL, "step") and isinstance(globals.MODEL.schedule, StagedActivation)
#  
#@when('the agents are activated in random order by type')
#def step_impl(context):
#  globals.MODEL.schedule = RandomActivationByType(globals.MODEL)
#  
#  setattr(globals.MODEL, "step",
#    MethodType(globals.step_no_data, globals.MODEL))
#
#  assert hasattr(globals.MODEL, "step") and isinstance(globals.MODEL.schedule, RandomActivationByType)
from globals import MODEL

from behave import *
from mesa.time import *

@when('the agents are activated one at a time') 
def step_impl(context):
  MODEL.schedule = BaseScheduler(MODEL)
  assert isinstance(MODEL.schedule, BaseScheduler)
  
@when('the agents are activated in random order')
def step_impl(context):
  MODEL.schedule = RandomActivation(MODEL)
  assert isinstance(MODEL.schedule, RandomActivation)
 
@when('the agents are activated in simultaneous order')
def step_impl(context):
  MODEL.schedule = SimultaneousActivation(MODEL)
  assert isinstance(MODEL.schedule, SimultaneousActivation)
  
@when('the agents are activated in order of stages')
def step_impl(context):
  MODEL.schedule = StagedActivation(MODEL)
  assert isinstance(MODEL.schedule, StagedActivation)
  
@when('the agents are activated in random order by type')
def step_impl(context):
  MODEL.schedule = RandomActivationByType(MODEL)
  assert isinstance(MODEL.schedule, RandomActivationByType)
import uuid

from models import AgentBasedModel, AgentInModel
from globals import MODEL

from behave import *


@given('an agent-based model')
@given('a model')
def step_impl(context):
  MODEL = AgentBasedModel()
  assert MODEL is not None
  
@then('the model has {num_agents} agents')
@then('there are {num_agents} agents in the model')
@then('there are {num_agents} agents')
@then('the number of agents={num_agents}')
@then('the number of agents = {num_agents}')
@then('the number of agents equals {num_agents}')
def step_impl(context, num_agents):
  MODEL.N = int(num_agents)
  for i in range(MODEL.N):
    agent = AgentInModel(uuid.uuid4().int, MODEL)
    MODEL.schedule.add(agent)
  assert len(MODEL.agents) == MODEL.N
  
import uuid

from models import AgentBasedModel
from globals import runtime_context, MODEL

from behave import *


@given('an agent-based model')
@given('a model')
def step_impl(context):
  MODEL = AgentBasedModel()
  assert MODEL is not None
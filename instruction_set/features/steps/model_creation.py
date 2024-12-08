import uuid

from models import AgentBasedModel
import globals

from behave import *


@given('an agent-based model')
@given('a model')
def step_impl(context):
  globals.MODEL = AgentBasedModel()
  globals.runtime_context.model_reporters = {} 
  globals.runtime_context.agent_reporters = {} 
  assert globals.MODEL is not None
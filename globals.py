#globals.py
from features.models import AgentBasedModel

def indent(indent):
  indent = indent + '  '
  return indent

def deindent(indent):
  indent = indent[:-2]
  return indent

class Context:
  """Object for storing context"""
  def __init__(self):
    pass
  
def init():
  global MODEL
  MODEL = AgentBasedModel()
  global runtime_context
  runtime_context = Context()
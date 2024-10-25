from mesa import Model, Agent

class AgentBasedModel(Model):
  """ Base defined model to be modified."""
  def __init__(self):
    super().__init__()
    
class AgentInModel(Agent):
  """ Base defined agent interacting in model to be modified. """
  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
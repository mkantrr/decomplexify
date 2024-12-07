from behave.__main__ import Runner
class AgentBasedModelingRunner(Runner):
      
    def order(self, section):
      feature = section.filename.split('/')[-1]
      return self.ORDER[feature]
      
    def feature_locations(self):
      locations = super().feature_locations()
      print(locations)
      
      self.ORDER = {'routines.feature' : 0,
                    'model.feature' : 1,
                    'model_routines.feature' : 2,
                    'agents.feature' : 3,
                    'agent_routines.feature' : 4,
                    'running.feature': 5
      }
      locations.sort(key=self.order)
      return locations
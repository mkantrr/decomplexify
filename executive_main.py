import sys
import os

import globals

from behave.__main__ import Configuration, run_behave, Runner

def setup_files():
  func_file = open('generated_functions.py', 'w')
  func_file.write("from globals import MODEL\n")
  func_file.write("from features.models import AgentBasedModel\n")
  func_file.write("import sys\n")
  func_file.write("sys.modules['os']=None\n")
  func_file.write("sys.modules['subprocess']=None\n")
  func_file.write("sys.modules['matplotlib']=None\n")
  func_file.close()
  agent_file = open('agent_classes.py', 'w')
  agent_file.write("from globals import MODEL\n")
  agent_file.write("from mesa import Agent\n")
  agent_file.close()
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
      #for location in locations:
      #  if location.filename.endswith("model.feature"):
      #    ordered_locations.insert(0, location)
      #  elif location.filename.endswith("routine.feature"):
      #    ordered_locations.insert(1, location)
      #  else:
      #    ordered_locations.append(location)
      return locations


def main():
    orig_stdout = sys.stdout
    f = open('out.txt', 'w')
    sys.stdout = f
    
    globals.init()
    
    setup_files() 
    config = Configuration(verbose=True)
    retval = run_behave(config, runner_class=AgentBasedModelingRunner)
    
    #os.remove('features/steps/generated_functions.py')
    #os.remove('features/steps/agent_classes.py')
    
    sys.stdout = orig_stdout
    f.close()
    
    return retval


if __name__ == '__main__':
    sys.exit(main())
import sys
import os

import globals

from behave.__main__ import Configuration, run_behave, Runner



class AgentBasedModelingRunner(Runner):
      
    def order(self, section):
      if section.filename.endswith(self.ORDER[0]):
        return 0
      elif section.filename.endswith(self.ORDER[1]):
        return 1
      elif section.filename.endswith(self.ORDER[2]):
        return 2
      elif section.filename.endswith(self.ORDER[3]):
        return 3
      
    def feature_locations(self):
      locations = super().feature_locations()
      
      self.ORDER = ['model.feature', 'routine.feature', 'agent.feature', 'running.feature'] 
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
    
    open('generated_functions.py', 'w').close()
    agent_file = open('agent_classes.py', 'w')
    agent_file.write("from mesa import Agent\n")
    agent_file.close ()
    
    config = Configuration(verbose=True)
    retval = run_behave(config, runner_class=AgentBasedModelingRunner)
    
    #os.remove('features/steps/generated_functions.py')
    #os.remove('features/steps/agent_classes.py')
    
    sys.stdout = orig_stdout
    f.close()
    
    return retval


if __name__ == '__main__':
    sys.exit(main())
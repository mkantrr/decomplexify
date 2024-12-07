import sys
import os

import globals
from behave_runner import AgentBasedModelingRunner

from behave.__main__ import Configuration, run_behave

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
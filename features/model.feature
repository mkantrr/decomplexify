Feature: Create the agent-based model.

  Scenario: Define the model 
     Given an agent-based model
      When the agents are activated in random order
       And the model attribute "x" is x
       And the model attribute "num_agents" is 50
       And the model variable "t" is 1
      Then the model has 50 agents

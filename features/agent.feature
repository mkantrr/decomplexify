@agent.definition
Feature: Define agents within the model.

  Scenario: Define an agent
     Given a Useful agent
      When the Useful agent attribute x is the result of routine compute_this
      Then put 50 Useful agents in the model 

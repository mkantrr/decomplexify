Feature: Create model routines.

  Scenario: Define a routine
     Given a model routine called compute_me
      When it has a variable x that is 50
       And the result of compute_me is x * 100
      Then the model routine compute_me is finished
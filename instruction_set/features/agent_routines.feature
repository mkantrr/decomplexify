Feature: Create agent routines.

  Scenario: Define a routine
     Given a Useful agent routine called compute_it
      When it has a variable x that is 50
       And the result of compute_it is x * 100
      Then the Useful agent routine compute_it is finished
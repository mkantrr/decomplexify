Feature: Create routines.

  Scenario: Define a routine
     Given a routine called compute_this
      When it has a variable x that is 50
       And the result of compute_this is x * 100
      Then the routine compute_this is finished
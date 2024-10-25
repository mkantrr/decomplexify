@function.definition
Feature: Create routines.

  Scenario: Define a routine
     Given a routine called compute_this
      When it has a variable x that is 50
      Then the result of compute_this is x * 100

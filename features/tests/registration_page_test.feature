# Created by johnharchar at 6/25/24
Feature: Registration Page Test
  # Enter feature description here

  Scenario: Verify information can be input into registration page
    Given Open the registration page
    When Enter full name
    Then Enter phone number
    Then Enter email
    Then Enter password
    Then Enter company name
    Then Select country
    Then Select company size
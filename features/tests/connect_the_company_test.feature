# Created by johnharchar at 7/2/24
Feature: Connect the Company test
  # Enter feature description here

  Scenario: Verify Connect the compnay button opens the correct page
    Given Open the main page
    When Enter email and password to login
    Then Click on Connect the Company button
    Then Switch to company window
    Then Verify correct page is open
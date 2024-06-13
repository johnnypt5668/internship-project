# Created by johnharchar at 5/28/24
Feature: Secondary Page Test
  # Enter feature description here

  Scenario: Verify Secondary pages can be accessed by user
    Given Open the main page
    When Enter email and password to login
    #Then Click on Secondary button
    Then Click on mobile Secondary button
    And Verify Secondary page is open
    Then Go to final page using pagination button
    Then Return to first page using pagination button
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

  Scenario: User can filter Secondary page by "want to sell" option
    Given Open the main page
    When Enter email and password to login
    Then Click on mobile Secondary button
    And Verify Secondary page is open
    Then Click on Filters tab
    And Filter by Want to sell
    And Click Apply Filter at page bottom
    Then Confirm all properties have For sale tag

  Scenario: Use can filter Secondary page by 'want to buy' option
    Given Open the main page
    When Enter email and password to login
    Then Click on mobile Secondary button
    And Verify Secondary page is open
    Then Click on Filters tab
    And Filter by Want to buy
    And Click Apply Filter at page bottom
    Then Confirm all properties have Want to buy tag
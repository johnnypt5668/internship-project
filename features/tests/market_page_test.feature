# Created by johnharchar at 12/12/24
Feature: Market page test
  # Enter feature description here

  Scenario: Verify user can open market page and click thru companies
    Given Open the main page
    When Enter email and password to login
    Then Click on market button on left side of page
    And Verify market page is open
    Then Go to final market page using pagination button
    Then Return to first market page using pagination button
    # Enter steps here
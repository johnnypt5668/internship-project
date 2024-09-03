# Created by johnharchar at 9/1/24
Feature: User Guide page test
  # Enter feature description here

  Scenario: Verify user can open User Guide page
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    And Click on User Guide button
    Then Verify User Guide page opened
# Created by johnharchar at 9/22/24
Feature: Support Page test
  # Enter feature description here

  Scenario: Verify Support page opens and features are available
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    And Click on Support button
    Then Switch to Support page
    And Verify Support page opened
    And Switch back to Settings page
    Then Click on News button
    And Verify News page opened
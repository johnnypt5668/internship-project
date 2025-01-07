# Created by johnharchar at 1/7/25
Feature: Verification page test
  # Enter feature description here

  Scenario: User can click on verifications settings option and verify the right page opens
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    And Click on Verification button
    Then Confirm Verification page opened
    And Verify Upload image button is available
    And Verify Next step button is available

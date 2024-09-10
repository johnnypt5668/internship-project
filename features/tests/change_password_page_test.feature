# Created by johnharchar at 9/10/24
Feature: Change Password page tests
  # Enter feature description here

  Scenario: Verify user can change password
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    And Click on Change password button
    Then Verify Change password page is open
    Then Enter and confirm new password
    And Verify Change paasword button is clickable
# Created by johnharchar at 9/17/24
Feature: Subscription Page test
  # Enter feature description here

  Scenario: Verify Subscription page is functioning properly for user
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    And CLick on Subscription button
    Then Verify Subscription page is open
    And Verify Subscription & payments header
    And Verify Back button is available
    And Verify Upgrade plan button is available
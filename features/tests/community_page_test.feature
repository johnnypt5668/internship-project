# Created by johnharchar at 8/22/24
Feature: Community page test# Enter feature name here
  # Enter feature description here

  Scenario: Verify user can open the community page
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    And Click on the Community button
    And Verify Community page is open
    And Verify Support button is clickable
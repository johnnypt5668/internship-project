# Created by johnharchar at 11/11/24
Feature: Off Plan Page test
  # Enter feature description here

  Scenario: Verify user can page through off plan selections
    Given Open the main page
    When Enter email and password to login
    Then Click on off plan button
    And Verify off plan page is open
    Then Go to final off page listings using pagination button
    Then Return to first off page listings using pagination button
    # Enter steps here
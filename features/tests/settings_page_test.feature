# Created by johnharchar at 8/2/24
Feature: Settings Page test
  # Enter feature description here

  Scenario: Verify user can change items on the Settings page

    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    Then Click on Edit Profile
    Then Input test name
    Then Input test number
    Then Input test company
    Then Verify correct text is in name field
    Then Verify correct text is in phone number field
    Then Verify correct text is in compnay field


  Scenario: Verify language can be changed on the main page to Russian
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    Then Change language to Russiian with button on top right
    Then Verify language has changed to RU


  Scenario: Verify correct number of buttons on Settings page
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    And Verify Settings page opened
    Then Verify number of Settings page buttons
    And Verify Connect the Company button is clickable



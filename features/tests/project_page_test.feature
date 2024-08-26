# Created by johnharchar at 8/17/24
Feature: Project page test
  # Enter feature description here

  Scenario: Verify user can add a project and information can be entered
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    Then Click on Add a Project button
    Then Verify Project page is open
    And Enter name
    And Enter company
    And Enter company role
    And Verify name is in text box
    And Verify company is in text box
    And Verify company role is in text box
    Then Enter company
    And Enter company role
    And Verify name is in text box
    And Verify company is in text box
    And Verify company role is in text box
    Then Enter company age
    And Enter project country
    And Enter project name
    And Enter company phone number
    And Enter company email
    Then Verify Send an application button is clickable
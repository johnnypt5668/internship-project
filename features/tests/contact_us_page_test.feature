# Created by johnharchar at 8/26/24
Feature: Contact Us page test
  # Enter feature description here

  Scenario: Verify user can open the Contact Us page
    Given Open the main page
    When Enter email and password to login
    Then Click on the Settings button
    And Click on the Contact us button
    Then Verify Contact us page is open
    Then Verify social media icons appear
    And Verify Connect the company button on contact us page is clickable
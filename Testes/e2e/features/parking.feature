Feature: Parking Management

  Background:
    Given I am logged in as admin

  Scenario: Add new parking spot
    When I add a new parking spot with following details:
      | plate   | spot  | apartment | block |
      | ABC1234 | A-101 | 101      | A     |
    Then I should see the new parking spot in the list

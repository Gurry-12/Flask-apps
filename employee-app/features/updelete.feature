Feature: Deleting the top-most employee

  Scenario: Deleting the top-most employee from the list
    Given I visit the employee management page
    When I locate the delete button for the top-most employee
    And I click the delete button
    Then I should not see the top-most employee in the list of employee

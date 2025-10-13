Feature: employee Management

  Scenario: Creating a new employee
    Given I am on the create employee page
    When I fill out the form with name "John Doe", age "22", and department "Backend"
    And I submit the form
    Then I should see "John Doe" in the list of employee

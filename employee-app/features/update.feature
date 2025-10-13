Feature: Update employee Information

  Scenario: Updating the top-most employee's details
    Given I visit the employee management page for updating
    When I locate the top-most student
    And I update the employee's details with name "John Smith", age "23", and department "Frontend"
    Then I should see "John Smith" in the list of employee after the update

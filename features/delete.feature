# features/delete.feature

Feature: Delete employee
  @delete_employee
  Scenario: The client wants to delete an existing employee
    Given the client wants to delete an existing employee
    When the client confirms the deletion of the employee
    Then the employee should be removed from the database

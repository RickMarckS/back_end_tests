# features/update.feature

Feature: Update employee
  @update_employee
  Scenario: Check and perform the update of an employee through a form
    Given the client wants to update an existing employee
    When the client fills out the form with the new data
    Then the client submits the form and the employee is updated

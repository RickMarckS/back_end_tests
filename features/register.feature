# features/register.feature

Feature: Register new employee
  @register_employee
  Scenario: Check and perform the registration of a new employee through a form
    Given the client wants to register a new employee
    When the client fills out the form with the data
    Then the client submits the form and the employee is registered

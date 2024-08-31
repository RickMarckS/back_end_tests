# features/query.feature

Feature: Test querying the employee list
  @query_employees
  Scenario: Verify if the query returns a list of employees
    Given the client wants to query the employee list
    When the client makes a query to the database
    Then the response should be a list with the employee data

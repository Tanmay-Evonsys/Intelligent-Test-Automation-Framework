Feature: Loan Application

Scenario: Successful loan submission.
    Given I am on the "https://google.com" page
    When I enter "10000" into the "Amount" field
    And I click on "Submit"
    Then I should see "Under Review" as the application status
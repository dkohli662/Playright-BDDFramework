Feature: Login functionality

    Scenario Outline: Validate login with different user types
      Given user is on the login page
      When user logs in with "<username>" and "<password>"
      Then login should be "<expected_result>"

      Examples:
      | username               | password     | expected_result |
      | newtest231@yopmail.com | Test@123     | pass            |
      | invalid@email.com      | wrongpass    | fail            |

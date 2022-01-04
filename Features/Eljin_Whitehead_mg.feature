Feature:Password syntax validation
  Scenario: Password must be at least six characters or longer
    Given User logs into moneygaming.qa.game account.com
    When User enters valid username and password with a minimum of six characters into password field
    And User presses enter
    Then Website validates password

  Scenario: Password has one number
    Given logs into moneygaming.qa.gameaccount.com
    When User enters a vaild username and password with at least one number into password field
    And User presses enter
    Then User presses enter to validate password

  Scenario: password has one special character
    Given logs into moneygaming.qa.gameaccount.com
    When User enter a valid username into a password with a least one special into password field
    And User presses enter
    Then User presses enter to validate password


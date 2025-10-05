Feature: General search functionality

  Scenario: Searching latest news
    Given the user is on home page
    When the user searches for 'semrush ai'
    And the user selects the 'News' category
    Then the 'News' category should be visually indicated as active
    When the user selects the 'Past 24 hours' time
    Then results should be within 1 day range

  Scenario Outline: Searching video
    Given the user is on home page
    When the user searches for 'semrush ai'
    And the user selects the 'Videos' category
    Then the 'Videos' category should be visually indicated as active
    When the user selects the '<resolution>' resolution
    Then results should include video thumbnail, title, and source

    Examples:
      | resolution |
      | 480p       |
      | 720p       |
      | 1080p      |

  Scenario: Verifying 'Clear all' button
    Given the user is on home page
    When the user searches for 'semrush ai'
    And the user selects the 'Videos' category
    And the user selects the '1080p' resolution
    Then the URL should reflect the '1080p' filter change
    When the user clicks Clear all button
    Then the page should display all types of content
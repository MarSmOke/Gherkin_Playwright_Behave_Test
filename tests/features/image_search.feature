Feature: Image search functionality

  Scenario: Searching images by color
    Given the user is on home page
    When the user searches for 'cats'
    And the user selects the 'Images' category
    Then the 'Images' category should be visually indicated as active
    When the user selects the 'Blue' color
    Then results should include images with 'Blue' accent

  Scenario: Verifying preview data
    Given the user is on home page
    When the user searches for 'cats'
    And the user selects the 'Images' category
    Then the 'Images' category should be visually indicated as active
    And result previews should have the same aspect ratio
    And result previews should include title and source

  Scenario: Searching gifs
    Given the user is on home page
    When the user searches for 'cats'
    And the user selects the 'Images' category
    Then the 'Images' category should be visually indicated as active
    When the user selects the 'GIF' type
    Then results should include only 'GIF'
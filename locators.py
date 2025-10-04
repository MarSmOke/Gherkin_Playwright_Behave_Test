class Locators:
    # URLs
    HOME_PAGE = 'https://ecosia.org/'

    # Search elements
    SEARCH_INPUT = 'input[placeholder="Search the web..."]'
    SEARCH_BUTTON = 'button[type="submit"]'

    # Filters
    CATEGORY = '//a[contains(., "{category}")]'
    TIME_FILTER = 'div[data-test-id="search-filter-freshness"]'
    RESOLUTION_FILTER = 'div[data-test-id="search-filter-resolution"]'
    DURATION_FILTER = 'div[data-test-id="search-filter-videoLength"]'
    FILTER_VALUE = '//span[contains(., "{value}")]'
    NEWS_SEARCH_RESULT = '//div[@class="news__result-wrapper"]'
    NEWS_RESULT_TIME = '//time[@data-test-id="news-result-date"]'

    # Elements
    VIDEO_THUMBNAIL = 'div[data-test-id="result-thumbnail-image"]'
    TITLE = 'h2[data-test-id="result-title"]'
    SOURCE = 'a[data-test-id="result-link"]'

    # Buttons
    CLEAR_ALL = 'button[data-test-id="search-filters-clear"]'
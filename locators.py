class Locators:
    # URLs
    HOME_PAGE = 'https://ecosia.org/' # not in separate file because there is only one

    # Search elements
    SEARCH_INPUT = 'input[placeholder="Search the web..."]'
    SEARCH_BUTTON = 'button[type="submit"]'

    # Filters
    CATEGORY = '//li/a[contains(., "{category}")]'
    TIME_FILTER = 'div[data-test-id="search-filter-freshness"]'
    RESOLUTION_FILTER = 'div[data-test-id="search-filter-resolution"]'
    DURATION_FILTER = 'div[data-test-id="search-filter-videoLength"]'
    FILTER_VALUE = '//span[contains(., "{value}")]'
    NEWS_SEARCH_RESULT = '//div[@class="news__result-wrapper"]'
    NEWS_RESULT_TIME = '//time[@data-test-id="news-result-date"]'
    COLOR_FILTER = 'div[data-test-id="search-filter-color"]'
    TYPE_FILTER = 'div[data-test-id="search-filter-imageType"]'
    COLOR = 'div[title="{color}"]'
    ACCENT = '//article[contains(@style, "1864B3")]'
    IMAGE_SEARCH_RESULTS = '//article[@data-test-id="images-result"]'
    IMAGE_RESULT_DIMENSIONS = '//div[@class="image-result__link-wrapper"]//div[@data-test-id="image-result-dimensions"]'
    IMAGE_RESULT_PREVIEW = '//img[@class="image-result__image"]'

    # Elements
    VIDEO_THUMBNAIL = 'div[data-test-id="result-thumbnail-image"]'
    VIDEO_TITLE = 'h2[data-test-id="result-title"]'
    VIDEO_SOURCE = 'a[data-test-id="result-link"]'
    IMAGE_TITLE = 'h2[class="image-result__details-title"]'
    IMAGE_SOURCE = 'a[class="image-result__details-link"]'
    IMAGE_BADGE = '//a/span[@data-test-id="image-result-badge"]'

    # Buttons
    CLEAR_ALL = 'button[data-test-id="search-filters-clear"]'
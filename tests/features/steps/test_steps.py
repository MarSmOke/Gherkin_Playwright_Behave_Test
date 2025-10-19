from behave import given, when, then
from playwright.sync_api import expect
from locators import Locators
import helpers

@given("the user is on home page")
def navigate_to_homepage(context):
    context.page.goto(Locators.HOME_PAGE)
    context.page.wait_for_load_state('load')  # could use 'networkidle' instead of 'load'

@when("the user searches for '{search_term}'")
def search_for_term(context, search_term):
    context.page.locator(Locators.SEARCH_INPUT).fill(search_term)
    context.page.locator(Locators.SEARCH_BUTTON).click()
    context.page.wait_for_load_state('load')

@when("the user selects the '{category}' category")
def select_category(context, category):
    context.page.locator(Locators.CATEGORY.format(category=category)).click()
    context.page.wait_for_load_state('load')

@when("the user selects the '{value}' time")
def select_time(context, value):
    context.page.locator(Locators.TIME_FILTER).click()
    context.page.locator(Locators.FILTER_VALUE.format(value=value)).click()
    context.page.wait_for_load_state('load')

@then("the '{category}' category should be visually indicated as active")
def verify_active_element(context, category):
    element = context.page.locator(Locators.CATEGORY.format(category=category))
    expect(element).to_have_class('tab tab--highlighted tab--highlight-bar tab--icon')

@then("results should be within 1 day range")
def verify_one_day_range(context):
    results = context.page.locator(Locators.NEWS_SEARCH_RESULT).all()
    # getting this error is a valid result since there are no fresh news for real sometimes
    assert len(results) > 0, "No search results found"
    for i, result in enumerate(results):
        timestamp_element = result.locator(Locators.NEWS_RESULT_TIME)
        if timestamp_element.count() > 0:
            timestamp_text = timestamp_element.text_content()
            if 'hours ago' in timestamp_text:
                continue
            elif 'day' in timestamp_text:
                assert '1 day' in timestamp_text, f"Result {i + 1} is older than 24 hours"
            else:
                continue

@when("the user selects the '{value}' resolution")
def select_resolution(context, value):
    context.page.locator(Locators.RESOLUTION_FILTER).click()
    context.page.locator(Locators.FILTER_VALUE.format(value=value)).click()
    context.page.wait_for_load_state('load')

@then("results should include video thumbnail, title, and source")
def verify_video_elements(context):
    expect(context.page.locator(Locators.VIDEO_THUMBNAIL).first).to_be_visible()
    expect(context.page.locator(Locators.VIDEO_TITLE).first).to_be_visible()
    expect(context.page.locator(Locators.VIDEO_SOURCE).first).to_be_visible()

@when("the user clicks Clear all button")
def clear_all_filters(context):
    context.page.locator(Locators.CLEAR_ALL).click()

@then("the URL should reflect the '{filter_type}' filter change")
def verify_url_filters(context, filter_type):
    current_url = context.page.url
    filter_parameters = helpers.get_all_filter_parameters(current_url)
    found = any(filter_type in values for values in filter_parameters.values())
    assert found, f"URL does not contain {filter_type}. Current parameters: {filter_parameters}"

@then("the page should display all types of content")
def verify_url_no_filters(context):
    current_url = context.page.url
    filter_parameters = helpers.get_all_filter_parameters(current_url)
    assert len(filter_parameters) == 1, f"Filters not cleared" # supposed to be {'q': ['{search_term}']}

@when("the user selects the '{color}' color")
def select_color(context, color):
    context.page.locator(Locators.COLOR_FILTER).click()
    context.page.locator(Locators.COLOR.format(color=color)).click()
    context.page.wait_for_load_state('load')

@then("results should include images with '{color}' accent")
def verify_image_color_accent(context, color):
    image_results = context.page.locator(Locators.IMAGE_SEARCH_RESULTS).all()
    assert len(image_results) > 0, "No image results with accent colors found"
    checked = 0
    matching = 0
    samples = []
    for img in image_results[:10]:
        accent_color = helpers.extract_accent_color(img)
        if accent_color:
            checked += 1
            samples.append(accent_color)
            if color == 'Blue' and helpers.is_blue_range(accent_color):
                matching += 1
    assert checked > 0, "No images with --image-result-accent found"
    # For the selected color, at least 50% should match
    if checked > 0:
        match_rate = (matching / checked) * 100
        assert match_rate >= 50, \
            f"Only {match_rate:.1f}% images match '{color}'"

@then("result previews should have the same aspect ratio")
def verify_aspect_ratio(context):
    preview_height = int(context.page.locator(Locators.IMAGE_RESULT_PREVIEW).first.get_attribute('height'))
    preview_width = int(context.page.locator(Locators.IMAGE_RESULT_PREVIEW).first.get_attribute('width'))
    preview_aspect_ratio = preview_width // preview_height
    dim_text = context.page.locator(Locators.IMAGE_RESULT_DIMENSIONS).first.text_content()
    width, height = helpers.parse_dimensions(dim_text)
    image_aspect_ratio = width // height
    assert preview_aspect_ratio == image_aspect_ratio, "Preview does not match the image"

@then("result previews should include title and source")
def verify_image_elements(context):
    expect(context.page.locator(Locators.IMAGE_TITLE).first).to_be_visible()
    expect(context.page.locator(Locators.IMAGE_SOURCE).first).to_be_visible()

@when("the user selects the '{image}' type")
def select_image_type(context, image):
    context.page.locator(Locators.TYPE_FILTER).click()
    context.page.locator(Locators.FILTER_VALUE.format(value=image)).click()
    context.page.wait_for_load_state('load')

@then("results should include only '{type}'")
def verify_image_type(context, type):
    image_results = context.page.locator(Locators.IMAGE_SEARCH_RESULTS).all()
    assert len(image_results) > 0, "No image results with accent colors found"
    expect(context.page.locator(Locators.IMAGE_BADGE).first).to_have_text(f'{type}')
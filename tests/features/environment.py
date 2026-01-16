from playwright.sync_api import sync_playwright
import allure
from allure_commons.types import AttachmentType

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def before_scenario(context, scenario):
    context.context = context.browser.new_context()
    context.page = context.context.new_page()
    allure.dynamic.title(scenario.name)
    allure.dynamic.description(f'Feature: {scenario.feature.name}')

def after_scenario(context, scenario):
    if scenario.status == 'failed':
        allure.attach(
            context.page.screenshot(),
            name='Screenshot on Failure',
            attachment_type=AttachmentType.PNG
        )

        allure.attach(
            context.page.content(),
            name='Page HTML',
            attachment_type=AttachmentType.HTML
        )

        allure.attach(
            context.page.url,
            name='Current URL',
            attachment_type=AttachmentType.TEXT
        )
    context.page.close()
    context.context.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()
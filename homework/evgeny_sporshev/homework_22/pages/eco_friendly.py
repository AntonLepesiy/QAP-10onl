from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class EcoFriendly(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    def is_page_opened(self):
        return self.find(locator.page_title).text == 'Eco Friendly'

    def is_search_placeholder_shown(self):
        return self.find(locator.search_placeholder)

    def is_search_suggest_shown(self):
        search_suggest = self.find(locator.search_placeholder)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator.body, 'Default welcome msg!'))
        search_suggest.send_keys('ana')
        return self.find(locator.search_suggest)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_later(self):
        # Terra has heard about a cool, new, online To-Do application. She goes to its homepage.
        self.browser.get('http://localhost:8000')

        # She notices that the page title and header mention "To-Do"
        self.assertIn('To-Do Lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Your To-Do List', header_text)

        # She is immediately invited to enter a to-do list item
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item...'
        )

        # She types "Buy more coffee syrups for the office" into a text box.
        input_box.send_keys('Buy more coffee syrups for the office')

        # When she hits enter, the page updates, and now the page lists...
        # "1: Buy peacock feathers" as an item in a to-do list.
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # There is still a text box inviting to add another item.
        # She enters "Use syrups to make myself a vanilla, iced coffee".
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy more coffee syrups for the office' for row in rows),
            'New to-do item did not appear in table.'
        )

        # The page updates again, and now both items are displayed on her list.
        self.fail('Finish user story!')

        # Terra is curious to see if the website will remember her list.
        # At that same moment, she notices some explanatory text saying that the currently listed
        # URL is unique to her currently displayed to-do list.

        # She browses elsewhere, but returns to the previous URL - her to-do list is still there.

        # Satisfied, she closes her browser and gets back to texting Kyle <3
        browser.quit()

if __name__ == '__main__':
    unittest.main()

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_later(self):
        # Terra has heard about a cool, new, online To-Do application. She goes to its homepage.
        self.browser.get("http://localhost:8000")

        # She notices that the page title and header mention "To-Do"
        self.assertIn('To-Do Lists', self.browser.title)
        self.fail('Finish the test')

        # She is immediately invited to enter a to-do list item

        # She types "Buy more coffee syrups for the office" into a text box.

        # When she hits enter, the page updates, and now the page lists...
        # "1: Buy peacock feathers" as an item in a to-do list.

        # There is still a text box inviting to add another item.
        # She enters "Use syrups to make myself a vanilla, iced coffee".

        # The page updates again, and now both items are displayed on her list.

        # Terra is curious to see if the website will remember her list.
        # At that same moment, she notices some explanatory text saying that the currently listed
        # URL is unique to her currently displayed to-do list.

        # She browses elsewhere, but returns to the previous URL - her to-do list is still there.

        # Satisfied, she closes her browser and gets back to texting Kyle <3
        browser.quit()

if __name__ == '__main__':
    unittest.main()

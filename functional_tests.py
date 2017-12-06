#!/usr/bin/env python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_creating_a_new_list_and_retrieve_it_later(self):
        # etwin has had about a cool new online to-do app
        # he goes to checkout its homepage
        self.browser.get('http://localhost:8000')

        # he notices that page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # he is invited to enter a to-do item right away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # he types "Visit space" into the text box
        # (etwin's dream is to go to space)

        # send_keys Selenium's way of typing into input elements
        input_box.send_keys('Visit Space') 

        # when he hits enter, the page updates and now the page lists
        # "1: Visit space" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_name('tr')
        self.assertTrue(
            any(row.text == '1: Visit Space' for row in rows) # returns true if iterble is True
        )

        # there is still a text box inviting him to add another item
        # he enters "Learn programming to build rockets"
        self.fail('Finish the tests')

        # the page updates again and now shows both items on his list.

        # etwin wonders whether the site will remember his list.
        # then he sees that the site has generated a unique URL for him
        # there is some explanatory text to that effect.

        # he visits that URL, his to-do list is still there.

        # satisified, he goes back to sleep.

if __name__ == "__main__":
    unittest.main()
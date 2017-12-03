#!/usr/bin/env python
import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_creating_a_new_list(self):
        # etwin has had about a cool new online to-do app
        # he goes to checkout its homepage
        self.browser.get('http://localhost:8000')

        # he notices that page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # he is invited to enter a to-do item right away

        # he types "Visit space" into the text box
        # (etwin's dream is to go to space)

        # when he hits enter, the page updates and now the page lists
        # "1: Visit space" as an item in a to-do list

        # there is still a text box inviting him to add another item
        # he enters "Learn programming to build rockets"

        # the page updates again and now shows both items on his list.

        # etwin wonders whether the site will remember his list.
        # then he sees that the site has generated a unique URL for him
        # there is some explanatory text to that effect.

        # he visits that URL, his to-do list is still there.

        # satisified, he goes back to sleep.

if __name__ == "__main__":
    unittest.main()
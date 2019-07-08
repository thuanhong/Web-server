import unittest
from selenium import webdriver


class PythonTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8000/")
        
    def test_title_homepage(self):
        self.assertEqual("Home Page", self.driver.title)
        
    def test_button(self):
        btn = self.driver.find_element_by_id('hp')
        btn.click()
        
    def test_vote(self):
        self.test_button()
        self.assertIn("Intek", self.driver.title)
    
    def tearDown(self):
        self.driver.close()
    

if __name__ == '__main__':
    unittest.main()
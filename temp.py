import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


class PythonTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.close()
        
    def test_title_homepage(self):
        driver = self.driver
        self.driver.get("http://127.0.0.1:8000/")
        self.assertEquals("Home Page", driver.title)

if __name__ == '__main__':
    unittest.main()
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class max_length(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_login(self):
        success = True
        wd = self.wd
        wd.get("file:///C:/Users/proko/Documents/GitHub/Zadanie_Piwik/index2%20(2).html")
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("GIYGIBKBIBUYGUTFUTVyjgsiduhuksfdvgdhkfuhskbkdjfbdkjfkbdjnkfjkdbjfn475937485u036050790"
                                                       "kjdkkdbnfdkbkdjfjbfgdfgdfhdfgdfgdhgdghdhdgh")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("JGYbskjgrnldfnlgbkmxfxhlkdgnlkxflngklxfknmglxkdmflnmkdlxkglnk8i359834u9tjdfngkjdfjg"
                                                      "jxfhvnkjdfnkjdbkfjbijgfiionjibnglklvgbnlmclgibjlfigjlifobhfgnklflgnijhoinjgihfihjn"
                                                      "ldfkbdljglbjlignlidjofiodgbijbgoidjpofgbidjofkgtoeirdojitjuwo48te49uti9e5t9ey0r59iy"
                                                      "dfijogidjfoioghidjohjfoidjgboidgjboijofihjoidhjoifogihjoifghjiofoihjoflast")
        #wd.find_element_by_name("submit").click()
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.assertTrue(success)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
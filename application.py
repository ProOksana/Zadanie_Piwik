from selenium.webdriver.chrome.webdriver import WebDriver

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def open_home_page(self):
        wd = self.wd
        wd.get("file:///C:/Users/proko/Documents/GitHub/Zadanie_Piwik/index2%20(2).html")


    def populating_fields(self, fields):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(fields.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(fields.lastname)


    def submit_data(self):
        wd = self.wd
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()


    def destroy(self):
        self.wd.quit()


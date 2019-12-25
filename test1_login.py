from selenium.webdriver.chrome.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class login(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("file:///C:/Users/proko/Documents/GitHub/Zadanie_Piwik/index2%20(2).html")


    def populating_fields(self, wd, firstname, lastname):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)


    def submit_data(self, wd):
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()


    def test_login(self):
        wd = self.wd
        self.open_home_page(wd)
        self.populating_fields(wd, firstname="Oksana", lastname="Prokopek")
        self.submit_data(wd)


    def test_empty_login(self):
        wd = self.wd
        self.open_home_page(wd)
        self.populating_fields(wd, firstname="   ", lastname="   ")
        self.submit_data(wd)


    def test_spec_char(self):
        wd = self.wd
        self.open_home_page(wd)
        self.populating_fields(wd, firstname="d426373!@#$%^&*()_+}{:?><", lastname="d426373!@#$%^&*()_+}{:?><")
        self.submit_data(wd)


    def test_max_length(self):
        wd = self.wd
        self.open_home_page(wd)
        self.populating_fields(wd, firstname="Start khgkudhfuhgkdfhog sldnvgldjnrgjndjlfngbjdnlbjngfnkjngfbkjnkjg73ryehwifhrkghdf"
                                             "sfhvbksbfkuksvbnfkskbfndkndbknkdunfknkdbjfkdurotiguw48t938w4u98tugef948ug9e8r9hu8rth"
                                             "dufhbogudofbuijdotibjoeitjboinjtrnojhtboiejr8ot3 oiwrjgo3ij4oe59hjr0e59jh950hjr9t50h riej"
                                             "eirojgboeirjboijetoibjojgtrnoibjrgoijrjntoietoigjot83u4r5o38409 iwvngoierngoienrooijgierjg"
                                             "ijbgoiejtbiojrtiobjrjtonirjtnoijroijtnoirjtniojoryitnjoityjnoirjtnjrtptjprjthpbeojpteeEND",
                               lastname="Start sfnlbdnflbjidofijtb slkrjgbe djfnbldnlfkblkdgmnlbknijroiobdjgtijcvjbnkjdngkjbngfkbjn"
                                        "dfkbmlkngflbjkgfnnlkfgklmflkgmnlkfmgnmkllfkmgobn ksjdngvkjsnkdvbf fjnvglbdjfnbljnclgbkn"
                                        "djfnbjdngbljndlgknblkdnglkbmldkmnlkndflkbnlgjnlbngfbkdjgkbjkf dlkfbhjldjitglhdjgfblknldkg"
                                        "df;kmblkdgmblkmdglknmlfmdfhbndljtnguheotoy8e5roigj jrglidjflhigdlj ldjgldjigjpdifjgnl djvnfds"
                                        "lsnfvblksnlfsm fdsjbnlsijrojifwoeurjoqw83u4982398ru49i7ytei547yt985ue9y804e58tguoerghero")
        self.submit_data(wd)


    def test_enter_link(self):
        wd = self.wd
        self.open_home_page(wd)
        self.populating_fields(wd, firstname="http://www.montypython.com/", lastname="http://www.montypython.com/")
        self.submit_data(wd)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

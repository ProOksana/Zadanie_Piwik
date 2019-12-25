from selenium.webdriver.chrome.webdriver import WebDriver
import unittest

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
        wd.find_element_by_name("firstname").send_keys("Mickeykdmh;skmedrz;lhm.kfngljxdnflhlbxflkhnxnkgmklcfmgnlk.mfcmngk;cfk.gmnl;fc;k"
                                                       "nmlgk;lcfmg.mnlselfijlshzgkuzdhflglzdjflzgsljijeglijzsldighlbzdnflnzsu45iUHSLDIJGL"
                                                       "IJS JNXFXBD LDFKNGLDIRJGIDJROIncxb vxclnxlodijgodijrhMickeykdmh;skmedrz;lhm.kfngl"
                                                       "jxdnflhlbxflkhnxnkgmklcfmgnlk.mfcmngk;cfk.gmnl;fc;knmlgk;lcfmg.mnlselfijlshzgkuz"
                                                       "dhflglzdjflzgsljijeglijzsldighlbzdnflnzsu45iUHSLDIJGLIJS JNXFXBD LDFKNGLDIRJGID"
                                                       "JROIncxb vxclnxlodijgodijrhdjzvnkjsdn andfnalejvgnljsnrlgdsgjlijdslfigjlijsdji"
                                                       "slijrofsidflisdjlfisj")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Mickeykdmh;skmedrz;lhm.kfngljxdnflhlbxflkhnxnkgmklcfmgnlk.mfcmngk;cfk.gmnl;fc;knmlgk"
                                                      ";lcfmg.mnlselfijlshzgkuzdhflglzdjflzgsljijeglijzsldighlbzdnflnzsu45iUHSLDIJGLIJS "
                                                      "JNXFXBD LDFKNGLDIRJGIDJROIncxb vxclnxlodijgodijrhMickeykdmh;skmedrz;lhm.kfn"
                                                      "gljxdnflhlbxflkhnxnkgmklcfmgnlk.mfcmngk;cfk.gmnl;fc;knmlgk;lcfmg.mnlsel"
                                                      "fijlshzgkuzdhflglzdjflzgsljijeglijzsldighlbzdnflnzsu45iUHSLDIJGLIJS JNXFXBD "
                                                      "LDFKNGLDIRJGIDJROIncxb vxclnxlodijgo"
                                                      "dijrhdjzvnkjsdn andfnalejvgnljsnrlgdsgjlijdslfigjlijsdjislijrofsidflisdjlfisj")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.assertTrue(success)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
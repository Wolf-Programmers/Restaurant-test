import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert

class AppSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        self.driver.get("http://localhost:3000")

    def test_find_restaurant(self):
        driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        driver.get('http://localhost:3000')
        search_bar = driver.find_element(by=By.CSS_SELECTOR, value=".search-bar")
        search_button = driver.find_element(by=By.CSS_SELECTOR, value=".search-icon")
        search_bar.send_keys('Katowice')
        search_button.click()
        time.sleep(3)
        driver.close()

    def test_login(self):
        driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        driver.get('http://localhost:3000/login/')

        search_input1 = driver.find_element(by=By.XPATH, value="""// *[ @ id = "login-form"] / div[1] / input""")
        search_input2 = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/div[2]/input""")

        search_input1.send_keys('manager@wp.pl')
        search_input2.send_keys('test1')

        search_btn = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/button""")
        search_btn.click()
        time.sleep(3)
        driver.close()

    def test_register(self):
        driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        driver.get('http://localhost:3000/register/')

        input_name = driver.find_element(by=By.XPATH, value="""//*[@id="registerName"]""")
        input_email = driver.find_element(by=By.XPATH, value="""//*[@id="registerEmail"]""")
        input_password = driver.find_element(by=By.XPATH, value="""//*[@id="registerPassword"]""")
        input_password2 = driver.find_element(by=By.XPATH, value="""//*[@id="registerPassword2"]""")
        input_phone = driver.find_element(by=By.XPATH, value="""//*[@id="registerPhone"]""")

        input_name.send_keys('testowy')
        input_email.send_keys('test@wp.pl')
        input_password.send_keys('test1')
        input_password2.send_keys('test1')
        input_phone.send_keys('+48101010101')

        search_btn = driver.find_element(by=By.CSS_SELECTOR, value=".btn")
        search_btn.click()
        time.sleep(3)
        driver.close()

    def test_menu_add_position(self):
        driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        driver.get('http://localhost:3000/login/')

        search_input1 = driver.find_element(by=By.XPATH, value="""// *[ @ id = "login-form"] / div[1] / input""")
        search_input2 = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/div[2]/input""")

        search_input1.send_keys('manager@wp.pl')
        search_input2.send_keys('test1')

        search_btn = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/button""")
        search_btn.click()
        time.sleep(3)

        driver.get('http://localhost:3000/manage/menu')
        input_name = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[2]/div/input""")
        input_price = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[3]/div/input""")
        input_weight = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[5]/div/input""")
        input_unit = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[6]/div/input""")
        input_description = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[11]/div/textarea""")
        driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[11]/div/textarea""").clear()

        input_name.send_keys('Makaroni')
        input_price.send_keys('30')
        input_weight.send_keys('500')
        input_unit.send_keys('g')
        driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[8]/div/select/option[2]""").click()
        driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[9]/div/select/option[2]""").click()
        input_description.send_keys('Przepyszne danie')
        search_btn1 = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[12]/button""")
        search_btn1.click()

        time.sleep(3)
        Alert(driver).dismiss()
        driver.close()

    def test_menu_add_menu(self):
        driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        driver.get('http://localhost:3000/login/')

        search_input1 = driver.find_element(by=By.XPATH, value="""// *[ @ id = "login-form"] / div[1] / input""")
        search_input2 = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/div[2]/input""")

        search_input1.send_keys('manager@wp.pl')
        search_input2.send_keys('test1')

        search_btn = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/button""")
        search_btn.click()
        time.sleep(3)

        driver.get('http://localhost:3000/manage/menu')
        driver.execute_script("window.scrollTo(0, 700);")
        time.sleep(1)
        driver.find_element(by=By.XPATH,
                            value="""/html/body/div/div/div/div[3]/div/div/div[2]/div/select/option[2]""").click()
        time.sleep(1)
        input_name = driver.find_element(by=By.XPATH,
                                         value="""/html/body/div/div/div/div[3]/div/div/div[4]/div/input""")
        time.sleep(1)
        driver.find_element(by=By.XPATH,
                            value="""/html/body/div/div/div/div[3]/div/div/div[6]/div/select/option[2]""").click()
        time.sleep(1)
        input_name.send_keys('testowa_nazwa')
        search_btn1 = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[3]/div/div/div[8]/button""")
        search_btn1.click()

        time.sleep(3)
        Alert(driver).dismiss()
        driver.close()

    def test_menu_add_to_menu(self):
        driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        driver.get('http://localhost:3000/login/')

        search_input1 = driver.find_element(by=By.XPATH, value="""// *[ @ id = "login-form"] / div[1] / input""")
        search_input2 = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/div[2]/input""")

        search_input1.send_keys('manager@wp.pl')
        search_input2.send_keys('test1')

        search_btn = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/button""")
        search_btn.click()
        time.sleep(3)

        driver.get('http://localhost:3000/manage/menu')
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(1)
        driver.find_element(by=By.XPATH,
                            value="""/html/body/div/div/div/div[4]/div/div/div[2]/div/select/option[2]""").click()
        time.sleep(1)
        driver.find_element(by=By.XPATH,
                            value="""/html/body/div/div/div/div[4]/div/div/div[4]/div/select/option[2]""").click()
        time.sleep(1)
        driver.find_element(by=By.XPATH,
                            value="""/html/body/div/div/div/div[4]/div/div/div[6]/div/select/option[3]""").click()
        time.sleep(1)
        search_btn1 = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[4]/div/div/div[8]/button""")
        search_btn1.click()

        time.sleep(3)
        Alert(driver).dismiss()
        driver.close()

    def test_add_employee(self):
        driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        driver.get('http://localhost:3000/login/')

        search_input1 = driver.find_element(by=By.XPATH, value="""// *[ @ id = "login-form"] / div[1] / input""")
        search_input2 = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/div[2]/input""")

        search_input1.send_keys('manager@wp.pl')
        search_input2.send_keys('test1')

        search_btn = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/button""")
        search_btn.click()
        time.sleep(3)

        driver.get('http://localhost:3000/manage/emploee')
        input_name = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[2]/div/input""")
        input_lastname = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[3]/div/input""")
        input_number = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[5]/div/input""")
        input_email = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[6]/div/input""")
        input_password = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[8]/div/input""")
        input_wage = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[9]/div/input""")

        input_name.send_keys('Anonim')
        input_lastname.send_keys('Anonimowy')
        input_number.send_keys('+48123456789')
        input_email.send_keys('anonim@anonim.pl')
        input_password.send_keys('test1')
        input_wage.send_keys('3000')
        driver.find_element(by=By.XPATH,
                            value="""/html/body/div/div/div/div[2]/div/div/div[11]/div/select/option[2]""").click()
        driver.find_element(by=By.XPATH,
                            value="""/html/body/div/div/div/div[2]/div/div/div[12]/div/select/option""").click()
        search_btn1 = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div/div[13]/button""")
        search_btn1.click()

        time.sleep(3)

        search_btn2 = driver.find_element(by=By.XPATH, value="""/html/body/div[3]/div/div/div[3]/button""")
        search_btn2.click()
        driver.close()

    def test_order(self):
        driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        driver.get('http://localhost:3000')
        search_bar = driver.find_element(by=By.CSS_SELECTOR, value=".search-bar")
        search_button = driver.find_element(by=By.CSS_SELECTOR, value=".search-icon")
        search_bar.send_keys('Katowice')
        search_button.click()
        time.sleep(3)

        search_btn1 = driver.find_element(by=By.XPATH,
                                          value="""/html/body/div/div/div/div[4]/div/div/div[2]/div/div[6]/a/button""")
        search_btn1.click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(3)

        search_btn2 = driver.find_element(by=By.XPATH,
                                    value="""/html/body/div/div/div/div[2]/div[2]/div/div[1]/div[4]/div[7]/button""")
        search_btn2.click()
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)

        search_btn3 = driver.find_element(by=By.XPATH,
                                          value="""/html/body/div/div/div/div[2]/button""")
        search_btn3.click()
        time.sleep(3)

        search_btn3 = driver.find_element(by=By.XPATH,
                                          value="""/html/body/div[3]/div/div/div[3]/button""")
        search_btn3.click()
        time.sleep(3)
        driver.close()

    def test_add_restaurant(self):
        driver = webdriver.Firefox(executable_path=r"C:\TestFiles\geckodriver.exe")
        driver.get('http://localhost:3000/login/')

        search_input1 = driver.find_element(by=By.XPATH, value="""// *[ @ id = "login-form"] / div[1] / input""")
        search_input2 = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/div[2]/input""")

        search_input1.send_keys('manager@wp.pl')
        search_input2.send_keys('test1')

        search_btn = driver.find_element(by=By.XPATH, value="""//*[@id="login-form"]/button""")
        search_btn.click()
        time.sleep(3)

        driver.get('http://localhost:3000/manage/restaurant')
        search_btn1 = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div[1]/a/button""")
        search_btn1.click()
        input_name = driver.find_element(by=By.XPATH,
                                         value="""/html/body/div/div/div/div[2]/div/div[3]/div/input""")
        input_number = driver.find_element(by=By.XPATH,
                                           value="""/html/body/div/div/div/div[2]/div/div[6]/div/input""")
        input_email = driver.find_element(by=By.XPATH,
                                          value="""/html/body/div/div/div/div[2]/div/div[7]/div/input""")
        input_address = driver.find_element(by=By.XPATH,
                                             value="""/html/body/div/div/div/div[2]/div/div[9]/div/input""")
        input_town = driver.find_element(by=By.XPATH,
                                            value="""/html/body/div/div/div/div[2]/div/div[10]/div/input""")
        input_monday_open = driver.find_element(by=By.XPATH,
                                         value="""/html/body/div/div/div/div[2]/div/div[13]/div/div/div[1]/input""")
        input_monday_close = driver.find_element(by=By.XPATH,
                                         value="""/html/body/div/div/div/div[2]/div/div[13]/div/div/div[2]/input""")
        input_tuesday_open = driver.find_element(by=By.XPATH,
                                                value="""/html/body/div/div/div/div[2]/div/div[14]/div/div/div[1]/input""")
        input_tuesday_close = driver.find_element(by=By.XPATH,
                                                 value="""/html/body/div/div/div/div[2]/div/div[14]/div/div/div[2]/input""")
        input_wednesday_open = driver.find_element(by=By.XPATH,
                                                value="""/html/body/div/div/div/div[2]/div/div[16]/div/div/div[1]/input""")
        input_wednesday_close = driver.find_element(by=By.XPATH,
                                                 value="""/html/body/div/div/div/div[2]/div/div[16]/div/div/div[2]/input""")
        input_thursday_open = driver.find_element(by=By.XPATH,
                                                value="""/html/body/div/div/div/div[2]/div/div[17]/div/div/div[1]/input""")
        input_thursday_close = driver.find_element(by=By.XPATH,
                                                 value="""/html/body/div/div/div/div[2]/div/div[17]/div/div/div[2]/input""")
        input_friday_open = driver.find_element(by=By.XPATH,
                                                value="""/html/body/div/div/div/div[2]/div/div[19]/div/div/div[1]/input""")
        input_friday_close = driver.find_element(by=By.XPATH,
                                                 value="""/html/body/div/div/div/div[2]/div/div[19]/div/div/div[2]/input""")
        input_saturday_open = driver.find_element(by=By.XPATH,
                                                value="""/html/body/div/div/div/div[2]/div/div[20]/div/div/div[1]/input""")
        input_saturday_close = driver.find_element(by=By.XPATH,
                                                 value="""/html/body/div/div/div/div[2]/div/div[20]/div/div/div[2]/input""")
        input_sunday_open = driver.find_element(by=By.XPATH,
                                                value="""/html/body/div/div/div/div[2]/div/div[22]/div/div/div[1]/input""")
        input_sunday_close = driver.find_element(by=By.XPATH,
                                                 value="""/html/body/div/div/div/div[2]/div/div[22]/div/div/div[2]/input""")

        input_name.send_keys('Majorowa2')
        input_number.send_keys('+48123456781')
        input_email.send_keys('anonim2@anonim.pl')
        input_address.send_keys('Szkolna 17')
        input_town.send_keys('Białystok')
        input_monday_open.send_keys('11:11')
        input_monday_close.send_keys('22:22')
        input_tuesday_open.send_keys('11:11')
        input_tuesday_close.send_keys('22:22')
        input_wednesday_open.send_keys('11:11')
        input_wednesday_close.send_keys('22:22')
        input_thursday_open.send_keys('11:11')
        input_thursday_close.send_keys('22:22')
        input_friday_open.send_keys('11:11')
        input_friday_close.send_keys('22:22')
        input_saturday_open.send_keys('11:11')
        input_saturday_close.send_keys('22:22')
        input_sunday_open.send_keys('11:11')
        input_sunday_close.send_keys('22:22')
        driver.find_element(by=By.XPATH,
                           value="""/html/body/div/div/div/div[2]/div/div[4]/div/select/option[2]""").click()
        driver.find_element(by=By.XPATH,
                            value="""/html/body/div/div/div/div[2]/div/div[11]/div/select/option[2]""").click()
        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(3)
        search_btn1 = driver.find_element(by=By.XPATH, value="""/html/body/div/div/div/div[2]/div/div[23]/button""")
        search_btn1.click()

        time.sleep(5)
        Alert(driver).dismiss()
        driver.close()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
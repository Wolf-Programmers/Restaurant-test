import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
     
   def test_title(self):
       driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
       driver.get('http://localhost:3000/login/')

       title = driver.title
       print(title)
       assert title == 'React App'
       driver.quit()
   def test_login(self):
       driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
       driver.get('http://localhost:3000/login/')
       options = webdriver.ChromeOptions()
       options.add_experimental_option('excludeSwitches', ['enable-logging'])
       driver = webdriver.Chrome(options=options)

       path1 = """// *[ @ id = "login-form"] / div[1] / input"""
       search_input1 = driver.find_element(by = By.XPATH, value=path1)
       print(search_input1.get_attribute('placeholder'))

       path2 = """//*[@id="login-form"]/div[2]/input"""
       search_input2 = driver.find_element(by = By.XPATH, value=path2)
       print(search_input2.get_attribute('placeholder'))

       search_input1.send_keys('test@wp.pl')
       search_input2.send_keys('zaq1@WSX')

       path3 = """//*[@id="login-form"]/button"""
       search_btn =  driver.find_element(by = By.XPATH, value=path3)
       search_btn.click()
       driver.close()


main = MainTests()
main.test_tile()
main.test_login()


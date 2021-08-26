import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\james\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")

driver.get("https://career4.successfactors.com/career?company=AMD&site=&lang=en_US&requestParams=HI6UlG%2f%2f00hnC5Aymlm2mJKUEhJ42m1Q3UqCQRCdNPMvKgm66xVEv%2biPLkoITUgIxG66%2bBrXSVe2%0a3XV3TCPoieohoieoy14guugdWq0LP2hg5mLOmTNn5ukbMt5BaYh3WB6zVOUz9IMW2kz24%2bV16%2fot%0aDak6FJTBXh0FG9eEPA8c%2bYFRvak9PoFZrE5yoW6ELDAse8k0drB5dT5XVaj75TY7qftHz%2b%2bXn1%2fb%0aD40UwNQG%2bhIDMOSEkqS52RuP4BHSv%2f3c0HR9NKEuQ0mgI3Jx6MSORrFMEDMH0WG0z1D0RkhUNWvV%0afQK%2fQeUp4GH8QlpSUtMivtIwpq8CYU0Y50ghS6PjpJniTlTZ3atG1WqlEojSNzWT06g6ntx%2fy7LC%0a3FrUCSPpWuuUIf93jPaL2PrsNgzWpZjvD2%2bc%2fS0hTTrutKc%2fMUd5Vg%3d%3d&login_ns=register&career_ns=job_application&career_job_req_id=82927&jobPipeline=Google&_s.crb=jYDowhpux7a5jEkXMiRRHCFXK4f3kcYClpNNRi3iKYg%3d")

driver.implicitly_wait(10)

print("Title of Webpage:",driver.title)

assert "Career Opportunities: Create an Account" in driver.title

links=driver.find_elements_by_tag_name("a")
print("Total number of links:",len(links))
for All_links in links:
    print("All links:",All_links.text)
driver.find_element_by_id("fbclc_userName").send_keys("jamesmchacko1234@gmail.com")
driver.find_element_by_css_selector("#fbclc_emailConf").send_keys("jamesmchacko1234@gmail.com")
driver.find_element_by_xpath("//input[@id='fbclc_pwd']").send_keys("Wecandoit@2015")
driver.find_element_by_name("fbclc_pwdConf").send_keys("Wecandoit@2015")
driver.find_element_by_id("fbclc_fName").send_keys("James")
driver.find_element_by_name("fbclc_lName").send_keys("chacko")

country=driver.find_element_by_id("fbclc_country")
dropdown=Select(country)
print("number of countries Available:",len(dropdown.options))
dropdown.select_by_visible_text("Canada")

All_countries=dropdown.options
for countries in All_countries:
    print(countries.text)

driver.find_element_by_id("dataPrivacyId").click()
driver.find_element_by_id("dlgButton_21:").click()



Email=driver.find_element_by_id("fbclc_emailEnabled").is_selected()
print("Email selected :", Email)

campaign=driver.find_element_by_id("fbclc_campaignEmailEnabled").is_selected()


print("campaign selected :", campaign)

time.sleep(5)

driver.close()

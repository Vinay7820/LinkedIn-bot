from selenium import webdriver
import time


def login_linkedin(myemail, mypassword):

	chromedriver = webdriver.Chrome(executable_path = 'C:\chromedriver_win32\chromedriver.exe')

	url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'

	chromedriver.get(url)

	email = chromedriver.find_element_by_xpath('//*[@id="session_key-login"]')
	email.send_keys(myemailid)


	password = chromedriver.find_element_by_xpath('//*[@id="session_password-login"]')
	password.send_keys(mypassword)


	sign_in = chromedriver.find_element_by_xpath('//*[@id="btn-primary"]')
	sign_in.click()

	time.sleep(10)

	//chromedriver.quit()


login_linkedin('your email','your password')



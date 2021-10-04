import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login, Logout
from util.conf import JIRA_SETTINGS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def app_specific_action(webdriver, datasets):
     page = BasePage(webdriver)
    #if datasets['custom_issues']:
     #   issue_key = datasets['custom_issue_key']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    
     @print_timing("selenium_app_specific_user_login")
     def measure():
         def app_specific_user_login(username='admin', password='admin'):
             login_page = Login(webdriver)
             login_page.delete_all_cookies()
             login_page.go_to()
             login_page.set_credentials(username=username, password=password)
             if login_page.is_first_login():
                 login_page.first_login_setup()
             if login_page.is_first_login_second_page():
                 login_page.first_login_second_page_setup()
             login_page.wait_for_page_loaded()
         app_specific_user_login(username='admin', password='admin')
     measure()

     @print_timing("selenium_app_custom_action")
     def measure():
        @print_timing("selenium_app_custom_action:fill_io_configuration_page")
        def sub_measure_1():
            #page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/{issue_key}")
            #page.wait_until_visible((By.ID, "summary-val"))  # Wait for summary field visible
            #page.wait_until_visible((By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT"))  # Wait for you app-specific UI element by ID selector
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/tenable/admin")
            webdriver.find_element_by_css_selector('#txt_access_key').send_keys('f4235a42ea1e4bc2051ffdf1249877ed2ffa9392fcc53767e66943ce998605c1')
            webdriver.find_element_by_css_selector('#txt_secret_key').send_keys('e3d8c091e4cc4d75044e07338d530cd3e32e2ed18121d8df4052b0a4ecd793cb')
            #WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable(By.XPATH,"//input[@id='tenable_admin_submit']")).click()
            webdriver.find_element_by_xpath("//input[@id='tenable_admin_submit']").click()
        @print_timing("selenium_app_custom_action:fill_io_configuration_page")
        def sub_measure_2():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/tenable/sc/admin")
            webdriver.find_element_by_css_selector('#txt_api_url').send_keys('sc.tenalab.online')
            webdriver.find_element_by_css_selector('#txt_access_key').send_keys('e36ed7bfbfa64399aebc8a5a1d9cfe25')
            webdriver.find_element_by_css_selector('#txt_secret_key').send_keys('0d494b7e5b614916b9cbc93de89e7855')
            webdriver.find_element_by_xpath("//input[@id='tenable_admin_submit']").click()
        sub_measure_1()
        sub_measure_2()
     measure()

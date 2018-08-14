import time
import os
from selenium import webdriver


def main():
    # chrome options
    # 阻止chrome弹窗通知
    options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                               chrome_options=options)
    # 浏览器最大化
    browser.maximize_window()
    print('打开浏览器')
    # 登录页
    print('登录pinterest')
    browser.get('https://www.pinterest.com/login/?referrer=home_page')
    # browser.implicitly_wait(1)
    # 查找登录框DOM并填入账号密码
    browser.find_element_by_id("email").send_keys("huaw.xia@gmail.com")
    browser.find_element_by_id("password").send_keys("xiatian315")
    # 查找登录按钮并模拟点击
    browser.find_element_by_class_name("SignupButton ").click()
    print('登录成功')
    time.sleep(5)
    # 模拟登录完成
    return browser
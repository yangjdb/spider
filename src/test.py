import download
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    # 测试下载
    # with open('../resource/index.html', 'rb') as foo_file:
    #     result = download.spiderDown(foo_file, 'test')

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
    browser.get('https://map.baidu.com')

# Created at 2018/8/3
# Created at 2018/8/3
# selenium + chromeDriver 实现自动登录网站搜索图片

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import download

def mkTwoDirs (path, seachKey):
    title = seachKey.strip().replace('?', '')
    path = path + title
    smallPath = path + '/small'

    flag = 0
    if (not os.path.exists(path)):
        os.makedirs(path)
        os.makedirs(smallPath)
        flag = 1
    else:
        if (not os.path.exists(smallPath)):
            os.makedirs(smallPath)
            flag = 1

    os.chdir(path)
    os.chdir(smallPath)

    return flag

def searchFunc(seachKey, path, page):

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
    browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', chrome_options=options)
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
    # 查找搜索按钮填入关键词并开始搜索
    SearchBtn = browser.find_element_by_class_name("SearchBoxInput")
    SearchBtn.click()
    time.sleep(1)
    SearchBtn.send_keys(seachKey)
    time.sleep(1)
    SearchBtn.send_keys(Keys.RETURN)
    print('开始搜索：' + seachKey)
    time.sleep(5)
    # 目标页加载完成

    # 创建文件夹和缩略图文件夹
    mkTwoDirs(path, seachKey)

    # 计算当前网页滚动条页面数
    js1 = "var q=window.screen.availHeight;return(q)"
    clientScreenHeight = browser.execute_script(js1)
    js2 = "var q=document.body.offsetHeight;return(q)"
    clientBodyHeight = browser.execute_script(js2)
    currentPages = round(clientBodyHeight/clientScreenHeight)

    count = 0
    i = 1

    while (i <= page):
        print('准备扒取第 ' + str(i) + '页')
        initClientHeight = browser.find_element_by_tag_name("body").get_property('clientHeight')
        # 开始下载图片
        count = download.spiderDown(browser.page_source, path)

        # 由于图片是动态加载，模拟浏览器向下滚动加载更多图片
        browser.execute_script('window.scrollBy(0, window.screen.height-220)')
        print('滚动第 ' + str(i) + ' 次')

        i += 1
        # 判断是否加载完
        currentClientHeight = browser.find_element_by_tag_name("body").get_property('clientHeight')

        if (currentClientHeight <= initClientHeight) and (i >= currentPages+1):
            print('已经加载到底部')
            break;
        # 等待加载
        time.sleep(5)

    browser.close()
    print('扒取完成:', count, '张')
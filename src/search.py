import time
import download
import os
from selenium.webdriver.common.keys import Keys


def mkTwoDirs (path):
    smallPath = path + '/' + 'small'

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

def main(browser, seachKeys, path):
    for key in seachKeys:
        browser.get("https://www.pinterest.com")
        browser.implicitly_wait(2)

        SearchBtn = browser.find_element_by_class_name("SearchBoxInput")
        SearchBtn.click()
        SearchBtn.send_keys(key)
        SearchBtn.send_keys(Keys.RETURN)
        print('开始搜索：' + key)
        browser.implicitly_wait(5)

        # 创建文件夹和缩略图文件夹
        title = key.strip().replace('?', '')
        savePath = path + '/' + title
        mkTwoDirs(savePath)

        # 层级递归搜索爬取
        download.spiderDown(browser, browser.current_url, 0, savePath)


    return
# Created at 2018/8/3
# Created at 2018/8/3
# selenium + chromeDriver 实现自动登录网站搜索图片

import fetchKeywords
import login
import search

filePath = None

def main(path):

    # 模拟登陆
    browser = login.main()

    # 读取excel文件想要搜索的关键词
    seachKeys = fetchKeywords.main()

    # 循环返回主页
    # 查找搜索按钮
    # 传入词组批量爬取
    search.main(browser, seachKeys, path)

    return
# Created at 2018/8/3
# selenium + chromeDriver 实现自动登录网站搜索图片

import search

seachKey = '腿环tattoo'
path = 'D:/tattoo/'
page = 5

if __name__ == "__main__":
    htmlCode = search.searchFunc(seachKey, path, page)
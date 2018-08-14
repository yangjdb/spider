
# 以下代码忽略

html = requests.get(url, headers=header, cookies=cookies, proxies=proxy)
html.encoding = 'utf-8'

soup = BeautifulSoup(browser, 'html.parser')

print(soup)  # 输出响应的html对象
print(soup.prettify())  # 使用prettify()格式化显示输出

with open('../resource/index.html', 'rb') as foo_file:
    soup = BeautifulSoup(foo_file.read(), "html.parser")

if (flag == 1 and len(os.listdir(path + title)) >= int(pic_max)):
    print('已经保存完毕，跳过')
    continue21


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
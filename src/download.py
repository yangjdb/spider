# Created at 2018/8/2
# coding=utf-8

import time
import requests
import re

# from bs4 import BeautifulSoup

iterators = [50, 12, 8, 5]
patter = re.compile(r'(https|http):\/\/i.pinimg.com\/originals\/[\w\-\.,@?^=%&:/~\+#]*.(jpg|png|jpeg)(?= 4x)')

sumCount = 0

def downloadImg(src, filePath):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.pinterest.com',
        'Referer': 'https://www.pinterest.com/',
        'Upgrade-Insecure-Requests': '1'
    }

    cookies = {
        'AID': 'AJHaeXJQfdnwcukMSIZItyE7Yh0pl01D1hu_wvQh7AzK-1EzR73Qloc',
        'G_ENABLED_IDPS': 'google',
        '_auth': '1',
        '_b': 'ATfs6U76A4JFa7jd886nY46IpPxUm+E6IwFVu3OqU+NvI+IuCeVpc09Np41dIpuRkpA=',
        '_pinterest_sess': '"TWc9PSZ5QkRreVhWSXBJemdQTVloMjAwVUlyencvT2VKVDVlY0xPNy9HeGxCTEp4QnZwYVZYTTlSQ0FMclNFOWFCZUdIaFRtOGJXUXZYeXVSRzNQdjhmYVByOWFicWxwUnd5NTVCTi9tUElvcWZKVFFSVkMrdGlCOFBoZXNubjREYUJGVGZhd090ZjZBa0dDTzMzVFU0Y242d3A0ZitUMEtNblhYV1RQcEVmYnhiQ09lcU8waDdnVkpEaWVJZlBXR1FVRGgrblBHakV2MEJqT1pZYzY5YzVMK083dVhOaWR3S0Rxdm5vM3JHNG5PcmdJS0hCWGpSazhVZjNPVlJNWFNOYmdhbUNDQUtPUmRCaDBTRlBLaGY1cG9Zd0pVOWRIbHRZUDBSclIvY2wxWUNLYzN4YS9ISzVqYVJsQUh3Slc1NDRTNXZLV21uNm5nKzZXb05KaGE2OGJxWmZTVEFKeldnYXM2VWZpSkpTVnFSdXhlT1dtYWhpaU5kaXM1ZmtXTVVtc2FTU3dTeENJYkxxbHhyVXg5WUU5am13Sk9DNEkrQm56WnRIc0FaRU15S0o1SUVocGtVTFp2ZElZSE9zZDArSnhrd1pJWDlZNTl6UHdYWFByTHRHVE9odUVXSHRFdmg3c3FuRTY4YjRJS0RwRVFSQjBQb3loSWJSRUxrNExsa1VxamM4ZlA1QjhXU1BKdGlNRlhudmo0ZnJWL2U5MFpQUTJuRTFrR1ZmKzdSeUZwbXU1bmxKbU9lU2E2UTRoYmxpcThFMURVcFlYakdXNkhJMFAxajlFbUdQVFU1cEczWU8rMnMvRU4wRm1tcGs1VGFXR28vb2t2SGloY0xkcWFpMWtubnBRWVlndkJnbkt5OElKSG56MHIzQTJPRnZxQTFnWUxnWEt1SEhqMHRHNmJFaExqL0pjS0pKTysrbzRDRUZxVllDa01JRHdXVERCYkxScHBjdHhQTDExNUJKNGpFTGEyaytuOWdCbTFKWEtLQ3Y2b0R3ZXRVM053aU1QQTdDb3pudWJyUlplblY3NmFGVE9RZHV1ekhtMXdXREZJdTlSYUtHV2N6cTJGaWVMSm5vakNyaHNuTjh3eUJkRmJlQWF4JjZEVjVMTE81VHk0SDlYWDBhTEp3MURCS0FlTT0="',
        'bei': 'false',
        'cm_sub': 'allowed',
        'csrftoken': 'VNjw4YEzQbWPFtwsFZYeQiijN1S1jfKc',
        'fba': 'True',
        'fr': '0OxtLFHn3H7oEb3jd..BbYld6...1.0.BbYld6.',
        'logged_out': 'True',
        'sessionFunnelEventLogged': '1'
    }

    proxy = {"http": "http://127.0.0.1:1080", "https": "https://127.0.0.1:1080"}

    count = 0

    while True:  # 一直循环，知道访问站点成功
        try:
            # 以下except都是用来捕获当requests请求出现异常时，
            # 通过捕获然后等待网络情况的变化，以此来保护程序的不间断运行
            if count >= 10:
                print('下载：' + src + ' 失败，请手动下载')
                break
            print('下载：' + src)
            html = requests.get(src, proxies=proxy, timeout=30)
            f = open(filePath, 'wb')
            f.write(html.content)
            f.close()
            break
        except requests.exceptions.SSLError:
            print('SSLError -- please wait 3 seconds')
            count += 1
            time.sleep(3)
        except requests.exceptions.ConnectionError:
            print('ConnectionError -- please wait 3 seconds')
            count += 1
            time.sleep(3)
        except requests.exceptions.ChunkedEncodingError:
            print('ChunkedEncodingError -- please wait 3 seconds')
            count += 1
            time.sleep(3)
        except:
            print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
            count += 1
            time.sleep(3)


def spiderDown(browser, url, iterateIndex, path):
    '''
    :param browser:
    :param url:
    :param iterator:
    :return:
    '''

    # html = requests.get(url, headers=header, cookies=cookies, proxies=proxy)
    # html.encoding = 'utf-8'

    # soup = BeautifulSoup(browser, 'html.parser')

    # print(soup)  # 输出响应的html对象
    # print(soup.prettify())  # 使用prettify()格式化显示输出

    # with open('../resource/index.html', 'rb') as foo_file:
    #     soup = BeautifulSoup(foo_file.read(), "html.parser")

    # if (flag == 1 and len(os.listdir(path + title)) >= int(pic_max)):
    #     print('已经保存完毕，跳过')
    #     continue21

    if iterateIndex >= 3:
        return

    imgList = set()
    urlList = set()
    i = 0

    print('打开URL: ', url)
    browser.get(url)
    # time.sleep(8)
    browser.implicitly_wait(6)

    while True:
        nodes = browser.find_element_by_class_name('gridCentered').find_elements_by_class_name('pinWrapper')
        # nodes = browser.find_element_by_xpath("//div[@class='gridCentered']/").find_elements_by_xpath("//div[@class='pinWrapper']")

        for node in nodes:

            try:
                urlList.add(node.find_element_by_tag_name('a').get_property('href'))
                srcSet = node.find_element_by_tag_name('img').get_property('srcset')
                srcSmall = node.find_element_by_tag_name('img').get_property('src')
                if srcSet and srcSmall:
                    result = patter.search(srcSet)
                    src = result.group(0)
                    filename = src.split(r'/')[-1]
                    filenameSmall = srcSmall.split(r'/')[-1]

                    if not filename:
                        # print(filename, 'error')
                        continue
                    else:
                        if filename not in imgList:
                            imgList.add(filename)
                        else:
                            continue
                        downloadImg(src, path + '/' + filename)
                        downloadImg(srcSmall, path + '/small/' + filenameSmall)
                        global sumCount
                        sumCount += 1
            except:
                continue

        print('已下载：', sumCount)

        if len(urlList) >= iterators[iterateIndex]:
            iterateIndex += 1
            for nestUrl in urlList:
                if nestUrl.find('www.pinterest.com') == -1:
                    continue
                else:
                    spiderDown(browser, nestUrl, iterateIndex, path)
            break
        else:
            i += 1
            browser.execute_script('window.scrollBy(0, window.screen.height-220)')
            print('滚动第 ' + str(i) + ' 次')
            time.sleep(2)
            continue

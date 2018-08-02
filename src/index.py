# Created at 2018/8/2

#coding=utf-8

import requests
import os
from bs4 import BeautifulSoup




path = 'E:/tattoo/'

if __name__ == "__main__":



    url = 'https://www.pinterest.com/search/pins/?q=%E8%85%BF%E7%8E%AFtattoo&rs=rs&eq=&etslf=795&term_meta[]=%E8%85%BF%E7%8E%AFtattoo%7Crecentsearch%7C0'
    # url = 'https://www.google.com.hk/'

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
    # html = requests.get(url, headers=header, cookies=cookies, proxies=proxy)
    # html.encoding = 'utf-8'

    url = 'https://www.pinterest.com/resource/BaseSearchResource/get/'

    result = requests.post(url, {
        'source_url': '/search/pins/?q=%E8%85%BF%E7%8E%AFtattoo&rs=rs&eq=&etslf=795&term_meta[]=%E8%85%BF%E7%8E%AFtattoo%7Crecentsearch%7C0',
        'data': {"options": {"bookmarks": [
            "Y2JVSG81V2sxcmNHRlpWM1J5VFVad1YxWlVSbGhXTVZwSlZGWlZNVlV3TVZkalJFSlhUVzVTVkZWWGN6RldNa3BKVW14S1YxSnNjR2hYVm1ONFpXc3hWMVZ1U2xaaE0wSnpWVzAxUTJWR1pIRlVibVJXVW10d1NGa3dhRWRXVjBWNFUyeFNXbFpGV2pOV01GcExWMWRPUms5V1pGTmhNMEl5Vm1wSmQyVkdUblJXYkdScVVsWmFWMWxzYUVOaFJteFlaRVphYkdKSFVucFhhMXAzVkRGS2RHVkVRbGRXZWtJMFZrZDRXbVF4V2xWUmJGWnBWa1ZhV1ZkV1ZtRmtNVTVIVm14c1lWSlViRlJWYWtwUFRrWmFTR1ZHVGxWTmEzQlhWREZhVjFWc1pFaFVWR3hRWWtaYVNsbHVjRk5pUmtwWllVVnNWMVp0YUROV1J6RlhZekZLV1dGR2FGZE5NRXBFVmtkMFZrMVdUa2RWYmxKT1ZsUldjMWxZY0VOT1JscEhXVE5vVTAxclducFphMmhUVmpGYVJrNVhSbHBpUmxwb1dYcEdVMWRIVGtoUFYyaE9Va1phUjFkV1VrOWhNVkY1VW01T1UxZElRbWhaVkVaTFVqRlNWbFpVUm10U2JIQXdWRlphZDFZeFNYcFVhazVYVWpOb1ZGVlVTa3RTTWtWNllrWmthVmRIYUZKV2JYUlhXVmRKZUZWWWFGWmlXRUp5VkZWU1ZrMXNXblJOVnpsVllsWmFlbFZzYUhOWFIwVjRVMjVhV2xaRldqTlpNVnBQVmxaYWNrOVhiRmRXYmtJelZtdGpNV1F4V1hsU2JGcE9WbFphVlZaclZrdFVNVkpZWlVWMGFrMVdTbGhYYTJSSFlWWmFkVkZ1YUZaaVZFWXpWbFZhWVZOSFVrVldiRlpYWWtWd1VWZFdWbFpPVmxwWFZHeHNhRkp1UWxoVmJHUjZaREZhU0dORmRGaGlSVXBUVlVaUmVFOUZOSGxWV0d4aFZqRlZlRmRXWkZOaE1ERlZVMWhvWVZaRk5YSlVhMUpTVFd4d1JXRXpiRTlTUld3MVYxUktWazVGTlZWVGJYaGFWa1ZGZVZSdE1WSk5iSEJWVkZSQ1RtVnRhSFJVYm5CR1pVVTVWVlJVU2xwaGJYaHhWR3hTVWs1Rk5VVmhSMnhhWldzMWRGZHNVbXRoTURGdVVGUXhPRTU2V1hoWmVrRXdUMVJDYUU1cVRYZGFWRUY0VFhwTk0xcHFRWGhaTWtWNVdXcEJlVTF0V21wT2VrcG9UMFJGTkU1VVVtdFBWRUV4VFhwUmVrOVVZekJhYWtGNFdtcEZNMDlIVW1wYWJVbDRUVVJrYkU1blBUMD06VUhvNWVsTnNWazVqUkZwd1pVUkdWbGRVTVdaTmFsWm1URlJHT0UxSFZtMWFiVkpxV1dwb2FFOUhWVEZPYlZFeVdWUkNhazFIVlhoYVIwNW9UVWRaTTA5WFVUQlphazV0VFhwb2JFNXFSbXROUjFVeFRsUkJlRTVIU1RGWlYwbDRXa2RTYUZwcVZUUlpiVlpzV1dwRmVscG5QVDA9fDg3ZTIwMmFiOWE3MWRlNzBjNmMzMDYxNDlkNmExMjk1MzkyM2ZkODk3ZjUxMDlmZTQ3OTJjY2U5ODAxNjRjMTM="],
                             "article": "null", "auto_correction_disabled": "false", "corpus": "null",
                             "customized_rerank_type": "null", "filters": "null", "page_size": "null", "query": "腿环tattoo",
                             "query_pin_sigs": "null", "redux_normalize_feed": "true", "rs": "rs", "scope": "pins",
                             "source_id": "null"}, "context": {}}
    }, cookies=cookies, proxies=proxy )

    print(result.content)

    exit();


    # index = open('../resource/index.html', 'wb')
    # index.write(html.content)
    # index.close()
    # exit()

    # soup = BeautifulSoup(html.text, 'html.parser')

    # print(soup)  # 输出响应的html对象
    # print(soup.prettify())  # 使用prettify()格式化显示输出

    with open('../resource/index.html', 'rb') as foo_file:
        soup = BeautifulSoup(foo_file.read(), "html.parser")

    title = soup.find('input', class_='SearchBoxInput').get('value')
    title = title.strip().replace('?', '')
    print("准备扒取：" + title)

    path = path + title
    if (os.path.exists(path)):
        flag = 1
    else:
        os.makedirs(path)
        flag = 0
    os.chdir(path)

    # if (flag == 1 and len(os.listdir(path + title)) >= int(pic_max)):
    #     print('已经保存完毕，跳过')
    #     continue

    all_a = soup.find('div', class_='gridCentered').find_all('img', class_='_s3 _3o _2l _40')
    # all_a = soup.find_all('img', class_='_s3 _3o _2l _40')

    count = 0

    for a in all_a:
        src = a.get('src')  # 提取文本
        print(src)
        filename = src.split(r'/')[-1]
        # f = open(filename, 'wb')
        # html = requests.get(src, proxies=proxy)
        # f.write(html.content)
        # f.close()
        count += 1
        print(src)
    print('扒取完成:', count, '张')



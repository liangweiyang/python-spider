# 单线程爬取
# 存储于image100

import requests
import re
from bs4 import BeautifulSoup
import time

address = "https://www.quanjing.com/category/1286521/"
url_list = []
pipei = re.compile('<img.*?lowsrc="(.*?)"')

# 构造url
def get_url_list():
    for i in range(1, 8):
        url = address + str(i) + '.html'
        url_list.append(url)
    return url_list


def run():
    y = 1
    i = 0
    for url in get_url_list():
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, 'lxml')
        divs = str(soup.find_all(attrs={"class": "list"}))  #正则必须是字符串类型
        lianjies = re.findall(pipei, divs)
        for lianjie in lianjies:
            result = requests.get(url=lianjie).content
            with open('E:\py project\quanjingwang\image100\{}.jpg'.format(i), 'wb') as f:
                f.write(result)
            i += 1
            print("第{0}张存储完成".format(i))
        print("******************第{0}页爬取完成*********************".format(y))
        y += 1


if __name__ == '__main__':
    start_time = time.time()
    run()
    print("单线程用时：%f" % (time.time()-start_time))



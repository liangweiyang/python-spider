import requests
import re
import threading

class Tiebatu(threading.Thread):

    #获取每个网页的url
    def get_url_list(self, start, end):
        url_list = []
        string = "https://tieba.baidu.com/p/2256306796?pn="
        for i in range(start, end):
            url = string+str(i)
            url_list.append(url)
        return url_list

    #请求每个url,获取html
    def get_content(self, url):
        response = requests.get(url)
        html = response.text
        return html

    #获取图片链接的列表
    def get_data(self, html):
        pattern = re.compile('<img.*?class="BDE_Image" src="(.*?)" ', re.S | re.I)
        items = re.findall(pattern, html)       #找到每个页面的所有图片链接，返回一个迭代器
        return items

    #开始函数
    def run(self, start, end):
        url_list = self.get_url_list(start, end)    #存储所需要的url
        x = 0
        for url in url_list:
            html = self.get_content(url)
            items = self.get_data(html)
            for item in items:
                jpg = requests.get(item)
                with open('E:\py project\spider\image\{}.jpg'.format(x), 'ab') as f:
                    f.write(jpg.content)
                    x += 1
                    print(x, end=' ')


if __name__ == '__main__':
    image = Tiebatu()
    image.run(1, 5)
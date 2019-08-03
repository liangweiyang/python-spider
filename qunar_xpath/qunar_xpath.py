from lxml import etree
import requests
import csv

url = 'http://bnb.qunar.com/hotcity.jsp'
html = requests.get(url=url).text
xpath_tree = etree.HTML(html)
ul_list = xpath_tree.xpath('//ul[@class="e_city_name clr_after"]')


def production(ul_list):
    i = 1
    for ul in ul_list:
        li_list = ul.xpath('./li')
        # print(len(li_list))
        for li in li_list:
            name = li.xpath('./a/text()')
            url = li.xpath('./a/@href')
            # print(name, url)
            yield zip(name, url)
            i += 1


def consumption(p1):

    print('消费者开始i运行,*************************')
    f = open('result.csv', 'a', encoding='utf-8', newline='')
    writer = csv.writer(f)
    writer.writerow(['name', 'url'])

    print('开始写入文件,*************************')
    while True:
        try:
            content = list(next(p1))
            for name, url in content:
                writer.writerow([name, url])
        except StopIteration:
            f.close()
            print('存储完成，文件关闭!!')
            break


if __name__ == '__main__':
    p1 = production(ul_list)
    consumption(p1)




# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from bs4 import BeautifulSoup
from qunar.items import CityItem

class QunarDemoSpider(scrapy.Spider):
    name = "qunar_demo"     # Scrapy定位(并初始化)spider
    allowed_domains = ["bnb.qunar.com"] # 包含了spider允许爬取的域名(domain)列表(list),域名不在列表中的URL不会被跟进。
    start_urls = ['http://bnb.qunar.com/hotcity.jsp']   # 第一个被获取到的页面的URL将是该列表之一。 后续的URL将会从获取到的数据中提取。

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        ul_list = soup.find_all(attrs={'class':'e_city_name clr_after'})

        for ul in ul_list:
            li_list = ul.find_all(name='li')
            for li in li_list:
                item = CityItem()

                item['name'] = li.find(name='a').get_text()
                item['url'] = li.find(name='a').get('href')
                # print(item['name'], item['url'])
                yield item
                # parse()方法的返回结果可以也仅可以有两种
                # 一种是item或者说是字典，scrapy会将item交给item pipeline去进行后续的处理，包括数据的清洗，存储；
                # 另一种是Request，此时scrapy会将这个请求放入调度器请求队列，后续会对其进行请求解析

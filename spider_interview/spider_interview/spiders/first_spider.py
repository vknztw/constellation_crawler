# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
from ..items import SpiderInterviewItem

class InterviewSpider(scrapy.Spider):
    name = 'vicky'
    start_urls = 'http://astro.click108.com.tw'

    def start_requests(self):
            yield scrapy.Request(url=self.start_urls,
                                 method='GET',
                                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'},
                                 callback=self.parse,
                                 dont_filter=True)

    def parse(self, response):
        res = BeautifulSoup(response.text)
        print("============PAGE ONE============")
        res = res.select('.STAR12_BOX')[0].select('a')
        for star in res:
            star_url_num = int(re.findall(r'star(\d+)', star['href'])[0])  # int把01變1  #[0]取配對到的第一個
            star_url = 'http://astro.click108.com.tw/daily_10.php?iAstro=' + str(star_url_num)
            star_name = star.text
            print(star_name, ':', star_url)
            yield scrapy.Request(url=star_url,
                                 method='GET',
                                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'},
                                 callback=self.parse_detail)
        print("============END OF PAGE ONE============")

    def parse_detail(self, response):
        res_content = BeautifulSoup(response.text)

        date = res_content.select('select#iAcDay')[0].text.split('\n')[1]
        cont_starname = re.findall('..座', res_content.select('div.TODAY_CONTENT')[0].select('h3')[0].text)[0]
        fortune = res_content.select('div.TODAY_CONTENT')[0].text

        interview_item = SpiderInterviewItem()
        interview_item['date'] = date
        interview_item['star_name'] = cont_starname
        interview_item['fortune'] = fortune.replace('\n','')

        yield interview_item

        # print("Date: ", date)
        # print("star name: ", cont_starname)
        # print("Fortune: ", fortune)
        # print("========================================")
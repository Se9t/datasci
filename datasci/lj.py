# -*- coding: utf-8 -*-
import scrapy
class LjSpider(scrapy.Spider):
    name = 'lj'
    start_urls = ['https://hz.lianjia.com/ershoufang/pg']

    def parse(self, response):
        for x in response.css('li.clear'):
            yield {
                'title':x.css('div.title a::text').extract(),
                'info':x.css('div.houseInfo ::text').extract(),
                'location':x.css('div.positionInfo ::text').extract(),
                'totalprice':x.css('div.totalPrice ::text').extract(),
                'unitprice':x.css('div.unitPrice ::text').extract()
            }
        for i in range(101):
            url='https://hz.lianjia.com/ershoufang/pg{}/'.format(i)
            yield response.follow(url,self.parse)

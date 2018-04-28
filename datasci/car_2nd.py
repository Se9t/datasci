# -*- coding: utf-8 -*-
import scrapy
class Car2ndSpider(scrapy.Spider):
    name = 'car_2nd'
    start_urls = ['https://www.xin.com/hangzhou/sn_y2/i1/']
    for i in range(2,51):
        url='https://www.xin.com/hangzhou/sn_y2/i{}/'.format(i)
        start_urls.append(url)
    def parse(self, response):
        for x in response.css('div.across'):
            yield {
                'title':x.css('h2 a::text').extract(),
                'info':x.css('h2+span ::text').extract(),
                'price':x.css('p em::text').extract(),
                'dprice':x.css('span.pay-price ::text').extract()
            }

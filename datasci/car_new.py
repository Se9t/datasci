# -*- coding: utf-8 -*-
import scrapy
import json
class CarNewSpider(scrapy.Spider):
    name = 'car_new'
    start_urls = ['https://appapi.youxinche.com/zz/web/car/zz_list?city_id=3001&city_ename=hangzhou&brand_id=&brand_ename=&dp_range=&mp_range=&page=1']
    for i in range(2,36):
        url='https://appapi.youxinche.com/zz/web/car/zz_list?city_id=3001&city_ename=hangzhou&brand_id=&brand_ename=&dp_range=&mp_range=&page={}'.format(i)
        start_urls.append(url)
    def parse(self, response):
        jd=json.loads(response.text)
        for x in jd['data']['list']:
            yield {
                'brand_id':x['brand_id'],
                'series_id':x['series_id'],
                'mode_id':x['mode_id'],
                'brand_name':x['brand_name'],
                'series_name':x['series_name'],
                'mode_name':x['mode_name'],
                'price':x['price'],
                'dp_price':x['dp_price'],
                'month_price':x['month_price']
            }

# -*- coding: utf-8 -*-
import scrapy
import json
import pandas as pd
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    start_urls = ['https://box.maoyan.com/promovie/api/box/second.json?beginDate=20110101']
    a=pd.period_range('20110102','20180428')
    b=pd.Series(a).astype(str).str.replace('-','').tolist()
    for i in b:
        url='https://box.maoyan.com/promovie/api/box/second.json?beginDate={}'.format(i)
        start_urls.append(url)
    def parse(self, response):
        for x in json.loads(response.text)['data']['list']:
            yield {
                'date':json.loads(response.text)['data']['queryDate'],
                'movieId':x['movieId'],
                'movieName':x['movieName'],
                'releaseInfo':x['releaseInfo'],
                'sumBoxInfo':x['sumBoxInfo'],
                'splitSumBoxInfo':x['splitSumBoxInfo'],
                'splitBoxInfo':x['splitBoxInfo'],
                'splitBoxRate':x['splitBoxRate'],
                'boxInfo':x['boxInfo'],
                'boxRate':x['boxRate'],
                'showInfo':x['showInfo'],
                'showRate':x['showRate'],
                'avgShowView':x['avgShowView'],
                'avgSeatView':x['avgSeatView']
            }
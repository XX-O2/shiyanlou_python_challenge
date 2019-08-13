# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import MultipageCourseItem

class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    allowed_domains = ['github.com']

    @property
    def start_urls(self):
        return ('https://github.com/shiyanlou?tab=repositories',)

    def parse(self, response):
        for course in response.css('div.col-10'):
            item = MultipageCourseItem(
                name = course.css('h3 a::text').extract_first().split(),
                update_time = course.css('relative-time::attr(datetime)').extract_first().split()
)
            #course_url = str(course.css('a.name.codeRepository::attr(href)').extract_first())
            full_course_url = response.urljoin(course.xpath('.//a/@href').extract_first())
            request = scrapy.Request(full_course_url,callback=self.parse_details)
            request.meta['item'] = item
            yield request
        spans = response.xpath('//div[@class="BtnGroup"]/button[@disabled="disabled"]/text()').extract()
        if len(spans)==0:
            next_url = response.xpath('//div[@class="BtnGroup"]/a/@href').extract()[1]
            yield response.follow(next_url,callback=self.parse)
        elif spans[0].strip() == 'Previous':
            next_url = response.xpath('//div[@class="BtnGroup"]/a/@href').extract()[0]
            yield response.follow(next_url,callback=self.parse)

    def parse_details(self,response):
        item = response.meta['item']
        item['commits'] = response.css('span.num.text-emphasized::text').extract()[0].strip()
        item['branches'] = response.css('span.num.text-emphasized::text').extract()[1].strip()
        item['releases'] = response.css('span.num.text-emphasized::text').extract()[2].strip()
        yield item

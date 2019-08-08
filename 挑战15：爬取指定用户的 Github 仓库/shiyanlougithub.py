import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):

    name='shiyanlou-courses'

    @property
    def start_urls(self):

        url_list=['https://github.com/shiyanlou?tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwODowNjo1MyswODowMM4FkpKN&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0zMVQyMDoyMDowMiswODowMM4BzHi1&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0wNFQwMDoxNzo1MyswODowMM4BpCnu&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0wOS0xNlQxMDowNjowMyswODowMM4Bb3Ud&tab=repositories']

        return url_list

    def parse(self,response):
        for course in response.css('div.col-10.col-lg-9.d-inline-block'):
            yield{
            'name':course.css('h3 a::text').extract_first().strip(),
            'update_time':course.css('relative-time::attr(datetime)').extract_first().strip()
            }

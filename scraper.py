import scrapy

class CompanySpider(scrapy.Spider):
    name = "company_spider"
    start_urls = ['http://clovisoncology.com/']

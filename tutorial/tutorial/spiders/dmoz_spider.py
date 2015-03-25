# coding=utf-8
from __future__ import print_function
import scrapy
import django
import json
from datetime import date
from tutorial.items import CarItem, CartypeItem, BrandItem
from fetchcar.models import Brand, CarType


django.setup()


class FetchcarSpider(scrapy.spider.Spider):
	name = "fetchcar"
	start_urls = ["http://cd.gongpingjia.com/used-car/search/"]

	def parse(self, response):
		for sel in response.xpath("//div[@class='car-name']/a/@href").extract():
			url = "http://cd.gongpingjia.com" + sel
			yield scrapy.Request(url, callback=self.parsedeep)

	def parsedeep(self, response):
			pass


class GetinfoSpider(scrapy.spider.Spider):
	name = "getinfo"
	start_urls = ["http://cd.gongpingjia.com/meta-data/brand/"]

	def parse(self, response):
		car_json = json.loads(response.body)
		for car in car_json['data']:
			slug = car['slug']
			if not Brand.objects.filter(name=car['name']):
				item = BrandItem()
				item['name'] = car['name']
				item.save()
			yield scrapy.Request("http://cd.gongpingjia.com/used-car/search/?brand=" + slug, callback=self.secondparse)


	def secondparse(self, response):
		brandname = response.xpath("//span[@class='selector-text']/text()").extract()[0].strip()
		for sel in response.xpath("//ul[@id='selector-small']//a/text()").extract():
			item = CartypeItem()
			if not CarType.objects.filter(name=sel):
				item['name'] = sel
				brand = Brand.objects.filter(name=brandname).first()
				item['brand'] = brand
				item.save()
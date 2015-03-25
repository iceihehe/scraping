# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from fetchcar.models import Car, Brand, CarType

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CarItem(DjangoItem):
	django_model = Car


class BrandItem(DjangoItem):
	django_model = Brand


class CartypeItem(DjangoItem):
	django_model = CarType
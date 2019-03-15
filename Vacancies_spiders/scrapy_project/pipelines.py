# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

#class ZorgnedProjectPipeline(object):
 #   def process_item(self, item, spider):
  #      return item

import csv
from zorgned_project.items import ZorgnedProjectItem


class CSVWriter(object):

    def __init__(self):
        self.item_obj = ZorgnedProjectItem()
        self.csv_file = 'zorginstellingen_output.csv'

    def open_spider(self, spider):
        #for writing headers
        self.fields = self.item_obj.fields.keys()
        with open(self.csv_file, 'w', newline='', encoding='UTF-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(self.fields)

    def process_item(self, item, spider):
        #appending the item
        with open(self.csv_file, 'a', newline='', encoding='UTF-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(item.values())
        return item

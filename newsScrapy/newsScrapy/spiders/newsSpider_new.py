# -*- coding: utf-8 -*-
import os.path
import sys
import re
import scrapy
import time
import calendar
import hashlib
import redis
from tld import get_tld
import json
from datetime import datetime as dt
from datetime import timedelta
from pymongo import MongoClient
from scrapy.conf import settings
from scrapy.selector import Selector
from scrapy.http import Request
from kafka import KafkaConsumer
from dateutil import parser

import requests

reload(sys)
sys.setdefaultencoding('utf-8')

'''%a 英文星期的简写
%A 英文星期的完整拼写
%b 英文月份的简写
%B 英文月份的完整拼写
%c 本地当前的日期与时间
%d 日期数,1-31之间
%H 小时数,00-23之间
%I 小时数,01-12之间
%m 月份,01-12之间
%M 分钟数,01-59之间
%j 本年从第1天开始计数到当天的天数
%w 星期数,0-6之间(0是周日)
%W 当天属于本年的第几周,周一作为一周的第一天进行计算
%x 本地的当天日期
%X 本地的当前时间
%y 年份,0-99之间
%Y 年份的完整拼写
%p am pm
%f 毫秒'''

class NewsSpider(scrapy.Spider):
	name = 'news_crawler_new'
	allowed_domains = []

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}

	rule = {
			'_id': 'inews.hket.com',
			'beforeScript':'',
			'startUrls':['http://inews.hket.com/sran001/%E5%85%A8%E9%83%A8'],
			'allFromOneApiItems': 0,
			'apiScript':'',
			'UrlsApiItems': 0,
			'nextPage': '',
			'maxPage': 0,
			'urlRule': '//a[contains(@href,"hket.com/article")]/@href',
			'isDetailApi': 0,
			'detailRule':{
				'content':'//div[@class="content-content"]/descendant-or-self::*/text() | //div[@id="eti-article-content-body"]/p/descendant-or-self::*/text()',
				'title':'//div[@id="headline"]/text() | //div[@id="eti-article-headline"]/h1/text()',
				'date':'//div[@id="news-date"]/text() | //div[@id="eti-article-functions"]/div/text()',
				'img':'',
				'isTimeStamp': 0,
				'dateScript': 'print(pDateStr); m = re.search(unicode("(\d{4}年\d{1,2}月\d{1,2}日 \d{2}:\d{2})"), pDateStr); pDateStr = m.group(0);',
				'dateFormat': '%Y年%m月%d日 %H:%M',
			},
			'lang':'zh-Hant',
			'st':1
		}


	rules = []
	rules.append(rule)
	# redis_interface = redis.StrictRedis(host=settings.get('REDIS_HOST'), port=6379, db=0, decode_responses=True)
	# mongoClient = MongoClient(host=settings.get('MONGO_HOST'), port=settings.get('MONGO_PORT'))
	# mongoClient.admin.authenticate(settings.get('MONGO_USER'), settings.get('MONGO_PASS'))
	#urls = mongoClient[settings.get('MONGO_DEDUP')]['ptt_cc'].find({'cDate':{'$exists': False}})


	def start_requests(self):
		# consumer = KafkaConsumer(TOPIC, group_id=GROUP_ID, bootstrap_servers=BOOTSTRAP_SERVERS)
		# for message in consumer:
		# 	startCrawl(message.value.decode('UTF-8'))
		rules = self.rules
		for rule in rules:
			print(rule)
			startUrls = rule['startUrls']
			if rule['beforeScript']:
				print(rule['beforeScript'])
				exec rule['beforeScript']

			for url in startUrls:
				r = scrapy.Request(url, self.parseUrl, headers=self.headers)
				r.meta['rule'] = rule
				r.meta['page'] = 0
				yield r


	def parseUrl(self, response):
		dRule = response.meta['rule']
		pageNum = response.meta['page']
		if dRule['allFromOneApiItems'] != 0:
			text = response.body_as_unicode()
			if dRule['apiScript']:
				exec dRule['apiScript']
			jsonResp = json.loads(text)

			items = self.getFieldValue(jsonResp, dRule['allFromOneApiItems'])
			for item in items:
				content = self.getFieldValue(item, dRule['detailRule']['content'])

				title = self.getFieldValue(item, dRule['detailRule']['title'])
				pDateStr = self.getFieldValue(item, dRule['detailRule']['date'])
				url = response.urljoin(self.getFieldValue(item, dRule['detailRule']['url']))

				if dRule['detailRule']['dateScript']:
					exec dRule['detailRule']['dateScript']

				pDate = dt.strptime(pDateStr, dRule['detailRule']['dateFormat'])

				result = {
					'title':title,
					'link': url,
					'pubDate': pDate.strftime('%Y-%m-%d %H:%M:%S'),
					'descripton': content,
					'lang': dRule['lang'],
					'st': dRule['st']
				}

				print(result)
				resItem = []
				resItem.append(result)
				# self.redis_interface.rpush('list-results-google-scraper', json.dumps(resItem))

		else:
			if dRule['UrlsApiItems'] != 0:
				text = response.body_as_unicode()
				if dRule['apiScript']:
					exec dRule['apiScript']
				jsonResp = json.loads(text)

				items = self.getFieldValue(jsonResp, dRule['UrlsApiItems'])
				for item in items:
					link = self.getFieldValue(item, dRule['urlRule'])
					if 'urlTrim' in dRule:
						exec dRule['urlTrim']
					link = response.urljoin(link)

					#print(link)
					l = scrapy.Request(link, self.parseDetail, headers=self.headers)
					l.meta['rule'] = dRule
					yield l

				if dRule['nextPage']:
					if pageNum < dRule['maxPage']:

						if 'nextPageScrip' in dRule:
							exec dRule['nextPageScrip']

						print(nextPageUrls)
						if nextPageUrls:
							nexpageurl = response.urljoin(nextPageUrls[0])
							nextP = scrapy.Request(nexpageurl, self.parseUrl, headers=self.headers)
							nextP.meta['rule'] = dRule
							nextP.meta['page'] = pageNum + 1
							yield nextP
			else:
				print(dRule['urlRule'])
				urls = response.xpath(dRule['urlRule']).extract()
				for link in urls:
					link = response.urljoin(link)
					#print(link)
					if 'urlTrim' in dRule:
						exec dRule['urlTrim']
					l = scrapy.Request(link, self.parseDetail)
					l.meta['rule'] = dRule
					yield l

				if dRule['nextPage']:
					if pageNum < dRule['maxPage']:
						nextPageUrls = response.xpath(dRule['nextPage']).extract()
						#print('xxxxxxxxxxxxxxxxxxxxxxx')
						if 'nextPageScrip' in dRule:
							exec dRule['nextPageScrip']
						print(nextPageUrls)
						if nextPageUrls:
							nexpageurl = response.urljoin(nextPageUrls[0])
							nextP = scrapy.Request(nexpageurl, self.parseUrl, headers=self.headers)
							nextP.meta['rule'] = dRule
							nextP.meta['page'] = pageNum + 1
							yield nextP


	def parseDetail(self, response):
		dRule = response.meta['rule']

		if dRule['isDetailApi'] != 0:
			jsonResp = json.loads(response.body_as_unicode())
			content = self.getFieldValue(jsonResp, dRule['detailRule']['content'])
			title = self.getFieldValue(jsonResp, dRule['detailRule']['title'])
			pDateStr = self.getFieldValue(jsonResp, dRule['detailRule']['date'])
			url = response.urljoin(self.getFieldValue(jsonResp, dRule['detailRule']['url']))

			if dRule['detailRule']['dateScript']:
				exec dRule['detailRule']['dateScript']

			pDate = dt.strptime(pDateStr, dRule['detailRule']['dateFormat'])

			result = {
				'title':title,
				'link': url,
				'pubDate': pDate.strftime('%Y-%m-%d %H:%M:%S'),
				'descripton': content,
				'lang': dRule['lang'],
				'st': dRule['st']
			}

			print(result)
			resItem = []
			resItem.append(result)
			# self.redis_interface.rpush('list-results-google-scraper', json.dumps(resItem))
		else:
			title = response.xpath(dRule['detailRule']['title']).extract()[0]
			content = response.xpath(dRule['detailRule']['content']).extract()

			pDateStrs = response.xpath(dRule['detailRule']['date']).extract()

			pDateStr = pDateStrs[0]

			if dRule['detailRule']['dateScript']:
				#print dRule['detailRule']['dateScript']
				exec dRule['detailRule']['dateScript']

			pDate = dt.strptime(pDateStr, dRule['detailRule']['dateFormat'])

			result = {
				'title':title,
				'link': response.url,
				'pubDate': pDate.strftime('%Y-%m-%d %H:%M:%S'),
				'descripton': re.sub(" +", " ", ' '.join(content)).replace('\t','').replace('\r\n',''),
				'lang': dRule['lang'],
				'st': dRule['st']
			}
			print(result)
			resItem = []
			resItem.append(result)
			# self.redis_interface.rpush('list-results-google-scraper', json.dumps(resItem))


	def getFieldValue(self, jsonObj, fieldName):
		if not fieldName:
			return jsonObj

		fields = fieldName.split('.')

		result = jsonObj
		for field in fields:
			result = result[field]

		return result

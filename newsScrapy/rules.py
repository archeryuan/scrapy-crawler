from pymongo import MongoClient


mongoClient = MongoClient(host='index-server2', port=50000)
mongoClient.admin.authenticate("root", "root")



rule1 = {
		'_id': 'hk.apple.nextmedia.com',
		'beforeScript':'',
		'startUrls':['http://hk.apple.nextmedia.com/enews/realtime/','http://hk.apple.nextmedia.com/realtime/realtimelist/china?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/top?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/news?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/china?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/breaking?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/international?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/finance?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/supplement?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/sports?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/nextplus?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/etw?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/ketchuper?page=top','http://hk.apple.nextmedia.com/realtime/realtimelist/racing?page=top'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 10,
		'urlRule': '//div[@class="RTitem"]/div[@class="RTitemRHS"]/div[@class="text"]/a/@href | //div[@id="enews_fashion"]/div[@id]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="ArticleContent_Inner"]/descendant-or-self::*/text()',
			'title':'//table[@class="LinkTable"]//h1/text()',
			'date':'//span[@class="pub_date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4} \d{1,2}:\d{1,2})", pDateStr); tmp = m.group(0); pDateStr = dt.now().strftime("%Y")+tmp;',
			'dateFormat': '%Y%m%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule2 = {
		'_id': 'www.scmp.com',
		'beforeScript':'',
		'startUrls':['http://www.scmp.com/news/hong-kong/politics','http://www.scmp.com/news/hong-kong/economy','http://www.scmp.com/news/hong-kong/health-environment','http://www.scmp.com/news/hong-kong/law-crime','http://www.scmp.com/news/hong-kong/education-community', 'http://www.scmp.com/china/policies-politics', 'http://www.scmp.com/china/diplomacy-defence', 'http://www.scmp.com/china/money-wealth', 'http://www.scmp.com/china/economy', 'http://www.scmp.com/china/society', 'http://www.scmp.com/technology', 'http://www.scmp.com/thisweekinasia', 'http://www.scmp.com/asia/australasia', 'http://www.scmp.com/asia/diplomacy', 'http://www.scmp.com/asia/east-asia', 'http://www.scmp.com/asia/southeast-asia', 'http://www.scmp.com/asia/south-asia', 'http://www.scmp.com/news/world/united-states-canada', 'http://www.scmp.com/news/world/europe', 'http://www.scmp.com/news/world/middle-east', 'http://www.scmp.com/news/world/americas', 'http://www.scmp.com/news/world/africa', 'http://www.scmp.com/news/world/russia-central-asia', 'http://www.scmp.com/comment/insight-opinion', 'http://www.scmp.com/comment/blogs', 'http://www.scmp.com/comment/letters', 'http://www.scmp.com/business/companies', 'http://www.scmp.com/business/markets', 'http://www.scmp.com/property', 'http://www.scmp.com/business/investor-relations', 'http://www.scmp.com/business/global-economy', 'http://www.scmp.com/topics/special-reports', 'http://www.scmp.com/topics/country-reports', 'http://www.scmp.com/technology/china-tech', 'http://www.scmp.com/technology/enterprises', 'http://www.scmp.com/technology/social-gadgets', 'http://www.scmp.com/technology/start-ups', 'http://www.scmp.com/technology/apps-gaming', 'http://www.scmp.com/technology/innovation', 'http://www.scmp.com/technology/leaders-founders', 'http://www.scmp.com/technology/science-research', 'http://www.scmp.com/technology/e-commerce', 'http://www.scmp.com/lifestyle/fashion-luxury', 'http://www.scmp.com/lifestyle/travel-leisure', 'http://www.scmp.com/lifestyle/motoring', 'http://www.scmp.com/lifestyle/families', 'http://www.scmp.com/lifestyle/food-drink', 'http://www.scmp.com/lifestyle/health-beauty', 'http://www.scmp.com/lifestyle/watches', 'http://www.scmp.com/magazines/style', 'http://www.scmp.com/topics/good-eating', 'http://www.scmp.com/culture/books', 'http://www.scmp.com/culture/music', 'http://www.scmp.com/culture/film-tv', 'http://www.scmp.com/culture/arts-entertainment', 'http://www.scmp.com/magazines/post-magazine/', 'http://www.scmp.com/sport/hong-kong', 'http://www.scmp.com/sport/china', 'http://www.scmp.com/sport/golf', 'http://www.scmp.com/sport/racing', 'http://www.scmp.com/sport/rugby', 'http://www.scmp.com/sport/soccer', 'http://www.scmp.com/sport/tennis', 'http://www.scmp.com/sport/boxing', 'http://www.scmp.com/sport/motorsport'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 10,
		'urlRule': '//article/div/h2/a/@href | //article/div/h3/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="pane-content"]/p/descendant-or-self::*/text()',
			'title':'//h1[@itemprop="name headline"]/text()',
			'date':'//div[@itemprop="dateModified"]/@content',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.split("+")[0]',
			'dateFormat': '%Y-%m-%dT%H:%M:%S',
		},
		'lang':'en',
		'st':1
	}


rule3 = {
		'_id': 'www.ft.com',
		'beforeScript':'',
		'startUrls':['https://www.ft.com/companies'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@data-trackable="next-page"]/@href',
		'maxPage': 10,
		'urlRule': '//ul[@class="o-teaser-collection__list"]/li[@class="o-teaser-collection__item o-grid-row"]//h2[@class="o-teaser__heading"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="article__body n-content-body"]/p/descendant-or-self::*/text()',
			'title':'//h1[@class="article-headline"]/span/text()',
			'date':'//time[@class="article__timestamp o-date"]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.split("Z")[0]',
			'dateFormat': '%Y-%m-%dT%H:%M:%S',
		},
		'lang':'en',
		'st':1
	}

rule4 = {
		'_id': 'orientaldaily.on.cc',
		'beforeScript':'startUrls.append("http://orientaldaily.on.cc/cnt/news/"+dt.now().strftime("%Y%m%d")+"/00186_001.html")',
		'startUrls':['http://orientaldaily.on.cc/cnt/news/index.html','http://orientaldaily.on.cc/cnt/china_world/index.html','http://orientaldaily.on.cc/cnt/finance/index.html','http://orientaldaily.on.cc/cnt/entertainment/index.html','http://orientaldaily.on.cc/cnt/lifestyle/index.html','http://orientaldaily.on.cc/cnt/adult/index.html','http://orientaldaily.on.cc/cnt/sport/index.html'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//ul[@class="commonBigList"]/li/a/@href | //select[@id="articleListSELECT"]/optgroup/option/@value',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="leadin"]/p/text() | //div[@id="contentCTN-right"]/h3/text() | //div[@id="contentCTN-right"]/p/descendant-or-self::*/text()',
			'title':'//div[@id="leadin"]/h1/text()',
			'date':'//div[@id="leadin"]/h1/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{8})", response.url); pDateStr=m.group(0)',
			'dateFormat': '%Y%m%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule5 = {
		'_id': 'hk.on.cc',
		'beforeScript':'startUrl = "http://hk.on.cc/hk/bkn/js/"+ dt.now().strftime("%Y%m%d") +"/news_dailyList.js"; startUrls = []; startUrls.append(startUrl)',
		'startUrls':[''],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': '',
		'nextPage': '',
		'maxPage': 0,
		'urlRule': 'link',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="breakingNewsContent"]/p/descendant-or-self::*/text()',
			'title':'//div[@class="topHeadline"]/h1/text()',
			'date':'//span[@class="datetime"]/descendant-or-self::*/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{17})", response.url); pDateStr=m.group(0)',
			'dateFormat': '%Y%m%d%H%M%S%f',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule6 = {
		'_id': 'news.mingpao.com',
		'beforeScript':'startUrls = []; key=dt.now().strftime("%Y%m%d"); startUrls.append("http://news.mingpao.com/dat/ins/ins_web_tc/feed1/"+key+"/content.js")',
		'startUrls':[''],
		'allFromOneApiItems': "result.rss.channel.item",
		'apiScript':'text = \'{"result":{"rss"\'+ text.split(\'{"rss"\')[1].split("}}}};")[0] + "}}}}"',
		'UrlsApiItems': '',
		'nextPage': '',
		'maxPage': 0,
		'urlRule': 'link',
		'isDetailApi': 0,
		'detailRule':{
			'content':'DESCRIPTION',
			'title':'TITLE',
			'date':'PUBDATE',
			'url': 'LINK',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'contentSelect = Selector(text=content).xpath("//p/text()").extract(); content = re.sub(" +", " ", " ".join(contentSelect)); pDateStr = pDateStr.split("  +")[0]',
			'dateFormat': '%a, %d %b %Y %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule7 = {
		'_id': 'www.soft4fun.net',
		'beforeScript':'',
		'startUrls':['https://www.soft4fun.net/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@class="nextpostslink"]/@href',
		'maxPage': 10,
		'urlRule': '//section/div[@class="clearfloat"]/header/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//span[@itemprop="articleBody"]/text() | //span[@itemprop="articleBody"]/descendant::*/text()',
			'title':'//h1[@class="title"]/span[@itemprop="headline"]/text()',
			'date':'//span[@itemprop="datePublished"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y/%m/%d',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule8 = {
		'_id': 'ithelp.ithome.com.tw',
		'beforeScript':'',
		'startUrls':['http://ithelp.ithome.com.tw/questions', 'http://ithelp.ithome.com.tw/articles'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li/a[@rel="next"]/@href',
		'maxPage': 10,
		'urlRule': '//h3[@class="qa-list__title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="markdown__style"]/p/text()',
			'title':'//h2[contains(@class, "qa-header__title")]/text()',
			'date':'//a[contains(@class, "qa-header__info-time")]/@title',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule9 = {
		'_id': 'www.beephone.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.beephone.com.tw/review.php', 'http://www.beephone.com.tw/report.php', 'http://www.beephone.com.tw/enews/', 'http://www.beephone.com.tw/showtelecomnews.php', 'http://www.beephone.com.tw/showphonenews.php', 'http://www.beephone.com.tw/shownetworksnews.php', 'http://www.beephone.com.tw/show3cnews.php', 'http://www.beephone.com.tw/showmobilenews.php', 'http://www.beephone.com.tw/showbusinessnews.php', 'http://www.beephone.com.tw/showadd-valuenews.php', 'http://www.beephone.com.tw/showinternationalnews.php', 'http://www.beephone.com.tw/showreleasenews.php', 'http://www.beephone.com.tw/showstorenews.php', 'http://www.beephone.com.tw/showpromotionsnews.php'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 10,
		'urlRule': '//a[contains(@href, "shownews.php?id=")]/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//body/table[2]/tr[4]/td[2]/center/table[1]/tr[3]/td[1]/text()',
			'title':'//body/table[2]/tr[4]/td[2]/center/table[1]/tr[2]/td/table/tr[1]/td[1]/descendant::*/text()',
			'date':'//body/table[2]/tr[4]/td[2]/center/table[1]/tr[2]/td/table/tr[2]/td[1]/font/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{2}/\\d{2}).*(\\d{2}:\\d{2})", pDateStr); pDateStr = m.group(1)+ " " + m.group(2)',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule10 = {
		'_id': 'www.cna.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.cna.com.tw/list/aall-1.aspx'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//ul/li/a[contains(.,">>")]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="article_list"]/ul/li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//section[@itemprop="articleBody"]/descendant::*/text()',
			'title':'//h1[@itemprop="headline"]/text()',
			'date':'//div[@class="update_times"]/p[1]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule11 = {
		'_id': 'www.setn.com',
		'beforeScript':'',
		'startUrls':['http://www.setn.com/ViewAll.aspx'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="pager"]/a/span[contains(., "下一頁")]/../@href',
		'maxPage': 100,
		'urlRule': '//div[@class="box"]/ul/li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="Content1"]/descendant::*/text() | //div[@id="Content2"]/descendant::*/text()',
			'title':'//div[@class="title"]/h1/text()',
			'date':'//span[@class="date"]/text() | //div[@class="time"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2}:\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule12 = {
			'_id': 'tw.news.yahoo.com',
			'beforeScript':'',
			'startUrls':['https://tw.news.yahoo.com/_td-news/api/resource/IndexDataService.getExternalMediaNewsList;newsTab=all;start=0;count=200&tag=null?bkt=news-TW-zh-Hant-TW-def&device=desktop&intl=tw&lang=zh-Hant-TW&partner=none&region=TW&site=news&returnMeta=true'],
			'allFromOneApiItems': 0,
			'apiScript':'',
			'UrlsApiItems': 'data',
			'nextPage': '//a[@class="yom-button next"]/@href',
			'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split(";start=")[0] + ";start=" +str((pageNum+1)*200) + ";count=200&tag=null?bkt=news-TW-zh-Hant-TW-def&device=desktop&intl=tw&lang=zh-Hant-TW&partner=none&region=TW&site=news&returnMeta=true")',
			'maxPage': 10,
			'urlRule': 'url',
			'isDetailApi': 0,
			'detailRule':{
				'content':'//article[@itemprop="articleBody"]/div/p/descendant-or-self::*/text()',
				'title':'//h1[@itemprop="headline"]/text()',
				'date':'//time[@datetime]/@datetime',
				'img':'',
				'isTimeStamp': 0,
				'dateScript': 'print("pppp===="+pDateStr); tmpDate=dt.strptime(pDateStr, "%Y-%m-%dT%H:%M:%S.%fZ"); tmpDate=tmpDate+timedelta(hours=8); pDateStr=tmpDate.strftime("%Y-%m-%dT%H:%M:%S.%fZ")',
				'dateFormat': '%Y-%m-%dT%H:%M:%S.%fZ',
			},
			'lang':'zh-Hant',
			'st':1
		}

rule13 = {
		'_id': 'udn.com',
		'beforeScript':'',
		'startUrls':['http://udn.com/news/breaknews/1/99#breaknews','http://udn.com/news/cate/2/6638','http://udn.com/news/cate/2/7227', 'http://udn.com/news/cate/2/7225', 'http://udn.com/news/cate/2/6639', 'http://udn.com/news/cate/2/6644', 'http://udn.com/news/cate/2/6645', 'http://udn.com/news/cate/2/6649', 'http://udn.com/news/cindex/1012', 'http://udn.com/news/cate/2/6643', 'http://udn.com/news/cate/2/6641', 'http://udn.com/news/cate/2/6640', 'http://udn.com/news/cate/2/7226', 'http://udn.com/news/cindex/1013', 'http://udn.com/news/cindex/1014', 'http://udn.com/news/cindex/1015'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="pagelink"]/a[contains(.,"下一頁")]/@href',
		'maxPage': 100,
		'urlRule': '//div[@id="breaknews_body"]/dl/dt/a/@href | //dl[@class="listing"]/dt/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="story_body_content"]/p/text()',
			'title':'//h1[@id="story_art_title"]/text()',
			'date':'//div[@id="story_bady_info"]/h3/text() | //div[@class="story_bady_info_author"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule14 = {
			'_id': 'news.ltn.com.tw',
			'beforeScript':'',
			'startUrls':['http://news.ltn.com.tw/list/breakingnews'],
			'allFromOneApiItems': 0,
			'apiScript':'',
			'UrlsApiItems': 0,
			'nextPage': '//a[@class="p_next"]/@href',
			'maxPage': 100,
			'urlRule': '//li/a[@class="tit"]/@href',
			'isDetailApi': 0,
			'detailRule':{
				'content':'//div[@class="news_p"]/p/text() | //div[@class="cont boxTitle"]/p/text() | //div[@id="newstext"]/p/text() | //div[@class="con"]/p/text() | //div[@id="news_content"]/p/text()',
				'title':'//div[contains(@class, "articlebody")]/h1/text() | //div[@class="conbox"]/h2/text() | //div[@class="conbox"]/h1/text() | //div[@id="content"]/h1/text() | //div[@class="content"]/h1/text() | //div[@class="news_content"]/h1/text()',
				'date':'//div[@itemprop="articleBody"]/span/text() | div[contains(@class, "writer_date")]/text() | //div[@class="c_time"]/text() | //span[@class="h1dt"]/text() | //div[@class="writer"]/span[2]/text() | //div[@id="newstext"]/span/text() | //div[@id="con"]/div[@class="con_writer"]/span[@class]/text() | //div[@class="date"]/text()',
				'img':'',
				'isTimeStamp': 0,
				'dateScript': 'pDateStr = pDateStr.replace("/", "-"); m = re.search("(\\d{4}-\\d{2}-\\d{2}).*(\\d{2}:\\d{2})", pDateStr); pDateStr = m.group(1)+ " " + m.group(2)',
				'dateFormat': '%Y-%m-%d %H:%M',
			},
			'lang':'zh-Hant',
			'st':1
		}


rule15 = {
		'_id': 'www.appledaily.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.appledaily.com.tw/realtimenews/section/new/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//nav[@class="page_switch lisw fillup"]/a[@class="enable"]/following-sibling::a/@href',
		'maxPage': 200,
		'urlRule': '//ul[@class="rtddd slvl"]/li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//p[@id="summary"]/text()',
			'title':'//h1[@id="h1"]/text()',
			'date':'//time[@datetime]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y年%m月%d日%H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule16 = {
		'_id': 'news.tvbs.com.tw',
		'beforeScript':'',
		'startUrls':['http://news.tvbs.com.tw/news/realtime/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="realtime_news_underbtn"]/ul/li/a[contains(.,"下一頁")]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="realtime_news_content_titel1"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="newsdetail-content"]/text()',
			'title':'//p[@class="titel26"]/strong/text()',
			'date':'//div[@class="newsdetail-time1"]/p[@class="under15"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule17 = {
		'_id': 'news.ftv.com.tw',
		'beforeScript':'',
		'startUrls':['http://news.ftv.com.tw/NewsIframe.aspx'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//div[@class="searchlist"]/table/tbody/tr/td/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//span[@id="newscontent"]/text()',
			'title':'//span[@id="ctl00_ContentPlaceHolder1_Label1"]/text()',
			'date':'//span[@id="ctl00_ContentPlaceHolder1_Label2"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule18 = {
		'_id': 'www.nextmag.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.nextmag.com.tw/breaking-news/latest'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//section[@class="list list-main"]/ul[@class="clear"]/li[contains(@aid, "")]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="article-content"]/p/text()',
			'title':'//header[@class="article-header clear"]/h2/text()',
			'date':'//time[@class="time"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y年%m月%d日 %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule19 = {
		'_id': 'www.chinatimes.com',
		'beforeScript':'',
		'startUrls':['http://www.chinatimes.com/realtimenews', 'http://www.chinatimes.com/newspapers/2601', 'http://www.chinatimes.com/newspapers/2602', 'http://www.chinatimes.com/newspapers/2603'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="pagination clear-fix"]/ul/li/a[contains(.,"下一頁")]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="listRight"]/ul/li/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//article[@class="clear-fix"]/p/text()',
			'title':'//article[@class="clear-fix"]/header/h1/text()',
			'date':'//time[@datetime]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y年%m月%d日 %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule20 = {
		'_id': 'www.ettoday.net',
		'beforeScript':'',
		'startUrls':['http://www.ettoday.net/news/news-list.htm'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="menu_page"]/a[contains(.," > ")]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="part_list_2"]/h3/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//section[@itemprop="articleBody"]/p/text() | //div[@class="story"]/p/text()',
			'title':'//h2[@itemprop="headline"]/text() | //h2[@class="title"]/text() | //h1[@class="title"]/text()',
			'date':'//span[@class="news-time"]/text() | //div[@class="date"]/text() | //p[@class="date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y年%m月%d日 %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule21 = {
		'_id': 'news.cts.com.tw',
		'beforeScript':'',
		'startUrls':['http://news.cts.com.tw/real/index.html'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@id="page-bar"]/span/a[@class="btn active"]/../following-sibling::span/a[not(contains(.,"最末頁"))]/@href',
		'maxPage': 100,
		'urlRule': '//div[@id="news_list_block"]/div[@class="single_news block100 bottom_dot clrboth"]/div[@class="news_right"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="article"]/p/text()',
			'title':'//h1[@class="newsbigtitle clrboth block100"]/text()',
			'date':'//div[@class="timebar datenews"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule22 = {
		'_id': 'www.epochtimes.com',
		'beforeScript':'',
		'startUrls':['http://www.epochtimes.com/gb/n24hr.htm'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="menu_page"]/a[contains(.,' > ')]/@href',
		'maxPage': 100,
		'urlRule': '//div[@id="artlist"]/div[@class="posts column"]/div[@class="arttitle column"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="artbody"]/p/text()',
			'title':'//h1[@class="blue18 title"]/text()',
			'date':'//time[@datetime]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.split("+")[0]',
			'dateFormat': '%Y-%m-%dT%H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule23 = {
		'_id': 'news.pchome.com.tw',
		'beforeScript':'',
		'startUrls':['http://news.pchome.com.tw/today'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@id="pages"]/a[contains(.,"下一頁")]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="contbar"]/section/div[@class="channel_newssection"]/p[1]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@calss="article_text"]/text()',
			'title':'//span[@id="iCliCK_SafeGuard"]/text()',
			'date':'//time[@datetime]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule24 = {
		'_id': 'www.ctv.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=1', 'http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=2', 'http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=3', 'http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=4', 'http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=5', 'http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=6', 'http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=7', 'http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=8', 'http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=9', 'http://www.ctv.com.tw/opencms/jsp/insidePage_list.jsp?fid=2&cid=10'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="pageLink"]/a[contains(.,"下一頁")]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="leftside"]/div[@class="listbox"]/h5/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="newsblock"]/p/text()',
			'title':'//div[@class="newsheaderblock"]/h3/text()',
			'date':'//div[@class="newsheaderblock"]/span[@class="newsarea_info"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2}:\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule25 = {
		'_id': 'www.ttv.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.ttv.com.tw/news/catlist/A', 'http://www.ttv.com.tw/news/catlist/C', 'http://www.ttv.com.tw/news/catlist/D', 'http://www.ttv.com.tw/news/catlist/E', 'http://www.ttv.com.tw/news/catlist/F', 'http://www.ttv.com.tw/news/catlist/G', 'http://www.ttv.com.tw/news/catlist/H', 'http://www.ttv.com.tw/news/catlist/I', 'http://www.ttv.com.tw/news/catlist/J', 'http://www.ttv.com.tw/news/catlist/K', 'http://www.ttv.com.tw/news/catlist/L', 'http://www.ttv.com.tw/news/catlist/M', 'http://www.ttv.com.tw/news/catlist/P'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//ul[@class="pagination pagination-md"]/li/a/span[@class="glyphicon glyphicon-forward"]/../a/@href',
		'maxPage': 100,
		'urlRule': '//ul[@class="list_style_none"]/li[@class="ellipsis newsText large"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="br"]/text()',
			'title':'//h1[@class="title"]/text()',
			'date':'//div[contains(@class, "ReportDate")]/a/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}-\\d{1,2}-\\d{1,2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule26 = {
		'_id': 'www.nownews.com',
		'beforeScript':'',
		'startUrls':['http://www.nownews.com/cat/politic', 'http://www.nownews.com/cat/finance', 'http://www.nownews.com/cat/life', 'http://www.nownews.com/cat/society', 'http://www.nownews.com/cat/sport', 'http://www.nownews.com/cat/entertainment', 'http://www.nownews.com/cat/global', 'http://www.nownews.com/cat/china', 'http://www.nownews.com/cat/novelty', 'http://www.nownews.com/cat/fashion', 'http://www.nownews.com/cat/eworld'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//ul[@class="pagination"]/li/a/span[contains(.,">")]/../a/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="media"]/div[@class="media-body"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="body"]/p/text()',
			'title':'//h1[@class="content-title"]/text()',
			'date':'//div[@class="news-info"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}.\\d{1,2}.\\d{1,2}) / \\d{2}:\\d{2}", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y.%m.%d / %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule27 = {
		'_id': 'news.pts.org.tw',
		'beforeScript':'',
		'startUrls':['http://news.pts.org.tw/list/1', 'http://news.pts.org.tw/list/2', 'http://news.pts.org.tw/list/3', 'http://news.pts.org.tw/list/4', 'http://news.pts.org.tw/list/5', 'http://news.pts.org.tw/list/6', 'http://news.pts.org.tw/list/7', 'http://news.pts.org.tw/list/8', 'http://news.pts.org.tw/list/13', 'http://news.pts.org.tw/list/14', 'http://news.pts.org.tw/list/15'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//ul[@class="list-news"]/li[@class="list-news-item"]/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="article-content"]/text()',
			'title':'//h1[@class="article-title"]/text()',
			'date':'//div[@class="list-news-time"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}-\\d{1,2}-\\d{1,2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule28 = {
		'_id': 'www.bcc.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.bcc.com.tw/newsList.%E7%94%9F%E6%B4%BB', 'http://www.bcc.com.tw/newsList.%E6%94%BF%E6%B2%BB', 'http://www.bcc.com.tw/newsList.%E5%9C%8B%E9%9A%9B', 'http://www.bcc.com.tw/newsList.%E5%85%A9%E5%B2%B8', 'http://www.bcc.com.tw/newsList.%E8%B2%A1%E7%B6%93', 'http://www.bcc.com.tw/newsList.%E7%A4%BE%E6%9C%83', 'http://www.bcc.com.tw/newsList.%E9%AB%94%E8%82%B2', 'http://www.bcc.com.tw/newsList.%E5%BD%B1%E8%97%9D', 'http://www.bcc.com.tw/newsList.%E8%BB%BC%E8%81%9E', 'http://www.bcc.com.tw/newsList.%E5%B0%88%E9%A1%8C'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//span[@id="body_body_myNewsList_upList"]/div[@class="ls10"]/div[@class="tt16"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="some-class-name"]/text()',
			'title':'//div[@class="tt26"]/text()',
			'date':'//div[@class="tt27"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{1,2}/\\d{1,2} \\d{2}:\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule29 = {
		'_id': 'www.businessweekly.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.businessweekly.com.tw/newlist.aspx'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[contains(@class, "nextpage")]/a/@href',
		'maxPage': 20,
		'urlRule': '//div[@class="channel_cnt"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="articlebody"]/descendant::*/text()',
			'title':'//header[@class="headline"]/h1/text()',
			'date':'//div[@class="articleDate"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}.\\d{1,2}.\\d{1,2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y.%m.%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule30 = {
		'_id': 'opinion.cw.com.tw',
		'beforeScript':'',
		'startUrls':['http://opinion.cw.com.tw/blog/list'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[@class="pager-next"]/a/@href',
		'maxPage': 20,
		'urlRule': '//span[@class="field-content title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="field-items"]/div/p/text()',
			'title':'//div[@id="main"]/h1/text()',
			'date':'//span[@class="date-display-single"]/@content',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.split("+")[0]',
			'dateFormat': '%Y-%m-%dT%H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule31 = {
		'_id': 'www.managertoday.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.managertoday.com.tw/articles/category/g_personal_growth', 'http://www.managertoday.com.tw/articles/category/g_leader', 'http://www.managertoday.com.tw/articles/category/g_work_career', 'http://www.managertoday.com.tw/articles/category/g_sales_marketing', 'http://www.managertoday.com.tw/articles/category/g_human_resource', 'http://www.managertoday.com.tw/articles/category/g_org_managment', 'http://www.managertoday.com.tw/skills', 'http://www.managertoday.com.tw/columns', 'http://www.managertoday.com.tw/articles/category/g_manager_life'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//div[@class="main-content table-cell fluid"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="row htmlview"]/p/text()',
			'title':'//h1[@class="post-subtitle"]/text()',
			'date':'//div[@class="info"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}-\\d{1,2}-\\d{1,2} \\d{2}:\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule32 = {
		'_id': 'statementdog.com',
		'beforeScript':'',
		'startUrls':['http://statementdog.com/blog/', 'https://statementdog.com/insight'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@class="nextpostslink"]/@href | //span[@class="next"]/a/@href',
		'maxPage': 20,
		'urlRule': '//div[@class="post-main"]/div[contains(@id, "post-")]/div[@class="post-hdr"]/h2/a/@href | //h2[@class="post-title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="post-body"]/p/descendant-or-self::*/text() | //div[@class="comment-content"]/p/text()',
			'title':'//h2[@class="post-title"]/text() | //h2[@class="post-title"]/a/text()',
			'date':'//div[@class="post-meta-in-header"]/span[@class="post-meta"]/text() | //li[@class="tm"][last()]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.replace(" ", ""); m = re.search("(\\d{4}/\\d{1,2}/\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule33 = {
		'_id': 'www.moneydj.com',
		'beforeScript':'',
		'startUrls':['http://www.moneydj.com/KMDJ/Common/ListNewArticles.aspx?svc=NW&a=X0000000'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//td[@class="curpage"]/following-sibling::td/a/@href',
		'maxPage': 20,
		'urlRule': '//td[@class="ArticleTitle"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="highlight"]/article/descendant::*/text() | //div[@id="highlight"]/article/text()',
			'title':'//span[@id="ctl00_ctl00_MainContent_Contents_lbTitle"]/text()',
			'date':'//span[@id="ctl00_ctl00_MainContent_Contents_lbDate"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule34 = {
		'_id': 'money.udn.com',
		'beforeScript':'',
		'startUrls':['http://money.udn.com/money/breaknews/1001', 'http://money.udn.com/rank/newest/1001/5590/1', 'http://money.udn.com/rank/newest/1001/5587/1', 'http://money.udn.com/rank/newest/1001/5588/1', 'http://money.udn.com/rank/newest/1001/5589/1', 'http://money.udn.com/rank/newest/1001/5591/1', 'http://money.udn.com/rank/newest/1001/10160/1', 'http://money.udn.com/rank/newest/1001/5592/1', 'http://money.udn.com/rank/newest/1001/5593/1', 'http://money.udn.com/rank/newest/1001/5595/1', 'http://money.udn.com/rank/newest/1001/5596/1'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="pagelink"]/a[contains(.,"下一頁")]/@href',
		'maxPage': 20,
		'urlRule': '//div[@id="ranking_body"]//a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="story_body_content"]/text() | //div[@id="story_body_content"]/p/text()',
			'title':'//h2[@id="story_art_title"]/text()',
			'date':'//div[@class="story_bady_info_author"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}-\\d{1,2}-\\d{2} \\d{1,2}:\\d{1,2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule35 = {
		'_id': 'money.yam.com',
		'beforeScript':'',
		'startUrls':['http://money.yam.com/news/real'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//li[@class="yamCSSPageNext"]/a/@href',
		'maxPage': 100,
		'urlRule': '//ul[@id="showAll"]/li/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="content"]/p/text()',
			'title':'//h1[@class="article_title"]/text()',
			'date':'//div[@class="source"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode("(\\d{4}年\\d{2}月\\d{2}日).*(\\d{2}:\\d{2})"), pDateStr); pDateStr = m.group(0); pDateStr = pDateStr.replace("下午", "pm ").replace("上午", "am ")',
			'dateFormat': '%Y年%m月%d日 %p %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule36 = {
		'_id': 'www.investor.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.investor.com.tw/onlineNews/TodayNews.asp'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 100,
		'urlRule': '//ul[@class="NEWS_TITLE"]/li[@class="TODAY_NEWS_TITLE"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="highslide-gallery ARTICLES_STYLE"]/p/text()',
			'title':'//li[@class="ARTICLE_TITLE"]/text()',
			'date':'//li[@class="ARTICLE_DATE"]/a/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{2}:\\d{2})", title); pDateStr = pDateStr + " " + m.group(0)',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule37 = {
		'_id': 'www.ithome.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.ithome.com.tw/news'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//a[contains(.,"下一頁 ›")]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="item"]/p[@class="title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="field-item even"]/p/descendant::*/text() | //div[@class="field-item even"]/p/text()',
			'title':'//h1[@class="page-header"]/text()',
			'date':'//span[@class="created"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule38 = {
		'_id': 'www.eprice.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.eprice.com.tw/news/all/1/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="pagelink"]/a[contains(.,"下一頁")]/@href',
		'maxPage': 100,
		'urlRule': '//li[@class="news"]/a[@class="title"]/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@itemprop="description"]/descendant::*/text() | //div[@itemprop="description"]/text()',
			'title':'//h1[@class="title"]/text()',
			'date':'//time[@itemprop="dateCreated"]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.split("+")[0]',
			'dateFormat': '%Y-%m-%dT%H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule39 = {
		'_id': 'www.sogi.com.tw',
		'beforeScript':'',
		'startUrls':['https://www.sogi.com.tw/articles'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//div[@class="info"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="editable"]/descendant::*/text() | //div[@class="editable"]/text()',
			'title':'//h1[@class="fixed-title"]/text()',
			'date':'//div[@class="subtitle"]/small/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{2}/\\d{2})", str(pDateStrs)); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule40 = {
		'_id': 'www.epochtimes.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.epochtimes.com.tw/%E6%9C%80%E6%96%B0%E6%96%87%E7%AB%A0/all/%E5%85%A8%E9%83%A8/p/1'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a/i[@class="td-icon-menu-right"]/../@href',
		'maxPage': 100,
		'urlRule': '//div[@class="td_module_11 td_module_wrap td-animation-stack"]/div[@class="item_inner"]/div[@class="item-details"]/h3/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="td-paragraph-padding-1"]/p/text()',
			'title':'//h1[@class="entry-title"]/text()',
			'date':'//time[@datetime]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule41 = {
		'_id': 'idn.com.tw',
		'beforeScript':'',
		'startUrls':['http://idn.com.tw/news/news_list.php?catid=1', 'http://idn.com.tw/news/news_list.php?catid=2', 'http://idn.com.tw/news/news_list.php?catid=3', 'http://idn.com.tw/news/news_list.php?catid=4', 'http://idn.com.tw/news/news_list.php?catid=5', 'http://idn.com.tw/news/news_list.php?catid=4&catsid=5'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//span/a[@class="btn active"]/../span/a/@href',
		'maxPage': 100,
		'urlRule': '//td[@class="body_9b"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//td[@class="newsa"]/text()',
			'title':'//td[@class="headnewsd"]/text()',
			'date':'//td[@class="newsa"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{8})", response.url); pDateStr = m.group(0)',
			'dateFormat': '%Y%m%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule42 = {
		'_id': 'chinese.engadget.com',
		'beforeScript':'',
		'startUrls':['http://chinese.engadget.com/page/1/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@class="o-btn o-btn--small w-55@m- w-130@tp+ th-btn"]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="container@m container@tp"]/article[@class="o-hit "]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="article-text c-gray-1"]/descendant-or-self::*/text()',
			'title':'//h1[@class="t-h4@m- t-h1-b@tp t-h1@tl+ mt-20 mt-15@tp mt-0@m-"]/text()',
			'date':'//div[@class="th-meta"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{2}/\\d{2})", response.url); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d',
		},
		'lang':'zh-Hant',
		'st':18
	}

rule43 = {
		'_id': 'www.bnext.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.bnext.com.tw/articles'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//a[@class="item_title block_link"]/@href | //div[@class="item_text_box div_td"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="content htmlview"]/text() | //div[@class="content htmlview"]/descendant::*/text()',
			'title':'//div[@class="main_title"]/text() | //h1[@class="article_title bitem_title"]/text()',
			'date':'//div[@class="info_box"]/span[@class="info"][2]/text() | //div[@class="article_info container-fluid"]/span[@class="item"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y.%m.%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule44 = {
		'_id': 'anntw.com',
		'beforeScript':'',
		'startUrls':['https://anntw.com/col/news', 'https://anntw.com/articles/20161212-MpF4', 'https://anntw.com/col/2-3-2', 'https://anntw.com/col/2'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[contains(@class, "next_page")]/a/@href',
		'maxPage': 50,
		'urlRule': '//h4[@class="article-title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="markdown-body"]/p/text()',
			'title':'//div[@class="span12 content-pad"]/h3/text()',
			'date':'//div[@class="meta-block"]/span[2]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule45 = {
		'_id': 'www.cardu.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.cardu.com.tw/news/list.php?nt_pk=4', 'http://www.cardu.com.tw/news/list.php?nt_pk=7', 'http://www.cardu.com.tw/news/list.php?nt_pk=26', 'http://www.cardu.com.tw/news/list.php?nt_pk=8', 'http://www.cardu.com.tw/news/list.php?nt_pk=6', 'http://www.cardu.com.tw/news/list.php?nt_pk=5', 'http://www.cardu.com.tw/news/list.php?nt_pk=27', 'http://www.cardu.com.tw/news/list.php?nt_pk=22', 'http://www.cardu.com.tw/news/list.php?nt_pk=28' ],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//li[@class="lists_item"]/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="page_content"]/p/text()',
			'title':'//div[@id="page"]/h3/text()',
			'date':'//div[@id="page"]/h5/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\\d{4}/\\d{2}/\\d{2})", pDateStr); pDateStr = m.group(0)',
			'dateFormat': '%Y/%m/%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule46 = {
		'_id': 'www.cdnews.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=107&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=108&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=109&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=110&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=111&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=112&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=113&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=114&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=115&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=116&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=117&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=118&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=119&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=120&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=121&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=122&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=123&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=124&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=125&kindid=0', 'http://www.cdnews.com.tw/cdnews_site/touch/outline.jsp?coluid=126&kindid=0'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@id="outline_gotopage"]/a[contains(.,"下一頁")]/@href',
		'maxPage': 20,
		'urlRule': '//ul[@class="news_list"]/li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="detail_content"]/text()',
			'title':'//div[@id="detail_title"]/h2/text()',
			'date':'//div[@id="detail_info"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1,
	}

rule47 = {
		'_id': 'www.chinanews.com',
		'beforeScript':'',
		'startUrls':['http://www.chinanews.com/scroll-news/news1.html'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="pagebox"]/span/following-sibling::a/@href',
		'maxPage': 10,
		'urlRule': '//div[@class="dd_bt"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="left_zw"]/p/text()',
			'title':'//div[@class="content"]/h1/text()',
			'date':'//div[@class="left-t"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode("(\d{4}年\d{1,2}月\d{1,2}日 \d{1,2}:\d{1,2})"), pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y年%m月%d日 %H:%M',
		},
		'lang':'zh',
		'st':1,
	}

rule48 = {
		'_id': 'e-info.org.tw',
		'beforeScript':'',
		'startUrls':['http://e-info.org.tw/taxonomy/term/258/all', 'http://e-info.org.tw/taxonomy/term/266', 'http://e-info.org.tw/taxonomy/term/35283/all', 'http://e-info.org.tw/taxonomy/term/359/all'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[@class="pager-next"]/a/@href',
		'maxPage': 10,
		'urlRule': '//div[@class="views-field views-field-title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[contains(@class, "field-item")]/p/text()',
			'title':'//h1[@id="page-title"]/text()',
			'date':'//div[@class="article-create-date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}/\d{1,2}/\d{1,2})", pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y/%m/%d',
		},
		'lang':'zh-Hant',
		'st':1,
	}

rule48 = {
		'_id': 'exmoo.com',
		'beforeScript':'',
		'startUrls':['http://exmoo.com/macau', 'http://exmoo.com/china', 'http://exmoo.com/leisure', 'http://exmoo.com/life', 'http://exmoo.com/world', 'http://exmoo.com/sports', 'http://exmoo.com/business'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//ul[@class="pagination pagination-lg"]/li/a[contains(., "›")]/@href',
		'maxPage': 10,
		'urlRule': '//h3[@class="tpl-01-main-title auto-trim"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[contains(@class, "article-content")]/p/text()',
			'title':'//h1[@class="article-main-title"]/text()',
			'date':'//div[@class="article-pub-date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%d/%m/%Y %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1,
	}

rule49 = {
		'_id': 'hk.crntt.com',
		'beforeScript':'',
		'startUrls':['http://hk.crntt.com/crn-webapp/msgOutline.jsp?coluid=7&kindid=0'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//ul/li/a/@href',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append("http://hk.crntt.com/crn-webapp/msgOutline.jsp?coluid=7&kindid=0&page=" + str(pageNum+2))',
		'maxPage': 10,
		'urlRule': '//ul/li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div/table[1]//tr/td/table[2]/descendant-or-self::*/text()',
			'title':'//div/table[1]//tr/td/table[1]//tr[3]/td/table//tr[1]//strong/text()',
			'date':'//div/table[1]//tr/td/table[1]//tr[3]/td/table//tr[2]/descendant-or-self::*/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})", str(pDateStrs)); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1,
	}

rule50 = {
		'_id': 'news.housefun.com.tw',
		'beforeScript':'',
		'startUrls':['https://news.housefun.com.tw/news'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//ul[@class="m-pagination-bd"]/li/a[contains(., "下一頁")]/@href',
		'maxPage': 20,
		'urlRule': '//div[@class="ct"]/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="section-body"]/p/text()',
			'title':'//h1[@class="main-heading"]/text()',
			'date':'//time[@datetime]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1,
	}

rule51 = {
		'_id': 'www.mygonews.com',
		'beforeScript':'',
		'startUrls':['http://www.mygonews.com/news/nextpage?cat_id=0'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="tit"]/a/@href',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append("http://www.mygonews.com/news/nextpage?cat_id=0&page=" + str(pageNum+1))',
		'maxPage': 20,
		'urlRule': '//div[@class="tit"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="editbox"]/text()',
			'title':'//div[@class="detailtitle"]/h1/text()',
			'date':'//div[@class="detaildate"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{1,2}-\d{1,2})", str(pDateStrs)); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1,
	}

rule52 = {
		'_id': 'n.yam.com',
		'beforeScript':'',
		'startUrls':['http://n.yam.com/all/real/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[@class="yamCSSPageNext"]/a/@href',
		'maxPage': 100,
		'urlRule': '//li[@class="both"]/h3/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="news_content"]/p/text()',
			'title':'//li[@class="title"]/h2/text()',
			'date':'//time[@class="time"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.replace("下午", "pm ").replace("上午", "am ")',
			'dateFormat': '%Y年%m月%d日 %p %H:%M',
		},
		'lang':'zh-Hant',
		'st':1,
	}


rule53 = {
		'_id': 'www.new7.com.tw',
		'beforeScript':'',
		'startUrls':['http://www.new7.com.tw/NewsList.aspx?t=03', 'http://www.new7.com.tw/NewsList.aspx?t=04', 'http://www.new7.com.tw/NewsList.aspx?t=05', 'http://www.new7.com.tw/NewsList.aspx?t=06', 'http://www.new7.com.tw/NewsList.aspx?t=07', 'http://www.new7.com.tw/NewsList.aspx?t=08'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//span[@id="ContentPlaceHolder1_DataListPage"]/span/a[contains(., "下一頁")]/@href',
		'maxPage': 10,
		'urlRule': '//a[contains(@id, "ContentPlaceHolder1_DataList1_lnNews")]/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="NewsPageCon"]/p/text()',
			'title':'//div[@class="NewsPageTitle"]/text()',
			'date':'//div[@class="NewsPageTitle"]/span/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1,
	}


rule54 = {
		'_id': 'news.rti.org.tw',
		'beforeScript':'',
		'startUrls':['http://news.rti.org.tw/news/list/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//li[@class="next"]/a/@href',
		'maxPage': 10,
		'urlRule': '//ul[@class="Listul"]/li/div[@class="newsRowsBox"]/h3/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="print_content"]/p/text()',
			'title':'//h4[@id="print_headline"]/text()',
			'date':'//p[@id="print_date"]/span/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2})", str(pDateStrs)); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1,
	}

rule55 = {
		'_id': 'newtalk.tw',
		'beforeScript':'',
		'startUrls':['http://newtalk.tw/news/summary/today'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//div[@class="news_title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="news_content"]//p/text()',
			'title':'//div[@class="content_title"]/text()',
			'date':'//div[@class="content_date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.replace(" | ", " "); print(pDateStr); m = re.search("(\d{4}.\d{1,2}.\d{1,2} \d{1,2}:\d{1,2}.*M)", pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y.%m.%d %I:%M %p',
		},
		'lang':'zh-Hant',
		'st':1,
	}

rule56 = {
		'_id': 'www.storm.mg',
		'beforeScript':'',
		'startUrls':['http://www.storm.mg/articles'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//span[contains(.,"»")]/../a/@href',
		'maxPage': 50,
		'urlRule': '//a[@class="gtm-article-list-news"]/@href',
		'isDetailApi': 0,
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append("http://www.storm.mg/articles/" + str(pageNum+2))',
		'detailRule':{
			'content':'//article/p/text()',
			'title':'//h1[@id="article_title"]/text()',
			'date':'//div[@class="author_date"]/span/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode("(\\d{4}年\\d{2}月\\d{2}日 \\d{2}:\\d{2})"), pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y年%m月%d日 %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule57 = {
		'_id': 'times.hinet.net',
		'beforeScript':'',
		'startUrls':['http://times.hinet.net/realtime'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//span[contains(.,"»")]/../a/@href',
		'maxPage': 50,
		'urlRule': '//div[@class="recentlyBox"]/ul/li/h4/a/@href',
		'isDetailApi': 0,
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append("http://times.hinet.net/realtime?pN=" + str(pageNum+2))',
		'detailRule':{
			'content':'//div[@class="newsContent"]/p/text()',
			'title':'//div[@class="inContent"]/h2/text()',
			'date':'//span[@class="cp"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode("(\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2})"), pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule58 = {
		'_id': 'www.cmoney.tw',
		'beforeScript':'',
		'startUrls':['http://www.cmoney.tw/notes/?cid=22814'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@class="next"]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="pt-bar-title"]/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="rec-content"]/p/text()',
			'title':'//div[@class="pt-bar-title"]/h1/text()',
			'date':'//div[contains(@class, "articleMnY")]/@notedate',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule59 = {
		'_id': 'hk.apple.nextmedia.com/news',
		'beforeScript':'',
		'startUrls':['http://hk.apple.nextmedia.com/catalog/index/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 10,
		'urlRule': '//div[@class="RTitem"]/div[@class="RTitemRHS"]/div[@class="text"]/a/@href | //div[@id="enews_fashion"]/div[@id]/a/@href | //div[@class="Archive"]//li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="ArticleContent_Inner"]/descendant-or-self::*/text()',
			'title':'//table[@class="LinkTable"]//h1/text()',
			'date':'//table[@class="LinkTable"]//h1/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{8})", response.url); pDateStr = m.group(0);',
			'dateFormat': '%Y%m%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule60 = {
		'_id': 'std.stheadline.com',
		'beforeScript':'',
		'startUrls':['http://std.stheadline.com/instant/articles/fetchlist/latest/1'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//div[@class="post-content"]//p/text()',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append("http://std.stheadline.com/instant/articles/fetchlist/latest/" + str(pageNum+2))',
		'maxPage': 20,
		'urlRule': '//a/@href',
		'urlTrim': 'link = link.replace("../instant", "")',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="post-content"]//p/text()',
			'title':'//div[@class="post-heading supplement-p-h"]/h1/text()',
			'date':'//div[@class="date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{2}-\d{2} \d{2}:\d{2})", str(pDateStrs)); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule61 = {
		'_id': 'packetstormsecurity.com',
		'beforeScript':'',
		'startUrls':['https://packetstormsecurity.com/files/page1/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//div[@id="nv"]/a[contains(., "Next")]/@href',
		'maxPage': 100,
		'urlRule': '//dl[@class="file"]/dt/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//dd[@class="detail"]/p/descendant-or-self::*/text()',
			'title':'//dl[@class="file first"]/dt/a/strong/text()',
			'date':'//dd[@class="datetime"]/a/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%b %d, %Y',
		},
		'lang':'en',
		'st':1
	}

rule62 = {
		'_id': 'securityaffairs.co',
		'beforeScript':'',
		'startUrls':['http://securityaffairs.co/wordpress/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//div[@class="pagination"]/a[contains(., "Next")]/@href',
		'maxPage': 100,
		'urlRule': '//div[@class="post_header single_post"]/h3/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="post_inner_wrapper"]/descendant-or-self::*/text()',
			'title':'//h1[@class="post_title"]/text()',
			'date':'//div[@class="post_detail"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.replace(" ", ""); pDateStr = pDateStr.replace("\t", ""); m = re.search("(.*\\d{4})", pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%B%d,%Y',
		},
		'lang':'en',
		'st':1
	}

rule63 = {
		'_id': 'www.greenvalleyconsulting.org',
		'beforeScript':'',
		'startUrls':['http://www.greenvalleyconsulting.org/security/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[@class="pagination-next"]/a/@href',
		'maxPage': 100,
		'urlRule': '//h2[@class="entry-title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="entry-content"]/p/descendant-or-self::*/text()',
			'title':'//h1[@class="entry-title"]/text()',
			'date':'//span[@class="date published time"]/@title',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%dT%H:%M:%S+00:00',
		},
		'lang':'en',
		'st':1
	}

rule64 = {
		'_id': 'www.securiteam.com',
		'beforeScript':'',
		'startUrls':['http://www.securiteam.com/securitynews/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 10,
		'urlRule': '//td[@class="contentarticletitle"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//tr[@align="LEFT"]/descendant-or-self::*/text()',
			'title':'//table[@id="ArticleTABLE"]//tr//td[@class="header"][1]/text()',
			'date':'//table[@id="ArticleTABLE"]//tr//td[@class="header"][2]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%d %b. %Y',
		},
		'lang':'en',
		'st':1
	}

rule65 = {
		'_id': 'www.proofpoint.com',
		'beforeScript':'',
		'startUrls':['https://www.proofpoint.com/us/news?type=All'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[@class="pager-next"]/a/@href',
		'maxPage': 10,
		'urlRule': '//h3[@class="big-title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="field-item even"]/descendant-or-self::*/text()',
			'title':'//h1[@class="page-title"]/text()',
			'date':'//span[@class="date-display-single"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%B %d, %Y',
		},
		'lang':'en',
		'st':1
	}

rule66 = {
		'_id': 'www.ibtimes.co.uk',
		'beforeScript':'',
		'startUrls':['http://www.ibtimes.co.uk', 'http://www.ibtimes.co.uk/world', 'http://www.ibtimes.co.uk/business', 'http://www.ibtimes.co.uk/politics', 'http://www.ibtimes.co.uk/fintech', 'http://www.ibtimes.co.uk/technology', 'http://www.ibtimes.co.uk/science', 'http://www.ibtimes.co.uk/sports', 'http://www.ibtimes.co.uk/entertainment'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[@class="pager-next"]/a/@href',
		'maxPage': 10,
		'urlRule': '//h3/a/@href',
		'isDetailApi': 0,
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("?page=")[0] + "?page=" + str(pageNum+2))',
		'detailRule':{
			'content':'//div[@itemprop="articleBody"]/p/descendant-or-self::*/text()',
			'title':'//h1[@itemprop="name headline"]/text()',
			'date':'//time[@itemprop="datePublished"]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%dT%H:%M:%S+00:00',
		},
		'lang':'en',
		'st':1
	}

rule67 = {
		'_id': 'www.bleepingcomputer.com',
		'beforeScript':'',
		'startUrls':['https://www.bleepingcomputer.com'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[@aria-label="Next"]/a/@href',
		'maxPage': 10,
		'urlRule': '//h4/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//span[@itemprop="articleBody"]/p/descendant-or-self::*/text()',
			'title':'//h2[@itemprop="headline"]/text()',
			'date':'//span[@itemprop="datePublished"]/@content',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%dT%H:%M:%S-05:00',
		},
		'lang':'en',
		'st':1
	}

rule68 = {
		'_id': 'www.telegraph.co.uk',
		'beforeScript':'',
		'startUrls':['http://www.telegraph.co.uk/news/loadmore1'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//h3/a/@href',
		'maxPage': 10,
		'urlRule': '//h3/a/@href',
		'isDetailApi': 0,
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("loadmore")[0] + "loadmore" + str(pageNum+2))',
		'detailRule':{
			'content':'//div[@class="component-content"]/p/descendant-or-self::*/text()',
			'title':'//h1[@itemprop="headline name"]/text()',
			'date':'//time[@itemprop="datePublished"]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%dT%H:%M+0000',
		},
		'lang':'en',
		'st':1
	}

rule69 = {
		'_id': 'news.mingpao.com/pns',
		'beforeScript':'startUrls = []; resp = requests.get("http://news.mingpao.com/dat/ins/issuelist.js"); key=dt.now().strftime("%Y%m%d"); startUrls.append("http://news.mingpao.com/dat/pns/pns_web_tc/feed1/"+key+resp.json()["INS_WEB_TC"]["1 "+key]["E"]+"/content.js"); rule["key"] = key+resp.json()["INS_WEB_TC"]["1 "+key]["E"];',
		'startUrls':[''],
		'allFromOneApiItems': 0,
		'apiScript':'text = \'{"result":{"rss"\'+ text.split(\'{"rss"\')[1].split("}}}};")[0] + "}}}}"',
		'UrlsApiItems': 'result.rss.channel.item',
		'nextPage': '',
		'maxPage': 0,
		'urlRule': 'ATTRIBUTES.NODEID',
		'urlTrim': 'link = "http://news.mingpao.com/dat/pns/pns_web_tc/article1/"+dRule["key"]+"/todaycontent_"+str(link)+".js"',
		'isDetailApi': '1',
		'detailRule':{
			'content':'DESCRIPTION',
			'title':'TITLE',
			'date':'PUBDATE',
			'url': 'LINK',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'contentSelect = Selector(text=content).xpath("//p/text()").extract(); content = re.sub(" +", " ", " ".join(contentSelect));  pDateStr = pDateStr.split("  +")[0]',
			'dateFormat': '%a, %d %b %Y %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule70 = {
		'_id': 'www.chinadaily.com.cn',
		'beforeScript':'',
		'startUrls':['http://www.chinadaily.com.cn/china/governmentandpolicy.html', 'http://www.chinadaily.com.cn/china/society.html', 'http://www.chinadaily.com.cn/china/scitech.html', 'http://www.chinadaily.com.cn/china/node_1082621.htm', 'http://www.chinadaily.com.cn/china/coverstory.html', 'http://www.chinadaily.com.cn/china/environment.html', 'http://www.chinadaily.com.cn/china/node_53006759.htm', 'http://www.chinadaily.com.cn/china/node_53006760.htm', 'http://www.chinadaily.com.cn/world/asia_pacific.html', 'http://www.chinadaily.com.cn/world/america.html', 'http://www.chinadaily.com.cn/world/europe.html', 'http://www.chinadaily.com.cn/world/middle_east.html', 'http://www.chinadaily.com.cn/world/africa.html', 'http://www.chinadaily.com.cn/world/china-us.html', 'http://www.chinadaily.com.cn/business/economy.html', 'http://www.chinadaily.com.cn/business/companies.html', 'http://www.chinadaily.com.cn/business/biz_industries.html', 'http://www.chinadaily.com.cn/business/tech/', 'http://www.chinadaily.com.cn/business/motoring/', 'http://www.chinadaily.com.cn/business/money.html', 'http://www.chinadaily.com.cn/fashion/', 'http://www.chinadaily.com.cn/celebrity/', 'http://www.chinadaily.com.cn/life/people.html'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//div[@id="div_currpage"]/a[contains(.,"Next Page")]/@href',
		'maxPage': 10,
		'urlRule': '//div[@class="lft_art"]//h4/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="Content"]/descendant-or-self::*/text()',
			'title':'//div[@class="lft_art"]/h1/text()',
			'date':'//span[@class="info_l"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{2}-\d{2} \d{2}:\d{2})", pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'en',
		'st':1
	}

rule71 = {
		'_id': 'www.hkcd.com',
		'beforeScript':'',
		'startUrls':['http://www.hkcd.com/node_4.html','http://www.hkcd.com/node_5.html', 'http://www.hkcd.com/node_6.html', 'http://www.hkcd.com/node_7.html', 'http://www.hkcd.com/node_8.html', 'http://www.hkcd.com/node_9.html', 'http://www.hkcd.com/node_10.html', 'http://www.hkcd.com/node_11.html', 'http://www.hkcd.com/node_12.html', 'http://www.hkcd.com/node_13.html', 'http://www.hkcd.com/node_14.html', 'http://www.hkcd.com/node_15.html', 'http://www.hkcd.com/node_23.html', 'http://www.hkcd.com/node_24.html', 'http://www.hkcd.com/node_25.html', 'http://www.hkcd.com/node_26.html', 'http://www.hkcd.com/node_27.html', 'http://www.hkcd.com/node_37.html', 'http://www.hkcd.com/node_51.html', 'http://www.hkcd.com/node_52.html', 'http://www.hkcd.com/node_50.html', 'http://www.hkcd.com/node_55.html', 'http://www.hkcd.com/node_40.html', 'http://www.hkcd.com/node_46.html', 'http://www.hkcd.com/node_85.html', 'http://www.hkcd.com/node_84.html', 'http://www.hkcd.com/node_83.html', 'http://www.hkcd.com/node_41.html', 'http://www.hkcd.com/node_32.html', 'http://www.hkcd.com/node_102.html', 'http://www.hkcd.com/node_62.html', 'http://www.hkcd.com/node_57.html', 'http://www.hkcd.com/node_58.html', 'http://www.hkcd.com/node_60.html', 'http://www.hkcd.com/node_59.html', 'http://www.hkcd.com/node_61.html','http://www.hkcd.com/node_72.html', 'http://www.hkcd.com/node_77.html', 'http://www.hkcd.com/node_78.html', 'http://www.hkcd.com/node_104.html', 'http://www.hkcd.com/node_183.html', 'http://www.hkcd.com/node_254.html', 'http://www.hkcd.com/node_256.html', 'http://www.hkcd.com/node_93.html', 'http://www.hkcd.com/node_90.html'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//div[@id="div_currpage"]/a[contains(.,"Next Page")]/@href',
		'nextPageScrip': 'nodeNum = response.url.split("hkcd.com/")[1].split(".")[0].split("_")[1]; nextPageUrls=[]; nextPageUrls.append("http://www.hkcd.com/node_" + nodeNum + "_" +str(pageNum+2) + ".html")',
		'maxPage': 5,
		'urlRule': '//div[@class="cat_new_zs cat_newlist"]/ul/li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="content_main"]/descendant-or-self::*/text()',
			'title':'//h2[@class="conten_title"]/text()',
			'date':'//span[@class="ti_l"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule72 = {
		'_id': 'hk.hkcd.com',
		'beforeScript':'',
		'startUrls':['http://hk.hkcd.com/node_30557.htm', 'http://hk.hkcd.com/node_30602.htm', 'http://hk.hkcd.com/node_30561.htm', 'http://hk.hkcd.com/node_30610.htm', 'http://hk.hkcd.com/node_30604.htm', 'http://hk.hkcd.com/node_30576.htm', 'http://hk.hkcd.com/node_30564.htm', 'http://hk.hkcd.com/node_30560.htm', 'http://hk.hkcd.com/node_30558.htm', 'http://hk.hkcd.com/node_31850.htm', 'http://hk.hkcd.com/node_30578.htm'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//div[@id="div_currpage"]/a[contains(.,"Next Page")]/@href',
		'nextPageScrip': 'nodeNum = response.url.split("hkcd.com/")[1].split(".")[0].split("_")[1]; nextPageUrls=[]; nextPageUrls.append("http://hk.hkcd.com/node_" + nodeNum + "_" +str(pageNum+2) + ".html")',
		'maxPage': 5,
		'urlRule': '//a[contains(@href, "content_")]/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="wenzi"]/p/descendant-or-self::*/text()',
			'title':'//div[@id="tst"]/font/b/text()',
			'date':'//div[@id="tst"]/font/b/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{2}/\d{2})", response.url); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m/%d',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule73 = {
		'_id': 'www2.hkej.com',
		'beforeScript':'',
		'startUrls':['http://www2.hkej.com/instantnews'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//div[@id="div_currpage"]/a[contains(.,"Next Page")]/@href',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("?page")[0] + "?page=" +str(pageNum+2))',
		'maxPage': 5,
		'urlRule': '//div[@class="hkej_toc_listingAll_news2_2014"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="article-content"]/p/descendant-or-self::*/text()',
			'title':'//h1[@id="article-title"]/text()',
			'date':'//span[@class="date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'today = dt.now(); yestoday = today - timedelta(days=1); pDateStr = pDateStr.replace(" ", "").replace(unicode("今日"), today.strftime("%Y-%m-%d")+" ").replace(unicode("昨日"), yestoday.strftime("%Y-%m-%d")+" "); ',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule74 = {
		'_id': 'www1.hkej.com',
		'beforeScript':'',
		'startUrls':['http://www1.hkej.com/dailynews', 'http://www1.hkej.com/dailynews/investment', 'http://www1.hkej.com/dailynews/commentary', 'http://www1.hkej.com/dailynews/finnews' ,'http://www1.hkej.com/dailynews/property', 'http://www1.hkej.com/dailynews/politics', 'http://www1.hkej.com/dailynews/views', 'http://www1.hkej.com/dailynews/cntw', 'http://www1.hkej.com/dailynews/international', 'http://www1.hkej.com/dailynews/culture'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//div[contains(@class, "new")]/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="article-content"]/descendant-or-self::*/text() | //div[@id="article-detail-wrapper"]/text()',
			'title':'//h1[@id="article-title"]/text()',
			'date':'//p[@id="date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y年%m月%d日',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule75 = {
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

rule76 = {
		'_id': 'www.macaodaily.com',
		'beforeScript':'startUrls = []; startUrls.append("http://www.macaodaily.com/html/" + dt.now().strftime("%Y-%m/%d/"))',
		'startUrls':[],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 0,
		'urlRule': '//a[contains(@href,"content_")]/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="ozoom"]/descendant-or-self::*/text()',
			'title':'//table/tbody/tr/td/strong/text()',
			'date':'//table/tbody/tr/td/strong/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{1,2}/\d{2})", response.url); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m/%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule77 = {
		'_id': 'www.singpao.com.hk',
		'beforeScript':'',
		'startUrls':['http://www.singpao.com.hk/index.php?fi=instantnews', 'http://www.singpao.com.hk/index.php?fi=video', 'http://www.singpao.com.hk/index.php?fi=news1', 'http://www.singpao.com.hk/index.php?fi=news2', 'http://www.singpao.com.hk/index.php?fi=news8', 'http://www.singpao.com.hk/index.php?fi=news3', 'http://www.singpao.com.hk/index.php?fi=news4', 'http://www.singpao.com.hk/index.php?fi=news5', 'http://www.singpao.com.hk/index.php?fi=news6', 'http://www.singpao.com.hk/index.php?fi=news7'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[contains(@class,"list_title")]/@href',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("&page")[0] + "&page=" +str(pageNum+2))',
		'maxPage': 10,
		'urlRule': '//a[contains(@class,"list_title")]/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//td/p/descendant-or-self::*/text()',
			'title':'//td[@class="news_title"]/text()',
			'date':'//td[@class="date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{1,2}-\d{2})", pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule78 = {
		'_id': 'www.takungpao.com.hk',
		'beforeScript':'',
		'startUrls':['http://www.takungpao.com.hk/hongkong/', 'http://www.takungpao.com.hk/taiwan/', 'http://www.takungpao.com.hk/mainland/', 'http://www.takungpao.com.hk/international/', 'http://www.takungpao.com.hk/opinion/', 'http://www.takungpao.com.hk/finance/', 'http://www.takungpao.com.hk/culture/', 'http://www.takungpao.com.hk/sports/', 'http://www.takungpao.com.hk/ent/', 'http://www.takungpao.com.hk/hongkong/video/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 10,
		'urlRule': '//li[@class="title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="tkp_content"]/p/descendant-or-self::*/text()',
			'title':'//h1[@class="tkp_con_title"]/text()',
			'date':'//h2[@class="tkp_con_author"]/span/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{1,2}-\d{2} \d{2}:\d{2}:\d{2})", pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule79 = {
		'_id': 'news.wenweipo.com',
		'beforeScript':'',
		'startUrls':['http://news.wenweipo.com/list_news.php?cat=000IN&instantCat=china', 'http://news.wenweipo.com/list_news.php?cat=000IN&instantCat=hk', 'http://news.wenweipo.com/list_news.php?cat=000IN&instantCat=world'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'maxPage': 10,
		'urlRule': '//article[@class="content-art"]/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="main-content"]/p/descendant-or-self::*/text()',
			'title':'//h1[@class="title"]/text()',
			'date':'//h1[@class="title"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}/\d{1,2}/\d{2})", response.url); pDateStr = m.group(0);',
			'dateFormat': '%Y/%m/%d',
		},
		'lang':'en',
		'st':1
	}

rule80 = {
		'_id': 'www.xinhuanet.com',
		'beforeScript':'',
		'startUrls':['http://qc.wa.news.cn/nodeart/list?nid=113321&cnt=100&tp=1&orderby=1&pgnum=1', 'http://qc.wa.news.cn/nodeart/list?nid=113207&cnt=100&tp=1&orderby=1&pgnum=1', 'http://qc.wa.news.cn/nodeart/list?nid=113352&cnt=100&tp=1&orderby=1&pgnum=1', 'http://qc.wa.news.cn/nodeart/list?nid=11139635&cnt=100&tp=1&orderby=1&pgnum=1', 'http://qc.wa.news.cn/nodeart/list?nid=11147664&cnt=100&tp=1&orderby=1&pgnum=1', 'http://qc.wa.news.cn/nodeart/list?nid=11145724&cnt=100&tp=1&orderby=1&pgnum=1', 'http://qc.wa.news.cn/nodeart/list?nid=11145727&cnt=100&tp=1&orderby=1&pgnum=1', 'http://qc.wa.news.cn/nodeart/list?nid=11145726&cnt=100&tp=1&orderby=1&pgnum=1', 'http://qc.wa.news.cn/nodeart/list?nid=11145728&cnt=100&tp=1&orderby=1&pgnum=1'],
		'allFromOneApiItems': 0,
		'apiScript':'text = text[1:-1]',
		'UrlsApiItems': 'data.list',
		'nextPage': u'//div[@class="menu_page"]/a[contains(.," > ")]/@href',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("pgnum=")[0] + "pgnum=" +str(pageNum+2))',
		'maxPage': 10,
		'urlRule': 'LinkUrl',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="p-detail"]/p/descendant-or-self::*/text()',
			'title':'//div[@class="h-title"]/text()',
			'date':'//span[@class="h-time"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = pDateStr.strip()',
			'dateFormat': '%Y-%m-%d %H:%M:%S',
		},
		'lang':'zh',
		'st':1
	}

rule81 = {
		'_id': 'news.people.com.cn',
		'beforeScript':'',
		'startUrls':['http://news.people.com.cn/210801/211150/index.js?_=1'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 'items',
		'nextPage': '',
		'nextPageScrip': '',
		'maxPage': 0,
		'urlRule': 'url',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="box_con"]/p/descendant-or-self::*/text() | //div[@class="artDet"]/p/descendant-or-self::*/text() | //div[contains(@class, "content")]/p/descendant-or-self::*/text() | //div[contains(@class, "box_text")]/p/descendant-or-self::*/text()',   ##### content的xpath，或者api json結果的字段名稱
			'title':'//div[contains(@class, "title")]/h1/text() | //div[@class="title"]/h2/text() | //div[contains(@class, "p2j_text")]/h1/text()',
			'date':'//div[contains(@class, "title")]/div[@class="box01"]/div[@class="fl"]/text() | //div[@class="artOri"]/text() | //div[@class="fr"]/text() | //div[contains(@class, "p2j_text")]/h2/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'pDateStr = str(pDateStrs).replace("\\u5e74", "-").replace("\\u6708", "-").replace("\\u65e5", " "); print(pDateStr); m = re.search(unicode(u"(\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2})"), str(pDateStr)); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh',
		'st':1
	}

rule82 = {
		'_id': 'big5.gov.cn',
		'beforeScript':'',
		'startUrls':['http://big5.gov.cn/gate/big5/sousuo.gov.cn/column/30611/0.htm', 'http://big5.gov.cn/gate/big5/sousuo.gov.cn/column/31421/0.htm', 'http://big5.gov.cn/gate/big5/sousuo.gov.cn/column/31250/0.htm', 'http://big5.gov.cn/gate/big5/sousuo.gov.cn/column/30469/0.htm'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'nextPageScrip': '',
		'maxPage': 0,
		'urlRule': '//ul[@class="listTxt"]/li/h4/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="pages_content"]/p/descendant-or-self::*/text()',   ##### content的xpath，或者api json結果的字段名稱
			'title':'//div[contains(@class, "article")]/h1/text()',
			'date':'//div[contains(@class, "pages-date")]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode("(\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2})"), pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh',
		'st':1
	}


rule83 = {
		'_id': 'www.rfa.org',
		'beforeScript':'',
		'startUrls':['http://www.rfa.org/mandarin/guojishijiao/story_archive', 'http://www.rfa.org/mandarin/guojishijiao/story_archive', 'http://www.rfa.org/mandarin/Xinwen/story_archive','http://www.rfa.org/mandarin/yataibaodao/story_archive'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '',
		'nextPageScrip': '',
		'maxPage': 0,
		'urlRule': '//div[@class="sectionteaser"]/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="storytext"]/p/descendant-or-self::*/text()',
			'title':'//div[contains(@id, "storypagemaincol")]/h1/text()',
			'date':'//span[contains(@id, "story_date")]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh',
		'st':1
	}

rule84 = {
		'_id': 'www.jinghua.cn',
		'beforeScript':'',
		'startUrls':['http://www.jinghua.cn/area/','http://tech.jinghua.cn/','http://wenshi.jinghua.cn/','http://lvyou.jinghua.cn/meizhou/','http://lvyou.jinghua.cn/ouzhou/','http://lvyou.jinghua.cn/yazhou/','http://jiankang.jinghua.cn/','http://happy.jinghua.cn/wangpai/','http://happy.jinghua.cn/tupian/','http://happy.jinghua.cn/bagua/','http://beijing.jinghua.cn/','http://junshi.jinghua.cn/','http://news.jinghua.cn/351/c/','http://news.jinghua.cn/353/c/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="menu_page"]/a[contains(.," > ")]/@href',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("pgnum=")[0] + "pgnum=" +str(pageNum+2))',
		'maxPage': 0,
		'urlRule': '//div[@class="news"]/h2/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="article_body"]/p/descendant-or-self::*/text()',
			'title':'//div[@class="w670"]/h1/text()',
			'date':'//div[@class="xinx"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode(u"(\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2})"), pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh',
		'st':1
	}


rule85 = {
		'_id': 'www.81.cn',
		'beforeScript':'',
		'startUrls':['http://www.81.cn/gjzx/xwrw.htm','http://www.81.cn/gjzx/gjjl.htm','http://www.81.cn/gjzx/tfsj.htm','http://www.81.cn/gjzx/hqpl.htm','http://www.81.cn/gjzx/sdbd.htm','http://www.81.cn/gjzx/tjyd.htm','http://www.81.cn/gjzx/rcdj.htm','http://www.81.cn/gjzx/hqzx.htm','http://www.81.cn/gnxw/shtt.htm','http://www.81.cn/gnxw/gdyw.htm', 'http://www.81.cn/gnxw/rsrm.htm', 'http://www.81.cn/gnxw/node_62877.htm', 'http://www.81.cn/gnxw/rdxw.htm', 'http://www.81.cn/gnxw/zybw.htm','http://www.81.cn/gnxw/gcdt.htm', 'http://www.81.cn/gnxw/xwjd.htm','http://www.81.cn/gnxw/xwrw.htm', 'http://www.81.cn/gnxw/rdzz.htm', 'http://www.81.cn/gnxw/szzt.htm','http://www.81.cn/gnxw/szyw.htm','http://www.81.cn/rd/node_92585.htm','http://www.81.cn/jwzb/node_86105.htm','http://www.81.cn/jwzb/node_86103.htm', 'http://www.81.cn/jwzb/node_61947.htm', 'http://www.81.cn/jwzb/ywyl.htm', 'http://www.81.cn/jmywyl/index.htm'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@id="displaypagenum"]//a[contains(.,"下一页")]/@href',
		'maxPage': 10,
		'urlRule': '//ul[contains(@class,"news-list")]/li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="article-content"]/p/descendant-or-self::*/text()',
			'title':'//div[@class="article-header"]/h1/text()',
			'date':'//i[@class="time"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode(u"(\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2})"), pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M',
		},
		'lang':'zh',
		'st':1
	}

rule86 = {
		'_id': 'blog.udn.com',
		'beforeScript':'',
		'startUrls':['http://blog.udn.com/v1/blog/rank/article_rank_ajax.jsp?f_type=&f_sub_type=&sort_type=p&pno=0'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@id="displaypagenum"]//a[contains(.,"下一页")]/@href',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("pno=")[0] + "pno=" +str(pageNum+1))',
		'maxPage': 1000,
		'urlRule': '//ul[@id="article"]/li/h1/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="article_show_content"]/p/descendant-or-self::*/text()',
			'title':'//div[@class="article_topic"]/text()',
			'date':'//div[@class="article_datatime"]/descendant-or-self::*/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'testStr = "".join(pDateStrs); pDateStr = testStr;',
			'dateFormat': '%Y/%m/%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':18
	}


rule87 = {
		'_id': 'blog.xuite.net',
		'beforeScript':'',
		'startUrls':['https://blog.xuite.net/index_next.php?type=hot_label&type_id=28','https://blog.xuite.net/index_next.php?type=hot_label&type_id=52','https://blog.xuite.net/index_next.php?type=hot_label&type_id=27','https://blog.xuite.net/index_next.php?type=hot_label&type_id=26', 'https://blog.xuite.net/index_next.php?type=hot_label&type_id=21', 'https://blog.xuite.net/index_next.php?type=hot_label&type_id=47','https://blog.xuite.net/index_next.php?type=hot_label&type_id=17','https://blog.xuite.net/index_next.php?type=hot_label&type_id=16','https://blog.xuite.net/index_next.php?type=hot_label&type_id=10', 'https://blog.xuite.net/index_next.php?type=hot_label&type_id=15', 'https://blog.xuite.net/index_next.php?type=hot_label&type_id=25','https://blog.xuite.net/index_next.php?type=hot_label&type_id=11'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@class="page-next"]/@href',
		'maxPage': 10,
		'urlRule': '//ul/li[not(@class)]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="content_all"]/p/descendant-or-self::*/text()',
			'title':'//span[@class="titlename"]/text()',
			'date':'//span[@class="titledate"]/descendant-or-self::*/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'testStr = "".join(pDateStrs); pDateStr = testStr;',
			'dateFormat': '%Y%m%d%H%M',
		},
		'lang':'zh-Hant',
		'st':18
	}

rule88 = {
		'_id': 'blog.youthwant.com.tw',
		'beforeScript':'',
		'startUrls':['http://blog.youthwant.com.tw/chart.php?w=art'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="newpage"]/a[contains(.,"下一頁")]/@href',
		'maxPage': 10,
		'urlRule': '//div[@class="postlist_td_article_icons"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="PostCon"]/div/p/descendant-or-self::*/text()',
			'title':'//div[@class="post_titlediv"]/text()',
			'date':'//div[@class="post_date"]/descendant-or-self::*/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode(u"(\d{4}-\d{1,2}-\d{1,2})"), str(pDateStrs)); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':18
	}

rule89 = {
		'_id': 'blog.roodo.com',
		'beforeScript':'',
		'startUrls':['http://blog.roodo.com/categories/baby/list&page=1', 'http://blog.roodo.com/categories/play/list&page=1', 'http://blog.roodo.com/categories/knowledge/list&page=1','http://blog.roodo.com/categories/video/list&page=1','http://blog.roodo.com/categories/life/list&page=1','http://blog.roodo.com/categories/creative/list&page=1'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//div[@class="newpage"]/a[contains(.,"下一頁")]/@href',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("page=")[0] + "page=" +str(pageNum+2))',
		'maxPage': 10,
		'urlRule': '//li[@class="cate_atitem"]/dl/dt/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[contains(@class, "article_cont")]/descendant::*/text()',
			'title':'//h1[@class="art_tilte"]/text()',
			'date':'//li[@class="author_in"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode(u"(\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2})"), str(pDateStrs)); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d %H:%M:%S',
		},
		'lang':'zh-Hant',
		'st':18
	}

rule90 = {
		'_id': 'life.tw',
		'beforeScript':'',
		'startUrls':['http://life.tw/?app=category&act=categorylist&no=25', 'http://life.tw/?app=category&act=categorylist&no=24', 'http://life.tw/?app=category&act=categorylist&no=58', 'http://life.tw/?app=category&act=categorylist&no=14', 'http://life.tw/?app=category&act=categorylist&no=44', 'http://life.tw/?app=category&act=categorylist&no=19', 'http://life.tw/?app=category&act=categorylist&no=55', 'http://life.tw/?app=category&act=categorylist&no=5', 'http://life.tw/?app=category&act=categorylist&no=52', 'http://life.tw/?app=category&act=categorylist&no=22', 'http://life.tw/?app=category&act=categorylist&no=39', 'http://life.tw/?app=category&act=categorylist&no=16', 'http://life.tw/?app=category&act=categorylist&no=60', 'http://life.tw/?app=category&act=categorylist&no=3', 'http://life.tw/?app=category&act=categorylist&no=13', 'http://life.tw/?app=category&act=categorylist&no=27', 'http://life.tw/?app=category&act=categorylist&no=8', 'http://life.tw/?app=category&act=categorylist&no=30', 'http://life.tw/?app=category&act=categorylist&no=51', 'http://life.tw/?app=category&act=categorylist&no=68', 'http://life.tw/?app=category&act=categorylist&no=12', 'http://life.tw/?app=category&act=categorylist&no=69', 'http://life.tw/?app=category&act=categorylist&no=23', 'http://life.tw/?app=category&act=categorylist&no=29', 'http://life.tw/?app=category&act=categorylist&no=38', 'http://life.tw/?app=category&act=categorylist&no=57', 'http://life.tw/?app=category&act=categorylist&no=4', 'http://life.tw/?app=category&act=categorylist&no=26', 'http://life.tw/?app=category&act=categorylist&no=63', 'http://life.tw/?app=category&act=categorylist&no=10', 'http://life.tw/?app=category&act=categorylist&no=17', 'http://life.tw/?app=category&act=categorylist&no=9', 'http://life.tw/?app=category&act=categorylist&no=35', 'http://life.tw/?app=category&act=categorylist&no=42', 'http://life.tw/?app=category&act=categorylist&no=6', 'http://life.tw/?app=category&act=categorylist&no=45', 'http://life.tw/?app=category&act=categorylist&no=67', 'http://life.tw/?app=category&act=categorylist&no=15', 'http://life.tw/?app=category&act=categorylist&no=70', 'http://life.tw/?app=category&act=categorylist&no=20', 'http://life.tw/?app=category&act=categorylist&no=36', 'http://life.tw/?app=category&act=categorylist&no=62', 'http://life.tw/?app=category&act=categorylist&no=49', 'http://life.tw/?app=category&act=categorylist&no=72', 'http://life.tw/?app=category&act=categorylist&no=54', 'http://life.tw/?app=category&act=categorylist&no=43', 'http://life.tw/?app=category&act=categorylist&no=47', 'http://life.tw/?app=category&act=categorylist&no=61', 'http://life.tw/?app=category&act=categorylist&no=7', 'http://life.tw/?app=category&act=categorylist&no=40', 'http://life.tw/?app=category&act=categorylist&no=48', 'http://life.tw/?app=category&act=categorylist&no=56', 'http://life.tw/?app=category&act=categorylist&no=1', 'http://life.tw/?app=category&act=categorylist&no=11'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//a[@class="next-page"]/@href',
		'maxPage': 10,
		'urlRule': '//li[@class="shadow radius5"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="mainContent"]/descendant::*/text()',
			'title':'//div[@class="aricle-detail-top"]/h1/text()',
			'date':'//span[@itemprop="datePublished"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode(u"(\d{4}-\d{1,2}-\d{1,2})"), str(pDateStrs)); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':18
	}

rule91 = {
		'_id': 'www.pixnet.net',
		'beforeScript':'',
		'startUrls':['https://www.pixnet.net/blog/articles/group/5', 'https://www.pixnet.net/blog/articles/group/7', 'https://www.pixnet.net/blog/articles/group/4', 'https://www.pixnet.net/blog/articles/group/13', 'https://www.pixnet.net/blog/articles/group/14', 'https://www.pixnet.net/blog/articles/group/3', 'https://www.pixnet.net/blog/articles/group/1', 'https://www.pixnet.net/blog/articles/group/12', 'https://www.pixnet.net/blog/articles/group/10', 'https://www.pixnet.net/blog/articles/group/8', 'https://www.pixnet.net/blog/articles/group/15', 'https://www.pixnet.net/blog/articles/group/6', 'https://www.pixnet.net/blog/articles/group/9', 'https://www.pixnet.net/blog/articles/group/11', 'https://www.pixnet.net/blog/articles/group/2'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//a[@class="page-next"]/@href',
		'maxPage': 10,
		'urlRule': '//ol[@class="article-list"]/li[contains(@class,"rank-")]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@id="article-content-inner"]/p/descendant-or-self::*/text()',
			'title':'//li[contains(@class, "title")]/h2/a/text()',
			'date':'//li[@class="publish"]/span/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'testStr = "".join(pDateStrs); print(testStr); pDateStr = testStr;',
			'dateFormat': '%b %d %a %Y %H:%M',
		},
		'lang':'zh-Hant',
		'st':18
	}

rule92 = {
		'_id': 'www.passiontimes.hk',
		'beforeScript':'',
		'startUrls':['http://www.passiontimes.hk/category/1/1/', 'http://www.passiontimes.hk/category/1/2/', 'http://www.passiontimes.hk/category/1/3/', 'http://www.passiontimes.hk/category/1/4/', 'http://www.passiontimes.hk/category/1/5/', 'http://www.passiontimes.hk/category/1/6/', 'http://www.passiontimes.hk/category/1/7/', 'http://www.passiontimes.hk/category/1/37/'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//div[contains(@class, "next-page")]/span[@class="text"]/a/@href',
		'maxPage': 10,
		'urlRule': '//li[contains(@class, "article")]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="article-body"]/p/descendant-or-self::*/text()',
			'title':'//header[@class="mainHead"]/h1/text()',
			'date':'//time[@class="published"]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%m-%d-%Y',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule93 = {
		'_id': 'www.tvmost.com.hk',
		'beforeScript':'',
		'startUrls':['http://www.tvmost.com.hk/articles?offset=0'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': u'//a[contains(., "下一頁")]/@href',
		'maxPage': 10,
		'urlRule': '//div[@class="item_main_article "]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="article_abstract"]/p/descendant-or-self::*/text()',
			'title':'//div[@class="article_title"]/text()',
			'date':'//div[@class="article_date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{12})", response.url); pDateStr = m.group(0);',
			'dateFormat': '%Y%m%d%H%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule94 = {
		'_id': 'www.inmediahk.net',
		'beforeScript':'',
		'startUrls':['https://www.inmediahk.net/taxonomy/term/5030', 'https://www.inmediahk.net/taxonomy/term/5034', 'https://www.inmediahk.net/taxonomy/term/5018', 'https://www.inmediahk.net/taxonomy/term/513024','https://www.inmediahk.net/taxonomy/term/', 'https://www.inmediahk.net/taxonomy/term/5027', 'https://www.inmediahk.net/taxonomy/term/https://www.inmediahk.net/taxonomy/term/513025', 'https://www.inmediahk.net/taxonomy/term/https://www.inmediahk.net/taxonomy/term/https://www.inmediahk.net/taxonomy/term/5043', 'https://www.inmediahk.net/taxonomy/term/https://www.inmediahk.net/taxonomy/term/https://www.inmediahk.net/taxonomy/term/510975'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[@class="pager-next"]/a/@href',
		'maxPage': 10,
		'urlRule': '//h3[@class="title"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="post-desc"]/p/descendant-or-self::*/text()',
			'title':'//h1[@class="title"]/text()',
			'date':'//span[@class="date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{2}-\d{2})", pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule95 = {
		'_id': 'speakout.hk',
		'beforeScript':'',
		'startUrls':['http://speakout.hk/index.php/2013-11-04-09-33-03'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//li[@class="pagination-next"]/a/@href',
		'maxPage': 50,
		'urlRule': '//div[contains(@class, "items-row")]/div[2]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//td/div/p/descendant-or-self::*/text()',
			'title':'//td/b/text()',
			'date':'//div[@class="published"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search("(\d{4}-\d{2}-\d{2})", pDateStr); pDateStr = m.group(0);',
			'dateFormat': '%Y-%m-%d',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule96 = {
		'_id': 'www.weekendhk.com',
		'beforeScript':'',
		'startUrls':['http://www.weekendhk.com/page/1'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@class="next page-numbers"]/@href',
		'maxPage': 50,
		'urlRule': '//div[@class="article--grid__header"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[contains(@class, "_page_")]/descendant-or-self::*/text()',
			'title':'//h1[contains(@class,"article__title")]/text()',
			'date':'//time[@datetime]/@datetime',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': '',
			'dateFormat': '%Y-%m-%dT%H:%M:%S+00:00',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule97 = {
			'_id': 'hk.news.yahoo.com',
			'beforeScript':'',
			'startUrls':['https://hk.news.yahoo.com/_td-news/api/resource/IndexDataService.getExternalMediaNewsList;newsTab=all;start=0;count=200&tag=null?bkt=news-HK-zh-Hant-HK-def&device=desktop&intl=hk&lang=zh-Hant-HK&partner=none&region=HK&site=news&returnMeta=true'],
			'allFromOneApiItems': 0,
			'apiScript':'',
			'UrlsApiItems': 'data',
			'nextPage': '//a[@class="yom-button next"]/@href',
			'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split(";start=")[0] + ";start=" +str((pageNum+1)*200) + ";count=200&tag=null?bkt=news-TW-zh-Hant-TW-def&device=desktop&intl=tw&lang=zh-Hant-TW&partner=none&region=TW&site=news&returnMeta=true")',
			'maxPage': 10,
			'urlRule': 'url',
			'isDetailApi': 0,
			'detailRule':{
				'content':'//article[@itemprop="articleBody"]/div/p/descendant-or-self::*/text()',
				'title':'//h1[@itemprop="headline"]/text()',
				'date':'//time[@datetime]/@datetime',
				'img':'',
				'isTimeStamp': 0,
				'dateScript': 'print("pppp===="+pDateStr); tmpDate=dt.strptime(pDateStr, "%Y-%m-%dT%H:%M:%S.%fZ"); tmpDate=tmpDate+timedelta(hours=8); pDateStr=tmpDate.strftime("%Y-%m-%dT%H:%M:%S.%fZ")',
				'dateFormat': '%Y-%m-%dT%H:%M:%S.%fZ',
			},
			'lang':'zh-Hant',
			'st':1
		}

rule98 = {
	    '_id': 'skypost.ulifestyle.com.hk',
	    'beforeScript':'',
	    'startUrls':['http://skypost.ulifestyle.com.hk/sras001/%E6%B8%AF%E8%81%9E?p=1','http://skypost.ulifestyle.com.hk/sras002/%E5%A8%9B%E6%A8%82', 'http://skypost.ulifestyle.com.hk/sras003/%E8%B2%A1%E7%B6%93%E5%9C%B0%E7%94%A2', 'http://skypost.ulifestyle.com.hk/sras004/%E4%B8%AD%E5%9C%8B%E5%9C%8B%E9%9A%9B'],
	    'allFromOneApiItems': 0,
	    'apiScript':'',
	    'UrlsApiItems': 0,
	    'nextPage': '//a[@aria-label="Next" and span[@class="skypost-icon-arrow-right"]]/@href',
	    'maxPage': 100,
	    'urlRule': '//div[@class="listing-widget-03"]/a[@class="listing-overlay"]/@href',
	    'isDetailApi': 0,
	    'detailRule':{
	      'content':'//div[@class="article-detail__img"]/p/text()',
	      'title':'//div[@class="article-title-widget"]/h3[@class="article-details__main-headline"]/text()',
	      'date':'//div[@class="article-details__date-time float-left"]/span/text()',
	      'img':'//picture[@class="photoswipe-img"]/img/@src',
	      'isTimeStamp': 0,
	      'dateScript': '', # pDateStr = pDateStr.replace("/", "-"); m = re.search("(\\d{4}-\\d{2}-\\d{2}).*(\\d{2}:\\d{2})", pDateStr); pDateStr = m.group(1)+ " " + m.group(2)
	      'dateFormat': '%Y/%m/%d',
	    },
	    'lang':'zh-Hant',
	    'st':1
	}

rule99 = {
    '_id': 'theinitium.com',
    'beforeScript':'',
    'startUrls':['https://theinitium.com/channel/feature/', 'https://theinitium.com/channel/news-brief/', 'https://theinitium.com/channel/notes-and-letters/'],
    'allFromOneApiItems': 0,
    'apiScript':'',
    'UrlsApiItems': 0,
    'nextPage': '//a[@class="c-pagination__next"]/@href',
    'maxPage': 100,
    'urlRule': '//a[@class="u-linkUnderline"]/@href',
    'isDetailApi': 0,
    'detailRule':{
        'content':'//div[@itemprop="articleBody"]/*[self::p or self::h2]/text() | //p[@itemprop="description"]/text() | //figcaption[@itemprop="caption"]/child::node()/text()',
        'title':'//h1[@class="p-article__title"]/text()',
        'date':'//time[@class="posted-time"]/@datetime',
        'img':'//figure[@class="p-article__cover image u-section u-section-top--clear"]/img/@src',
        'isTimeStamp': 0,
        'dateScript': '', # pDateStr = pDateStr.replace("/", "-"); m = re.search("(\\d{4}-\\d{2}-\\d{2}).*(\\d{2}:\\d{2})", pDateStr); pDateStr = m.group(1)+ " " + m.group(2)
        'dateFormat': '%Y-%m-%dT%H:%M:%S+08:00',
		},
    'lang':'zh-Hant',
    'st':1
	}

rule100 = {
            '_id': 'news.memehk.com',
            'beforeScript':'',
            'startUrls':['http://news.memehk.com/localnews'],
            'allFromOneApiItems': 0,
            'apiScript':'',
            'UrlsApiItems': 0,
            'nextPage': '//li[@class="next"]/a/@href',
            'maxPage': 30,
            'urlRule': '//div[@class="info"]/p[@class="title"]/a/@href',
            'isDetailApi': 0,
            'detailRule':{
	            'content':'//div[contains(@class, "content")]/descendant-or-self::*/text()',
	            'title':'//h1[@itemprop="name"]/text()',
	            'date':'//div[contains(@class, "publish_date")]/span/text()',
	            'img':'//div[@id="mainimg"]/img/@src',
	            'isTimeStamp': 0,
	            'dateScript': '', # pDateStr = pDateStr.replace("/", "-"); m = re.search("(\\d{4}-\\d{2}-\\d{2}).*(\\d{2}:\\d{2})", pDateStr); pDateStr = m.group(1)+ " " + m.group(2)
	            'dateFormat': u'%Y年%m月%d日 %H時%M分',
            },
            'lang':'zh-Hant',
            'st':1
        }

rule110 = {
		'_id': 'info.gov.hk/ch',
		'beforeScript':'',
		'startUrls':['http://www.info.gov.hk/gia/general/ctoday.htm'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@class="next page-numbers"]/@href',
		'maxPage': 0,
		'urlRule': '//ul[contains(@class, "list")]/li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//span[@id="pressrelease"]/text()',
			'title':'//head/title/text()',
			'date':'//div[@class="mB15 f15"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode("(\\d{4}年\\d{2}月\\d{2}日)"), pDateStrs[1]); part1 = m.group(0); m = re.search(unicode("(\\d{2}時\\d{2}分)"), pDateStrs[2]); part2=m.group(0); pDateStr=part1+part2;',
			'dateFormat': '%Y年%m月%d日%H時%M分',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule111 = {
		'_id': 'info.gov.hk/en',
		'beforeScript':'',
		'startUrls':['http://www.info.gov.hk/gia/general/today.htm'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@class="next page-numbers"]/@href',
		'maxPage': 0,
		'urlRule': '//ul[contains(@class, "list")]/li/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//span[@id="pressrelease"]/text()',
			'title':'//head/title/text()',
			'date':'//div[@class="mB15 f15"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'm = re.search(unicode("(\\d{6}/\\d{2}/)"), response.url); part1 = m.group(0); m = re.search(unicode("(\\d{2}:\\d{2})"), pDateStrs[1]); part2=m.group(0); pDateStr=part1+part2;',
			'dateFormat': '%Y%m/%d/%H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}


rule112 = {
		'_id': 'hk.news.appledaily.com',
		'beforeScript':'',
		'startUrls':['https://hk.news.appledaily.com/realtime/realtimelist/breaking?page=top','https://hk.news.appledaily.com/realtime/realtimelist/top?page=top','https://hk.news.appledaily.com/realtime/realtimelist/local?page=top', 'https://hk.news.appledaily.com/realtime/realtimelist/china?page=top', 'https://hk.news.appledaily.com/realtime/realtimelist/international?page=top', 'https://hk.news.appledaily.com/realtime/realtimelist/finance?page=top' , 'https://hk.news.appledaily.com/realtime/realtimelist/sports?page=top'],
		'allFromOneApiItems': 0,
		'apiScript':'',
		'UrlsApiItems': 0,
		'nextPage': '//a[@class="o-btn o-btn--small w-55@m- w-130@tp+ th-btn"]/@href',
		'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("/page/")[0] + "/page/" + str(pageNum+2))',
		'maxPage': 0,
		'urlRule': '//div[@class="RTitemRHS"]/div[@class="text"]/a/@href',
		'isDetailApi': 0,
		'detailRule':{
			'content':'//div[@class="ArticleContent_Inner"]/p/descendant-or-self::*/text()',
			'title':'//div[@id="articleContent"]//h1/text()',
			'date':'//span[@class="pub_date"]/text()',
			'img':'',
			'isTimeStamp': 0,
			'dateScript': 'print(pDateStrs); m = re.search("(\d{4} \d{1,2}:\d{1,2})", str(pDateStrs)); pDateStr = "2018"+m.group(0);',
			'dateFormat': '%Y%m%d %H:%M',
		},
		'lang':'zh-Hant',
		'st':1
	}

rule113 = {
	'_id': 'paper.wenweipo.com',
	'beforeScript':'',
	'startUrls':['http://paper.wenweipo.com/001YO/', 'http://paper.wenweipo.com/003HK/', 'http://paper.wenweipo.com/002CH/', 'http://paper.wenweipo.com/003TW/', 'http://paper.wenweipo.com/004GJ/', 'http://paper.wenweipo.com/006FI/', 'http://paper.wenweipo.com/007ME/', 'http://paper.wenweipo.com/008ED/', 'http://paper.wenweipo.com/010SP/'],
	'allFromOneApiItems': 0,
	'apiScript':'',
	'UrlsApiItems': 0,
	'nextPage': '//a[@class="o-btn o-btn--small w-55@m- w-130@tp+ th-btn"]/@href',
	'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("/page/")[0] + "/page/" + str(pageNum+2))',
	'maxPage': 0,
	'urlRule': '//div[@class="news-block-content"]//a/@href',
	'isDetailApi': 0,
	'detailRule':{
		'content':'//div[@id="main-content"]/p/descendant-or-self::*/text()',
		'title':'//div[@id="main-header"]/h1/text()',
		'date':'//span[@class="date"]/text()',
		'img':'',
		'isTimeStamp': 0,
		'dateScript': '',
		'dateFormat': '%Y-%m-%d',
	},
	'lang':'zh-Hant',
	'st':1
}

rule114 = {
	'_id': 'hd.stheadline.com',
	'beforeScript':'self.headers["Referer"]="http://hd.stheadline.com/news/realtime"',
	'startUrls':['http://hd.stheadline.com/ajax/getMoreInstantNewsOnList.php?cid=a&page=0', 'http://hd.stheadline.com/ajax/getMoreInstantNewsOnList.php?cid=d&page=0', 'http://hd.stheadline.com/ajax/getMoreInstantNewsOnList.php?cid=h&page=0', 'http://hd.stheadline.com/ajax/getMoreInstantNewsOnList.php?cid=e&page=0', 'http://hd.stheadline.com/ajax/getMoreInstantNewsOnList.php?cid=b&page=0', 'http://hd.stheadline.com/ajax/getMoreInstantNewsOnList.php?cid=c&page=0'],
	'allFromOneApiItems': 0,
	'apiScript':'',
	'UrlsApiItems': 0,
	'nextPage': '//a[@class="o-btn o-btn--small w-55@m- w-130@tp+ th-btn"]/@href',
	'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("page=")[0] + "page=" + str(pageNum+1))',
	'maxPage': 10,
	'urlRule': '//div[@class="topic"]/h4[not(@class)]/a/@href',
	'isDetailApi': 0,
	'detailRule':{
		'content':'//div[@id="news-content"]/p/descendant-or-self::*/text()',
		'title':'//div[@class="topic"]/h1/text()',
		'date':'//time[@class="op-published"]/text()',
		'img':'',
		'isTimeStamp': 0,
		'dateScript': '',
		'dateFormat': '%Y-%m-%d %H:%M',
	},
	'lang':'zh-Hant',
	'st':1
}

rule115 = {
	'_id': 'hd.stheadline.com/news',
	'beforeScript':'',
	'startUrls':['http://hd.stheadline.com/news/realtime/spt/', 'http://hd.stheadline.com/news/realtime/hk/', 'http://hd.stheadline.com/news/realtime/fin/', 'http://hd.stheadline.com/news/realtime/pp/', 'http://hd.stheadline.com/news/realtime/chi/', 'http://hd.stheadline.com/news/realtime/wo/'],
	'allFromOneApiItems': 0,
	'apiScript':'',
	'UrlsApiItems': 0,
	'nextPage': '//a[@class="o-btn o-btn--small w-55@m- w-130@tp+ th-btn"]/@href',
	'nextPageScrip': 'nextPageUrls=[]; nextPageUrls.append(response.url.split("page=")[0] + "page=" + str(pageNum+1))',
	'maxPage': 0,
	'urlRule': '//div[@class="topic"]/h4[not(@class)]/a/@href',
	'isDetailApi': 0,
	'detailRule':{
		'content':'//div[@id="news-content"]/p/descendant-or-self::*/text()',
		'title':'//div[@class="topic"]/h1/text()',
		'date':'//time[@class="op-published"]/text()',
		'img':'',
		'isTimeStamp': 0,
		'dateScript': '',
		'dateFormat': '%Y-%m-%d %H:%M',
	},
	'lang':'zh-Hant',
	'st':1
}
rule116 = {
          '_id': 'paper.hket.com',
          'beforeScript':'',
          'startUrls':['http://paper.hket.com/srap001/%E8%A6%81%E8%81%9E'],
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
              'dateScript': 'print(pDateStr); m = re.search(unicode("(\d{4}年\d{1,2}月\d{1,2}日)"), pDateStr); pDateStr = m.group(0);',
              'dateFormat': '%Y年%m月%d日',
          },
          'lang':'zh-Hant',
          'st':1
      }
#mongoClient['rule']['scrapyRule'].insert(rule53)
#mongoClient['rule']['scrapyRule'].insert(rule54)
#mongoClient['rule']['scrapyRule'].insert(rule55)
#mongoClient['rule']['scrapyRule'].insert(rule56)
#mongoClient['rule']['scrapyRule'].insert(rule58)
#mongoClient['rule']['scrapyRule'].insert(rule61)
#mongoClient['rule']['scrapyRule'].insert(rule62)
#mongoClient['rule']['scrapyRule'].insert(rule63)
#mongoClient['rule']['scrapyRule'].insert(rule64)
#mongoClient['rule']['scrapyRule'].insert(rule65)
#mongoClient['rule']['scrapyRule'].insert(rule66)
#mongoClient['rule']['scrapyRule'].insert(rule67)
#mongoClient['rule']['scrapyRule'].insert(rule68)
#mongoClient['rule']['scrapyRule'].insert(rule69)
#mongoClient['rule']['scrapyRule'].insert(rule70)
#mongoClient['rule']['scrapyRule'].insert(rule71)
#mongoClient['rule']['scrapyRule'].insert(rule72)
#mongoClient['rule']['scrapyRule'].insert(rule73)
#mongoClient['rule']['scrapyRule'].insert(rule92)
#mongoClient['rule']['scrapyRule'].insert(rule93)
#mongoClient['rule']['scrapyRule'].insert(rule97)
#mongoClient['rule']['scrapyRule'].insert(rule98)
#mongoClient['rule']['scrapyRule'].insert(rule100)
mongoClient['rule']['scrapyRule'].insert(rule110)
mongoClient['rule']['scrapyRule'].insert(rule111)

#mongoClient['rule']['scrapyRule'].update({'_id':'hk.news.yahoo.com'}, {'$set':rule97}, True)
#mongoClient['rule']['scrapyRule'].update({'_id':'tw.news.yahoo.com'}, {'$set':rule12}, True)

# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
from wechatSpider.items import WechatspiderItem
class WechatSpider(scrapy.Spider):
    name = "wechat"
    allowed_domains = ["mp.weixin.qq.com"]
    start_urls = ['http://mp.weixin.qq.com/']
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'IPLOC=CN4420; SUV=1506943186112167; ABTEST=7|1506942416|v1; weixinIndexVisited=1; CXID=5D12500D59021E7399D71313F1F3736E; SNUID=FE101C8A55530E4D7C80B78B561D857E; ppinf=5|1507547135|1508756735|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo2OnF6dXNlcnxjcnQ6MTA6MTUwNzU0NzEzNXxyZWZuaWNrOjY6cXp1c2VyfHVzZXJpZDo0NDoyNzVGNzI2NzhEQTEyMDQ1NkEzNjYyNTc1MEIwNDQwREBxcS5zb2h1LmNvbXw; pprdig=qWa4OUzE1V7jnZWg4yi28BlzbppqmCEVxtugIH_Fggcpg4miTfTinUIVxlSH1hajo0HFOsvjeh1MEK7ZcMOZTkIMJrydWDM7AY4XFBQNqNuctnJkdwXT0DejbkAbY72KyREVSQHkScUzsQoYijJD5k3JTfLYyGe34WOzaBkR6xw; sgid=08-31389655-AVnbVicibgcwK5wiaicVxicoibAYM; pgv_pvi=2191015936; sw_uuid=5806069797; dt_ssuid=197528870; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; ssuid=3172653254; cd=1507558955&1f77085a987b907d27e166ccf0d64aa6; GOTO=Af22417-3002; ad=MN4tSZllll2BCESBlllllVXbAgYlllllns@mxkllllwllllljylll5@@@@@@@@@@; SUID=554549DF1508990A00000000591EB0DE; ld=Byllllllll2BLcR7QNm9ICXb0CJBLcYrT1OV$llllx6lllljjylll5@@@@@@@@@@; LSTMV=242%2C73; LCLKINT=95504; ppmdig=15075639020000004eb5e8a786550e64db4915a5227e0eeb; sct=60; JSESSIONID=aaa_21YiQD6W_8okinz6v',
        'Host':'weixin.sogou.com',
        'Pragma':'no-cache',
        'Referer':'http://weixin.sogou.com/weixin?type=2&query=python&ie=utf8&s_from=input&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=14&sourceid=sugg&sut=0&sst0=1507564693572&lkt=0%2C0%2C0&p=40040108',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    searchURl="http://weixin.sogou.com/weixin?type=1&s_from=input&query={keyword}&ie=utf8&_sug_=n&_sug_type_="
    wechatPub=[]
    wechatID=[]
    def start_requests(self):
        keyword=input("关键词输入:")
        yield Request(url=self.searchURl.format(keyword=keyword),dont_filter=True,callback=self.parse,headers=self.headers)
    def parse(self, response):
        for i in range(10):
            condition="sogou_vr_11002301_box_"+str(i)
            pathSelect="//*[@id='"+condition+"']/div/div[2]/p[1]/a/@href"
            href=response.xpath(pathSelect).extract_first()
            self.wechatPub.append(href)
        for i in range(len(self.wechatPub)):
            url=re.sub("^'","",self.wechatPub[i])
            url=re.sub("'$","",self.wechatPub[i])
            yield Request(url=url,callback=self.getBiz,headers=self.headers,dont_filter=True)
    def getBiz(self,response):
        scriptText=response.xpath("/html/body/script[6]/text()").extract_first()
        bizText=scriptText.split(";")[1]
        bizText=bizText.split('"')[1]
        # self.wechatID.append(bizText)
        item=WechatspiderItem()
        item["wechatID"]=bizText
        yield item




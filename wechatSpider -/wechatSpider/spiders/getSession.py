# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from .mongo import MongoOperate
import re
from wechatSpider.items import GetsessionspiderItem
from .settings import *
class GetsessionSpider(Spider):
    name = "getSession"
    allowed_domains = ["mp.weixin.qq.com"]
    start_urls = ['https://mp.weixin.qq.com/']
    headers={
        'Host':'mp.weixin.qq.com',
        # 'X-WECHAT-KEY': 'a83687cde3ca46be517cdbcba60732159f229a03507e9afa1e0dfee00e3cf00562aee022e84b9011924fdbb0c7af8c647c33b1338b11ebdc8893d5df41dd34a536e1af5b48d15c87b4aef629ad8685f3',
        'X-WECHAT-KEY': '33c1fdebcfc1d1ecd9df5003dc9d9ccb6a1f5458eb704e58a05e80c73e8793dede6b52115a74a515d4d12c9a6f2d8f00238afe17cca3635d80d661a612a4a0bf48a2547516b12030efd8a224548636d2',
        'X-WECHAT-UIN':'MTU2MzIxNjQwMQ%3D%3D',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.5.18 NetType/WIFI Language/zh_CN',
        'Accept-Language':'zh-cn',
        'Accept-Encoding':'gzip, deflate',
        'Connection':'keep-alive',
        'Cookie':'wxuin=1563216401;pass_ticket=oQDl45NRtfvQIxv2j2pYDSOOeflIXU7V3x1TUaOTpi6SkMp2B3fJwF6TE40ATCpU;ua_id=Wz1u21T8nrdNEyNaAAAAAOcFaBcyz4SH5DoQIVDcnao=;pgv_pvid=7103943278;sd_cookie_crttime=1501115135519;sd_userid=8661501115135519;3g_guest_id=-8872936809911279616;tvfe_boss_uuid=8ed9ed1b3a838836;mobileUV=1_15c8d374ca8_da9c8;pgv_pvi=8005854208',
        'Referer':"https://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MjM5MzI5MTQ1Mg==&devicetype=iOS10.0.1&version=16051220&lang=zh_CN&nettype=WIFI&ascene=3&fontScale=100&pass_ticket=oQDl45NRtfvQIxv2j2pYDSOOeflIXU7V3x1TUaOTpi6SkMp2B3fJwF6TE40ATCpU&wx_header=1"
   }
    # 查看历史消息列表，现在需要捕获wap_sid2这个值，来获取访问权限
    url="https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz={biz}&scene=124&devicetype=iOS10.0.1&version=16051220&lang=zh_CN&nettype=WIFI&a8scene=3&fontScale=100&pass_ticket=oQDl45NRtfvQIxv2j2pYDSOOeflIXU7V3x1TUaOTpi6SkMp2B3fJwF6TE40ATCpU&wx_header=1"
    def start_requests(self):
        MongoObj=MongoOperate(MONGO_URI,MONGO_DATABASE,MONGO_USER,MONGO_PASS,WECHATID)
        MongoObj.connect()
        items=MongoObj.finddata()
        for item in items:
            biz=item["wechatID"]
            yield Request(url=self.url.format(biz=biz),dont_filter=True,headers=self.headers,callback=self.parse,meta={"proxy":"http://127.0.0.1:8888","biz":biz})
    def parse(self, response):
       item=GetsessionspiderItem()
       data=response.headers
       needCon=data["Set-Cookie"]
       wap=needCon.decode("utf-8")
       wap=wap.split(';')
       wap=wap[0].split('=')
       wap_sid2=wap[1]
       print(wap_sid2)
       item["biz"]=response.request.meta["biz"]
       item["wap_sid2"]=str(wap_sid2)
       yield item
       # print(item)

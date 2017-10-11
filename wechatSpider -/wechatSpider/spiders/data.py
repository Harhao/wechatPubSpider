# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from .mongo import MongoOperate
import json
from .settings import *
class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["mp.weixin.qq.com"]
    start_urls = ['https://mp.weixin.qq.com/']
    count=10
    url="https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz={biz}&f=json&offset={index}&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=ULeI%2BILkTLA2IpuIDqbIla4jG6zBTm1jj75UIZCgIUAFzOX29YQeTm5UKYuXU6JY&wxtoken=&appmsg_token=925_%252B4oEmoVo6AFzfOotcwPrPnBvKbEdnLNzg5mK8Q~~&x5=0&f=json"
    def start_requests(self):
        MongoObj=MongoOperate(MONGO_URI,MONGO_DATABASE,MONGO_USER,MONGO_PASS,RESPONSE)
        MongoObj.connect()
        items=MongoObj.finddata()
        for item in items:
            headers={
                'Accept-Encoding':'gzip, deflate',
                'Connection':'keep-alive',
                'Accept':'*/*',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.5.18 NetType/WIFI Language/zh_CN',
                'Accept-Language': 'zh-cn',
                'X-Requested-With': 'XMLHttpRequest',
                'X-WECHAT-KEY': '62526065241838a5d44f7e7e14d5ffa3e87f079dc50a66e615fe9b6169c8fdde0f7b9f36f3897212092d73a3a223ffd21514b690dd8503b774918d8e86dfabbf46d1aedb66a2c7d29b8cc4f017eadee6',
                'X-WECHAT-UIN': 'MTU2MzIxNjQwMQ%3D%3D',
                'Cookie':';wxuin=1563216401;pass_ticket=oQDl45NRtfvQIxv2j2pYDSOOeflIXU7V3x1TUaOTpi6SkMp2B3fJwF6TE40ATCpU;ua_id=Wz1u21T8nrdNEyNaAAAAAOcFaBcyz4SH5DoQIVDcnao=;pgv_pvid=7103943278;sd_cookie_crttime=1501115135519;sd_userid=8661501115135519;3g_guest_id=-8872936809911279616;tvfe_boss_uuid=8ed9ed1b3a838836;mobileUV=1_15c8d374ca8_da9c8;pgv_pvi=8005854208'

            }
            biz=item["biz"]
        #主要验证是wap_sid2;pass_ticket不一样无所谓
            headers["Cookie"]="wap_sid2="+item["wap_sid2"]+headers["Cookie"]
            yield Request(url=self.url.format(biz=biz,index="10"),headers=headers,callback=self.parse,dont_filter=True,meta={"biz":biz,"headers":headers},)
    def parse(self, response):
        biz=response.request.meta["biz"]
        headers=response.request.meta["headers"]
        resText=json.loads(response.text)
        print(resText)
        list=json.loads(resText["general_msg_list"])
        print(list)
        yield list
        if resText["can_msg_continue"]==1:
            self.count=self.count+10
            yield Request(url=self.url.format(biz=biz,index=str(self.count)),headers=headers,callback=self.parse,dont_filter=True,meta={"biz":biz,"headers":headers})
        else:
            print("end")










# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from .mongo import MongoOperate
import json
class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["mp.weixin.qq.com"]
    start_urls = ['https://mp.weixin.qq.com/']
    headers={
        'Accept-Encoding':'gzip, deflate',
        'Cookie':'wxuin=1563216401; pass_ticket=87+VFUR2WIQtCxajERVead0UhgT/Y4JCXCDtIiIm24H/Lmg3MyMXScWRuC58xhet; wap_sid2=CJGUs+kFElx0QmpNS3pDX3JxUVRlUWhWcTg5ZkplSVJKUlRsZnItT0xsd0ExYVNvckpIbmdBRjA0R29UMGJOSkxrZ2hNUWIxSkc4QlVmY05XRW5OSl9YN2ZmSlVuNTBEQUFBfjDFm/HOBTgNQJVO; ua_id=Wz1u21T8nrdNEyNaAAAAAOcFaBcyz4SH5DoQIVDcnao=; pgv_pvid=7103943278; sd_cookie_crttime=1501115135519; sd_userid=8661501115135519; 3g_guest_id=-8872936809911279616; tvfe_boss_uuid=8ed9ed1b3a838836; mobileUV=1_15c8d374ca8_da9c8; pgv_pvi=8005854208',
        'Connection':'keep-alive',
        'Accept':'*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.5.18 NetType/WIFI Language/zh_CN',
        "Referer":"https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzAxMjcyNjE5MQ==&scene=124&devicetype=iOS10.0.1&version=16051220&lang=zh_CN&nettype=WIFI&a8scene=3&fontScale=100&pass_ticket=87%2BVFUR2WIQtCxajERVead0UhgT%2FY4JCXCDtIiIm24H%2FLmg3MyMXScWRuC58xhet&wx_header=1",
        'Accept-Language': 'zh-cn',
        'X-Requested-With': 'XMLHttpRequest',
        'X-WECHAT-KEY': '62526065241838a5d44f7e7e14d5ffa3e87f079dc50a66e615fe9b6169c8fdde0f7b9f36f3897212092d73a3a223ffd21514b690dd8503b774918d8e86dfabbf46d1aedb66a2c7d29b8cc4f017eadee6',
        'X-WECHAT-UIN': 'MTU2MzIxNjQwMQ%3D%3D'
    }
    count=10
    url="https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz={biz}&f=json&offset={index}&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=87%2BVFUR2WIQtCxajERVead0UhgT%2FY4JCXCDtIiIm24H%2FLmg3MyMXScWRuC58xhet&wxtoken=&appmsg_token=925_%252B4oEmoVo6AFzfOotcwPrPnBvKbEdnLNzg5mK8Q~~&x5=0&f=json"
    def start_requests(self):
        # MongoObj=MongoOperate("ip","zhihu","user","pwd")
        # MongoObj.connect()
        # items=MongoObj.finddata()
        # for item in items:
        #     biz=item["wechatID"]
        yield Request(url=self.url.format(biz="MzAxMjcyNjE5MQ==",index="10"),headers=self.headers,callback=self.parse,dont_filter=True)
    def parse(self, response):
        resText=json.loads(response.text)
        list=json.loads(resText["general_msg_list"])
        print(list)
        # yield list
        if resText["can_msg_continue"]==1:
            self.count=self.count+10
            yield Request(url=self.url.format(biz="MzAxMjcyNjE5MQ==",index=str(self.count)),headers=self.headers,callback=self.parse,dont_filter=True)
        else:
            print("end")















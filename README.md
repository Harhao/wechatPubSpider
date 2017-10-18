# wechatPubSpider
> 微信公众号爬虫，限制一：微信搜狗引擎每个公众号只能爬取10条最近的文章；所以为了爬取喜欢的所有的公众文章。萌发以下思路:要想抓取微信公众号，主要需要两个主要参数:1. __biz(微信公众号id),2.wap_sid2(类似于获取公众号单一文章的权限)。

- 1.获取公众号id:
	- 随意输入关键词，然后获取关键词相关的微信公众号，接着获取微信公众号id。微信公众号id的获取首先是从搜狗引擎微信公众号搜索获取。获取方法：首先通过搜狗的搜索框输入关键词获取你想要的微信公众号（网址 http://weixin.sogou.com/weixin?type=1&s_from=input&query=java&ie=utf8&_sug_=n&_sug_type_= ）其中query是搜索的关键词。获取微信公众号列表。然后从微信公众号中获取单个公众号的链接。例如：( http://mp.weixin.qq.com/profile?src=3&timestamp=1507726402&ver=1&signature=iMJCDXFhGBo97Op01uxzNsyq-ZgPVvXxWmxhi*MFxbO-jY0GKJ7jjKzHiAhLGMldG95QBT6F4B7IKNsGI8G*WQ== )
	- 进入单个微信公众号，然后获取其中的页面的代码。在其中的javascript中存在这个公众号的__biz（微信公众号id）
  ```
     <script type="text/javascript">
     document.domain="qq.com";
     var biz = "MzI3MTA2OTkxNQ==" || "";
     var src = "3" ; 
     var ver = "1" ; 
     var timestamp = "1507726402" ; 
     var signature = "MgPVC3IPsaxxEYqtBq2IOampNVHLxE*D2-f9b*rLZKzoGtUHRNbDczmbZCSVr2xU0so04b-YJ5*pnPENrnDsMg==" ; 
     var name="java--demon"||"xxxx";
     var msgList = {"list":[{"app_msg_ext_info":{"author":"","content":"","content_url":"/s?timestamp=1507726847&amp;src=3&amp;ver=1&amp;signature=7m*l*VL7N2rmoUqDTJ0cU8HGgyZ6W6vz6lCZESAIKyM0FoT7uPgVZghVou*eg9godSOwuIuNLi3tpwgBVaJEIUtJJTebhtJ*I9ld*q8au3PdmTGHiPtNiNqD1RqpDdG25J7*-jP2pSUJIlp8Ygf90XvblaJQpv9RHGCv-Urxljc=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz/xP5fTfMpdGWskgFKqK158QFLCRtvEAqzD5K97yKF7Hd3Gp34JFR0bFrGahRblIfh6eQxcEpDCAnia1I7UIyrL7w/0?wx_fmt=jpeg","del_flag":1,"digest":"111","fileid":403730075,"is_multi":0,"item_show_type":0,"multi_app_msg_item_list":[],"source_url":"","subtype":9,"title":"新年活动"},"comm_msg_info":{"content":"","datetime":1463107392,"fakeid":"3271069915","id":421070031,"status":2,"type":49}},{"app_msg_ext_info":{"author":"","content":"","content_url":"/s?timestamp=1507726847&amp;src=3&amp;ver=1&amp;signature=7m*l*VL7N2rmoUqDTJ0cU8HGgyZ6W6vz6lCZESAIKyM0FoT7uPgVZghVou*eg9godSOwuIuNLi3tpwgBVaJEIT-v9GhM*P30y4ABR7qZCplkPTZPR8fUsx38LmdErF7aPGHE6cTvHYCllVIQS6-rn6VNpzVAO53lVxwGp9*KyME=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz/xP5fTfMpdGWskgFKqK158QFLCRtvEAqzD5K97yKF7Hd3Gp34JFR0bFrGahRblIfh6eQxcEpDCAnia1I7UIyrL7w/0?wx_fmt=jpeg","del_flag":1,"digest":"111","fileid":403730075,"is_multi":0,"item_show_type":0,"multi_app_msg_item_list":[],"source_url":"","subtype":9,"title":"新年活动"},"comm_msg_info":{"content":"","datetime":1453978263,"fakeid":"3271069915","id":403730105,"status":2,"type":49}}]};seajs.use("sougou/profile.js");
  
  ``` 
- 2.wap_sid2单一公众号的所有文章获取的权限值。
	- wap_sid2参数值的获取需要通过对微信手机客户端app进行抓包分析，然后获取其中的权限。从Fiddler中观察，微信客户端进入到单一具体的公众号，获取公众号的历史消息列表。经历了几个网址获取获取的权限值。
  
- 3.使用方法：
	- wechatPubSpider/wechatSpider -/wechatSpider/目录下面的settings文件，MONGO_URI，MONGO_DATABASE，MONGO_USER，MONGO_PASS分别填写项目保存数据的地址IP，数据库，用户以及密码。
	- wechatPubSpider/wechatSpider -/wechatSpider/spiders/目录下面settings文件,MONGO_URI，MONGO_DATABASE,MONGO_USER,MONGO_PASS,ARTICLE,WECHATID,RESPONSE(相同的是如上)，其中不同的，是数据库里面的collectionName，可以随意起喜欢的名字。
- 4.启用顺序：
	- 运行wechat.py文件，然后输入关键词，获取微信公众号ID。存入MongoDB数据库。
	```
	$ scrapy crawl wechat
	```
	- 运行getSession.py文件，获取权限值wap_sid2，并把biz与wap_sid2对应入库。
	```
	$ scrapy crawl getSession
	```
	- 运行data.py文件，爬取数据，存入数据库。
	```
	$ scrapy crawl data
	```
![](https://github.com/laternkiwis/wechatPubSpider/blob/master/%E6%8D%95%E8%8E%B7.PNG)	
> 如果遇到异常，可以通过抓包，获取请求头信息的X-wechat-key值。这个值有时间限制，大概几分钟更新一次。所以可以手动去更新该值,如果想了解更多，可以浏览(微信公众号文章爬虫)[http://www.jianshu.com/p/67a8f5c92b49]

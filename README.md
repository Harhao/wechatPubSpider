# wechatPubSpider
> 微信公众号爬虫，限制一：微信搜狗引擎每个公众号只能爬取10条最近的文章；所以为了爬取喜欢的所有的公众文章。萌发以下思路:要想抓取微信公众号，主要需要两个主要参数:1. __biz(微信公众号id),2.wap_sid2(类似于获取公众号单一文章的权限)。

- 1.获取公众号id:
  - 随意输入关键词，然后获取关键词相关的微信公众号，接着获取微信公众号id。微信公众号id的获取首先是从搜狗引擎微信公众号搜索获取。获取方法：首先通过搜狗的搜索框输入关键词获取你想要的微信公众号（网址 http://weixin.sogou.com/weixin?type=1&s_from=input&query=java&ie=utf8&_sug_=n&_sug_type_= ）其中query是搜索的关键词。获取微信公众号列表。然后从微信公众号中获取单个公众号的链接。例如：( http://mp.weixin.qq.com/profile?src=3&timestamp=1507726402&ver=1&signature=iMJCDXFhGBo97Op01uxzNsyq-ZgPVvXxWmxhi*MFxbO-jY0GKJ7jjKzHiAhLGMldG95QBT6F4B7IKNsGI8G*WQ== ) 
  - 进入单个微信公众号，然后获取其中的页面的代码。在其中的javascript中存在这个公众号的__biz（微信公众号id）


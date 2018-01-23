import scrapy
from mnews.items import MnewsItem
from datetime import datetime

class InfoMoneySpider(scrapy.Spider):
    name = "infomoney"
    last_time = datetime_object = datetime.strptime('23 jan, 2005 - 17h:04', '%d %b, %Y - %Hh:%M')
    base_url = "http://www.infomoney.com.br"

    def start_requests(self):
        urls = [
            "http://www.infomoney.com.br/ultimas-noticias"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        str_time = response.xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/text()").extract()
        str_time = str_time[1].replace(u'\xa0','').rstrip()
        print(str_time)
        time_object =  datetime.strptime(str_time, '%d %b, %Y - %Hh%M')
        if time_object > self.last_time:
            self.last_time = time_object
            link = response.xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div[1]/div/div[2]/a/@href")
            link = link.extract()[0]
            link = self.base_url + link
            print(link)
            yield scrapy.Request(url=link, callback=self.parse2)

    def parse2(self, response):
        text = response.xpath("//*[@id='notcopyarea']/div[1]/div[1]/div[1]").extract()
        print(text)

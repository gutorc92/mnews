import scrapy
from mnews.items import MnewsItem

class Brasil247Spider(scrapy.Spider):
    name = "brasil247"

    def start_requests(self):
        urls = [
            'https://www.brasil247.com/pt/247/economia/336427/Guru-de-Alckmin-quer-privatizar-Petrobras.htm',
            'https://www.brasil247.com/pt/247/brasil/336517/Temer-adia-recurso-pela-posse-de-Cristiane-para-evitar-derrota-no-STF.htm',
            'https://www.brasil247.com/pt/colunistas/geral/336437/A-desinformação-como-fonte-de-ira.htm',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ps = response.xpath("//*[@id='wrapper']/div[6]/section[1]/div[1]/p[not(@*)]/text()")
        text = ""
        for p in ps:
            text += p.extract() + " "
        text = text.strip("\n\r")
        title = response.xpath("//*[@id='wrapper']/div[5]/h2/text()").extract()
        if type(title) == list and len(title) == 1:
            title = title[0].strip("\n\r ")
        date = response.xpath("//*[@id='wrapper']/div[5]/p[4]/text()").extract()
        item = MnewsItem(title=title, date = date, text = text)
        return item
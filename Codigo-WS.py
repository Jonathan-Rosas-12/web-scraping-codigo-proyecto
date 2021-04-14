# -*- coding: utf-8 -*-
#Librerias 
'''from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
import random
from time import sleep

numItems=0
dominiosP=''
semilla=''
#Item a extraer

class item(Item):
    dato1=Field()
    dato2=Field()
    dato3=Field()
    
#Crawler/Spider 

class Crawler(CrawlSpider):
    name='Crawler'
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': numItems
    }
    allowed_domains = [dominiosP]

    start_urls = [semilla]

    download_delay = sleep(random.uniform(1.0, 4.0))
    
    rules = (
        Rule( 
            LinkExtractor(
                allow=r'/ciencia-ficcion/d+'
            ), follow=True),
        Rule( 
            LinkExtractor(
                allow=r'/ebook/' 
            ), follow=True, callback='parse_items'), 
    )
class Spider(Spider):
    name='Spider'
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',

    }
    allowed_domains = ['tuslibros.com']

    start_urls = ['https://www.tuslibros.com/categoria/ciencia-ficcion']

    download_delay = sleep(random.uniform(1.0, 4.0))
    

process= CrawlerProcess({
    'FEED_FORMAT':'json',
    'FEED_URI': 'lib.json'
    })
process.crawl(Crawler)
process.start()'''
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r"C:\dChrome\chromedriver.exe")
driver.get('http://sigeh.hidalgo.gob.mx/pags/crear_consulta.php')
sleep(4)
driver.refresh() # Solucion de un bug extraño en Windows en donde los anuncios solo cargan al hacerle refresh o al darle click a algun elemento
sleep(5)

boton = driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/ul/li[1]')
boton.click()
sleep(3)
boton2 = driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/div/div/form/div/div/select/option[2]')
boton2.click()
sleep(4)  

driver.close()     
     
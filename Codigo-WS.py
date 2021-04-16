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
import random

driver = webdriver.Chrome(executable_path=r"C:\dChrome\chromedriver.exe")
driver.get('http://sigeh.hidalgo.gob.mx/pags/crear_consulta.php')
sleep(random.uniform(3.0, 4.0))
driver.refresh() 
sleep(random.uniform(2.0, 4.0))
contador =0
try:
    
    while contador <84:
        seleccion = str(contador+2)
        boton = driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/ul/li[1]')
        boton.click()
        sleep(random.uniform(3.0, 4.0))
        boton1 = driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/div/div/form/div/div/select')
        boton1.click()
        sleep(random.uniform(2.0, 4.0))

        boton2 = driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/div/div/form/div/div/select/option['+seleccion+']')
        boton2.click()
        sleep(random.uniform(5.0, 6.0))
        print('Municipio: '+boton2.text)

        for j in range(3):
            a = str(j+1)
            for k in range(4):
                b = str(k+1)
                c= '//div[@class="container landing-wrapper"]/div/div/div/form/div/div/div/div['+a+']/div['+b+']/label/input'
                boton3 = driver.find_element_by_xpath(c)
                boton3.click()
                sleep(random.uniform(3.0, 4.0))
            
        boton0= driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/div/div/form/div/div[2]/div/div/div/label/input')  
        boton0.click()
        sleep(random.uniform(2.0, 4.0))

        boton4=  driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/div/div/form/div/button')
        boton4.click()
        sleep(random.uniform(10.0, 12.0))
        titulos= driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/h2')
        fuentes = driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/p')
        i=0

        for i in range(len(titulos)):
            a= str(i+3)
            print(titulos[i].text)
            print(fuentes[i].text)
            conceptos = driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/div'+'['+a+']'+'/table/tbody/tr/th')
            valores = driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/div'+'['+a+']'+'/table/tbody/tr/td')
            print('Concepto: ')
            for j in range(len(conceptos)):
                b = str(j+1)
                c = '//div[@class="container landing-wrapper"]/div'+'['+a+']'+'/table/tbody/tr'+'['+b+']'+'/th'
                concepto = driver.find_element_by_xpath(c)
                print (concepto.text) 
                print('valor: ')
                a= str(i+3)
            for k in range(len(valores)):
                b = str(k+1)
                c= '//div[@class="container landing-wrapper"]/div'+'['+a+']'+'/table/tbody/tr'+'['+b+']'+'/td'
                valor = driver.find_element_by_xpath(c)
                print(valor.text)
            
        boton5= driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/article/h3/a')
        boton5.click()
        
        sleep(random.uniform(4.0, 6.0))
        contador+=1
        
except:
    print('Error')
driver.close()  
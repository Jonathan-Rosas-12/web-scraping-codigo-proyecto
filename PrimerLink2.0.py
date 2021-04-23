from time import sleep
from selenium import webdriver
import random

driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
driver.get('http://sigeh.hidalgo.gob.mx')
sleep(random.uniform(3.0, 4.0))
driver.refresh() 
sleep(random.uniform(2.0, 4.0))
contador =0
archivo = "indicadores.csv"
csv= open(archivo,"w")
try:
    selector1= driver.find_element_by_xpath('//*[@id="navbarMainCollapse2"]/ul/li[2]/a')
    selector1.click()
    sleep(random.uniform(3.0, 4.0))

    seleccion= driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/article[2]/h3/a')
    seleccion.click()
    sleep(random.uniform(2.0, 5.0))

    for i in range(2):
        indicadores= driver.find_elements_by_xpath('//div[@class="col-lg-12"]/div/div/div/h4/a')
        a=str(i+2)
        ejes= driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/div['+a+']/div/div/div/div/ul/a')

        titulor= indicadores[i].text +","+"Indicador, Fuente, Descripcion, Teporalidad,Confiabilidad de la fuente, Ultimo Dato Disponible,Valor Hidalgo, Valor Nacional,Lugar Nacional\n"
        csv.write(titulor)
        
        for j in range(len(ejes)):
            indicadores= driver.find_elements_by_xpath('//div[@class="col-lg-12"]/div/div/div/h4/a')
            indicador= indicadores[i]
            sleep(random.uniform(5.0, 7.0))
            k= str(j+1)
            indicador.click()
            
            sleep(random.uniform(3.0, 6.0))
            indicador_consulta= driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div['+a+']/div/div/div/div/ul['+k+']/a')
            indicador_consulta.click()
            sleep(random.uniform(2.0, 5.0))
            nombre_indicador= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div/div/h5')

            fuente_indicador= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[1]/div/h3')

            descripcion_indicador= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div/div/p[2]')

            temporalidad_indicador= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[2]/div/h3')

            confiabilidad_de_la_fuente= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[3]/div[1]/h3')

            ultimo_dato= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[6]/div[1]/p[2]')

            valor_hidalgo= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[6]/div[2]/p[2]')

            valor_nacional= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[6]/div[3]/p[2]')

            lugar_nacional= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[6]/div[4]/p[2]')
 
            filas = "   "+","+ nombre_indicador.text+","+fuente_indicador.text+","+descripcion_indicador.text+","+temporalidad_indicador.text+","+confiabilidad_de_la_fuente.text+","+ultimo_dato.text+","+valor_hidalgo.text+","+valor_nacional.text+","+lugar_nacional.text+","+"\n"
            csv.write(filas)
            driver.back()
        
except Exception as e:
    print(e)
    print("Fin de la extraccion")
    
driver.close()

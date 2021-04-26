from time import sleep
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import urllib
from urllib import request
from urllib.parse import urlparse
from flask import Flask, render_template, redirect, url_for, request

app=Flask(__name__)
@app.route('/')
def home():    
       return render_template('SitioWeb-Sigeh-Principal.html')

@app.route('/extraccion', methods=['POST', 'GET'])
def extraccion():
    liga=request.form['link']
    xpath1=request.form['xpath1']
    xpath2=request.form['xpath2']
    xpath3=request.form['xpath3']
    xpath4=request.form['xpath4']
    nItems=request.form['numberI']
    archivo=request.form['docdest']

    validadorNItems=nItems.isdigit()
    partes=urlparse(liga)
    if(partes.scheme==""):
         return render_template('ErrorExtraccion.html')
    resp=urllib.request.urlopen(liga)
    validacionU=resp.code
    if(validacionU!=200):
          return render_template('ErrorExtraccion.html')
    if(validadorNItems==False):
         return render_template('ErrorExtraccion.html')
    nItems=int(nItems)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"./chromedriver.exe")
    driver.get(liga)
    sleep(random.uniform(2.0, 3.0))
    driver.refresh() 
    sleep(random.uniform(2.0, 3.0))
    datos="DatosE-Principal-Sigeh"+archivo
    documento = "docs/DatosE-Principal-Sigeh"+archivo
    DE= open(documento,"w")
    try:
        
        for i in range(nItems):
            sleep(random.uniform(3.0, 4.0))
            indicadores= driver.find_elements_by_xpath('//div[@class="col-lg-12"]/div/div/div/h4/a')
            a=str(i+2)
            ejes= driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/div['+a+']/div/div/div/div/ul/a')

            titulor= indicadores[i].text +","+"Indicador, Fuente, Confiabilidad de la fuente, Descripcion, Teporalidad,Confiabilidad de la fuente, Ultimo Dato Disponible,Valor Hidalgo, Valor Nacional,Lugar Nacional\n"
            DE.write(titulor)
            for j in range(len(ejes)):
                indicadores= driver.find_elements_by_xpath('//div[@class="col-lg-12"]/div/div/div/h4/a')
                indicador= indicadores[i]
                sleep(random.uniform(3.0, 4.0))
                k= str(j+1)
                indicador.click()
            
                sleep(random.uniform(3.0, 5.0))
                indicador_consulta= driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div['+a+']/div/div/div/div/ul['+k+']/a')
                indicador_consulta.click()
                sleep(random.uniform(2.0, 3.0))
                if xpath1=="titulos" or xpath2=="titulos" or xpath3=="titulos" or xpath4=="titulos":
                    nombre_indicador= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div/div/h5')
                    fila1=" "+","+nombre_indicador.text
                    DE.write(fila1)
                if xpath1=="fuentes" or xpath2=="fuentes" or xpath3=="fuentes" or xpath4=="fuentes":
                    fuente_indicador= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[1]/div/h3')
                    confiabilidad_de_la_fuente= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[3]/div[1]/h3')
                    fila2= ","+fuente_indicador.text+","+confiabilidad_de_la_fuente.text
                    DE.write(fila2)
                if xpath1=="conceptos" or xpath2=="conceptos" or xpath3=="conceptos" or xpath4=="conceptos":
                    descripcion_indicador= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div/div/p[2]')
                    fila3=","+descripcion_indicador.text
                    DE.write(fila3)
                if xpath1=="" or xpath2=="" or xpath3=="" or xpath4=="":
                    temporalidad_indicador= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[2]/div/h3')
                    fila4=","+temporalidad_indicador.text
                    DE.write(fila4)
                    
                if xpath1=="valores" or xpath2=="valores" or xpath3=="valores" or xpath4=="valores":
                    ultimo_dato= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[6]/div[1]/p[2]')
                    valor_hidalgo= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[6]/div[2]/p[2]')
                    valor_nacional= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[6]/div[3]/p[2]')
                    lugar_nacional= driver.find_element_by_xpath('//div[@class="container-fluid"]/div/div/div[6]/div[4]/p[2]')
                    filas = ","+ ultimo_dato.text+","+valor_hidalgo.text+","+valor_nacional.text+","+lugar_nacional.text+","+"\n"
                    DE.write(filas)
                boton5= driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/article/h3/a')
                boton5.click()
                sleep(random.uniform(2.0, 4.0))
                
        
    except Exception as e:
           print(e)
           print('Error de extraccion')
           return render_template('ErrorExtraccion.html')
    driver.close()
    print('Fin de la extraccion')
    DE.close()
    return render_template('Extraccion.html', doc=datos, dat=documento) 


if __name__=='__main__':
    app.run(debug=True)   



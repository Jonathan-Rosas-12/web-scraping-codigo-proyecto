from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import urllib
from urllib import request
from urllib.parse import urlparse
from flask import Flask, render_template, redirect, url_for, request
from selenium.webdriver.chrome.options import Options

app=Flask(__name__)
@app.route('/')
def home():    
       return render_template('SitioWeb.html')

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
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"./chromedriver.exe")
    driver.get(liga) 
    contador =0
    if archivo==".csv":
        csv= open("archivo8.csv","w")
    
    try:
    
        while contador < nItems:
              
              
              seleccion = str(contador+2)
              boton = driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/ul/li[1]')
              boton.click()
              WebDriverWait(driver,10).until(
                  EC.presence_of_all_elements_located((By.XPATH, '//div[@class="container landing-wrapper"]')
                  ))
              

              boton2 = driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/div/div/form/div/div/select/option['+seleccion+']')
              boton2.click()
              csv.write(boton2.text)
              csv.write("\n")
        
              botones= driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/div/div/div/form/div/div/div/div/div/label/input')
              for i in range(len(botones)):
                  boton3 = botones[i]
                  boton3.click()
                  
              boton4= WebDriverWait(driver,10).until(
                  EC.presence_of_element_located((By.XPATH, '//div[@class="container landing-wrapper"]/div/div/div/form/div/button')
                  ))    

              boton4.click()
                          
              
              WebDriverWait(driver,8).until(
                        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="container landing-wrapper"]')
                        ))

              titulos= driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/h2')
              fuentes = driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/p')

              for i in range(len(titulos)):
                    a= str(i+3)
                    if xpath1=="titulos" or xpath2=="titulos" or xpath3=="titulos" or xpath4=="titulos":
                        titulo= titulos[i].text
                        titulo = titulo.replace(',',' ')
                        csv.write(titulo)
                        csv.write("\n")
                    if xpath1=="fuentes" or xpath2=="fuentes" or xpath3=="fuentes" or xpath4=="fuentes":
                        fuente=fuentes[i].text
                        fuente= fuente.replace(',',' ')
                        csv.write(fuente)
                        csv.write("\n")
                    if xpath1=="conceptos" or xpath2=="conceptos" or xpath3=="conceptos" or xpath4=="conceptos":
                        if xpath1=="valores" or xpath2=="valores" or xpath3=="valores" or xpath4=="valores":
                            titulor= "Concepto,valor\n"
                            csv.write(titulor)

                    conceptos = driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/div'+'['+a+']'+'/table/tbody/tr/th')
                    
                    
                    for j in range(len(conceptos)):
                        b = str(j+1)
                        if xpath1=="conceptos" or xpath2=="conceptos" or xpath3=="conceptos" or xpath4=="conceptos":
                            c = '//div[@class="container landing-wrapper"]/div'+'['+a+']'+'/table/tbody/tr'+'['+b+']'+'/th'
                            concepto = driver.find_element_by_xpath(c).text
                            concepto = concepto.replace(',',' ')
                            if xpath1=="valores" or xpath2=="valores" or xpath3=="valores" or xpath4=="valores":
                                c = '//div[@class="container landing-wrapper"]/div'+'['+a+']'+'/table/tbody/tr'+'['+b+']'+'/th'
                                concepto = driver.find_element_by_xpath(c).text
                                concepto = concepto.replace(',',' ')
                                d= '//div[@class="container landing-wrapper"]/div'+'['+a+']'+'/table/tbody/tr'+'['+b+']'+'/td'
                                valor = driver.find_element_by_xpath(d).text
                                valor = valor.replace(',',' ')
                                filas = concepto+","+valor+"\n"
                                csv.write(filas)
                            else:
                                 csv.write(concepto)
                                 csv.write("\n")
                        else: 

                            if xpath1=="valores" or xpath2=="valores" or xpath3=="valores" or xpath4=="valores":
                                d= '//div[@class="container landing-wrapper"]/div'+'['+a+']'+'/table/tbody/tr'+'['+b+']'+'/td'
                                valor = driver.find_element_by_xpath(d).text
                                valor = valor.replace(',',' ')
                                csv.write(valor)
                                csv.write("\n")
 
              boton5= driver.find_element_by_xpath('//div[@class="container landing-wrapper"]/div/article/h3/a')
              boton5.click()
              
              WebDriverWait(driver,8).until(
                  EC.presence_of_all_elements_located((By.XPATH, '//div[@class="container landing-wrapper"]')
                  ))
              
              contador+=1
              csv.write("\n")
    except Exception as e:
       print(e)
       print('Error de extraccion')
       return render_template('ErrorExtraccion.html')
    driver.close()
    print('Fin de la extraccion')
    return render_template('Extraccion.html')    

      
if __name__=='__main__':
    app.run(debug=True)    
    
   


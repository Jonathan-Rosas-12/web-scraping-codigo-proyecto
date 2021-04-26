from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import urllib
from urllib import request
from urllib.parse import urlparse
from flask import Flask, render_template, redirect, url_for, request

app=Flask(__name__)
@app.route('/')
def home():    
       return render_template('SitioWeb-PoblacionHidalgo.html')

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
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\dChrome\chromedriver.exe")
    #driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
    driver.get(liga)
    datos="Informacion-Poblacion"+archivo
    documento = "docs/Informacion-Poblacion"+archivo
    DE= open(documento,"w")
    try:
        #archivo = "Poblacion.csv"
        #DE= open(archivo,"w")
    
        boton = WebDriverWait(driver,10).until(
                 EC.presence_of_element_located((By.XPATH, '//*[@id="Modalveda"]/div/div/div[1]/button/span'))
                 )
        boton.click()
        WebDriverWait(driver,10).until(
                  EC.presence_of_all_elements_located((By.XPATH, '//div[@class="col-md-4 card-indicador"]/a')
        ))
        cantidades=driver.find_elements_by_xpath('//div[@class="col-md-4 card-indicador"]/a/h2')
        parrafos=driver.find_elements_by_xpath('//div[@class="col-md-4 card-indicador"]/a/p')
        
        if xpath1=='indices' or xpath2=='indices' or xpath3=='indices' or xpath4=='indices':
            DE.write('Indices:'+'\n')
            for j in range(len(cantidades)):
                WebDriverWait(driver,20).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-4 card-indicador"]/a')
                ))
                cantidad = cantidades[j].text
                cantidad= cantidad.replace(',',' ')
                parrafo=parrafos[j].text
                parrafo=parrafo.replace(',',' ')
                DE.write(cantidad+','+parrafo+'\n')
        
        
        WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="row row-gob row-body"]/div/div/article')
            ))

        boton1 = driver.find_element_by_xpath('//div[@class="row row-gob row-body"]/div/div/article[1]/h3/a')
        boton1.click()
        
        WebDriverWait(driver,6).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div/div/div')
            ))
        informacion= driver.find_element_by_xpath('/html/body/div[2]/div/div/h2').text
        informacion=informacion.replace(',',' ')
        DE.write(informacion)
        DE.write("\n")
        parrafo1= driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p').text
        parrafo1=parrafo1.replace(',',' ')
        DE.write(parrafo1)
        DE.write(informacion+','+parrafo1+'\n')
        DE.write("\n")
        sleep(random.uniform(10.0, 12.0))

        for i in range(nItems):
            boton = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Modalveda"]/div/div/div[1]/button/span'))
                )
            boton.click()
        
            WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="container container-small"]/div/div/div/div/div/article')
                ))
            sleep(random.uniform(10.0, 12.0))
            elementos= driver.find_elements_by_xpath('//div[@class="container container-small"]/div/div/div/div/div/article/a')
            try:
                elemento= elementos[i].get_attribute('href')
                driver.get(elemento)
                sleep(random.uniform(10.0, 12.0))
                if elementos[i]==elementos[0] or elementos[i]==elementos[3] or elementos[i]==elementos[8]:
                    if xpath1=="titulos" or xpath2=="titulos" or xpath3=="titulos" or xpath4=="titulos":
                        titulo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/h2').text
                        titulo2= titulo2.replace(',',' ')
                        DE.write(titulo2)
                        DE.write("\n")
                    if xpath1=="conceptos" or xpath2=="conceptos" or xpath3=="conceptos" or xpath4=="conceptos":
                        parrafo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p').text
                        parrafo2=parrafo2.replace(',',' ')
                        DE.write(parrafo2)
                        DE.write("\n")
                    driver.back()
                    
                if elementos[i]== elementos[1] or elementos[i]==elementos[2]:
                    titulos=driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/section/header/h2')
                    parrafos=driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/section/div/div/p')
                    for k in range(len(titulos)):
                        if xpath1=="titulos" or xpath2=="titulos" or xpath3=="titulos" or xpath4=="titulos":
                            titulo2=titulos[k].text
                            titulo2= titulo2.replace(',',' ')
                            DE.write(titulo2)
                            DE.write("\n")
                        if xpath1=="conceptos" or xpath2=="conceptos" or xpath3=="conceptos" or xpath4=="conceptos":
                            parrafo2=parrafos[k].text
                            parrafo2=parrafo2.replace(',',' ')
                            DE.write(parrafo2)
                            DE.write("\n")
                    driver.back()
                    
                if elementos[i]== elementos[4]:
                    if xpath1=="titulos" or xpath2=="titulos" or xpath3=="titulos" or xpath4=="titulos":
                        titulo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/header/h2').text
                        titulo2= titulo2.replace(',',' ')
                        DE.write(titulo2)
                        DE.write("\n")
                    if xpath1=="conceptos" or xpath2=="conceptos" or xpath3=="conceptos" or xpath4=="conceptos":
                        parrafo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/div/p').text
                        parrafo2=parrafo2.replace(',',' ')
                        DE.write(parrafo2)
                        DE.write("\n")
                    driver.back()
                    
                if elementos[i]== elementos[5]:
                    if xpath1=="titulos" or xpath2=="titulos" or xpath3=="titulos" or xpath4=="titulos":
                        titulo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/div/header/h2').text
                        titulo2= titulo2.replace(',',' ')
                        DE.write(titulo2)
                        DE.write("\n")
                    if xpath1=="conceptos" or xpath2=="conceptos" or xpath3=="conceptos" or xpath4=="conceptos":
                        parrafo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/div/div/div/p').text
                        parrafo2=parrafo2.replace(',',' ')
                        DE.write(parrafo2)
                        DE.write("\n")
                    driver.back()
                   
                if elementos[i]== elementos[6] or elementos[i]== elementos[7]:
                    if xpath1=="titulos" or xpath2=="titulos" or xpath3=="titulos" or xpath4=="titulos":
                        titulo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/section/h2').text
                        titulo2= titulo2.replace(',',' ')
                        DE.write(titulo2)
                        DE.write("\n")
                    if xpath1=="conceptos" or xpath2=="conceptos" or xpath3=="conceptos" or xpath4=="conceptos":
                        parrafo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div[2]/div/p').text
                        parrafo2=parrafo2.replace(',',' ')
                        DE.write(parrafo2)
                        DE.write("\n")
                    driver.back()
                    
                    
            except Exception as e:
                print(e)
                driver.back()


    except Exception as e:
        print(e)
        print('Error en la extraccion')
        return render_template('ErrorExtraccion.html')
    driver.close()
    print('Fin de la extraccion')
    DE.close()
    return render_template('Extraccion.html', doc=datos, dat=documento) 

if __name__=='__main__':
    app.run(debug=True)   


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
#chrome_options = Options()
#chrome_options.add_argument("--headless")

#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\dChrome\chromedriver.exe")
driver = webdriver.Chrome(executable_path=r"C:\dChrome\chromedriver.exe")
driver.get('http://poblacion.hidalgo.gob.mx/')
archivo = "consulta_municipio.csv"
csv= open(archivo,"w")
try:
    
        boton = WebDriverWait(driver,10).until(
                 EC.presence_of_element_located((By.XPATH, '//*[@id="Modalveda"]/div/div/div[1]/button/span'))
                 )
        boton.click()
        WebDriverWait(driver,10).until(
                  EC.presence_of_all_elements_located((By.XPATH, '//div[@class="col-md-4 card-indicador"]/a')
        ))
        cantidades=driver.find_elements_by_xpath('//div[@class="col-md-4 card-indicador"]/a/h2')
        parrafos=driver.find_elements_by_xpath('//div[@class="col-md-4 card-indicador"]/a/p')
        print(len(cantidades))

        for j in range(len(cantidades)):
            WebDriverWait(driver,20).until(
                  EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-4 card-indicador"]/a')
            ))
            cantidad = cantidades[j].text
            parrafo=parrafos[j].text
            print(cantidad+' '+parrafo)
        
        
        WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="row row-gob row-body"]/div/div/article')
            ))

        boton1 = driver.find_element_by_xpath('//div[@class="row row-gob row-body"]/div/div/article[1]/h3/a')
        boton1.click()
        
        WebDriverWait(driver,6).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div/div/div')
            ))
        informacion= driver.find_element_by_xpath('/html/body/div[2]/div/div/h2')
        print(informacion.text)
        parrafo1= driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p')
        print(parrafo1.text)
        sleep(random.uniform(10.0, 12.0))

        for i in range(3):
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
                print(elemento)
                #driver.back()
                sleep(random.uniform(10.0, 12.0))
                if elementos[i]==elementos[0] or elementos[i]==elementos[3] or elementos[i]==elementos[8]:
                    titulo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/h2')
                    print(titulo2.text)
                    parrafo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p')
                    print(parrafo2.text)
                    driver.back()
                    sleep(random.uniform(10.0, 12.0))
                if elementos[i]== elementos[1] or elementos[i]==elementos[2]:
                    titulos=driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/section/header/h2')
                    parrafos=driver.find_elements_by_xpath('//div[@class="container landing-wrapper"]/section/div/div/p')
                    for k in range(len(titulos)):
                        titulo2=titulos[k]
                        print(titulo2.text)
                        parrafo2=parrafos[k]
                        print(parrafo2.text)
                    driver.back()
                    sleep(random.uniform(10.0, 12.0))
                if elementos[i]== elementos[4]:
                    titulo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/header/h2')
                    print(titulo2.text)
                    parrafo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/div/p')
                    print(parrafo2.text)
                    driver.back()
                    sleep(random.uniform(10.0, 12.0))
                if elementos[i]== elementos[5]:
                    titulo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/div/header/h2')
                    print(titulo2.text)
                    parrafo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/div/div/div/p')
                    print(parrafo2.text)
                    driver.back()
                    sleep(random.uniform(10.0, 12.0))
                if elementos[i]== elementos[6] or elementos[i]== elementos[7]:
                    titulo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/section/h2')
                    print(titulo2.text)
                    parrafo2=driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div[2]/div/p')
                    print(parrafo2.text)
                    sleep(random.uniform(10.0, 12.0))
            except Exception as e:
                print(e)
                driver.back()
        WebDriverWait(driver,6).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="container container-small"]/div/div/div/div/div/article')
            ))
        sleep(random.uniform(10.0, 12.0))

except Exception as e:
    print(e)

driver.close()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Importe a classe Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Especifique o caminho para o driver executável
driver_path = 'C:\\Users\\rodmi\\Desktop\\Programação\\Python\\drivers\\chromedriver.exe'

# Inicialize o serviço do Chrome
chrome_service = Service(driver_path)

# Inicialize o driver do Selenium
driver = webdriver.Chrome(service=chrome_service)

# Abra a página da web
driver.get('https://statusinvest.com.br/acoes/bbas3')

# Role para baixo para garantir que o elemento seja carregado
driver.execute_script('window.scrollBy(0, 500);')

# Aguarde até que a div com a classe "indicator-today-container" seja visível
wait = WebDriverWait(driver, 10)
div_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'indicator-today-container')))

# Encontre o elemento dentro da div com a classe "indicator-today-container"
value_element = div_element.find_element(By.CSS_SELECTOR, '.value')

# Extraia o texto do elemento
valor = value_element.text

# Imprima o valor coletado
print('Valor do DY:', valor)

# Feche o navegador
driver.quit()

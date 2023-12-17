import urllib
import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd

from IPython.display import display
import openpyxl

contatos_df = pd.read_excel("Enviar (1).xlsx")
display(contatos_df)


navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")


wait = WebDriverWait(navegador, 30)
elemento_side = wait.until(EC.presence_of_element_located((By.ID, "side")))


while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(10)

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(20)

    navegador.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(20)

print(selenium.__version__)

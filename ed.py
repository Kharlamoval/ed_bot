import requests
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


apiServer = 'https://api.alor.ru'
def DayMarketAlor(apiServer, symbol):
    return requests.get(url=f'{apiServer}/md/v2/Securities/{symbol}/quotes')
ed = DayMarketAlor(apiServer,'MOEX:EDM3').json()

seconds_ed = ed[0]['last_price_timestamp']
time_ed = time.strftime('%H:%M:%S %d.%m.%y',time.localtime(seconds_ed))


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://ru.tradingview.com/chart/?symbol=FX%3AEURUSD")
driver.implicitly_wait(20)

while True:
    #fiyat_Bilgisi = driver.find_element_by_xpath().text
    fiyat_Bilgisi = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[5]/span[1]/span[1]").text
    print(fiyat_Bilgisi)
    sleep(10)


spred = int((fiyat_Bilgisi - ed[0]['last_price'])*10000)


def edit_msg(text):
    token = "5886218730:AAHgUBVQJg4V9t_bomUnsCHi4BFgtGLISac"
    chat_id = "-1001854452864"
    message_id = 16
    url_req = "https://api.telegram.org/bot" + token + "/editMessageText" + "?chat_id=" + chat_id + "&text=" + text + "&message_id=" + str(message_id)
    results = requests.get(url_req)
  
time.strftime('%H:%M:%S %d.%m.%y',time.localtime())
edit_msg(str(spred) + 'pt' + str(' [') + str(time.strftime('%H:%M:%S %d.%m.%y',time.localtime()))+ str(']') + '\n%F0%9F%87%B7%F0%9F%87%BA ' + str(ed[0]['last_price']) + str (' [')+ str(time_ed)+ str(']')+ '\n%F0%9F%87%AA%F0%9F%87%BA '+ str(round(fiyat_Bilgisi, 4)) + str (' [')+ str(time_eurusd)+ str(']'))


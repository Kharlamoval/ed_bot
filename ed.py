#!/usr/bin/env python3
import requests


apiServer = 'https://api.alor.ru'
def DayMarketAlor(apiServer, symbol):
   
    return requests.get(url=f'{apiServer}/md/v2/Securities/{symbol}/quotes')

ed = DayMarketAlor(apiServer,'MOEX:EDH3').json()


def DayMarcetPriceYahooFinance(Tiker):
    
    session = requests.session()
    # -------- заголовки для URL запроса
    headers = 'Mozilla/5.0 ' \
              '(Windows NT 10.0; WOW64) ' \
              'AppleWebKit/537.36' \
              ' (KHTML, like Gecko) ' \
              'Chrome/91.0.4472.135 ' \
              'Safari/537.36'

    link = f"https://query2.finance.yahoo.com/v7/finance/quote?symbols={Tiker}"

    response = session.get(link, headers={'User-Agent': headers})
    #print(response.json()['quoteResponse']['result'][0]['regularMarketPrice'])
    return response.json()['quoteResponse']['result'][0]['regularMarketPrice']
   
eurusd = DayMarcetPriceYahooFinance('eurusd=X')
spred = int((eurusd - ed[0]['last_price'])*10000)


def edit_msg(text):
    token = "5886218730:AAHgUBVQJg4V9t_bomUnsCHi4BFgtGLISac"
    chat_id = "-1001854452864"
    message_id = 16
    url_req = "https://api.telegram.org/bot" + token + "/editMessageText" + "?chat_id=" + chat_id + "&text=" + text + "&message_id=" + str(message_id)
    results = requests.get(url_req)
  
 
edit_msg(str(spred) +str('pt') + str(' EURUSD') +'\nФ: ' + str(round(eurusd, 4)) + ';' + ' \nМ: ' + str(ed[0]['last_price']))

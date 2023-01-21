import requests
import time

apiServer = 'https://api.alor.ru'
def DayMarketAlor(apiServer, symbol):
   
    return requests.get(url=f'{apiServer}/md/v2/Securities/{symbol}/quotes')

ed = DayMarketAlor(apiServer,'MOEX:EDH3').json()

seconds_ed = ed[0]['last_price_timestamp']
time_ed = time.strftime('%H:%M:%S %d.%m.%y',time.localtime(seconds_ed))


def DayMarcetPriceYahooFinance(Tiker):
    
    session = requests.session()
   
    headers = 'Mozilla/5.0 ' \
              '(Windows NT 10.0; WOW64) ' \
              'AppleWebKit/537.36' \
              ' (KHTML, like Gecko) ' \
              'Chrome/91.0.4472.135 ' \
              'Safari/537.36'

    link = f"https://query2.finance.yahoo.com/v7/finance/quote?symbols={Tiker}"

    response = session.get(link, headers={'User-Agent': headers})
   # print(response.json()['quoteResponse'])
    return response.json()['quoteResponse']['result'][0]
    
eurusd = DayMarcetPriceYahooFinance('eurusd=X')['regularMarketPrice']
seconds_eurusd = DayMarcetPriceYahooFinance('eurusd=X')['regularMarketTime']
time_eurusd = time.strftime('%H:%M:%S %d.%m.%y',time.localtime(seconds_eurusd))



spred = int((eurusd - ed[0]['last_price'])*10000)


def edit_msg(text):
    token = "5886218730:AAHgUBVQJg4V9t_bomUnsCHi4BFgtGLISac"
    chat_id = "-1001854452864"
    message_id = 16
    url_req = "https://api.telegram.org/bot" + token + "/editMessageText" + "?chat_id=" + chat_id + "&text=" + text + "&parse_mode=Markdown"+ "&message_id=" + str(message_id)
    results = requests.get(url_req)
  
time.strftime('%H:%M:%S %d.%m.%y',time.localtime())
edit_msg(str('*') + str(spred)  + 'pt' +str('*') + '\n%F0%9F%87%B7%F0%9F%87%BA ' +str('*')+ str(ed[0]['last_price']) +str('*')+ str (' (')+ str(time_ed)+ str(')')+ '\n%F0%9F%87%AA%F0%9F%87%BA '+str('*')+str(round(eurusd, 4)) +str('*')+ str (' (')+ str(time_eurusd)+ str(')'))
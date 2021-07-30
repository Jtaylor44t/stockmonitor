import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import smtplib

api_key = ''  #go to https://www.alphavantage.co/ to get your own custom API Key and insert it in ''

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol='USAC', outputsize = 'full') #insert the stock of your choice in symbol=''
print(data)

#To get real time data continuously
a = 1
#while a==1:
#    data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
#    data.to_excel("output.xlsx")
#    time.sleep(60)

#Getting the closing data for the stock(s) and checking the change in percentage
close_data = data['4. close']
percentage_change = close_data.pct_change()
print(percentage_change)

#Pulls last value of series
last_change = percentage_change[-1]

#An alert to notify if the stock gets above a certain percentage.
if abs(last_change) > 0.0004:
    print(f"Stock Alert {str(last_change)}")

#Email sender authentication (enter your own email and password)
gmail_user = ''
gmail_password = ''

#email send properties (enter your own email addresses)
sent_from='email@gmail.com'
to = 'email@aol.com'
subject = 'Alert in USA Compression stock price change'
email_text = str(last_change)

#email send request
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except Exception as e:
    print(e)
    print ('Something went wrong...')
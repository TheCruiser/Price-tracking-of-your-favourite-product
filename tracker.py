#author is someone named Satish aka The Cruiser



#importing the request library package & BeautifulSoup from bs4 & smtplib for mail
import requests 
from bs4 import BeautifulSoup
import smtplib


#the product link we need to track
url = "https://www.amazon.in/gp/product/B07MRKVXG3?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=AMTWS7E9XBED7BSZ8JBY"

#just the info regarding my user agent
headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price():
    #requested and found
    page = requests.get(url, headers=headers)

    #everything got parsed :)
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice")
    conv_price = float(price[0:5])

    if(conv_price < 3500):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sanecybernerd@gmail.com','apppasswordgoeshere')

    subject = "Price fell down!"

    body = 'check the amazon link https://www.amazon.in/gp/product/B07MRKVXG3?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=AMTWS7E9XBED7BSZ8JBY'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sanecybernerd@gmail.com',
        'abcd@gmail.com',
        msg
    )

    print('Hey! Email Sent')

    server.quit()


check_price()
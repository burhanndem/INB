import requests
from pprint import pprint
from http import HTTPStatus
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import itertools


class Mhs():
    def __init__(self):
        self.path = "http://dnsbil.com/"  # default bir path olusturuyorum ki her seferinde girmeyeyim

    def hubele(self, site):
        basliklar = []  # basliklarin datasini tutacağım list
        col1text = []  # ilk kolonun datasini tutacağım list
        col2text = []
        col3text = []
        col4text = []
        col5text = []
        col6text = []

        resp = requests.get(f"{self.path}{site}.com")  # default pathin yanına girilen argümanı alıp yönlendiriyorum
        if resp.status_code == HTTPStatus.OK:
            soup = BeautifulSoup(resp.text, 'html.parser')
            headers = soup.find_all("h3")  # basliklarin oldugu dizin
            if headers != []:
                for i in range(0, len(headers), 1):
                    basliklar.append(headers[i].text)
            col1 = soup.find_all("ul", {"class": "listNS"})  # nameserver dns bilgilerinin datasını bulduğumuz dizin
            if col1 != []:
                for i in range(0, len(col1), 1):
                    col1text.append(col1[i].text)
            col2 = soup.find_all("ul", {"class": "listMX"})  # MX Kayıtlarının datasını bulduğumuz dizin
            if col2 != []:
                for i in range(0, len(col2), 1):
                    col2text.append(col2[i].text)
            col3 = soup.find_all("p", {"class": "text-left"})
            if col3 != []:
                for i in range(0, len(col3), 1):
                    col3text.append(col3[i].text)
            col5 = soup.find_all("ul", {"class": "list"})
            if col5 != []:
                for i in range(0, len(col5), 1):
                    col5text.append(col5[i].text)


        x = PrettyTable()

        c1 = col1text[0].split() + col1text[1].split()
        c2 = col2text[0].split()
        c3 = col3text[0].split()
        c4 = col4text
        c5 = col5text[0].split()
        c6 = col5text[1].split()

        check = True
        while check:
            check = False
            for i in range(len(c2)):
                if c2[i] == '[' or c2[i] == ']':
                    del c2[i]
                    check = True
                    break

        length = max(len(c1), len(c2), len(c3), len(c4), len(c5), len(c6))
        while len(c1) < length:
            c1.append(" ")
        while len(c2) < length:
            c2.append(" ")
        while len(c3) < length:
            c3.append(" ")
        while len(c4) < length:
            c4.append(" ")
        while len(c5) < length:
            c5.append(" ")
        while len(c6) < length:
            c6.append(" ")

        x.add_column(basliklar[0], c1)
        x.add_column(basliklar[1], c2)
        x.add_column(basliklar[2], c3)
        x.add_column(basliklar[3], c4)
        x.add_column(basliklar[4], c5)
        x.add_column(basliklar[5], c6)
        print(x.get_string(title=f"{site} Sitesinin Bilgileri"))




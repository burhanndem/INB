import requests
from pprint import pprint
from http import HTTPStatus
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import itertools


class Mhs():
    def __init__(self):
        self.path = "http://dnsbil.com/"        #default bir path olusturuyorum ki her seferinde girmeyeyim

    def hubele(self, site):
        basliklar = []  #basliklarin datasini tutacağım list
        col1text = []   #ilk kolonun datasini tutacağım list
        col2text = []
        col3text = []
        resp = requests.get(f"{self.path}{site}.com")   #default pathin yanına girilen argümanı alıp yönlendiriyorum
        if resp.status_code == HTTPStatus.OK:
            soup = BeautifulSoup(resp.text, 'html.parser')
            headers = soup.find_all("h3")           #basliklarin oldugu dizin
            if headers != []:
                for i in range(0, len(headers), 1):
                    basliklar.append(headers[i].text)
            col1 = soup.find_all("ul", {"class": "listNS"})     #nameserver dns bilgilerinin datasını bulduğumuz dizin
            if col1 != []:
                for i in range(0, len(col1), 1):
                    col1text.append(col1[i].text)
            col2 = soup.find_all("ul", {"class": "listMX"})      #MX Kayıtlarının datasını bulduğumuz dizin
            if col2 != []:
                for i in range(0, len(col2), 1):
                    col2text.append(col2[i].text)

        x = PrettyTable()
        x.field_names = basliklar           #tablonun sütunlarını basliklar listemin elemanları olarak tanımlıyorum

        x.add_column(x.field_names[0], col1text[0].split()+col1text[1].split())    #datanın içinde bolca \n var onlardan kurtulup kolonun içine atıyorum

        x.add_column(x.field_names[1], col2text[0].split())


        # for title, lst in zip(basliklar, itertools.zip_longest(col1text, fillvalue="")):      #zip_longest denemeleri başarısız
        #     x.add_column(title, lst)

        print(x.get_string(title=f"{site} Sitesinin Bilgileri"))
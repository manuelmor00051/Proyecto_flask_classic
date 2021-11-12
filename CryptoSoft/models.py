import sqlite3
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests.sessions import Session
import json
import os

class BBDDoperations():
    def __init__(self, url_BBDDates):
        self.url_BBDDates = url_BBDDates

    def urlCreate(self):
        urlActual = os.getcwd()
        try:
            os.stat("{}/data/".format(urlActual))
        except:
            url = ("{}/data/".format(urlActual))
            os.mkdir(url)

    def create_tables(self):
        con = sqlite3.connect(self.url_BBDDates)
        cur = con.cursor()
        cur.execute("CREATE TABLE if not exists Movimientos (fecha TEXT NOT NULL, hora TEXT NOT NULL, coinsfrom REAL NOT NULL, qf REAL NOT NULL, coinsto REAL NOT NULL, qt REAL NOT NULL, pu REAL NOT NULL)")
        cur.execute("CREATE TABLE if not exists saldo (ETH REAL NOT NULL, LTC REAL NOT NULL, BNB REAL NOT NULL, EOS REAL NOT NULL, XLM REAL NOT NULL, TRX REAL NOT NULL, BTC REAL NOT NULL, XRP	REAL NOT NULL, BCH	REAL NOT NULL, USDT REAL NOT NULL, BSV REAL NOT NULL, ADA REAL NOT NULL, inversión REAL NOT NULL)")
        con.close() 
        self.fix_saldo_if_empty()   
    
    def fix_saldo_if_empty(self):
        con = sqlite3.connect(self.url_BBDDates)
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM saldo")
        lentable = cur.fetchall()
        con.close()
        if lentable[0][0] == 0:
            self.insertZeros()

    def insertZeros(self):
        con = sqlite3.connect(self.url_BBDDates)
        cur = con.cursor()
        cur.execute("INSERT INTO saldo VALUES(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
        con.commit()
        con.close()

    def consultation(self, consult, params=[]):
        con = sqlite3.connect(self.url_BBDDates)
        cur = con.cursor()
        cur.execute(consult, params)

        keys = []
        for key in cur.description:
            keys.append(key[0])

        records = []
        for record in cur.fetchall():
            dicc = {}
            id_key = 0
            for key in keys:
                dicc[key] = record[id_key]
                id_key += 1
            records.append(dicc)
        con.close()
        return records

    def recordMovements(self, consult, lista):
        con = sqlite3.connect(self.url_BBDDates)
        cur = con.cursor()
        cur.execute(consult, lista)
        con.commit()
        con.close()

    def getAvaibleCoins(self):
        consult = "SELECT * FROM saldo"
        con = sqlite3.connect(self.url_BBDDates)
        cur = con.cursor()
        cur.execute(consult)
        quantities = cur.fetchall()
        quantities = quantities[0]

        keys = ["--Seleccione moneda origen--", "EUR"]
        for index in range(len(cur.description)):
            if quantities[index] > 0:
                if cur.description[index][0] == "inversión":
                    pass
                else:
                    keys.append(cur.description[index][0])

        con.close()
        return keys

class ConectApi():
    def conecta(fcoin, tcoin, api_key):
        url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1&symbol={}&convert={}'.format(fcoin, tcoin)

        headers = {
            'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url)
            data = json.loads(response.text)
            return data['data']['quote'][tcoin]['price']
        except (ConnectionError, TooManyRedirects, Timeout) as e:
            return e
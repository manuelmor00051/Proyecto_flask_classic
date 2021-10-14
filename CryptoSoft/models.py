import sqlite3
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests.sessions import Session
import json

class BBDDoperations():
    def __init__(self, url_BBDDates):
        self.url_BBDDates = url_BBDDates
    
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

class ConectApi():
    def conecta(fcoin, tcoin):
        url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1&symbol={}&convert={}'.format(fcoin, tcoin)

        headers = {
            'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': '49a64db8-368a-4fa7-84cf-662392101276'
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url)
            data = json.loads(response.text)
            return data['data']['quote'][tcoin]['price']
        except (ConnectionError, TooManyRedirects, Timeout) as e:
            return e

             #con variable.data['status']['error_code'] saco el código del error que debe ser 0 para que todo vaya bien

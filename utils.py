import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote:str, base:str, amount:str):
          
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {quote}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Неудалось обработать количество {amount}.')
        
        api_key = '03c94bf1e3e640ba561bcd265694572fff0b0559048af48694dcad3fcbf820f5'
        url = f'https://min-api.cryptocompare.com/data/price?fsym={keys[base]}&tsyms={keys[quote]}&api_key={api_key}'

        r = requests.get(url)
        total_base = json.loads(r.content)[keys[quote]]
    
        return total_base

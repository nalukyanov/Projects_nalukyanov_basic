# taken from https://www.youtube.com/watch?v=txKBWtvV99Y&ab_channel=TechWithTim   https://github.com/techwithtim/3-Mini-Python-Projects-For-Intermediates/blob/main/currency-converter.py 

from requests import get
from pprint import PrettyPrinter

BASIC_URL = "https://free.currconv.com/"
API_KEY = "2667056297dfefbbe166" # ключ придет на почту через пару дней :))))

printer = PrettyPrinter() #позволяет сделать красивое отображение в JSON-е

def get_currencies(): # выдает 
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASIC_URL + endpoint
    data = get(url).json() #так как json возвращает нам словарь, то к ключевоу слову results относится еще один словарь, его мы и вытаскиваем таким образом. Во втором словаре у нас ключ в виде валюты, и словарь с наименованием, сокращением и символом
    return data

def print_currencies(currencies):
    for name, currency in currencies: # нужно две переменные, так как мы передаем список таплов
        name = currency['currencyName']
        _id = currency['id']

        symbol = currency.get("currencySymbol", "") # применяем get(), так как символ это опциональный элемент словаря для каждой валюты
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASIC_URL + endpoint
    data = get(url).json()

    return list(data.values())[0]

def converter(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    amount = float(amount)
    converted = amount * rate

    return f"{amount} {currency1} equals {converted} {currency2}"

def main():
    currencies = get_currencies()

    print("welcome to the currency converter")
    print("you can get currencies, currency rate or convert one currency to another")
    
    while True:
        request = input("What whould you like to do?\
        1. Get currencies\
        2. Get currency rate\
        3. Convert currency\
        4. Quit\n").lower().strip()

        if request == "get currencies":
            print_currencies(currencies)
        elif request == "get currency rate":
            q1 = input("Enter a base currency ")
            q2 = input("Enter a currency to convert to ")
            print(exchange_rate(q1, q2))
        elif request == "convert currency":
            q1 = input("Enter a base currency ").capitalize()
            q2 = input("Enter a currency to convert to ").capitalize()
            am = input("Enter an amount of money ")
            print(converter(q1, q2, am))
        elif request == "quit":
            break

if __name__ == "__main__":
    main()

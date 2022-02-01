from tkinter import *
from tkinter import ttk, messagebox
import urllib.request as request
import json
import xml.etree.ElementTree as ET
from pprint import pprint

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
URL_XML = "http://www.cbr.ru/scripts/XML_daily.asp"

# JSON
try:
    data_json = json.loads(request.urlopen(URL).read())
except:
    messagebox.showerror("Error", "Ошибка получения курсов валют")

# XML
# opener = request.build_opener()
# tree = ET.parse(opener.open(URL_XML))
# __Поиск по значению__
# print(tree.findall('./Valute[@ID="R01235"]/Name')[0].text)
# __Парсинг по записям__
# root = tree.getroot()
# for elem in root:
#     print(elem.attrib)
#     for subelem in elem:
#         print(subelem.tag, subelem.text)


root = Tk()
root.title("Конвертер валют")
root.geometry("300x250+1000+300")
root.resizable(False, False)

START_AMOUNT = 1000


def exchange():
    e_usd.delete(0, END)
    e_eur.delete(0, END)
    e_cny.delete(0, END)
    try:
        e_usd.insert(0, round(float(e_rub.get()) / round(data_json['Valute']['USD']['Value'] * 1.05, 4), 2))
        e_eur.insert(0, round(float(e_rub.get()) / round(data_json['Valute']['EUR']['Value'] * 1.05, 4), 2))
        e_cny.insert(0, round(float(e_rub.get()) / round(data_json['Valute']['CNY']['Value'] * 1.05, 4), 2))
    except:
        messagebox.showwarning('Внимание', "Введите верную сумму")



header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure([0, 1, 2], weight=1)

# Шапка
h_currency = Label(header_frame, text="Валюта", bg="#ccc", font="Arial 12 bold")
h_currency.grid(row=0, column=0, sticky=EW)
h_buy = Label(header_frame, text="Покупка", bg="#ccc", font="Arial 12 bold")
h_buy.grid(row=0, column=1, sticky=EW)
h_sale = Label(header_frame, text="Продажа", bg="#ccc", font="Arial 12 bold")
h_sale.grid(row=0, column=2, sticky=EW)

# Курс доллара
usd_currency = Label(header_frame, text="USD", font="Arial 10")
usd_currency.grid(row=1, column=0, sticky=EW)
usd_buy = Label(header_frame, text=round(data_json['Valute']['USD']['Value']*1.05, 4), font="Arial 10")
usd_buy.grid(row=1, column=1, sticky=EW)
usd_sale = Label(header_frame, text=round(data_json['Valute']['USD']['Value']*0.95, 4), font="Arial 10")
usd_sale.grid(row=1, column=2, sticky=EW)

# Курс евро
eur_currency = Label(header_frame, text="EUR", font="Arial 10")
eur_currency.grid(row=2, column=0, sticky=EW)
eur_buy = Label(header_frame, text=round(data_json['Valute']['EUR']['Value']*1.05, 4), font="Arial 10")
eur_buy.grid(row=2, column=1, sticky=EW)
eur_sale = Label(header_frame, text=round(data_json['Valute']['EUR']['Value']*0.95, 4), font="Arial 10")
eur_sale.grid(row=2, column=2, sticky=EW)

# Курс юань
cny_currency = Label(header_frame, text="CNY", font="Arial 10")
cny_currency.grid(row=3, column=0, sticky=EW)
cny_buy = Label(header_frame, text=round(data_json['Valute']['CNY']['Value']*1.05, 4), font="Arial 10")
cny_buy.grid(row=3, column=1, sticky=EW)
cny_sale = Label(header_frame, text=round(data_json['Valute']['CNY']['Value']*0.95, 4), font="Arial 10")
cny_sale.grid(row=3, column=2, sticky=EW)

# Обмен
calc_frame = Frame(root, bg="#fff")
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

# RUB
l_rub = Label(calc_frame, text="Рубль", bg="#fff", font="Arial 10 bold")
l_rub.grid(row=0, column=0, padx=10)
e_rub = ttk.Entry(calc_frame, justify=CENTER, font="Arial 10")
e_rub.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)
e_rub.insert(0, START_AMOUNT)

# Кнопка обмена
btn_calc = ttk.Button(calc_frame, text="Обмен", command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

# Итог
res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

# Доллар
l_usd = Label(res_frame, text="USD:", font="Arial 10 bold")
l_usd.grid(row=0, column=0, padx=10)
e_usd = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
e_usd.grid(row=0, column=1, columnspan=2, padx=10, sticky=EW)
e_usd.insert(0, round(START_AMOUNT/round(data_json['Valute']['USD']['Value']*1.05, 4), 2))

# Евро
l_eur = Label(res_frame, text="EUR:", font="Arial 10 bold")
l_eur.grid(row=1, column=0, padx=10)
e_eur = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
e_eur.grid(row=1, column=1, columnspan=2, padx=10, sticky=EW)
e_eur.insert(0, round(START_AMOUNT/round(data_json['Valute']['EUR']['Value']*1.05, 4), 2))

# Юань
l_cny = Label(res_frame, text="CNY:", font="Arial 10 bold")
l_cny.grid(row=2, column=0, padx=10)
e_cny = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
e_cny.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)
e_cny.insert(0, round(START_AMOUNT/round(data_json['Valute']['CNY']['Value']*1.05, 4), 2))

root.mainloop()

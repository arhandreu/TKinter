import requests
import time
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

API_KEY = 'f1d5b7547d970896de2d9e102b25d0d7'
URL = "http://api.openweathermap.org/data/2.5/weather/"


def show_weather(weather):
    try:
        weather_dict = {'Город': weather['name'],
                        'Страна': weather['sys']['country'],
                        'Температура': weather['main']['temp'],
                        'Давление': weather['main']['pressure'],
                        'Влажность': weather['main']['humidity'],
                        'Ветер': weather['wind']['speed'],
                        'Описание': weather['weather'][0]['description'],
                        'Восход': time.strftime("%H:%M:%S", time.localtime(weather['sys']['sunrise'])),
                        'Закат': time.strftime("%H:%M:%S", time.localtime(weather['sys']['sunset'])),
                        }
        return ',\n'.join([f'{k}: {v}' for k, v in weather_dict.items()])
    except Exception as error:
        return messagebox.showwarning(error, "Ошибка получения данных")


def get_weather(event=''):
    if not entry.get():
        messagebox.showwarning('Внимание', 'Введите город в формате {город, код страны}.')
    else:
        params = {
            'appid': API_KEY,
            'q': entry.get(),
            'units': 'metric',
            'lang': 'ru',
        }
        weather = requests.get(URL, params=params).json()
        label["text"] = show_weather(weather)


root = ThemedTk(theme='arc')
root.geometry("500x400+1000+300")
root.resizable(0, 0)
s = ttk.Style()
s.configure("TLabel", padding=5, font="Arial 12")

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.7, relheight=1)

button = ttk.Button(top_frame, text="Запрос погоды", command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(lower_frame, anchor='nw')
label.place(relwidth=1, relheight=1)

entry.bind("<Return>", get_weather)

root.mainloop()

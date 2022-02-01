from tkinter import *
from tkinter import filedialog, messagebox, ttk
import os
from datetime import datetime


def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)


def start_sort():
    cur_path = e_path.get()
    if cur_path:
        for folder, sub_folders, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime("%Y-%m-%d")
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo('Успех', 'Файлы отсортированы')
        e_path.delete(0, END)
    else:
        messagebox.showwarning('Ошибка', 'Выберите папку')


root = Tk()
root.title('PhotoSort')
root.geometry("500x150+1000+300")

s = ttk.Style()
s.configure('my.TButton', font=("Helvetika", 15))

frame = Frame(root, bg="#56ADFF", bd=5)
frame.pack(pady=10, padx=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=1, fill=X)

btn_dialog = ttk.Button(frame, text="Выбрать папку", command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, text="Старт", style="my.TButton", command=start_sort)
btn_start.pack(fill=X, padx=10)

root.mainloop()

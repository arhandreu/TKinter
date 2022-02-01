from tkinter import *

root = Tk()
colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}

l = Label(root, bg="#fff")
l.pack(pady=10, fill=X)


class MyLabels:
    def __init__(self, master, color):
        self.color = color
        self.b = Label(master, bg=color, width=4, height=2)
        self.b.pack(side=LEFT, padx=1)
        self.b.bind("<Button-1>", lambda event, key="lk": self.get_color(event, key))
        self.b.bind("<Button-3>", lambda event, key="rk": self.get_color(event, key))

    def get_color(self, event, key):
        if key == 'lk':
            l['bg'] = self.color
        else:
            l['bg'] = '#fff'


for k in colors.keys():
    MyLabels(root, k)

root.mainloop()

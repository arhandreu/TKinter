from tkinter import *

root = Tk()

"""

"""
colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}


def get_color(hex_color, text_color):
    l['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)


l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()


class MyButtons:
    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(master, bg=self.hex_color, command=self.get_color)
        self.b.pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


for k, v in colors.items():
    MyButtons(root, v, k)

root.mainloop()


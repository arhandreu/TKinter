from tkinter import *
import time

root = Tk()


def tick():
    watch['text'] = time.strftime('%H:%M:%S')
    watch.after(200, tick)


watch = Label(root, font='Arial 70')
watch.pack()
tick()

root.mainloop()

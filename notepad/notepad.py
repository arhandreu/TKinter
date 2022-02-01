from tkinter import *
from tkinter import messagebox, filedialog

root = Tk()
root.geometry('1000x500+1000+300')

main_menu = Menu(root)
root.config(menu=main_menu)


def about_program():
    messagebox.showinfo('Информация', 'Блокнот')


def note_exit():
    if messagebox.askokcancel('Выход', 'Закрыть программу?'):
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title="Выбор файла", filetypes=(('Текстовые документы', '*.txt'),
                                                                           ('Все файлы', '*.*')))
    if file_path:
        t.delete('1.0', END)
        with open(file_path, encoding='utf-8') as file:
            t.insert('1.0', file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(title="Выбор файла", filetypes=(('Текстовые документы', '*.txt'),
                                                                             ('Все файлы', '*.*')))
    with open(file_path, 'w', encoding='utf-8') as file:
        text = t.get('1.0', END)
        file.write(text)


def change_theme(color):
    t['bg'] = theme_colors[color]['text_bg']
    t['fg'] = theme_colors[color]['text_fg']
    t['insertbackground'] = theme_colors[color]['cursor']
    t['selectbackground'] = theme_colors[color]['select_bg']


file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=note_exit)
main_menu.add_cascade(label='Файл', menu=file_menu)

theme_menu = Menu(main_menu, tearoff=0)

theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Light', command=lambda: change_theme('light'))
theme_menu_sub.add_command(label='Dark', command=lambda: change_theme('dark'))

theme_menu.add_cascade(label='Темы', menu=theme_menu_sub)
theme_menu.add_command(label='О программе', command=about_program)
main_menu.add_cascade(label='Разное', menu=theme_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

theme_colors = {
    'dark': {
        "text_bg": "#343d46", "text_fg": "#c6dec1",
        "cursor": "#eda756", "select_bg": "#4e6a65",
    },
    'light': {
        "text_bg": "#fff", "text_fg": "#000",
        "cursor": "#8000ff", "select_bg": "#777",
    }
}

t = Text(f_text, bg=theme_colors['dark']['text_bg'],
         fg=theme_colors['dark']['text_fg'], padx=10, pady=10, wrap=WORD,
         insertbackground=theme_colors['dark']['cursor'],
         selectbackground=theme_colors['dark']['select_bg'], width=30, spacing3=10,
         font=("Courier_New", 10))
t.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()

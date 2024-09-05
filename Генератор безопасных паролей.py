""" import tkinter
from tkinter import ttk

root = tkinter.Tk()

style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

colored_btn = ttk.Button(text="Test", style="C.TButton").pack()

root.mainloop() """


""" from tkinter import *
root = Tk()

lbl = Label(root, text='hello world')


def copy_to_clipboard():
    root.clipboard_clear()  # Очистить буфер обмена
    root.clipboard_append(lbl['text'])  # Добавить текст в буфер обмена


btn = Button(root, text='copy', command=copy_to_clipboard)

lbl.grid(row=0, column=0)
btn.grid(row=1, column=0)

root.mainloop() """


""" import tkinter as tk
from tkinter import ttk


class main_interface():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("20x450")
        self.create_widgets()

    def create_widgets(self):

        self.window['padx'] = 10
        self.window['pady'] = 10

        entry = ttk.Entry(self.window, width=30)
        entry.grid(row=1, column=1, sticky=tk.W, pady=3)

        frame1 = ttk.LabelFrame(self.window, text="Frame A", relief=tk.RIDGE, width=200, height=200)
        frame1.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        frame2 = ttk.LabelFrame(self.window, text="Frame B", relief=tk.RIDGE, width=200, height=200)
        frame2.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        entry = ttk.Entry(frame2, width=30)
        entry.grid(row=1, column=1, sticky=tk.W, pady=3)

        request = {"NSK": "9383XXXX",
                   "OMS": "9381XXXX",
                   "TMN": "9345XXXX",
                   "KZN": "9843XXXX",
                   "NNV": "9831XXXX"}

        for row, (key, value) in enumerate(request.items()):
            formated_text = " {} - {}".format(key, value)
            found_result_label = ttk.Label(frame1, text=formated_text)

            selected_string = key, value
            found_result_label.bind("<Button-1>", func=lambda event, text=selected_string: user_choice(text))
            found_result_label.grid(row=row, column=1, sticky=tk.W)

            self.button = None

    def user_choice(text):

        entry.delete(0, "end")
        entry.insert(0, text)

        if self.button:  # Если кнопка уже существует -
            self.button.destroy()  # уничтожить!!!
            self.button = None

        if text[0] == "OMS":
            self.button = ttk.Button(frame2, text="Do Smt", command=lambda: fx())
            self.button.grid(row=2, column=1, sticky=tk.W)

        def fx():
            pass

program = main_interface()
program.window.mainloop() """



from tkinter import *
root = Tk()
root.geometry('600x400')

""" def on_press():
    b.grid_remove() """

b = Button(root, text = '+', background='pink')
b.pack()
#command=on_press
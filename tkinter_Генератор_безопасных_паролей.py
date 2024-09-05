from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from tkinter.ttk import Combobox
root = Tk()
root.title('Генератор безопасных паролей.')
root.geometry('600x470')
root.resizable(False, False)
root.iconbitmap(r"D:\IT\Python\Мини-проекты\2. Генератор безопасных паролей\iconka.ico")
#Colors 
color_1 = ['#062E65', '#6C99C2', '#D1AC7D', '#C1C5C6']  
color_2 = ['#536E01', '#E9B101', '#8A9994', '#FCE3AE'] 
color_3 = ['#192A02', '#758D45', '#4F5F36', '#AFBF9C']
color_4 = ['#6B5C54', '#FDBB06', '#E48D02', '#AFA5A4']
color_5 = ['#53387E', '#CDEB87', '#D8A4B4', '#9682A9']
color_6 = ['#3B372F', '#E99F98', '#7B7B70', '#DDCACE']
color_7 = ['#97020D', '#ECCECE', '#F24E40', '#B6CAB9']
color_8 = ['#620005', '#E04591', '#CA1A59', '#ECD0EB']
color_9 = ['#074A4F', '#EDE2CF', '#D8C5BC', '#78A0A6']
color_10 = ['#563E20', '#EBDF00', '#7E7B15', '#B38540']
color_11 = ['#FA4032', '#FEF3E2', '#FA812F', '#FAAF08']
color_12 = ['#662E1C', '#EBDCB2', '#AF4425', '#C9A66B']
color_13 = ['#896E69', '#F9F9FF', '#D55448', '#FFA577']

colors = [color_1, color_2, color_3, color_4, color_5, color_6, color_7, color_8, color_9, color_10, color_11, color_12, color_13]

#Автоматическое изменение цвета, который по умолчанию
frame_bottom = Frame(root) 
frame_right = Frame(frame_bottom) 
var_colors = StringVar()
combobox_colors = Combobox(frame_right, textvariable = var_colors, justify = CENTER, state = 'readonly', width =50)
combobox_colors['values'] = ('Дом у воды', 'Коктель на пляже', 'Лесной дождь', 'Звезды в лужах', 'Лавандовое поле', 'Цветы у двери', 'Маки в вазе', 'Малиновый джем', 'Волны на берегу', 'Природная элегантность', 'Солнечный цитрус', 'Пряность', 'Тыквенная дыня')
var_colors.set('Пряность')
help_colors_number = combobox_colors['values'].index(var_colors.get())
default_color = colors[help_colors_number]
#Начальные наборы цвета
set_bg4_frames = {'bg' : default_color[3]}
set_bg3_fgblack_metki = {'background' : default_color[2], 'foreground': 'black'}
set_btn_generation = {'background' : default_color[2], 'foreground' : 'black', 'activebackground' : default_color[1], 'activeforeground' : default_color[0]}
set_bg2_fg1_special_metki = {'bg' : default_color[1], 'fg' : default_color[0]}
set_spin_button = {'buttonbackground' : default_color[2]}
set_dark_buttom ={ 'bg' : default_color[0], 'fg' : 'white', 'activebackground' :  default_color[1], 'activeforeground' : default_color[0] }

frame_bottom.config(**set_bg4_frames)
frame_right.config(**set_bg4_frames)

better_number = Label(root, text = '0')
root.config(**set_bg4_frames)
def choose_color():
    number = combobox_colors['values'].index(combobox_colors.get())
    name_new_color = combobox_colors['values'][number]
    better_number['text'] = number

    dark = colors[number][0]
    almost_dark_colors = colors[number][1]
    light_dark_colors = colors[number][2]
    color_for_frame = colors[number][3]
    #dark_colors
    set_dark_colors = {'background' : dark, 'foreground' : 'white', 'activebackground' : almost_dark_colors, 'activeforeground' : dark}
    message1.config(**set_dark_colors)
    message2.config(**set_dark_colors)
    message3.config(**set_dark_colors)
    message4.config(**set_dark_colors)
    message5.config(**set_dark_colors)
    btn_select.config(**set_dark_colors)
    btn_colors.config(**set_dark_colors)
    #almost_dark_colors
    set_almost_dark_colors = {'bg' : almost_dark_colors, 'fg' : dark}
    lbl_lenth.config(**set_almost_dark_colors)
    lbl_count.config(**set_almost_dark_colors)
    lbl_body.config(**set_almost_dark_colors)
    #light_dark_colors
    spin_lenth.config(buttonbackground = light_dark_colors)
    lbl_name.config(background = light_dark_colors)
    btn_generation.config(background = light_dark_colors, activebackground = almost_dark_colors, activeforeground = dark)    
    set_light_dark_colors ={'background' : light_dark_colors}
    lbl_check1.config(**set_light_dark_colors)
    lbl_check2.config(**set_light_dark_colors)
    lbl_check3.config(**set_light_dark_colors)
    lbl_check4.config(**set_light_dark_colors)
    lbl_check5.config(**set_light_dark_colors)
    #color_for_frame
    set_color_for_frame = {'background' : color_for_frame}
    frame_general.config(**set_color_for_frame)
    frame_main_passwords.config(**set_color_for_frame)
    frame_bottom.config(**set_color_for_frame)
    frame_left.config(**set_color_for_frame)
    frame_generation.config(**set_color_for_frame)
    frame_right.config(**set_color_for_frame)
    frame_lenth_count.config(**set_color_for_frame)
    frame_lenth.config(**set_color_for_frame)
    frame_count.config(**set_color_for_frame)
    frame_body.config(**set_color_for_frame)
    frame_melochy.config(**set_color_for_frame)
    frame_message.config(**set_color_for_frame)
    frame_checks.config(**set_color_for_frame)
    frame_labels.config(**set_color_for_frame)
    root['bg'] = color_for_frame

    showinfo('Цвет!', f'Цветовая палитра "{name_new_color}" успешно установлена!')

def generate_password(length, spis_chars):
    import random
    password = ''
    while len(password) < length:
        random.shuffle(spis_chars)
        for i in range (len(spis_chars)):
            password += random.choice(spis_chars[i]) 
            if len(password) == length:
                break
    password = ''.join(random.sample(password, length))
    return password

def play():
    color_in_use = colors[combobox_colors['values'].index(combobox_colors.get())]#colors[int(better_number['text'])]
    dark = color_in_use[0]
    almost_dark_colors = color_in_use[1]
    color_for_frame = color_in_use[3]
    set_dark_colors = {'background' : dark, 'foreground' : 'white', 'activebackground' : almost_dark_colors, 'activeforeground' : dark}
    set_passw_label = {'bg' : almost_dark_colors, 'fg' : dark}
    #Получение информации и создание переменных
    length = int(spin_lenth.get())
    count = int(combobox_count.get())
    spis = list()
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    bad = ['i', 'l', '1', 'L', 'I', 'o', '0', 'O']
    if var1.get() == 'no' and var2.get() == 'no' and var3.get() == 'no' and var4.get() == 'no':
        showerror('Ошибка!', "Пароль не может быть пустым!")
    else:
        if var1.get() == 'yes':
            spis.append(digits)
        if var2.get() == 'yes':
            spis.append(lowercase_letters)
        if var3.get() == 'yes':
            spis.append(uppercase_letters)
        if var4.get() == 'yes':
            spis.append(punctuation)
        if var5.get() == 'yes':
            spis_chars = list()
            for j in range (len(spis)):
                stroka = []
                for k in range (len(spis[j])):
                    stroka += spis[j][k]
                for c in bad:
                    if c in stroka:
                        stroka.remove(c)
                new_stroka = ''.join(stroka)
                spis_chars.append(new_stroka)
        else:
            spis_chars = spis
    # Генерация паролей
    def copy1():
        root.clipboard_clear()  # Очистить буфер обмена
        root.clipboard_append(password1)
        showinfo('', 'Пароль успешно скопирован!')
    def copy2():
        root.clipboard_clear() 
        root.clipboard_append(password2)
        showinfo('', 'Пароль успешно скопирован!')
    def copy3():
        root.clipboard_clear()  
        root.clipboard_append(password3)
        showinfo('', 'Пароль успешно скопирован!')
    if count >= 1:
        frame_password_1 = Frame(frame_main_passwords, height = 90, bg = color_for_frame) #Создали ячейку для пароля и кнопки копировать
        label_password_1 = Label(frame_password_1, **set_passw_label, font="Cambria 17 normal roman", pady = 7) #Создали саму метку для пароля
        password1 = generate_password(length, spis_chars)
        label_password_1['text'] = password1 #Внесли пароль в метку
        button_password_1 = Button(frame_password_1, text = 'Копировать', **set_dark_colors, command = copy1) #Создали кнопку копирования
        # размещение 
        label_password_1.pack(pady = 6)
        button_password_1.pack()
        if count == 1:
            side_for_passw_1 = TOP
            padx_for_passw_1 = 0
        else:
            side_for_passw_1 = LEFT
            padx_for_passw_1 = 30
        frame_password_1.pack(side = side_for_passw_1, padx = padx_for_passw_1)
        if count >= 2:
            frame_password_2 = Frame(frame_main_passwords, height = 90, bg = color_for_frame)
            label_password_2 = Label(frame_password_2, **set_passw_label, font="Cambria 17 normal roman", pady = 7)     
            password2 = generate_password(length, spis_chars)
            label_password_2['text'] = password2
            button_password_2 = Button(frame_password_2, text = 'Копировать', **set_dark_colors, command = copy2)
            # размещение 
            label_password_2.pack(pady = 6)
            button_password_2.pack()
            frame_password_2.pack(side = LEFT, padx = 30)
            if count == 3:
                frame_password_3 = Frame(frame_main_passwords, height = 90, bg = color_for_frame)
                label_password_3 = Label(frame_password_3, **set_passw_label, font="Cambria 17 normal roman", pady = 7)
                password3 = generate_password(length, spis_chars)
                label_password_3['text'] = password3
                button_password_3 = Button(frame_password_3, text = 'Копировать', **set_dark_colors, command = copy3)
                # размещение 
                label_password_3.pack(pady = 6)
                button_password_3.pack()
                frame_password_3.pack(side = LEFT, padx = 30)
    def restart(count):
        frame_password_1.pack_forget() 
        label_password_1.pack_forget()     
        button_password_1.pack_forget() 
        if count >= 2:
            frame_password_2.pack_forget() 
            label_password_2.pack_forget()     
            button_password_2.pack_forget() 
            if count == 3:
                frame_password_3.pack_forget() 
                label_password_3.pack_forget()     
                button_password_3.pack_forget() 
        btn_generation['text'] = 'ГЕНЕРИРОВАТЬ'
        btn_generation.configure(command = play)
        # активация кнопки выбор цвета
        btn_colors.config(text = 'Изменить', command = choose_color)
    def help_color():
        showinfo('Цвет!', 'Изменить цветовую палитру можно только после нажатия кнопки "ЗАНОВО"!')

    #Удаление кнопки СГЕНЕРИРОВАТЬ и добавление кнопки ЗАНОВО
    btn_generation['text'] = 'ЗАНОВО'
    btn_generation.configure(command =lambda : restart(count))
    #Дезактивация кнопки выбор цвета
    btn_colors.config(text = '???', command = help_color) 
lbl_name = ttk.Label(root, text = 'ГЕНЕРАТОР БЕЗОПАСНЫХ ПАРОЛЕЙ.', **set_bg3_fgblack_metki, font="Cambria 11 normal roman") 
lbl_name.pack(side = TOP, pady = 10)
frame_general = Frame(root, **set_bg4_frames)
frame_general.pack()
frame_main_passwords = Frame(root, height = 90, **set_bg4_frames)
frame_main_passwords.pack(pady = 25)
# for COLORS
frame_left = Frame(frame_bottom, **set_bg4_frames, width = 90)
frame_left.pack(side = LEFT)
frame_generation = Frame(frame_bottom, pady = 10, **set_bg4_frames)
frame_generation.pack(side = LEFT)
frame_right.pack(side = LEFT, padx = 60)
#В Нижнем правом углу цвета
btn_colors = Button(frame_right, text = 'Изменить', command = choose_color, **set_dark_buttom)
btn_colors.pack(side = RIGHT)
combobox_colors.pack(side = LEFT, padx = 10)
btn_generation = Button(frame_generation, text = 'СГЕНЕРИРОВАТЬ', **set_btn_generation, font="Cambria 12 normal roman", pady = 5, command = play)
btn_generation.pack()
#Объединение lenth and count
frame_lenth_count = Frame(frame_general, height=30, **set_bg4_frames)
frame_lenth_count.pack(side = LEFT)
#Длина пароля
frame_lenth = Frame(frame_lenth_count, padx=100, **set_bg4_frames)
lbl_lenth = Label(frame_lenth, text = 'Длина пароля:', **set_bg2_fg1_special_metki, pady = 7)
var_spin = IntVar(value = 8) #значение по умолчанию
spin_lenth = Spinbox(frame_lenth, from_= 4, to=20, textvariable=var_spin, wrap = TRUE, justify=CENTER, state = 'readonly', width = 7, **set_spin_button)
lbl_lenth.pack(pady = 10)
spin_lenth.pack()
frame_lenth.pack()
#Количество паролей
frame_count = Frame(frame_lenth_count, pady = 45, **set_bg4_frames)
lbl_count = Label(frame_count, text = 'Количество паролей:', **set_bg2_fg1_special_metki, pady = 7)
var_count = IntVar(value = 1)
combobox_count = Combobox(frame_count, textvariable = var_count, justify = CENTER, width = 7, state = 'readonly')
combobox_count['values'] = (1, 2, 3)
lbl_count.pack(pady = 10)
combobox_count.pack()
frame_count.pack()
#Состав пароля
def show1():
    showinfo('Цифры.', '0123456789')
def show2():
    showinfo('Строчные буквы.', 'abcdefghijklmnopqrstuvwxyz')
def show3():
    showinfo('Прописные буквы.', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
def show4():
    showinfo('Пунктуационные символы.', '! # $ % & * + - = ? @ ^ _')
def show5():
    showinfo('Неоднозначные символы.', 'i  l  1  L  I  o  0  O')
def select_all():
    listik = [var1, var2, var3, var4, var5]
    count = 0
    for c in listik:
        if c.get() == 'yes':
            count+=1
    if count == 5:
        for c in listik:
            c.set('no')
    else:
        for c in listik:
            c.set('yes')
position = {"pady":3, "anchor":NW}
frame_body = Frame(frame_general, pady= 25, **set_bg4_frames)
frame_melochy = Frame(frame_body, **set_bg4_frames)
lbl_body = Label(frame_body, text = 'Состав пароля:', **set_bg2_fg1_special_metki, pady = 7)
frame_checks = Frame(frame_melochy, **set_bg4_frames)
frame_labels = Frame(frame_melochy, **set_bg4_frames)

var1 = StringVar(value = 'yes')
check1 = ttk.Checkbutton(frame_checks, variable = var1, onvalue='yes', offvalue='no')
lbl_check1 = ttk.Label(frame_labels, text = 'Цифры', **set_bg3_fgblack_metki)
lbl_check1.pack(**position)

var2 = StringVar(value = 'yes')
check2 = ttk.Checkbutton(frame_checks,  variable = var2, onvalue='yes', offvalue='no')
lbl_check2 = ttk.Label(frame_labels, text = 'Строчные буквы', **set_bg3_fgblack_metki)
lbl_check2.pack(**position)

var3 = StringVar(value = 'no')
check3 = ttk.Checkbutton(frame_checks, variable = var3, onvalue='yes', offvalue='no')
lbl_check3 = ttk.Label(frame_labels, text = 'Прописные буквы', **set_bg3_fgblack_metki)
lbl_check3.pack(**position)

var4 = StringVar(value = 'no')
check4 = ttk.Checkbutton(frame_checks,  variable = var4, onvalue='yes', offvalue='no')
lbl_check4 = ttk.Label(frame_labels,text = 'Пунктуационные символы', **set_bg3_fgblack_metki)
lbl_check4.pack(**position)

var5 = StringVar(value = 'no')
check5 = ttk.Checkbutton(frame_checks, variable = var5, onvalue='yes', offvalue='no')
lbl_check5 = ttk.Label(frame_labels, text = 'Исключить неоднозначные символы', **set_bg3_fgblack_metki)
lbl_check5.pack(**position)

spis_of_checks = [check1, check2, check3, check4, check5]
frame_message = Frame(frame_melochy, **set_bg4_frames)
frame_checks.pack(side = LEFT)
frame_labels.pack(side = LEFT)
frame_message.pack(side = RIGHT)

message1 = Button(frame_message, text = '?', command = show1, width=2, **set_dark_buttom)
message1.pack()

message2 = Button(frame_message, text = '?', command = show2, width=2, **set_dark_buttom)
message2.pack()

message3 = Button(frame_message, text = '?', command = show3, width=2, **set_dark_buttom)
message3.pack()

message4 = Button(frame_message, text = '?', command = show4, width=2, **set_dark_buttom)
message4.pack()

message5 = Button(frame_message, text = '?', command = show5, width=2, **set_dark_buttom)
message5.pack()

position = {"pady":2, "anchor":NW}
check1.pack(**position)
check2.pack(**position)
check3.pack(**position)
check4.pack(**position)
check5.pack(**position)

btn_select = Button(frame_body, text = 'Выбрать всё', command = select_all, **set_dark_buttom)

lbl_body.pack(side = TOP)
frame_melochy.pack(side = TOP)
btn_select.pack(side = TOP)
frame_body.pack(side = RIGHT) 
frame_bottom.pack(side = BOTTOM)
root.mainloop()


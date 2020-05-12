import datetime
import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title('FilesSortApp')
root.iconbitmap('/run/media/stevejops/My Disk/Python/PycharmProjects/PhotoSortApp/folder cute.ico')  # подобрать
# подходящую иконку
root.geometry('800x600+300+25')
root.resizable(0, 0)

# Menu
main_menu = Menu(root)
root.config(menu=main_menu)


def file_startfold():
    file_path = filedialog.askdirectory(title='Выберите папку: ')
    entry1.delete(0, END)
    entry1.insert(0, file_path)

    def get_start(folder):
        if folder:
            for root1, dirs, files in os.walk(folder):
                for filename in files:
                    all_files = os.path.join(root1, filename)  # получаем путь
                    get_date = datetime.datetime.fromtimestamp(
                        os.stat(all_files).st_mtime)  # отсекаем файлы по дате мод.
                    date_format = datetime.datetime.strftime(get_date, '%Y-%m-%d')  # преобразовыем  в формат ГГГГ-ММ-ДД
                    folderwithdatename = os.path.join(folder, date_format)  # подготовка к созданию папки с именем даты
                    if not os.path.exists(folderwithdatename):
                        os.mkdir(folderwithdatename)  # создание папки
                    os.rename(all_files, os.path.join(folderwithdatename, filename))  # перемещение файлов в папку
            messagebox.showinfo('Successful operation', 'Files successfully sorted')
            entry1.delete(0, END)

    get_start(entry1.get())


def file_startarchive():
    file_path = filedialog.askdirectory(title='Выберите папку: ')
    entry1.delete(0, END)
    entry1.insert(0, file_path)

    def getstart(folder):
        if folder:
            for root1, dirs, files in os.walk(folder):
                for filename in files:
                    all_files = os.path.join(root1, filename)  # получаем путь
                    get_date = datetime.datetime.fromtimestamp(
                        os.stat(all_files).st_mtime)  # отсекаем файлы по дате мод.
                    date_format = datetime.datetime.strftime(get_date, '%Y-%m-%d')  # преобразовыем  в формат ГГГГ-ММ-ДД
                    folderwithdatename = os.path.join(folder, date_format)  # подготовка к созданию папки с именем даты
                    if not os.path.exists(folderwithdatename):
                        os.mkdir(folderwithdatename)  # создание папки
                    os.rename(all_files, os.path.join(folderwithdatename, filename))  # перемещение файлов в папку
                    shutil.make_archive(folderwithdatename, "zip", folderwithdatename)
                    shutil.rmtree(folderwithdatename)

            messagebox.showinfo('Successful operation', 'Files successfully sorted')
            entry1.delete(0, END)

    getstart(entry1.get())


def quit_program():
    answer = messagebox.askokcancel('Quit', 'Do you really want to exit?')
    if answer:
        root.destroy()


def instruct_open():
    messagebox.showinfo('Инструкция', 'Данная программа сортирует файлы любого расширения, по дате последней '
                                      'модификации файла.'
                                      '\n '
                                      '\nДанная программа сортирует только!!! файлы(если в указанном расположении'
                                      ' кроме файлов'
                                      '\nесть папки, архивы, и прочее, - программа их не отсортирует, '
                                      '\nпри этом файлы находящиеся там же, - отсортирует.'
                                      '\n '
                                      '\nПрограмма находится в стадии разработки, просьба отправлять'
                                      '\nсвои отзывы и идеи по телефону разработчика=)))')


def about_program():
    messagebox.showinfo('About program', 'The FileSortApp program ver: 1.0'
                                         '\n '
                                         '\nDesigned by KSV Development in 2020th'
                                         '\n '
                                         '\nThis product is free pay'
                                         '\n '
                                         '\nAll Icons was taken from google.com')


# File Menu
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Начать сортировку', command=file_startfold)
file_menu.add_command(label='Сортировка с архивированием', command=file_startarchive)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit_program)
main_menu.add_cascade(label='Файл', menu=file_menu)

# Instruction Menu
instruct_menu = Menu(main_menu, tearoff=0)
instruct_menu.add_command(label='Прочесть Инструкцию', command=instruct_open)
main_menu.add_cascade(label='Инструкция', menu=instruct_menu)

# About Menu
help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label='About program', command=about_program)
main_menu.add_cascade(label='Help', menu=help_menu)


def get_path():
    file_path = filedialog.askdirectory(title='Выберите папку: ')
    entry1.delete(0, END)
    entry1.insert(0, file_path)


def btn2_func():
    folder = entry1.get()
    if folder:
        for root1, dirs, files in os.walk(folder):
            for filename in files:
                all_files = os.path.join(root1, filename)  # получаем путь
                get_date = datetime.datetime.fromtimestamp(os.stat(all_files).st_mtime)  # отсекаем файлы по дате мод.
                date_format = datetime.datetime.strftime(get_date, '%Y-%m-%d')  # преобразовыем  в формат ГГГГ-ММ-ДД
                folderwithdatename = os.path.join(folder, date_format)  # подготовка к созданию папки с именем даты
                if not os.path.exists(folderwithdatename):
                    os.mkdir(folderwithdatename)  # создание папки
                os.rename(all_files, os.path.join(folderwithdatename, filename))  # перемещение файлов в папку
        messagebox.showinfo('Successful operation', 'Files successfully sorted')
        entry1.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Выберите папку')


def btn3_func():
    folder = entry1.get()
    if folder:
        for root1, dirs, files in os.walk(folder):
            for filename in files:
                all_files = os.path.join(root1, filename)  # получаем путь
                get_date = datetime.datetime.fromtimestamp(os.stat(all_files).st_mtime)  # отсекаем файлы по дате мод.
                date_format = datetime.datetime.strftime(get_date, '%Y-%m-%d')  # преобразовыем  в формат ГГГГ-ММ-ДД
                folderwithdatename = os.path.join(folder, date_format)  # подготовка к созданию папки с именем даты
                if not os.path.exists(folderwithdatename):
                    os.mkdir(folderwithdatename)  # создание папки
                os.rename(all_files, os.path.join(folderwithdatename, filename))  # перемещение файлов в папку
                shutil.make_archive(folderwithdatename, "zip", folderwithdatename)
                shutil.rmtree(folderwithdatename)

        messagebox.showinfo('Successful operation', 'Files successfully sorted')
        entry1.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Выберите папку')


# start window

label_text = '1. Перед началом работы прочесть инструкцию.\n' \
             '2. Для начала работы приложения\nвыберите Вашу папку с файламы ' \
             'которые нужно отсортировать\nнажав кнопку "Выберите папку" .'
labelframe1 = LabelFrame(root, padx=10, pady=10, bg='light blue')
labelframe1.place(relx=0.5, rely=0.1, anchor='n')

label1 = Label(labelframe1, text=label_text, bg='light gray', fg='black', padx=100, pady=50, font='Arial 16', )
label1.pack()

entry1 = Entry(root, fg='black', width=45, font='Arial 14', )
entry1.place(relx=0.5, rely=0.6, anchor='s')

label_entry = Label(root, text='Путь к папке :', font='Arial 14')
label_entry.place(relx=0.1, rely=0.6, anchor='s')

btn1 = Button(root, text='Выберите папку', font=('Arial', '12'), command=get_path)
btn1.place(relx=0.9, rely=0.6, anchor='s')

btn2 = Button(root, text='Начать\nсортировку ', font=('Arial', '14'), bg='light green', height=5, width=15,
              activebackground='white', command=btn2_func)
btn2.place(relx=0.3, rely=0.95, anchor='s')

btn3 = Button(root, text='Начать \nсортировку \nи архивировать ', font=('Arial', '14'), bg='violet', height=5, width=15,
              activebackground='white', command=btn3_func)
btn3.place(relx=0.7, rely=0.95, anchor='s')

root.mainloop()

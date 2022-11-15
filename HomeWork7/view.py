import model
from tkinter import *
from tkinter import ttk

def CreateMenu():
    global root
    global frm
    root = Tk()
    frm = ttk.Frame(root, padding=200)
    frm.grid()
    ttk.Label(frm, text="Телефонный справочник").grid(column=0, row=0)
    ttk.Button(frm, text="Показать контакты", command=Print_Result).grid(column=0, row=1)
    ttk.Button(frm, text="Добавить контакт", command=model.Add_Contacts).grid(column=0, row=2)
    ttk.Button(frm, text="Найти контакт", command=Print_Search_Name).grid(column=0, row=3)    
    ttk.Button(frm, text="Выход", command=root.destroy).grid(column=1000, row=1000)
    root.mainloop()

def Print_Result():
    global root
    global frm
    ttk.Label(frm, text=f"{str(model.Open_Contacts())}").grid(column=0, row=10)

def Print_Search_Name():
    global root
    global frm
    ttk.Label(frm, text=f"{str(model.Search_Contacts())}").grid(column=0, row=30)


import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def criar_banco():
    return  sqlite3.connect('nome.db')


def inserir_bd():
    c  = criar_banco()
    cursor =  c.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro(

                    nome TEXT NOT NULL,
                    idade INTERGER NOT NULL
                        

                    )""")
    c.commit()
    try:
        nome_  =  nome.get()
        idade_ = idade.get()
        cursor.execute("INSERT INTO cadastro VALUES(?, ?)", (nome_, idade_))
        c.commit() 
        messagebox.showinfo('', 'dados inseridos')

        cursor.execute('SELECT * FROM  cadastro')
        dados_  =  cursor.fetchall()
        dados.config(text = dados_)
    except:
        messagebox.showerror('', 'ocorreu um erro')    
    




    # y = [
    # ['a', 25],
    # ['b', 30]

    # ]

    # cursor.executemany("INSERT INTO cadastro VALUES(?, ?)", y)
    # c.commit() 


 

    # for d in dados:
    #     print('nome: ', d[0], 'idade', d[1])



root  =  tk.Tk()

root.geometry('300x300')

tk.Label(root, text= 'nome').pack()

nome  =  tk.Entry(root)
nome.pack()


tk.Label(root, text= 'idade').pack()
idade  =  tk.Entry(root)
idade.pack()


btn = tk.Button(root, text='inserir', command= inserir_bd )
btn.pack(pady= 10)


dados = tk.Label(root, text='')
dados.pack(pady=10)



root.mainloop()
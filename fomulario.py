import tkinter as tk


def enviar():
    print("Cadastro de Cliente")
    print("Nome:", nome.get())
    print("Idade:", idade.get())
    print("E-mail:", email.get())


janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("1700x750")


tk.Label(janela, text="Nome:").pack(pady=5)
nome = tk.Entry(janela, width=40)
nome.pack()


tk.Label(janela, text = "Idade:").pack(pady=5)
idade = tk.Entry(janela, width=40)
idade.pack()


tk.Label(janela, text="E-mail:").pack(pady=5)
email = tk.Entry(janela, width=40)
email.pack()


tk.Button(janela, text="Enviar", command=enviar).pack(pady=20)


janela.mainloop()
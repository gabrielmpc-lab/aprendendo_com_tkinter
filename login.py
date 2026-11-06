#Abrir uma janela e definir suas dimensões
import tkinter as tk 

janela = tk.Tk()

janela.title ("Aprendendo com Tkinter")
janela.geometry ("700x400")
janela.config(bg="white")


#Adicionar uma imagem e posicioná-la
imagem = tk.PhotoImage(file="logot.png")
print(imagem.width(), imagem.height())

foto = tk.Label(janela, image=imagem)
foto.pack(pady=(45, 45))
foto.config(bg="white")

#Opção de escrever o e-mail (não interativa)
email = tk.Entry(
    janela,
    width=30,
    disabledbackground="white",
    disabledforeground="black",
    highlightbackground="gray",
    highlightthickness=1
)
email.insert(0, "E-mail")
email.config(state="disabled")
email.pack(pady=2, ipady=10)

#Opção de escrever a senha (não interativa)
senha = tk.Entry(
    janela,
    width=30,
    disabledbackground="white",
    disabledforeground="black",
    highlightbackground="gray",
    highlightthickness=1
)
senha.insert(0, "Senha")
senha.config(state="disabled")
senha.pack(pady=2, ipady=10)

#Opção de acessar (não interativa)
acessar = tk.Entry(
    janela,
    width=35,
    justify="center",
    relief="flat",
    bd=0,
    highlightthickness=0,
    disabledbackground="blue",
    disabledforeground="white"
)
acessar.insert(0, "Acessar")
acessar.config(state="disabled")
acessar.pack(pady=8, ipady=10)

primeiro_acesso = tk.Entry(
    janela,
    width=20,
    justify="center",
    relief="flat",
    bd=0,
    highlightthickness=0,
    disabledbackground="white",
    disabledforeground="blue"
)
primeiro_acesso.insert(0, "Primeiro acesso")
primeiro_acesso.config(state="disabled")
primeiro_acesso.pack(pady=2, ipady=10)

janela.mainloop()
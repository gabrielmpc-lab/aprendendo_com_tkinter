import tkinter as tk 

janela = tk.Tk()

janela.title ("Aprendendo com Tkinter")
janela.geometry ("1100x900")
janela.config(bg="white")


imagem = tk.PhotoImage(file="perfil.png")
imagem = imagem.subsample(2, 2)
print(imagem.width(), imagem.height())

foto = tk.Label(janela, image=imagem)
foto.grid(
    row=0,
    column=0, 
    padx=20,
    ipady=15
)
foto.config(bg="white")

bem_vindo = tk.Entry(
    janela,
    width=25,
    justify="center",
    disabledbackground="#e8f1fd",
    disabledforeground="#2c7fed",
    relief="flat",
    bd=0,
    highlightthickness=0,
)
bem_vindo.insert(0, "BEM VINDO LEONID")
bem_vindo.config(state="disabled")
bem_vindo.grid(
    row=0, 
    column=1, 
    padx=20,
    sticky="",
    ipady=20
)

sinoo = tk.PhotoImage(file="sino.png")
sinoo = sinoo.subsample(9, 9)
print(sinoo.width(), sinoo.height())

sino = tk.Label(janela, image=sinoo)
sino.grid(
    row=0, 
    column=2,
    padx=20
)
sino.config(bg="white")

logot = tk.PhotoImage(file="logot.png")
logot = logot.subsample(2, 2)
print(logot.width(), logot.height())

logo = tk.Label(janela, image=logot)
logo.grid(
    row=0,
    column=3, 
    padx=490,
    ipady=15
)
logo.config(bg="white")

janela.mainloop()
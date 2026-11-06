import tkinter as tk 

janela = tk.Tk()

janela.title ("Aprendendo com Tkinter")
janela.geometry ("900x600")


imagem = tk.PhotoImage(file="logot.png")
print(imagem.width(), imagem.height())

foto = tk.Label(janela, image=imagem)
foto.pack(pady=100)

janela.mainloop()
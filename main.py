from tkinter import *
from utils import seleciona_imagens


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.msg = Label(self.primeiroContainer, text="Insira a quantidade de imagens a selecionar:")
        self.msg["font"] = ("Arial", "10", "italic", "bold")
        self.msg.pack()

        self.quant_imagens = Entry(self.primeiroContainer)
        self.quant_imagens["width"] = 8
        self.quant_imagens.pack()

        self.selecionar = Button(self.primeiroContainer)
        self.selecionar["text"] = "Selecionar imagens"
        self.selecionar["font"] = self.fontePadrao
        self.selecionar['bg'] = "green"
        self.selecionar["command"] = self.selecionar_files
        self.selecionar.pack()

        self.texto_info = Label(self.segundoContainer)
        self.texto_info["font"] = self.fontePadrao
        self.texto_info['fg'] = "red"
        self.texto_info.pack()

        self.sair = Button(self.terceiroContainer, width=3)
        self.sair["text"] = "Sair"
        self.sair["font"] = self.fontePadrao
        self.sair['bg'] = "green"
        self.sair["width"] = 5
        self.sair["command"] = self.terceiroContainer.quit
        self.sair.pack()

    def selecionar_files(self):
        seleciona_imagens(self.quant_imagens.get())
        self.texto_info['text'] = "Imagens inseridas no arquivo, com sucesso!" \
                                  "\nVerifique na pasta documentos_gerados."


root = Tk()
root.title("AppImages")
Application(root)
root.mainloop()

import tkinter as tk
from tkinter import ttk
import utils


class DataEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inserir Dados da OAE")

        # Criar variáveis de controle para os campos de entrada
        self.km_var = tk.StringVar()
        self.linha_var = tk.StringVar()
        self.cidade_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.natureza_var = tk.StringVar()
        self.bitola_var = tk.StringVar()
        self.tracado_var = tk.StringVar()
        self.trilhos_var = tk.StringVar()
        self.fixacao_var = tk.StringVar()
        self.comprimento_var = tk.StringVar()
        self.largura_var = tk.StringVar()
        self.altura_var = tk.StringVar()

        # Adicionar campos de entrada (Entry) e rótulos (Label) para cada variável
        self.create_input_field("Km:", self.km_var)
        self.create_input_field("Linha:", self.linha_var)
        self.create_input_field("Cidade:", self.cidade_var)
        self.create_input_field("Estado:", self.estado_var)
        self.create_input_field("Natureza da Transposição:", self.natureza_var)
        self.create_input_field("Bitola:", self.bitola_var)
        self.create_input_field("Traçado:", self.tracado_var)
        self.create_input_field("Trilhos:", self.trilhos_var)
        self.create_input_field("Fixação:", self.fixacao_var)
        self.create_input_field("Comprimento:", self.comprimento_var)
        self.create_input_field("Largura:", self.largura_var)
        self.create_input_field("Altura:", self.altura_var)

        # Adicionar botão para submeter os dados
        submit_button = ttk.Button(root, text="Submeter", command=self.submit_data)
        submit_button.pack(pady=5)

    def create_input_field(self, label_text, variable):
        label = ttk.Label(self.root, text=label_text)
        label.pack(pady=2)
        entry = ttk.Entry(self.root, textvariable=variable)
        entry.pack(pady=2)

    def submit_data(self):
        data = {
            'km': self.km_var.get(),
            'linha': self.linha_var.get(),
            'cidade': self.cidade_var.get(),
            'estado': self.estado_var.get(),
            'natureza_transposicao': self.natureza_var.get(),
            'bitola': self.bitola_var.get(),
            'tracado': self.tracado_var.get(),
            'trilhos': self.trilhos_var.get(),
            'fixacao': self.fixacao_var.get(),
            'comprimento': self.comprimento_var.get(),
            'largura': self.largura_var.get(),
            'altura': self.altura_var.get(),
        }

        utils.generate_diagnostic_report(data)



        # Você pode imprimir os dados ou realizar outra ação com eles
        print(data)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryApp(root)
    root.mainloop()

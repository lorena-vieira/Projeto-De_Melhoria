# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from docxtpl import DocxTemplate

def get_user_input():
    km = input("Informe o Km da OAE: ")
    linha = input("Informe a linha: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe o estado: ")
    natureza_transposicao = input("Informe a natureza da transposição: ")
    bitola = input("Informe a bitola: ")
    tracado = input("Informe o traçado: ")
    trilhos = input("Informe os trilhos: ")
    fixacao = input("Informe a fixação: ")
    comprimento = input("Informe o comprimento: ")
    largura = input("Informe a largura: ")
    altura = input("Informe a altura: ")

    return {
        'km': km,
        'linha': linha,
        'cidade': cidade,
        'estado': estado,
        'natureza_transposicao': natureza_transposicao,
        'bitola': bitola,
        'tracado': tracado,
        'trilhos': trilhos,
        'fixacao': fixacao,
        'comprimento': comprimento,
        'largura': largura,
        'altura': altura,
    }

def generate_diagnostic_report(output_path, user_input):
    # Carregar o modelo docx
    doc = DocxTemplate(r'C:\Users\Lorena\Documents\PONTES-MH\ProjetoDeMelhoria\arquivoBasePython\RelatorioMetalica.docx')

    # Adicionar os dados do usuário ao contexto
    context = user_input

    # Renderizar o documento
    doc.render(context)

    # Salvar o relatório gerado
    doc.save(output_path)

# Exemplo de uso
if __name__ == '__main__':
    output_path = 'diagnostic_report.docx'

    # Obter informações do usuário
    user_input = get_user_input()

    # Gerar relatório
    generate_diagnostic_report(output_path, user_input)

    print(f"Relatório gerado com sucesso em {output_path}")


#A seguir a criação de tela para seleção de patologias, inserção de fotos e classificação (notas)

import tkinter as tk
from tkinter import messagebox
from docxtpl import DocxTemplate
import sqlite3

class DiagnosticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação de Diagnóstico")

        # Conectar ao banco de dados (substitua 'seu_banco_de_dados.db' pelo nome do seu banco de dados)
        self.conn = sqlite3.connect('banco_patoloigias_descricoes.db')
        self.cursor = self.conn.cursor()

        # Interface do Usuário
        self.anomaly_label = tk.Label(root, text="Selecione a Anomalia:")
        self.anomaly_label.pack()

        # Obtém anomalias do banco de dados
        self.anomalies = self.fetch_anomalies()
        self.anomaly_var = tk.StringVar(root)
        self.anomaly_var.set(self.anomalies[0])  # Define o valor padrão

        self.anomaly_menu = tk.OptionMenu(root, self.anomaly_var, *self.anomalies)
        self.anomaly_menu.pack()

        self.photos_entry_label = tk.Label(root, text="Insira aqui as fotos da anomalia:")
        self.photos_entry_label.pack()

        self.photos_entry = tk.Entry(root)
        self.photos_entry.pack()

        self.durability_note_label = tk.Label(root, text="Nota para Durabilidade (1-5):")
        self.durability_note_label.pack()

        self.durability_note_entry = tk.Entry(root)
        self.durability_note_entry.pack()

        self.structural_note_label = tk.Label(root, text="Nota Estrutural (1-5):")
        self.structural_note_label.pack()

        self.structural_note_entry = tk.Entry(root)
        self.structural_note_entry.pack()

        self.submit_button = tk.Button(root, text="Submeter", command=self.generate_report)
        self.submit_button.pack()

    def fetch_anomalies(self):
        # Substitua 'anomalies_table' pelo nome da sua tabela de anomalias
        self.cursor.execute("SELECT anomaly_name FROM anomalies_table")
        anomalies = self.cursor.fetchall()
        return [anomaly[0] for anomaly in anomalies]

    def generate_report(self):
        anomaly = self.anomaly_var.get()
        photos_count = self.photos_entry.get()
        durability_note = self.durability_note_entry.get()
        structural_note = self.structural_note_entry.get()

        # Validar entrada (adapte conforme necessário)
        if not photos_count.isdigit() or int(photos_count) % 2 != 0:
            messagebox.showerror("Erro", "Informe uma quantidade par de fotos.")
            return

        try:
            durability_note = int(durability_note)
            structural_note = int(structural_note)
            if not (1 <= durability_note <= 5) or not (1 <= structural_note <= 5):
                raise ValueError("Notas devem estar entre 1 e 5.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return

        # Gerar relatório .docx
        self.generate_diagnostic_report(anomaly, photos_count, durability_note, structural_note)

    def generate_diagnostic_report(self, anomaly, photos_count, durability_note, structural_note):
        # Carregar o modelo docx
        doc = DocxTemplate(r'C:\Users\Lorena\Documents\PONTES-MH\ProjetoDeMelhoria\arquivoBasePython\RelatorioMetalica.docx')

        # Adicionar os dados ao contexto
        context = {
            'anomaly': anomaly,
            'photos_count': photos_count,
            'durability_note': durability_note,
            'structural_note': structural_note,
        }

        # Renderizar o documento
        doc.render(context)

        # Salvar o relatório gerado (substitua 'output_report.docx' pelo nome desejado)
        doc.save('output_report.docx')

        messagebox.showinfo("Relatório Gerado", "Relatório gerado com sucesso.")

if __name__ == '__main__':
    root = tk.Tk()
    app = DiagnosticsApp(root)

    label = tk.Label(root, text="Olá, tkinter!")
    label.pack()



    root.mainloop()






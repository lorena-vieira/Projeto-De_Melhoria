import tkinter as tk
from tkinter import messagebox
from docxtpl import DocxTemplate
from pymongo import MongoClient
from tkinter import filedialog
import utils
import Tela1


# Exemplo de uso
if __name__ == '__main__':
    root = tk.Tk()
    app = Tela1.DataEntryApp(root)
    root.mainloop()


#A seguir a criação de tela para seleção de patologias, inserção de fotos e classificação (notas)

CONNECTION_STRING = "mongodb+srv://lorenavieira:lorenas2fabinho@cluster0.f65bx3a.mongodb.net/"
client = MongoClient(CONNECTION_STRING)
db = client['PatologiasDescricoes']
collection = db['anomalias']


class DiagnosticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagnóstico de OAE")

                # Interface do Usuário
        self.anomaly_label = tk.Label(root, text="Anomalias e não conformidades")
        self.anomaly_label.pack()

        # Obtém anomalias do banco de dados
        self.anomalies = self.fetch_anomalies()
        self.selected_anomalies = []

        # Checkbox para anomalias
        self.anomalies_frame = tk.Frame(root)
        self.anomalies_frame.pack(pady=10)
        self.anomalies_label = tk.Label(self.anomalies_frame, text="Selecione as anomalias existentes na OAE:")
        self.anomalies_label.pack()

        for anomaly_name in self.anomalies:
            checkbox = tk.Checkbutton(self.anomalies_frame, text=anomaly_name, variable=anomaly_name)
            checkbox.pack()


        self.anomaly_var = tk.StringVar(root)
        self.anomaly_var.set(self.anomalies[0])  # Define o valor padrão

        self.anomaly_menu = tk.OptionMenu(root, self.anomaly_var, *self.anomalies)
        self.anomaly_menu.pack()

        self.durability_note_label = tk.Label(root, text="Nota para Durabilidade (1-5):")
        self.durability_note_label.pack()

        self.durability_note_entry = tk.Entry(root)
        self.durability_note_entry.pack()

        self.structural_note_label = tk.Label(root, text="Nota Estrutural (1-5):")
        self.structural_note_label.pack()

        self.structural_note_entry = tk.Entry(root)
        self.structural_note_entry.pack()

        # Botão para adicionar fotos
        self.add_photos_button = tk.Button(root, text="Adicionar Fotos", command=self.add_photos_and_notes)
        self.add_photos_button.pack(pady=5)

        self.submit_button = tk.Button(root, text="Incluir dados da anomalia")
        self.submit_button.pack(pady=5)


        self.submit_button = tk.Button(root, text="Submeter", command=self.generate_report)
        self.submit_button.pack(pady=5)

    def fetch_anomalies(self):
        anomalies_cursor = collection.find({}, {"anomaly_name": 1})
        anomaly_names = [anomaly["anomaly_name"] for anomaly in anomalies_cursor]
        return anomaly_names

    def generate_report(self):
        anomaly = self.anomaly_var.get()
        durability_note = self.durability_note_entry.get()
        structural_note = self.structural_note_entry.get()


        # Validar entrada

        try:
            durability_note = int(durability_note)
            structural_note = int(structural_note)
            if not (1 <= durability_note <= 5) or not (1 <= structural_note <= 5):
                raise ValueError("Notas devem estar entre 1 e 5.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return

        # Gerar relatório .docx
        self.generate_diagnostic_report(anomaly, durability_note, structural_note)

    def generate_diagnostic_report(self, anomaly, durability_note, structural_note):
        # Carregar o modelo docx
        doc = DocxTemplate(r'C:\Users\Lorena\PycharmProjects\Projeto-de-melhoria\diagnostic_report.docx')

        # Adicionar os dados ao contexto
        context = {
            'anomaly': anomaly,
            'durability_note': durability_note,
            'structural_note': structural_note,
        }

        # Renderizar o documento
        doc.render(context)

        # Salvar o relatório gerado (substitua 'output_report.docx' pelo nome desejado)
        output_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Documentos Word", "*.docx")])
        if output_path:
            doc.save(output_path)
            messagebox.showinfo("Relatório Gerado", f"Relatório gerado com sucesso em {output_path}")
        else:
            messagebox.showwarning("Aviso", "Operação cancelada pelo usuário.")


    def add_photos_and_notes(self):
        selected_anomalies = [anomaly for anomaly in self.anomalies if anomaly is not None]

        for anomaly in selected_anomalies:
            # Adicione aqui a lógica para adicionar campos de fotos e notas
            print(f"Anomalia: {anomaly}")

            # Exemplo: Pedir ao usuário para selecionar uma foto
            file_path = filedialog.askopenfilename(title=f"Selecione uma foto para {anomaly}", filetypes=[("JPEG files", "*.jpg;*.jpeg")])
            print(f"Foto selecionada: {file_path}")

            # Exemplo: Pedir ao usuário para inserir notas de durabilidade e estrutural
            durabilidade = input(f"Insira a nota de durabilidade para {anomaly} (1-5): ")
            estrutural = input(f"Insira a nota estrutural para {anomaly} (1-5): ")
            print(f"Notas - Durabilidade: {durabilidade}, Estrutural: {estrutural}")



if __name__ == '__main__':
    root = tk.Tk()
    app = DiagnosticsApp(root)

    label = tk.Label(root)
    label.pack()



    root.mainloop()






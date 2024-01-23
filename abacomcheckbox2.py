import tkinter as tk
from tkinter import ttk

class DiagnosticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagnóstico de OAEs")
        self.root.geometry(f"1280x720")

        # Configuração da Notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        # Adicionando abas
        checkboxes_tab1 = [
            ("checkbox 1", "off"),
            ("Checkbox 2", "off")
        ]
        self.add_tab("Características da OAE", checkboxes_tab1)

        checkboxes_tab2 = [
            ("Inadequações de contraventamento", "off"),
            ("Corrosão média, com perda de seção de aço", "off"),
            ("Sujeira e vegetação", "off"),
            ("Desgaste da pintura e corrosão", "off")
        ]
        self.add_tab("Anomalias e não conformidades", checkboxes_tab2)

    def add_tab(self, tab_title, checkboxes):
        # Criando a aba
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=tab_title)

        # Adicionando checkboxes na aba
        for checkbox_text, initial_value in checkboxes:
            check_var = tk.StringVar(value=initial_value)
            checkbox = ttk.Checkbutton(tab, text=checkbox_text, variable=check_var, onvalue="on", offvalue="off")
            checkbox.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiagnosticsApp(root)
    root.mainloop()

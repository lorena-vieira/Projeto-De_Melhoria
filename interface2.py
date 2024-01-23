import customtkinter as ctk

janela = ctk.CTk()
janela.title("Diagnóstico de OAE")
janela.geometry("1250x800")
ctk.CTkLabel(janela, text="Insira as caracterísitcas da OAE: ", font=("arial bold", 20)).pack(pady=20,padx=5)

check_var1 = ctk.StringVar(value="off")
check_var2 = ctk.StringVar(value="off")
check_var3 = ctk.StringVar(value="off")
check_var4 = ctk.StringVar(value="off")

def check_value():
    pass
    #valor = check_var.get():
    #if valor == "on":
        #print("Checkbox marcada")
        #comando para inserir/substituir no .docx


checkbox1 = ctk.CTkCheckBox(janela, text="Inadequações de contraventamento", variable=check_var1, onvalue="on", offvalue="off", command=check_value)
checkbox1.pack(pady=5)

ctk.CTkLabel(janela, text="Selecione a nota de Durabilidade: ", font=("arial bold", 12)).pack(pady=5)
transposicao = ctk.CTkOptionMenu(janela, values=["1", "2", "3", "4", "5"])
transposicao.pack(pady=5)
transposicao.set("selecione")

ctk.CTkLabel(janela, text="Selecione a nota Estrutural: ", font=("arial bold", 12)).pack(pady=5)
transposicao = ctk.CTkOptionMenu(janela, values=["1", "2", "3", "4", "5"])
transposicao.pack(pady=5)
transposicao.set("selecione")

checkbox2 = ctk.CTkCheckBox(janela, text="Corrosão média, com perda de seção de aço", variable=check_var2, onvalue="on", offvalue="off", command=check_value)
checkbox2.pack(pady=5)

ctk.CTkLabel(janela, text="Selecione a nota de Durabilidade: ", font=("arial bold", 12)).pack(pady=5)
transposicao = ctk.CTkOptionMenu(janela, values=["1", "2", "3", "4", "5"])
transposicao.pack(pady=5)
transposicao.set("selecione")

ctk.CTkLabel(janela, text="Selecione a nota Estrutural: ", font=("arial bold", 12)).pack(pady=5)
transposicao = ctk.CTkOptionMenu(janela, values=["1", "2", "3", "4", "5"])
transposicao.pack(pady=5)
transposicao.set("selecione")

checkbox3 = ctk.CTkCheckBox(janela, text="Sujeira e vegetação", variable=check_var3, onvalue="on", offvalue="off", command=check_value)
checkbox3.pack(pady=5)

ctk.CTkLabel(janela, text="Selecione a nota de Durabilidade: ", font=("arial bold", 12)).pack(pady=5)
transposicao = ctk.CTkOptionMenu(janela, values=["1", "2", "3", "4", "5"])
transposicao.pack(pady=5)
transposicao.set("selecione")

ctk.CTkLabel(janela, text="Selecione a nota Estrutural: ", font=("arial bold", 12)).pack(pady=5)
transposicao = ctk.CTkOptionMenu(janela, values=["1", "2", "3", "4", "5"])
transposicao.pack(pady=5)
transposicao.set("selecione")

checkbox4 = ctk.CTkCheckBox(janela, text="Desgaste da pintura e corrosão", variable=check_var4, onvalue="on", offvalue="off", command=check_value)
checkbox4.pack(pady=5)

ctk.CTkLabel(janela, text="Selecione a nota de Durabilidade: ", font=("arial bold", 12)).pack(pady=5)
transposicao = ctk.CTkOptionMenu(janela, values=["1", "2", "3", "4", "5"])
transposicao.pack(pady=5)
transposicao.set("selecione")

ctk.CTkLabel(janela, text="Selecione a nota Estrutural: ", font=("arial bold", 12)).pack(pady=5)
transposicao = ctk.CTkOptionMenu(janela, values=["1", "2", "3", "4", "5"])
transposicao.pack(pady=5)
transposicao.set("selecione")

def inserir ():
    pass
        #INSERIR COMANDO PARA SUBSTITUIR INFORMAÇÕES NO WORD

#Botão para inserir dados
ctk.CTkButton(janela, width=300, text="Inserir anomalias selecionadas no relatório", command=inserir).pack(pady=10)

janela.mainloop()

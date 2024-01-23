import customtkinter as ctk

janela = ctk.CTk()
janela.title("Diagnóstico de OAE")
janela.geometry("1250x800")
ctk.CTkLabel(janela, text="Insira as caracterísitcas da OAE: ", font=("arial bold", 20)).pack(pady=10,padx=5)

#Digite o Km da OAE:
entry1 = ctk.CTkEntry(janela, width=300, placeholder_text="Digite o Km da OAE")
entry1.pack(pady=5)

#Digite a linha:
entry2 = ctk.CTkEntry(janela, width=300, placeholder_text="Digite a linha")
entry2.pack(pady=5)

#Digite a Cidade:
entry3 = ctk.CTkEntry(janela, width=300, placeholder_text="Digite a cidade")
entry3.pack(pady=5)

#Seleção de UF
ctk.CTkLabel(janela, text="Defina a UF: ", font=("arial bold", 12)).pack(pady=5)
estado_var = ctk.StringVar(value="selecione")
estado = ctk.CTkOptionMenu(janela, values=["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA",
                                           "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"])
estado.set("selecione")
estado.pack(pady=5)

#Seleção de natureza da transposição
ctk.CTkLabel(janela, text="Defina a natureza da transposição: ", font=("arial bold", 12)).pack(pady=5)
transposicao = ctk.CTkOptionMenu(janela, values=["superfície aquífera", "rodovia", "ferrovia", "vale", "grota",
                                                 "contorno de encosta", "passagem rural", "outros"])
transposicao.pack(pady=5)
transposicao.set("selecione")

#Seleção de traçado
ctk.CTkLabel(janela, text="Defina o traçado: ", font=("arial bold", 12)).pack(pady=5)
tracado = ctk.CTkOptionMenu(janela, values=["tangente", "curva"])
tracado.pack(pady=5)
tracado.set("selecione")

#Seleção de trilhos
ctk.CTkLabel(janela, text="Defina o perfil trilhos: ", font=("arial bold", 12)).pack(pady=5)
trilhos = ctk.CTkOptionMenu(janela, values=["TR-32", "TR-37", "TR-45", "TR-57", "TR-68"])
trilhos.pack(pady=5)
trilhos.set("selecione")

#Seleção de fixação
ctk.CTkLabel(janela, text="Defina o tipo de fixação dos trilhos: ", font=("arial bold", 12)).pack(pady=5)
fixacao = ctk.CTkOptionMenu(janela, values=["Prego de linha", "Tirefonds", "Pandrol", "Deenick"])
fixacao.pack(pady=5)
fixacao.set("selecione")

#Digite o comprimento
entry4 = ctk.CTkEntry(janela, width=300, placeholder_text="Digite o comprimento")
entry4.pack(pady=5)

#Digite a largura
entry5 = ctk.CTkEntry(janela, width=300, placeholder_text="Digite a largura")
entry5.pack(pady=5)

#Digite a altura
entry6 = ctk.CTkEntry(janela, width=300, placeholder_text="Digite a altura")
entry6.pack(pady=5)

def inserir ():
    print(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get())
    #INSERIR COMANDO PARA SUBSTITUIR INFORMAÇÕES NO WORD

#Botão para inserir dados
ctk.CTkButton(janela, width=300, text="Inserir todos os dados no relatório", command=inserir).pack()

janela.mainloop()

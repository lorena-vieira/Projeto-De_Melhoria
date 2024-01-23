import customtkinter as ctk

janela = ctk.CTk()

janela.title("Diagnóstico de OAE")
janela.geometry("1280x720")
janela._set_appearance_mode("light")

tabview = ctk.CTkTabview(janela, width=1200, height=700, corner_radius=20, border_width=1, segmented_button_fg_color="white",
                         segmented_button_selected_color="green", segmented_button_unselected_hover_color="blue", segmented_button_unselected_color= "gray")
tabview.pack()
tab = tabview.add("Caracterísitcas da OAE")
tab = tabview.add("Anomalias e não conformidades")
tabview.tab("Caracterísitcas da OAE").grid_columnconfigure(0, weight=1)
tabview.tab("Anomalias e não conformidades").grid_columnconfigure(0, weight=1)

#Adicionar elementos na Tab
caracteristicas = ctk.CTkLabel(tabview.tab("Caracterísitcas da OAE"), text="Km\nLinha\nCidade\nEstado\nNatureza da transposição\nTraçado\nTrilhos\nFixação\nComprimento\nLargura\nAltura")
caracteristicas.pack()
anomalias = ctk.CTkLabel(tabview.tab("Anomalias e não conformidades"),
                         text="Inadequações de Contraventamento\nCorrosão média, com perda de seção de aço\nSujeira e vegetação\nDesgaste da pintura e corrosão")
anomalias.pack()

#Digite o Km da OAE:
entry1 = ctk.CTkEntry(janela, width=300, placeholder_text="Digite o Km da OAE")
entry1.pack(pady=5)

#Seleção de traçado
ctk.CTkLabel(janela, text="Defina o traçado: ", font=("arial bold", 12)).pack(pady=5)
tracado = ctk.CTkOptionMenu(janela, values=["tangente", "curva"])
tracado.pack(pady=5)
tracado.set("selecione")

janela.mainloop()

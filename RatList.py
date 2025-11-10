import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Variáveis permanentes
nome_arquivo = 'lista.txt'
meu_icone = 'RatDev.ico'
# Configuração do CustomTkinter
ctk.set_appearance_mode("Dark") # Definindo o tema escuro
ctk.set_default_color_theme("blue") # Definindo o esquema de cores
# --- Funções ---
def carregar_tarefas():
    try:
        with open(nome_arquivo, 'r') as f:
            for linha in f:
                mostrando_tarefas.insert(ctk.END, linha.strip())
    except FileNotFoundError:
        pass
def salvar_tarefas():
    todas_tarefas = mostrando_tarefas.get(0, ctk.END)
    with open(nome_arquivo, 'w') as f:
        for tarefas in todas_tarefas:
            f.write(tarefas + '\n')
def adicionar_tarefas():
    nova_tarefa = entrada_tarefa.get()
    if nova_tarefa:
        mostrando_tarefas.insert(ctk.END, nova_tarefa)
        entrada_tarefa.delete(0, ctk.END)
        messagebox.showinfo('Parabéns!','Nova tarefa adicionada com sucesso! ')
    else:
        messagebox.showwarning('Aviso', 'Por favor, digite uma tarefa para adicionar. ')
def excluir_tarefas():
    try:
        # Usa o mesmo método de seleção, pois o CTkListbox não existe nativamente,
        # mas mantemos o Listbox padrão ou aprimoramos a interface.
        indice_selecionado = mostrando_tarefas.curselection()[0]
        mostrando_tarefas.delete(indice_selecionado)
        messagebox.showinfo('Parabéns!', 'Tarefa excluída com sucesso.')
    except IndexError:
        messagebox.showwarning('Aviso', 'Por favor, exclua alguma tarefa da lista. ')
# --- Janela Principal ---
app = ctk.CTk()
app.title('Lista De Tarefas')
app.geometry('300x500')
# Configuração do Ícone
app.iconbitmap(meu_icone)
# Protocolo de Fechamento de Janela
app.protocol('WM_DELETE_WINDOW', lambda: (salvar_tarefas(), app.destroy()))
# --- Widgets ---
lista_label = ctk.CTkLabel(app, text='Minha Lista', font=ctk.CTkFont(size=20, weight="bold"))
lista_label.pack(pady=10)
frame_entrada = ctk.CTkLabel(app, text='Digite a tarefa que deseja adicionar: ', font=ctk.CTkFont(weight="bold"))
frame_entrada.pack(pady=5)
# 3. Campo de Entrada
entrada_tarefa = ctk.CTkEntry(app, width=250)
entrada_tarefa.pack(pady=10)
mostrando_tarefas = tk.Listbox(app, width=40, height=10, bd=0,bg='#242424',fg='white',selectbackground='#1f6aa5',selectforeground='white')
mostrando_tarefas.pack(pady=10)
# 5. Botões
botao_add_tarefas = ctk.CTkButton(app, text='Adicionar Tarefa', command=adicionar_tarefas)
botao_add_tarefas.pack(pady=10)
botao_del_tarefas = ctk.CTkButton(app, text='Excluir Tarefa', command=excluir_tarefas, fg_color="#8B0000", hover_color="#800000") # Exemplo de cor customizada para o botão de exclusão
botao_del_tarefas.pack(pady=10)
# --- Carregar e Rodar ---
carregar_tarefas()
app.mainloop()



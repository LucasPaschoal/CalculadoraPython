from tkinter import *
import customtkinter as ctk

root = ctk.CTk()
root.title("Calculadora")
root.geometry("408x355")
root.minsize(382, 570)
root.maxsize(382, 570)

entrada = ctk.CTkEntry(root, width=382, height=65, font=('Arial', 30), justify=RIGHT)
entrada.insert(END, 0)
entrada.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def criar_botao(texto, comando=None):
    botao = ctk.CTkButton(
        master=root,
        text=texto,
        command=comando,
        font=("Arial", 25),
        width=65,
        height=70,
        fg_color='#3c3c3c',
        corner_radius=8
    )

    return botao

def click(num):
    atual = entrada.get()
    if atual == '0' or atual == 'Erro':
        entrada.delete('0', END)
    entrada.insert(END, num)

def apagar():
    entrada.delete('0', END)
    entrada.insert(END, '0')

def ultimo_digito():
    atual = entrada.get()
    if atual != "":
        novo_valor = atual[:-1]
        entrada.delete(0, "end")
        entrada.insert("end", novo_valor)
        if entrada.get() == '':
            entrada.insert(END, '0')

def calcular():
    try:
        expressao = entrada.get()
        tamanho = len(expressao)

        for i in range(0, tamanho):
            if expressao[i] == 'x':
                expressao = expressao[:i] + '*' + expressao[i + 1:]

            if expressao[i] == '÷':
                expressao = expressao[:i] + '/' + expressao[i + 1:]

            if expressao[i] == '%':
                expressao = expressao[:i] + '/100' + expressao[i + 1:]

        resultado = str(eval(expressao))
        entrada.delete(0, "end")
        entrada.insert("end", resultado)
    except:
        entrada.delete(0, "end")
        entrada.insert("end", "Erro")

btn_c = criar_botao('C', apagar)
btn_c.configure(text_color='Red')
btn_c.place(x=10, y=80)

btn_apagar = criar_botao('<', ultimo_digito)
btn_apagar.configure(text_color='Red')
btn_apagar.place(x=110, y=80)

btn_pcent = criar_botao('%', lambda: click('%'))
btn_pcent.configure(text_color='Red')
btn_pcent.place(x=210, y=80)

btn_div = criar_botao('÷', lambda: click('÷'))
btn_div.configure(text_color='Red', font=('Arial', 40))
btn_div.place(x=310, y=80)

# Fileira 2:

btn_7 = criar_botao('7', lambda: click('7'))
btn_7.place(x=10, y=180)

btn_8 = criar_botao('8', lambda: click('8'))
btn_8.place(x=110, y=180)

btn_9 = criar_botao('9', lambda: click('9'))
btn_9.place(x=210, y=180)

btn_mult = criar_botao('X', lambda: click('x'))
btn_mult.configure(text_color='Red')
btn_mult.place(x=310, y=180)

# Fileira 3:

btn_4 = criar_botao('4', lambda: click('4'))
btn_4.place(x=10, y=280)

btn_5 = criar_botao('5', lambda: click('5'))
btn_5.place(x=110, y=280)

btn_6 = criar_botao('6', lambda: click('6'))
btn_6.place(x=210, y=280)

btn_menos = criar_botao('-', lambda: click('-'))
btn_menos.configure(text_color='Red', font=('Arial', 40))
btn_menos.place(x=310, y=280)

# Fileira 4:

btn_1 = criar_botao('1', lambda: click('1'))
btn_1.place(x=10, y=380)

btn_2 = criar_botao('2', lambda: click('2'))
btn_2.place(x=110, y=380)

btn_3 = criar_botao('3', lambda: click('3'))
btn_3.place(x=210, y=380)

btn_mais = criar_botao('+', lambda: click('+'))
btn_mais.configure(text_color='Red')
btn_mais.place(x=310, y=380)

# Fileira 5:

btn_ponto = criar_botao('.', lambda: click('.'))
btn_ponto.place(x=10, y=480)

btn_0 = criar_botao('0', lambda: click('0'))
btn_0.place(x=110, y=480)

btn_igual = criar_botao('=', calcular)
btn_igual.configure(width=165, text_color='Red', font=('Arial', 40))
btn_igual.place(x=210, y=480)

root.mainloop()

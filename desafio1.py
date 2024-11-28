import tkinter as tk

janela  =  tk.Tk()

def imc():
        peso = float(entry_peso.get())  
        altura = float(entry_altura.get())  
        imc = peso // altura ** 2  
        resultado_label.config(text=f'IMC: {imc}') 

janela.geometry('500x500')
janela.title('IMC')

label_peso = tk.Label(janela, text="Digite seu peso (kg):")
label_peso.pack(pady=10)

entry_peso = tk.Entry(janela)
entry_peso.pack(pady=10)

label_altura = tk.Label(janela, text="Digite sua altura (m)")
label_altura.pack(pady=10)

entry_altura = tk.Entry(janela)
entry_altura.pack(pady=10)

botao_imc = tk.Button(janela, text="Calcular IMC", command=imc)
botao_imc.pack(pady=20)


resultado_label = tk.Label(janela, text="IMC: ")
resultado_label.pack(pady=10)


janela.mainloop()
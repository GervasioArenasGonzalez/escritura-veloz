import tkinter as tk
import time
import random

#creo la ventana
ventana=tk.Tk()
ventana.title('¿Que tan rapido escribes?')
ventana.geometry(f'{500}x{500}+{670}+{250}')
ventana.resizable(False,False)
ventana.config(bg='lightblue')

#creo la frase aleatoria
frases = [
    "el sol se esconde detras de las montañas",
    "a veces una pausa es lo mas productivo que podes hacer",
    "las ratas son mas inteligentes de lo que muchos creen",
    "el codigo bien escrito se entiende solo",
    "nunca subestimes el poder de una buena siesta"
]

frase=random.choice(frases)

#creo la etiqueta y el entry
etiqueta=tk.Label(ventana, text=f'Escribe la siguiente frase: \n{frase}',bg='yellow',fg='red')
etiqueta.pack()

entrada=tk.Entry(ventana, width=50)
entrada.pack()


#averiguo si la frase esta bien escrita
def corregir_frase():
    label2=tk.Label(ventana, text='',width=40)
    label2.pack(pady=7)
    escritura=entrada.get()

    if escritura in frases:
        label2.config(text='Escribiste con presicion.')
    else:
        label2.config(text='Te equivocaste al escribir.')


#calculo el tiempo y lo muestro en pantalla
def calcular_tiempo():
    #obtengo el tiempo
    tiempo_final=time.time()
    tiempo_total=tiempo_final-tiempo_inicial

    #creo una etiqueta para mostrar el tiempo por pantalla
    mostrar_tiempo=tk.Label(ventana, text=f'Te has tardado {tiempo_total:.3f} segundos',width=40)
    mostrar_tiempo.pack(pady=7)


#creo una funcion que combine las dos anteriores
def oprimir_boton():
    calcular_tiempo()
    corregir_frase()


#obtengo el tiempo
tiempo_inicial=time.time()

#creo el boton
boton=tk.Button(ventana, text='Calcular tiempo', command=oprimir_boton,background='green',foreground='white')
boton.pack(pady=20)

ventana.bind('<Return>', lambda event:oprimir_boton())





ventana.mainloop()

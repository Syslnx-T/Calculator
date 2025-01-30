import tkinter as tk
from tkinter import font

# Función para actualizar la expresión en la pantalla
def click_boton(valor):
    current = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, current + valor)

# Función para evaluar la expresión
def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Función para limpiar la pantalla
def limpiar():
    pantalla.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Elegante")
ventana.geometry("400x600")
ventana.configure(bg="#2E3440")

# Configuración de la fuente
fuente = font.Font(family="Helvetica", size=18, weight="bold")

# Pantalla de la calculadora
pantalla = tk.Entry(ventana, font=fuente, borderwidth=0, bg="#4C566A", fg="#D8DEE9", justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# Crear botones y asignarles funciones
for (texto, fila, columna) in botones:
    if texto == 'C':
        boton = tk.Button(ventana, text=texto, font=fuente, bg="#BF616A", fg="#D8DEE9", borderwidth=0, command=limpiar)
    elif texto == '=':
        boton = tk.Button(ventana, text=texto, font=fuente, bg="#A3BE8C", fg="#D8DEE9", borderwidth=0, command=calcular)
        boton.grid(row=fila, column=columna, columnspan=4, sticky="nsew", padx=10, pady=10)
    else:
        boton = tk.Button(ventana, text=texto, font=fuente, bg="#434C5E", fg="#D8DEE9", borderwidth=0, command=lambda valor=texto: click_boton(valor))
    boton.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

# Ajustar el tamaño de las filas y columnas
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)
for j in range(4):
    ventana.grid_columnconfigure(j, weight=1)

# Iniciar la aplicación
ventana.mainloop()
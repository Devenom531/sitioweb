import tkinter as tk
from tkinter import ttk
import sqlite3

def agregar_producto():
    nombre = nombre_entry.get()
    cantidad = cantidad_entry.get()

    if nombre and cantidad:
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inventario (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
        conn.commit()
        conn.close()
        listar_productos()
    else:
        mensaje_label.config(text="Nombre y cantidad son campos requeridos")

def listar_productos():
    productos_tree.delete(*productos_tree.get_children())
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventario")
    productos = cursor.fetchall()
    conn.close()

    for producto in productos:
        productos_tree.insert("", "end", values=producto)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Inventario")

# Etiquetas y campos de entrada
nombre_label = ttk.Label(ventana, text="Nombre:")
nombre_label.pack()
nombre_entry = ttk.Entry(ventana)
nombre_entry.pack()

cantidad_label = ttk.Label(ventana, text="Cantidad:")
cantidad_label.pack()
cantidad_entry = ttk.Entry(ventana)
cantidad_entry.pack()

agregar_button = ttk.Button(ventana, text="Agregar Producto", command=agregar_producto)
agregar_button.pack()

mensaje_label = ttk.Label(ventana, text="")
mensaje_label.pack()

# Lista de productos
productos_tree = ttk.Treeview(ventana, columns=("ID", "Nombre", "Cantidad"))
productos_tree.heading("ID", text="ID")
productos_tree.heading("Nombre", text="Nombre")
productos_tree.heading("Cantidad", text="Cantidad")
productos_tree.pack()

listar_productos()

ventana.mainloop()

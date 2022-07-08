from tkinter import*

#creamos la ventana y le damos dimensiones
menu=Tk()
menu.geometry('200x200')

#Nombre de la venta
menu.title('Menú')

#Creamos una label para identificar la lista
desayunos = Label(menu, text="Desayunos disponibles").grid (pady=5, padx=36)

#Lista de opciones
listaComida=Listbox(menu)
listaComida.insert(0,'- Café')
listaComida.insert(1,'- Jugo de Naranjas')
listaComida.insert(3,'- Sandwich')
listaComida.insert(4,'- Tostadas')
listaComida.insert(5,'- Mermelada')

#Ubicar la lista dentro de la ventana
listaComida.grid (pady=10, padx=20)
menu.mainloop()
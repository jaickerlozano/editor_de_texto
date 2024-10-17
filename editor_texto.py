from tkinter import *
from tkinter import filedialog as FileDialog

ruta = "" # Esta variable nos permitirá almacenar en ella la ruta del fichero

def nuevo() -> None:
    'Esta función permite abrir un nuevo fichero'

    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Notepad")

def abrir() -> None:
    'Esta función permite abrir un fichero existente'

    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(initialdir='.', 
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto"
    )
    mensaje.set('Editor de Texto en python')

    # Verifica si la ruta no está vacía para indicar que la ruta de archivo seleccionada es válida
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete('1.0', END)
        texto.insert('insert', contenido)
        nombre_archivo = ruta.split("/")[-1] # Tomo solo el nombre del archivo en la ruta 
        nombre_archivo = nombre_archivo.replace(".txt","") # Elimino el .txt del nombre del archivo
        fichero.close()
        root.title(f"{nombre_archivo}") # Muestro como título el nombre del archivo abierto

def guardar() -> None:
    'Esta función permite guardar un fichero'

    global ruta
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()

def guardar_como() -> None:
    'Esta función permite guardar un fichero'

    global ruta
    mensaje.set("Guardar fichero como")
    
    fichero = FileDialog.asksaveasfile(title="Guardar fichero",
        mode="w", defaultextension=".txt")

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")

    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


# Ventana principal
root = Tk()
root.title("Mi Editor de Texto")
root.geometry("800x500")

# Barra de menú
menubar = Menu(root) # Se instancia la barra Menú
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como...", command=guardar_como)
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo") 

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)


# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")

root.config(menu=menubar)

# Bucle de la aplicacion
root.mainloop()

from tkinter import *
from tkinter import filedialog as FileDialog
import time

ruta = "" # Esta variable nos permitirá almacenar en ella la ruta del fichero

def mostrar_mensaje_temporal(texto, duracion=3000):
    mensaje.set(texto)
    root.after(duracion, lambda: mensaje.set("Editor de Texto en Python"))

def nuevo() -> None:
    'Esta función permite abrir un nuevo fichero'

    global ruta
    mostrar_mensaje_temporal("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi Editor de Texto")

def abrir() -> None:
    'Esta función permite abrir un fichero existente'

    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(initialdir='.', 
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto"
    )
    mensaje.set('Editor de Texto en Python')

    # Verifica si la ruta no está vacía para indicar que la ruta de archivo seleccionada es válida
    if ruta != "":
        with open(ruta, 'r') as fichero:
            contenido = fichero.read()
            texto.delete('1.0', END)
            texto.insert('insert', contenido)
        nombre_archivo = ruta.split("/")[-1].replace(".txt","") # Tomo solo el nombre del archivo en la ruta,
                                                                # y elimino el .txt del nombre del archivo
        root.title(f"{nombre_archivo}") # Muestro como título el nombre del archivo abierto

def guardar() -> None:
    'Esta función permite guardar un fichero'

    global ruta
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        with open(ruta, 'w+') as fichero:
            fichero.write(contenido)
            mostrar_mensaje_temporal("Fichero guardado correctamente")
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
        fichero.write(contenido)
        fichero.close()
        mostrar_mensaje_temporal("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


# Ventana principal
root = Tk()
root.title("Mi Editor de Texto")
root.geometry("800x500")

# Caja de texto central
texto = Text(root)
texto.pack(side="top", fill="both", expand=True)

# Crear un widget scrollbar vertical
scroll_y = Scrollbar(texto, orient="vertical", command=texto.yview)
scroll_y.pack(side="right", fill="y")

# Asociar el scrollbar con el widget Text
texto.config(yscrollcommand=scroll_y.set)

# Configurar el cursor para que cambie cuando se posicione sobre el scrollbar
scroll_y.config(cursor='arrow') # Arrow es la flecha por defecto pero se puede poner otra forma como corazón -> 'heart'

# Crear menú
menubar = Menu(root) # Se instancia la barra Menú
root.config(menu=menubar)

# Añadir Archivo menú
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como...", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")
 

# Añadir Editar menú
editarmenu = Menu(menubar, tearoff=0)
editarmenu.add_command(label="Cortar")
editarmenu.add_command(label="Copiar")
editarmenu.add_command(label="Pegar")
menubar.add_cascade(menu=editarmenu, label="Editar") 


# Monitor inferior
mensaje = StringVar()
mostrar_mensaje_temporal("Bienvenido a Mi Editor de Texto")
monitor = Label(root, textvar=mensaje, justify='left', bg="lightgrey", relief="sunken", anchor="w")
monitor.pack(side="left", fill="x", padx=10, pady=5)

# Bucle de la aplicacion
root.mainloop()

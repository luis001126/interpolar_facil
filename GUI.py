import tkinter as ttk
from tkinter import *
from tkinter import Menu, IntVar
from tkinter import messagebox as mBox
from tkinter.ttk import Notebook



# funciones
def Salir():
    ventana.destroy()
    ventana.quit()
    exit(ventana)


def Referencias():
    mBox.showinfo('Referencias', 'Este programa fue realizado por Luis Alexis Rojas Rondan'
                                 ' para mas informacion ponerse en contacto por via email: luisalexisrojasrondan@gmail.com'
                                 ' o al numero de telefono +53 59484201')
def GetValorsI():
    x0 = entrada_x1.get()
    x1 = entrada_x3.get()
    y0 = entrada_y1.get()
    y1 = entrada_y3.get()
    x_seek = entrada_x2.get()

    resultado1:float = ((y1 - y0 )/(x1 - x0 )*(x_seek - x0))
    resultado2:float = resultado1 + y0
    entrada_y2.set(f' {resultado2} ')


ventana = Tk()
ventana.title('Interpolacion y Extrapolacion ')
ventana.geometry('450x400')
ventana.resizable(0, 0)
# --------------------------------------------
barra_de_menu: Menu = Menu(ventana)
ventana.config(menu=barra_de_menu)

opc1 = Menu(barra_de_menu, tearoff=0)
opc1.add_command(label='Fucionamiento')
opc1.add_separator()
opc1.add_command(label='Referencias', command=Referencias)
barra_de_menu.add_cascade(label='Ayuda', menu=opc1)

texto1 = Label(ventana, text='Seleccione la opcion deseada, o busque apoyo en el menu', justify=CENTER)
texto1.pack()
# --------------------------------------------
tabla_control = Notebook(ventana)
tabla1 = ttk.Frame(tabla_control, bg='pink')
tabla_control.add(tabla1, text='Interpolacion')
tabla_control.pack(expand=True, fill='both')

texto_tabla1 = Label(tabla1, text='Introduzca los valores deseados en la tabla')
texto_tabla1.place(x=0, y=0)

texto_xI = Label(tabla1, text='valores asociados a X')
texto_xI.place(x=0, y=50)
texto_yI = Label(tabla1, text='valores asociados a Y')
texto_yI.place(x=150, y=50)

# entradas------------------------------------
entrada_x1: IntVar = IntVar()
entrada_x1.set('')
entrada_x1_entrar = Entry(tabla1, textvariable=entrada_x1, justify=CENTER)
entrada_x1_entrar.place(x=0, y=80)

entrada_x2 = IntVar()
entrada_x2.set('Val_des')
entrada_x2_entrar = Entry(tabla1, textvariable=entrada_x2, justify=CENTER)
entrada_x2_entrar.place(x=0, y=100)


entrada_x3 = IntVar()
entrada_x3.set('')
entrada_x3_entrar = Entry(tabla1, textvariable=entrada_x3, justify=CENTER)
entrada_x3_entrar.place(x=0, y=120)


entrada_y1 = IntVar()
entrada_y1.set('')
entrada_y1_entrar = Entry(tabla1, textvariable=entrada_y1, justify=CENTER)
entrada_y1_entrar.place(x=150, y=80)


entrada_y2 = IntVar()
entrada_y2.set('Resp')
entrada_y2_entrar = Entry(tabla1, textvariable=entrada_y2, justify=CENTER)
entrada_y2_entrar.place(x=150, y=100)


entrada_y3 = IntVar()
entrada_y3.set('')
entrada_y3_entrar = Entry(tabla1, textvariable=entrada_y3, justify=CENTER)
entrada_y3_entrar.place(x=150, y=120)


# --------------------------------------------
tabla2 = ttk.Frame(tabla_control, bg='pink')
tabla_control.add(tabla2, text='Extrapolacion')

texto_tabla2 = Label(tabla2, text='Introduzca los valores deseados en la tabla')
texto_tabla2.place(x=0, y=0)

texto_xE = Label(tabla2, text='valores asociados a X')
texto_xE.place(x=0, y=50)
texto_yE = Label(tabla2, text='valores asociados a Y')
texto_yE.place(x=150, y=50)
# --------------------------------------------
tabla3 = ttk.Frame(tabla_control, bg='gray')
tabla_control.add(tabla3, text='Logica')

texto3 = Label(tabla3, text='insertar como funciona')
texto3.pack()
# --------------------------------------------
boton_salir = Button(ventana, text='Sair', command=Salir)
boton_salir.place(x=390, y=360, width=50, height=25)
# --------------------------------------------
boton_calcularI = Button(tabla1, text='Calcular',command=GetValorsI)
boton_calcularI.place(x=300, y=200, width=50, height=25)

ventana.mainloop()

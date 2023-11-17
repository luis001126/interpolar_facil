import tkinter as ttk
from tkinter import *
from tkinter import Menu, IntVar, PhotoImage
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

def Funcionamiento():
    mBox.showinfo('Funcionamiento','Seleccionar entre Widget (Interpolacion y Extrapolacion), llenar los campos como se indica '
                                   'en la interfaz del programa, llenar los campos vacios y presionar el boton calcular para obtener los '
                                   'resultados, El boton salir sirve para cerrar la ventana definitivamente')

def Acerca():
    open(file='Ecuacion-I-E.docx',mode='r')
    return True


def GetValorsI():
    x0 = entrada_x1.get()
    x1 = entrada_x3.get()
    y0 = entrada_y1.get()
    y1 = entrada_y3.get()
    x_seek = entrada_x2.get()

    resultado1:float = ((y1 - y0 )/(x1 - x0 )*(x_seek - x0))
    resultado2:float = resultado1 + y0
    entrada_y2.set(f' {resultado2} ')


def GetValorsE():
        x1E = entrada_xE1.get()
        x2E = entrada_xE2.get()
        y1E = entrada_yE1.get()
        y2E = entrada_yE2.get()
        x_seekE = entrada_xE3.get()

        resultado1E: float = ((y2E - y1E) / (x2E - x1E) * (x_seekE - x1E))
        resultado2E: float = resultado1E + y1E
        entrada_yE3.set(f' {resultado2E} ')




ventana = Tk()
ventana.title('Interpolacion y Extrapolacion ')
ventana.geometry('450x400')
ventana.resizable(0, 0)
# --------------------------------------------
barra_de_menu: Menu = Menu(ventana)
ventana.config(menu=barra_de_menu)

opc1 = Menu(barra_de_menu, tearoff=0)
opc1.add_command(label='Fucionamiento', command=Funcionamiento)
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

entrada_xE1: IntVar = IntVar()
entrada_xE1.set('')
entrada_xE1_entrar = Entry(tabla2, textvariable=entrada_xE1, justify=CENTER)
entrada_xE1_entrar.place(x=0, y=80)

entrada_xE2 = IntVar()
entrada_xE2.set('')
entrada_xE2_entrar = Entry(tabla2, textvariable=entrada_xE2, justify=CENTER)
entrada_xE2_entrar.place(x=0, y=100)


entrada_xE3 = IntVar()
entrada_xE3.set('Var_des')
entrada_xE3_entrar = Entry(tabla2, textvariable=entrada_xE3, justify=CENTER)
entrada_xE3_entrar.place(x=0, y=200)

entrada_yE1 = IntVar()
entrada_yE1.set('')
entrada_yE1_entrar = Entry(tabla2, textvariable=entrada_yE1, justify=CENTER)
entrada_yE1_entrar.place(x=150, y=80)


entrada_yE2 = IntVar()
entrada_yE2.set('')
entrada_yE2_entrar = Entry(tabla2, textvariable=entrada_yE2, justify=CENTER)
entrada_yE2_entrar.place(x=150, y=100)

entrada_yE3 = IntVar()
entrada_yE3.set('Resp')
entrada_yE3_entrar = Entry(tabla2, textvariable=entrada_yE3, justify=CENTER)
entrada_yE3_entrar.place(x=150, y=200)

texto3 = Label(tabla2,text= 'Interpolar',justify=CENTER)
texto3.place(x=0,y=150)
# --------------------------------------------
tabla3 = ttk.Frame(tabla_control, bg='gray')
tabla_control.add(tabla3, text='Logica')

texto3 = Label(tabla3, text='Ecuaciones utilizadas')
texto3.place(x=0,y=0)

imagen1 = PhotoImage(file='interpol_extrapol.png')
Label(tabla3,image=imagen1,bd=12).place(x=0,y=0)

# ------------------------------------------------
boton_salir = Button(ventana, text='Salir', command=Salir, bg='gray')
boton_salir.place(x=390, y=360, width=50, height=25)
boton_salir.config(cursor='heart')
# ------------------------------------------------
boton_calcularI = Button(tabla1, text='Calcular',command=GetValorsI)
boton_calcularI.place(x=300, y=200, width=50, height=25)
boton_calcularI.config(cursor='heart')

boton_calcularE = Button(tabla2, text='Calcular',command=GetValorsE)
boton_calcularE.place(x=300, y=200, width=50, height=25)
boton_calcularE.config(cursor='heart')
#---------------------------------------------------

ventana.mainloop()

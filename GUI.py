from tkinter import *
from tkinter import messagebox as mBox, Menu
from tkinter import Menu
import tkinter as ttk
from tkinter.ttk import Notebook
#funciones
def Salir():
    ventana.destroy()
    ventana.quit()
    exit(ventana)

def Referencias():
    mBox.showinfo('Referencias','Este programa fue realizado por Luis Alexis Rojas Rondan'
                                ' para mas informacion ponerse en contacto por via email: luisalexisrojasrondan@gmail.com'
                                ' o al numero de telefono +53 59484201')

ventana = Tk()
ventana.title('Interpolacion y Extrapolacion ')
ventana.geometry('450x400')
ventana.resizable(0,0)
#--------------------------------------------
barra_de_menu: Menu = Menu(ventana)
ventana.config(menu=barra_de_menu)

opc1 = Menu(barra_de_menu,tearoff=0)
opc1.add_command(label='Fucionamiento')
opc1.add_separator()
opc1.add_command(label='Referencias',command=Referencias)
barra_de_menu.add_cascade(label='Ayuda',menu=opc1)


texto1 = Label(ventana,text='Seleccione la opcion deseada, o busque apoyo en el menu',justify=CENTER)
texto1.pack()
#--------------------------------------------
tabla_control =Notebook(ventana)
tabla1 = ttk.Frame(tabla_control,bg='gray')
tabla_control.add(tabla1,text='Interpolacion')
tabla_control.pack(expand=True, fill='both')

texto_tabla1 = Label(tabla1,text='Introduzca los valores deseados en la tabla')
texto_tabla1.place(x=0,y=0)

texto_xI = Label(tabla1,text='valores asociados a X')
texto_xI.place(x=0,y=50)
texto_yI = Label(tabla1,text='valores asociados a Y')
texto_yI.place(x=150,y=50)
#--------------------------------------------
tabla2 =ttk.Frame(tabla_control,bg='gray')
tabla_control.add(tabla2,text='Extrapolacion')

texto_tabla2 = Label(tabla2,text='Introduzca los valores deseados en la tabla')
texto_tabla2.place(x=0,y=0)

texto_xE = Label(tabla2,text='valores asociados a X')
texto_xE.place(x=0,y=50)
texto_yE = Label(tabla2,text='valores asociados a Y')
texto_yE.place(x=150,y=50)
#--------------------------------------------
boton_salir=Button(ventana,text='Sair',command=Salir)
boton_salir.place(x=390,y=360,width=50,height=25)

ventana.mainloop()

# Diseñar:
# 2- Una ventana que permita ingresar los siguientes datos:
# - Apellido y Nombre
# - Domicilio
# - Teléfono
# - DNI

#import tkinter as tk
from tkinter import *

# Create new instance - class Tk()  
window = Tk()
window.geometry( '600x450' )
window.iconbitmap( './images/logo.ico' )
window.title( 'Form - Python' )
window.resizable( 0, 0 )
window.config( background = '#2B3A4A' )

# Define Label Fields
username_label = Label( text = 'Name', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
username_label.place(x = 180, y = 70)

address_label = Label( text = 'Address', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
address_label.place( x = 180, y = 140 )

phone_label = Label( text = 'Phone', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
phone_label.place( x = 180, y = 210 )

dni_label = Label( text = 'D.N.I', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
dni_label.place( x = 180, y = 280 )



# Get and store data
username = StringVar()
address = StringVar()
phone = StringVar()
dni = StringVar()

username_entry = Entry( textvariable = username, width = '40' )
address_entry = Entry( textvariable = address, width = '40' )
phone_entry = Entry( textvariable = phone, width = '40' )
dni_entry = Entry( textvariable = dni, width = '40' )

# Define fields place
username_entry.place( x = 180, y = 100 )
address_entry.place( x = 180, y = 170 )
phone_entry.place( x = 180, y = 240 )
dni_entry.place( x = 180, y = 310 )


window.mainloop()

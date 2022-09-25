# Diseñar:
# 1- Una ventana que permita ingresar usuario y contraseña.

#import tkinter as tk
from tkinter import *

# Create new instance - class Tk()  
root = Tk()
root.geometry( '600x400' )
root.iconbitmap( './images/logo.ico' )
root.title( 'User Login' )
root.resizable( 0, 0 )
root.config( background = '#2B3A4A' )

# Define Label Fields
username_label = Label( text = 'Name', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
username_label.place( x = 180, y = 70 )
password_label = Label( text = 'Password', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
password_label.place( x = 180, y = 130 )

# Get and store data 
username = StringVar()
password = StringVar()

username_entry = Entry( textvariable = username, width = '40' )
password_entry = Entry( textvariable = password, width = '40',  show = '*' )

# Define fields place
username_entry.place( x = 180, y = 100 )
password_entry.place( x = 180, y = 160 )


root.mainloop()

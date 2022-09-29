# 4 Utilizando los widgets Menu y Notebook diseñar una pantalla de Menú/Solapas de la temática que desees.

#import tkinter 
from cProfile import label
from tkinter import*
from tkinter import ttk
from tkinter.tix import NoteBook
from turtle import bgcolor, color

# Create new instance Tk()
root=Tk()
root.iconbitmap ('logo.ico')
root.title ('Menu - Python')
root.resizable (0, 0)

# Create menu bar
menu_bar = Menu (root)
root.config (menu=menu_bar, width=800, height=500, bg='#2B3A4A')

# File menu
fileMenu=Menu (menu_bar, tearoff=0) 
menu_bar.add_cascade (label="File", menu=fileMenu) 
fileMenu.add_command (label="New") #Item
fileMenu.add_command (label="Open") #Item

# Open Recent submenu
openRecentMenu=Menu (menu_bar, tearoff=0)
fileMenu.add_cascade (label="Open Recent", menu=openRecentMenu)
openRecentMenu.add_command (label="My file 1") #Item
openRecentMenu.add_command (label="My file 2") #Item
openRecentMenu.add_command (label="My file 3") #Item

fileMenu.add_command (label="Save") #Item

# Save as submenu
saveAsMenu=Menu (menu_bar, tearoff=0) 
fileMenu.add_cascade (label="Save as", menu=saveAsMenu) 
saveAsMenu.add_command (label="PDF") #Item
saveAsMenu.add_command (label="PNG") #Item
saveAsMenu.add_command (label="JPG") #Item

# separator
fileMenu.add_separator () 

fileMenu.add_command (label="Close") #Item
fileMenu.add_command (label="Exit") #Item

# Edit menu
editMenu=Menu (menu_bar, tearoff=0)
menu_bar.add_cascade  (label="Edit", menu=editMenu) 
editMenu.add_command (label="Copy") #Item
editMenu.add_command  (label="Cut") #Item
editMenu.add_command (label="Paste") #Item

# Terminal menu
terminalMenu=Menu (menu_bar, tearoff=0)
menu_bar.add_cascade (label="Terminal", menu=terminalMenu) 
terminalMenu.add_command (label="New Terminal") #Item
terminalMenu.add_command (label="Split Terminal") #Item

# Separator
terminalMenu.add_separator () 

terminalMenu.add_command (label="Run Task") #Item
terminalMenu.add_command (label="Run Build Task") #Item

# Run menu
runMenu=Menu (menu_bar, tearoff=0)
menu_bar.add_cascade (label="Run", menu=runMenu) 
runMenu.add_command (label="Start Debugging") #Item
runMenu.add_command (label="Start Without Debugging") #Item

# Help menu
helpMenu=Menu (menu_bar, tearoff=0)
menu_bar.add_cascade (label="Help", menu=helpMenu) 
helpMenu.add_command (label="License") #Item
helpMenu.add_command (label="About Python") #Item

# block 15 footer
block15 = Frame(root)
block15.config(width ='800', height='2', bg = '#EB7A5D')
block15.pack()
block15 = Frame(root)
block15.config(width ='800', height='2', bg = '#3A424F')
block15.pack()
block15 = Frame(root)
block15.config(width ='800', height='2', bg = '#EB7A5D')
block15.pack()


#Incluimos panel para pastañas root = ttk.Notebook (ventanal)
archive=ttk.Notebook(root)
archive.config(width=800, height=500)
archive.pack () 
#Creamos las pestañas
file_1 = Frame (archive)
file_2 = Frame (archive)
file_3 = Frame (archive)
file_4 = Frame (archive)
#Agregamos pestañas creadas
archive.add (file_1, text="Label_1" ) 
archive.add (file_2, text="Label_2")
archive.add (file_3, text="Label_3")
archive.add (file_4, text="Label_4")

file_1.config(bg='#3A424F')
Label(file_1, text="Label-1", font="Calibri 25", fg="white", bg='#3A424F').place(x=350, y=200)
file_2.config(bg='#72819C')
Label(file_2, text="Label-2", font="Calibri 25", fg="white", bg='#72819C').place(x=350, y=200)
file_3.config(bg='#323D4F')
Label(file_3, text="Label-3", font="Calibri 25", fg="white", bg='#323D4F').place(x=350, y=200)
file_4.config(bg='#2D4369')
Label(file_4, text="Label-4", font="Calibri 25", fg="white", bg='#2D4369').place(x=350, y=200)







root.mainloop()

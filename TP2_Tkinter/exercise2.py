
# 2- Tomando como base la Ventana del ejercicio 2 del TP 1 diseñar lo siguiente 
# a. Apellido y Nombre 
# b. Tipo DNI (permitir seleccionar DNI LE LC CI PAS) 
# c. Nro Doc (Debe tener 8 digitos)  
# d. Fecha Nacimiento (Permitir seleccionar de un combobox mes (nombres) Día (1 a 31) el año se ingresa directamente. 
# e. Utilizar alguna ventana Modal si lo cree conveniente.


#import tkinter as tk
from tkinter import*
from tkinter import ttk
from msilib.schema import ComboBox
from tkinter import messagebox

# function to validate no more than 8 characters on document field
def validate_docNumber(text1, newText1):
    if len(newText1) > 8:
        messagebox.showinfo("", "8 characters max")
        return False
    return text1.isdecimal()

# function to validate no more than 4 characters on year field
def validate_year(text2, newText2): 
    if len(newText2) > 4:
        messagebox.showinfo("", "4 characters max")
        return False
    return text2.isdecimal()


# Create new instance class Tk()
root2 = Tk()
root2.iconbitmap( 'logo.ico' )
root2.title( 'Form - Python' )
root2.resizable( 0, 0 )
root2.config( background = '#2B3A4A' )

# block 7 header
block7 = Frame()
block7.grid(row = 0, column = 0, columnspan=2)
block7.config(width ='400', height='50', bg = '#2B3A4A')
header_label = Label( text = 'Welcome Admin', fg = 'white', font = 'Cambria 15 bold', background = '#2B3A4A' )
header_label.grid( row = 0, column = 0, columnspan=2 )

# block 8 logo
block8 = Frame()
block8.grid(row = 1, column = 0, columnspan=2)
block8.config(width ='400', height='60', bg = '#15202B')
python_image=PhotoImage( file = 'python.png' )
label=Label( root2, image = python_image, bg = '#15202B' )
label.grid( row = 1, column= 0, columnspan=2 )

# block 9 name label
block9 = Frame()
block9.grid(row = 2, column = 0)
block9.config(width ='150', height='50', bg = '#2B3A4A')
name_label = Label( text = 'Name', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
name_label.grid( row = 2, column = 0, sticky="e", padx=10 )

# block 10 name entry 
block10 = Frame()
block10.grid( row = 2, column = 1 )
block10.config( width = '250', height = '50', bg = '#2B3A4A' )
name = StringVar()
name_entry = Entry( textvariable = name, width = '30' )
name_entry.grid( row = 2, column = 1, sticky="w" )

# block 11 surname label
block11 = Frame()
block11.grid(row = 3, column = 0)
block11.config(width ='150', height='50', bg = '#2B3A4A')
surname = Label( text = 'Surname', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
surname.grid( row = 3, column = 0, sticky="e", padx=10)

# block 12 surname entry 
block12 = Frame()
block12.grid( row = 3, column = 1 )
block12.config( width = '250', height = '50', bg = '#2B3A4A' )
surname = StringVar()
surname_entry = Entry( textvariable = surname, width = '30' )
surname_entry.grid( row = 3, column = 1, sticky="w" )

# Docs type
docsType_box = ttk.Combobox(root2)
docsType_box.grid(row = 4, column = 0, sticky="e", padx=10)
docsType_box['values']=('DNI', 'LE', 'LC', 'CI', 'PAS')
docsType_box.set('DNI')
docsType_box.config(width=6)

# block 13 doc number entry 
block13 = Frame()
block13.grid( row = 4, column = 1 )
block13.config( width = '250', height = '50', bg = '#2B3A4A' )
docNumber = ttk.Entry(validate="key",width = '30', validatecommand=(root2.register(validate_docNumber), "%S", "%P")) # "%S", "%P" are the arguments
docNumber.grid( row = 4, column = 1, sticky="w" )

# block 14 birthday label
block14 = Frame()
block14.grid(row = 5, column = 0)
block14.config(width ='150', height='50', bg = '#2B3A4A')
birthday = Label( text = 'Birthday', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
birthday.grid( row = 5, column = 0, sticky="e", padx=10)

# block day box
day_box = ttk.Combobox(root2)
day_box.grid(row = 5, column = 1, sticky="w")
day_box['values']=('1', '2', '3', '4', '5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
day_box.set('Day')
day_box.config(width=5)

# block month box
month_box = ttk.Combobox(root2)
month_box.place(x=207, y=274)
month_box['values']=('January', 'February', 'March', 'April', 'May', "June", "July", "August", "September", "Octuber", "November", "December")
month_box.set('Month')
month_box.config(width=11)

# block year entry 
year = StringVar()
year_entry = ttk.Entry(validate="key",width = '5',  validatecommand=(root2.register(validate_year), "%S", "%P"))
year_entry.place( x=300, y=274 )

# block 15 footer
block15 = Frame()
block15.grid(row = 6, column = 0, columnspan=2)
block15.config(width ='400', height='100', bg = '#2B3A4A')

root=mainloop()
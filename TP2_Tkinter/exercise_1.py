
# 1-Tomamos como base el Ejercicio 1 del TP1 donde pedimos usuario y contraseña  y realizamos lo siguiente:
# a. Al título de la Ventana poner Ingreso de Usuario. Cambiar el icono por defecto. 
# b. Cambiar el color de fondo de la ventana. Establecer un tamaño adecuado y no permitir modificarlo. 
# c. Controlar que el usuario ingresado sea admin contraseña admin o su apellido 
# como  usuario y contraseña caso contrario mostrar que es incorrecto puede 
# realizarlo con un mensaje o una ventana modal.
# Si el usuario es correcto mostrar la ventana del ejercicio 2 minimizando o cerrando la primera.

#import tkinter and messagebox
from tkinter import*
from tkinter import messagebox

def login ():
    username = user_entry.get()
    password = password_entry.get()
    
    if (username == "" or password == ""):
        messagebox.showinfo("", "Fields Blank Not Allowed")
    
    elif(username == "admin" and password == "admin"):
        messagebox.showinfo("","Successful Access")
        otra_ventana = Toplevel()          #Acá iría el ejercicio 2, deberia poder traerlo de alguna manera
        window.iconify()  
        
    else:
        messagebox.showinfo("", "Incorrect Username or Password")

# Create new instance - class Tk() 
window = Tk()
window.iconbitmap('logo.ico')
window.title('Form - Python')
window.resizable(0, 0)
window.config(background = '#2B3A4A')

# block 0 header
block0 = Frame()
block0.grid(row = 0, column = 0, columnspan = 2)
block0.config(width ='400', height='50', bg = '#2B3A4A')
header_label = Label(text = 'Tkinter - Access', fg = 'white', font = 'Cambria 15 bold', background = '#2B3A4A')
header_label.grid(row = 0, column = 0, columnspan=2)

# block 1 logo
block1 = Frame()
block1.grid(row = 1, column = 0, columnspan = 2)
block1.config(width = '400', height = '60', bg = '#15202B')
python_image=PhotoImage(file = 'python.png')
label=Label(window, image = python_image, bg = '#15202B')
label.grid(row = 1, column = 0, columnspan = 2)

# block 2 user label
block2 = Frame()
block2.grid(row = 2, column = 0)
block2.config(width ='150', height='50', bg = '#2B3A4A')
user_label = Label(text = 'Name', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
user_label.grid(row = 2, column = 0, sticky = "e", padx = 10)

# block 3 name entry 
block3 = Frame()
block3.grid(row = 2, column = 1)
block3.config(width = '250', height = '50', bg = '#2B3A4A')
user = StringVar()
user_entry = Entry(textvariable = user, width = '30')
user_entry.grid(row = 2, column = 1, sticky = "w")

# block 4 password label
block4 = Frame()
block4.grid(row = 3, column = 0)
block4.config(width ='150', height='50', bg = '#2B3A4A')
password_label = Label(text = 'Password', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
password_label.grid(row = 3, column = 0, sticky = "e", padx = 10)

# block 5 password entry 
block5 = Frame()
block5.grid(row = 3, column = 1)
block5.config(width = '250', height = '50', bg = '#2B3A4A')
password = StringVar()
password_entry = Entry(textvariable = password, width = '30', show = "*")
password_entry.grid(row = 3, column = 1, sticky = "w")

# block 6 header
block6 = Frame()
block6.grid(row = 4, column = 0, columnspan = 2)
block6.config(width = '400', height = '100', bg = '#2B3A4A')

# block 7 button
btn = Button(window, text = 'LOGIN', command = login, font = 'Cambria 12', bg = '#15202B', fg = 'white')
btn.grid(row = 4, column = 0, columnspan = 2)


root=mainloop()

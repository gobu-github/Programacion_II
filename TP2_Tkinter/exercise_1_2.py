from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from msilib.schema import ComboBox

# function to validate 8 characters on document field
def validate_docNumber(text1, newText1):
    if len(newText1) > 8:
        messagebox.showinfo("", "8 characters max")
        return False
    return text1.isdecimal()

# function to validate only 4 characters and year less than 2022 in the year field
def validate_year(text2, newText2):
    if len(newText2) > 4:
        messagebox.showinfo("", "4 characters max")
        return False
    elif (newText2) > "2022":
        messagebox.showinfo("", "Please, enter a valid year")
        return False
    return text2.isdecimal()

# function to validate "admin" as username and password
def login():
    global user_entry
    username = user_entry.get()
    global password_entry
    password = password_entry.get()
    
    if(username == "a" and password == "a"):
    
# screen1, it can only be accessed with the correct username and password
        screen.iconify()
        global screen1
        
        screen1 = Toplevel(screen)
        screen1.iconbitmap( 'logo.ico' )
        screen1.title( 'Form - Python' )
        screen1.resizable( 0, 0 )
        screen1.config( background = '#2B3A4A' )

        # block 7 header
        block7 = Frame(screen1)
        block7.grid(row = 0, column = 0, columnspan=2)
        block7.config(width ='400', height='50', bg = '#2B3A4A')
        header_label = Label(screen1, text = 'Welcome Admin', fg = 'white', font = 'Cambria 15 bold', background = '#2B3A4A' )
        header_label.grid( row = 0, column = 0, columnspan=2 )

        # block 8 logo
        block8 = Frame(screen1)
        block8.grid(row = 1, column = 0, columnspan=2)
        block8.config(width ='400', height='60', bg = '#15202B')

        # block 9 name label
        block9 = Frame(screen1)
        block9.grid(row = 2, column = 0)
        block9.config(width ='150', height='50', bg = '#2B3A4A')
        name_label = Label(screen1, text = 'Name', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
        name_label.grid( row = 2, column = 0, sticky="e", padx=10 )

        # block 10 name entry 
        block10 = Frame(screen1)
        block10.grid( row = 2, column = 1 )
        block10.config( width = '250', height = '50', bg = '#2B3A4A' )
        name = StringVar()
        name_entry = Entry(screen1, textvariable = name, width = '30' )
        name_entry.grid( row = 2, column = 1, sticky="w" )

        # block 11 surname label
        block11 = Frame(screen1)
        block11.grid(row = 3, column = 0)
        block11.config(width ='150', height='50', bg = '#2B3A4A')
        surname = Label(screen1, text = 'Surname', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
        surname.grid( row = 3, column = 0, sticky="e", padx=10)

        # block 12 surname entry 
        block12 = Frame(screen1)
        block12.grid( row = 3, column = 1 )
        block12.config( width = '250', height = '50', bg = '#2B3A4A' )
        surname = StringVar()
        surname_entry = Entry(screen1, textvariable = surname, width = '30' )
        surname_entry.grid( row = 3, column = 1, sticky="w")

        # Docs type
        docsType_box = ttk.Combobox(screen1)
        docsType_box.grid(row = 4, column = 0, sticky="e", padx=10)
        docsType_box['values']=('DNI', 'LE', 'LC', 'CI', 'PAS')
        docsType_box.set('DNI')
        docsType_box.config(width=6)

        # block 13 doc number entry 
        block13 = Frame(screen1)
        block13.grid( row = 4, column = 1 )
        block13.config( width = '250', height = '50', bg = '#2B3A4A' )
        docNumber = ttk.Entry(screen1, validate="key",width = '30', validatecommand=(screen1.register(validate_docNumber), "%S", "%P")) # "%S", "%P" are the arguments)
        docNumber.grid( row = 4, column = 1, sticky="w", pady=10 )

        # block 14 birthday label
        block14 = Frame(screen1)
        block14.grid(row = 5, column = 0)
        block14.config(width ='150', height='50', bg = '#2B3A4A')
        birthday = Label(screen1, text = 'Birthday', fg = 'white', font = 'Cambria 11', background = '#2B3A4A' )
        birthday.grid( row = 5, column = 0, sticky="e", padx=10)

        # block day box
        day_box = ttk.Combobox(screen1)
        day_box.grid(row = 5, column = 1, sticky="w")
        day_box['values']=('1', '2', '3', '4', '5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
        day_box.set('Day')
        day_box.config(width=5)

        # block month box
        month_box = ttk.Combobox(screen1)
        month_box.place(x=207, y=274)
        month_box['values']=('January', 'February', 'March', 'April', 'May', "June", "July", "August", "September", "Octuber", "November", "December")
        month_box.set('Month')
        month_box.config(width=11)

        # block year entry 
        year = StringVar(screen1)
        year_entry = ttk.Entry(screen1, validate="key",width = '5',  validatecommand=(screen1.register(validate_year), "%S", "%P"))
        year_entry.place( x=300, y=274 )

        # block 15 footer
        block15 = Frame(screen1)
        block15.grid(row = 6, column = 0, columnspan=2)
        block15.config(width ='400', height='100', bg = '#2B3A4A')

    elif (username == "" or password == ""):
        messagebox.showinfo("", "Fields Blank Not Allowed")

    else:
        messagebox.showinfo("", "Incorrect Username or Password")

# main screen
def main_screen():
    global screen
    screen= Tk()

    screen.iconbitmap('logo.ico')
    screen.title('Form - Python')
    screen.resizable(0, 0)
    screen.config(background = '#2B3A4A')

    # block 0 header
    block0 = Frame()
    block0.grid(row = 0, column = 0, columnspan = 2)
    block0.config(width ='400', height='50', bg = '#2B3A4A')
    header_label = Label(screen, text = 'Tkinter - Access', fg = 'white', font = 'Cambria 15 bold', background = '#2B3A4A')
    header_label.grid(row = 0, column = 0, columnspan=2)
    
    # block 1 logo
    block1 = Frame()
    block1.grid(row = 1, column = 0, columnspan = 2)
    block1.config(width = '400', height = '60', bg = '#15202B')
    python_image=PhotoImage(file = 'python.png')
    label=Label(screen, image = python_image, bg = '#15202B')
    label.grid(row = 1, column = 0, columnspan = 2)

    # block 2 user label
    block2 = Frame()
    block2.grid(row = 2, column = 0)
    block2.config(width ='150', height='50', bg = '#2B3A4A')
    user_label = Label(screen, text = 'Name', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
    user_label.grid(row = 2, column = 0, sticky = "e", padx = 10)

    # block 3 name entry 
    block3 = Frame()
    block3.grid(row = 2, column = 1)
    block3.config(width = '250', height = '50', bg = '#2B3A4A')
    user = StringVar()
    global user_entry
    user_entry = Entry(screen, textvariable = user, width = '30')
    user_entry.grid(row = 2, column = 1, sticky = "w")

    # block 4 password label
    block4 = Frame()
    block4.grid(row = 3, column = 0)
    block4.config(width ='150', height='50', bg = '#2B3A4A')
    password_label = Label(screen, text = 'Password', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
    password_label.grid(row = 3, column = 0, sticky = "e", padx = 10)

    # block 5 password entry 
    block5 = Frame()
    block5.grid(row = 3, column = 1)
    block5.config(width = '250', height = '50', bg = '#2B3A4A')
    password = StringVar()
    global password_entry
    password_entry = Entry(screen, textvariable = password, width = '30', show = "*")
    password_entry.grid(row = 3, column = 1, sticky = "w")

    # block 6 separator
    block6 = Frame()
    block6.grid(row = 4, column = 0, columnspan = 2)
    block6.config(width = '400', height = '100', bg = '#2B3A4A')

    # block 7 button
    btn = Button(text = 'Login', width="20", command = login, font = 'Cambria 12', bg = '#15202B', fg = 'white')
    btn.grid(row = 4, column = 0, columnspan = 2)
    

    screen.mainloop()

main_screen()
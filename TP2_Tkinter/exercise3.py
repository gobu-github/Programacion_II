#import tkinter and ttk
from tkinter import*
from tkinter import ttk

# Create new instance - class Tk()
root = Tk()
root.iconbitmap('logo.ico')
root.title('Customized Travel Solutions')
root.geometry("1400x700")
root.resizable(0, 0)
root.config(bg = '#2B3A4A')

# Block 1 background photoImage
block1 = Frame(root, width=1305, height=655)
bgImage=PhotoImage(file="bgImage01.png")
labelImage=Label(root, image=bgImage)
labelImage.place(x=50, y=20)

# Block Background 3 (labelFrame)
block2 = Frame(root, width=575, height=320)
block2.config(bg='#2B3A4A')
block2.place(x=770, y=30)

# Block 3 labelFrame CTS - Flights
block3 = LabelFrame(root, text="CTS - Flights", width=520, height=300, fg="white", font="Arial 12")
block3.config(bg="#2B3A4A")
block3.pack()
block3.place(x=780, y=35)

# Row 0 check buttons
round_trip = Checkbutton(block3, text="Round trip", width=12, bg="#A1B8CF")
round_trip.grid(row = 0, column = 0, padx=7,pady=15, sticky="w")

one_way = Checkbutton(block3, text="One Way", width=16, bg="#A1B8CF")
one_way.grid(row = 0, column = 1, padx=0,pady=5, sticky="w")

multi = Checkbutton(block3, text="Multi Destination", width=35, bg="#A1B8CF")
multi.grid(row = 0, column = 2, padx=5,pady=5, sticky="w", columnspan=2)

# Row 1 boarding label
boarding_label = Label(block3, text="- BOARDING -")
boarding_label.grid(row=1, column=0, padx=5, pady=20, sticky="w")
boarding_label.config(width = '15', bg = '#2B3A4A', fg="white", font="Arial 8 bold")

# Row 1 boarding entry
boarding_entry = Entry(block3, width = '15', bg="#2B3A4A", fg="white", font="Arial 12")
boarding_entry.grid(row=1, column=1, sticky="w")

# Row 1 destination label 
destination_label = Label(block3, text="- DESTINATION -")
destination_label.grid(row=1, column=2, padx=5, pady=20, sticky="w")
destination_label.config(width = '15', bg = '#2B3A4A', fg="white", font="Arial 8 bold")

# Row 1 destination entry 
destination_entry = Entry(block3, width = '17', bg="#2B3A4A", fg="white", font="Arial 12")
destination_entry.grid(row=1, column=3, sticky="w")

# Row 2 passengers label
passengers = Label(block3, text="Passengers", bg="#15202B")
passengers.grid(row=2, column=0, padx=5, pady=5, sticky="e")
passengers.config(width = '16', bg = '#15202B', fg="white")

# Row 2 passengers combobox 
passengers_box = ttk.Combobox(block3)
passengers_box.grid(row = 2, column = 1, sticky="w")
passengers_box['values']=('1', '2', '3', '4', '5','6','7','8','9','10')
passengers_box.set('1')
passengers_box.config(width=5)

# Row 3 div (separator)
div_separator = Frame(block3)
div_separator.grid(row = 3, column = 0, columnspan = 2)
div_separator.config(height='75', bg = '#2B3A4A')

# Row 4 buttons exit and reserve
exit_btn = Button(block3, text = 'Exit', font = 'Arial 12 bold', bg = '#15202B', fg = 'white', width=15)
exit_btn.grid(row = 4, column = 0, pady=5, columnspan = 2)

reserve_btn = Button(block3, text = 'Reserve', font = 'Arial 12 bold', bg = '#15202B', fg = 'white', width=15)
reserve_btn.grid(row = 4, column = 2, pady=15, columnspan = 2)


root.mainloop()
#import tkinter and messagebox
from ast import Num
from tkinter import*
from tkinter import messagebox


# function to validate stock < order quantity
def check():
    codeArt = code_entry.get()
    descArt = description_entry.get()
    priceArt = price_entry.get()
    stock = int(stock_entry.get())
    order = int(quantity_entry.get())
    
    if (stock < order):
        messagebox.showinfo ("Order not executed", "There are not enough products in stock!")
        messagebox.showinfo ("Info", f"Quantity Orderer: {order}\n\nQuantity in Stock: {stock}")

    else:
        messagebox.showinfo ("Order executed", "Order executed successfully")
        messagebox.showinfo ("Order Checkout", f"Code: {codeArt}\n\nDescription: {descArt}\n\nPrice: ${priceArt}\n\nQuantity Ordered: {order}\n\nQuantity in Stock: {stock}")


# Create new instance - class Tk()
root = Tk()
root.iconbitmap ('logo.ico')
root.title ('Product Order Software')
root.resizable (0, 0)
root.config (background = '#2B3A4A')

# block 1/2 article code label and entry
block1 = Frame (root)
block1.grid (row = 2, column = 0)
block1.config (width ='150', height ='50', bg = '#2B3A4A')
code_label = Label (root, text = 'Article Code Number', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
code_label.grid (row = 2, column = 0, sticky = "e", padx = 10)

block2 = Frame (root)
block2.grid ( row = 2, column = 1 )
block2.config ( width = '250', height = '50', bg = '#2B3A4A')
code = StringVar()
code_entry = Entry(root, textvariable = code, width = '30')
code_entry.grid ( row = 2, column = 1, sticky="w")

# block 3/4 description label and entry
block3 = Frame (root)
block3.grid (row = 3, column = 0)
block3.config (width ='150', height ='50', bg = '#2B3A4A')
description = Label (root, text = 'Description', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
description.grid (row = 3, column = 0, sticky = "e", padx = 10)

block4 = Frame (root)
block4.grid (row = 3, column = 1)
block4.config ( width = '250', height = '50', bg = '#2B3A4A')
description = StringVar()
description_entry = Entry(root, textvariable = description, width = '30')
description_entry.grid (row = 3, column = 1, sticky = "w")

# block 5/6 description label and entry
block5 = Frame (root)
block5.grid (row = 4, column = 0)
block5.config (width ='150', height ='50', bg = '#2B3A4A')
price = Label (root, text = 'Unit Price', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
price.grid (row = 4, column = 0, sticky = "e", padx = 10)

block6 = Frame (root)
block6.grid (row = 4, column = 1)
block6.config ( width = '250', height = '50', bg = '#2B3A4A')
price = StringVar()
price_entry = Entry(root, textvariable = price, width = '30')
price_entry.grid (row = 4, column = 1, sticky = "w")

# block 7/8 stock label and entry
block7 = Frame (root)
block7.grid (row = 5, column = 0)
block7.config (width ='150', height ='50', bg = '#2B3A4A')
stock = Label (root, text = 'Stock', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
stock.grid (row = 5, column = 0, sticky = "e", padx = 10)

block8 = Frame (root)
block8.grid (row = 5, column = 1)
block8.config ( width = '250', height = '50', bg = '#2B3A4A')
stock =IntVar()
stock_entry = Entry(root, textvariable = stock, width = '30')
stock_entry.grid (row = 5, column = 1, sticky = "w")

# block 9/10 order quantity label and entry
block9 = Frame (root)
block9.grid (row = 6, column = 0)
block9.config (width ='150', height ='50', bg = '#2B3A4A')
quantity = Label (root, text = 'Order Quantity', fg = 'white', font = 'Cambria 11', background = '#2B3A4A')
quantity.grid (row = 6, column = 0, sticky = "e", padx = 10)

block10 = Frame (root)
block10.grid (row = 6, column = 1)
block10.config ( width = '250', height = '50', bg = '#2B3A4A')
quantity = IntVar()
quantity_entry = Entry(root, textvariable = quantity, width = '30')
quantity_entry.grid (row = 6, column = 1, sticky = "w")

btn = Button (text = 'Check', width = "20", command = check, font = 'Cambria 12', bg = '#15202B', fg = 'white')
btn.grid (row = 7, column = 0, columnspan = 2, pady=10)

root.mainloop()
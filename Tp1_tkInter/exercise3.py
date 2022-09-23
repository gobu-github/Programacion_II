# Diseñar:
# 3- Disponer dos Botones con las etiquetas: 'varón' y 'mujer', al presionarse mostrar un
# Texto en color según el botón elegido


#import tkinter as tk
from tkinter import *

# Define function isWoman / isMan
def isWoman():
    response1 = Label( window, text = 'Women' + entryWoman.get(), font = 'Cambria 15 bold', fg = '#777FE4', background = '#15202B' ).grid( row = 2, column = 0 )

def isMan():
    response2 = Label( window, text = 'Man' + entryMan.get(), font = 'Cambria 15 bold', fg = '#FAA954', background = '#15202B' ).grid( row = 2, column = 1 )


# Create new instance class Tk()  
window = Tk()
window.iconbitmap( './logo.ico' )
window.title( 'Exercise3' )
window.config( background = '#4B4B4D' )


# Block 1 define Woman label
block1 = Frame()
block1.grid( row = 0, column = 0 )
block1.config( width ='150', height = '150', bg = '#15202B' )
username_label = Label( text = 'Women',fg ='white', font = 'Cambria 15', background = '#15202B' )
username_label.grid( row = 0, column= 0 )

# Block 2 define Man label
block2 = Frame()
block2.grid( row = 0, column = 1 )
block2.config( width = '150', height = '150', bg = '#15202B' )
password_label = Label( text = 'Man', fg = 'white', font = 'Cambria 15', background = '#15202B' )
password_label.grid( row = 0, column = 1 )

# Block 3 submit button Women
block3 = Frame()
block3.grid( row = 1, column = 0 )
block3.config( width = '150', height = '150', bg = '#15202B' )
submit_btn = Button( window, text = 'Women', command = isWoman, fg = 'white', font = 'Cambria, 10', width = '10', height = '2', bg = '#2B3A4A' )
submit_btn.grid( row = 1, column = 0 )

# Block 4 submit button Man
block4 = Frame()
block4.grid( row = 1, column = 1 )
block4.config( width = '150', height = '150', bg = '#15202B' )
submit_btn = Button( window, text = 'Man', command = isMan, fg = 'white', font = 'Cambria, 10', width = '10', height = '2', bg = '#2B3A4A' )
submit_btn.grid( row = 1, column = 1 )

# Block 5 get and store data 
block5 = Frame()
block5.grid( row = 2, column = 0 )
block5.config( width = '150', height = '150', bg = '#15202B' )
entryMan = StringVar()

# Block 6 get and store data
block6 = Frame()
block6.grid( row = 2, column = 1 )
block6.config( width ='150', height = '150', bg = '#15202B' )
entryWoman = StringVar()

window.mainloop()
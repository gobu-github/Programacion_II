# Diseñar:
# 4- Mostrar una windowy en su interior dos botones y una label. La label muestra inicialmente el valor 1. 
# Cada uno de los botones permiten incrementar o decrementar en uno el contenido de la label

#import tkinter as tk
from tkinter import*

# Define class counter
class counter:
    def __init__( self ):
        self.window = Tk()
        self.window.resizable( 0, 0 )
        self.window.config( background = '#4B4B4D' )
        self.window.iconbitmap( './images/logo.ico' )
        self.window.title( 'Exercise4' )

        # block 1
        block1 = Frame()
        block1.grid(row = 0, column = 0)
        block1.config(width ='150', height='150', bg = '#2B3A4A')

        # block 2 Define label counter
        block2 = Frame()
        block2.grid( row = 0, column = 1 )
        block2.config( width = '150', height = '150', bg = '#15202B' )
        self.value = 1
        self.label = Label( self.window, text = self.value )
        self.label.grid( row = 0, column = 1 )
        self.label.configure( fg ='white', font = 'Cambria 40 bold', background = '#15202B' )

        # block 3
        block3 = Frame()
        block3.grid( row = 0, column = 2 )
        block3.config( width ='150', height ='150', bg = '#2B3A4A' )

        # block 4 create a button decrease
        block4 = Frame()
        block4.grid( row = 1, column= 0 )
        block4.config( width = '150', height = '150', bg = '#15202B' )

        self.btn1 = Button( self.window, text = 'Decrease', font = 'Cambria 12 bold', bg = '#FE7984', fg = '#2B3A4A', command = self.decrease )
        self.btn1.grid( row = 1, column= 0 )

        # block 5 insert logo image
        block5 = Frame()
        block5.grid( row = 1, column = 1 )
        block5.config( width = '150', height = '150', bg = '#2B3A4A' )
        logo_image=PhotoImage( file = './images/logo.png' )
        label=Label( self.window, image = logo_image, bg = '#2B3A4A' )
        label.grid( row = 1, column= 1 )

        # block 6 create a button increase
        block6 = Frame()
        block6.grid( row = 1, column = 2 )
        block6.config( width = '150', height = '150', bg = '#15202B' )
        self.btn2 = Button( self.window, text = 'Increase', font = 'Cambria 12 bold', bg = '#3DF2B8', fg = '#2B3A4A', command = self.increase )
        self.btn2.grid( row = 1, column = 2 )

        # block 7
        block7 = Frame()
        block7.grid( row = 2, column = 0 )
        block7.config( width = '150', height = '150', bg = '#2B3A4A' )

        # block 8
        block8 = Frame()
        block8.grid( row = 2, column = 1 )
        block8.config( width = '150', height = '150', bg = '#15202B' )

        # block 9
        block9 = Frame()
        block9.grid( row = 2, column = 2 )
        block9.config( width = '150', height = '150', bg = '#2B3A4A' )

        self.window.mainloop()

# Define functions increase
    def increase( self ):
        self.value = self.value + 1
        self.label.config( text = self.value )

# Define functions decrease
    def decrease( self ):
        self.value = self.value - 1
        self.label.config( text = self.value )        

counter1 = counter()
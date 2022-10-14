# import tkinter
from tkinter import*

class changeLanguage:
    def __init__(self):
        
        # Create new instance TK
        self.root=Tk()
        self.root.iconbitmap ('logo.ico')
        self.root.title("Toggle Language")
        self.root.geometry ("500x200")
        self.root.resizable (0, 0)
        self.root.config (background = '#2B3A4A')

        # block 0 header
        self.block0 = Frame ()
        self.block0.grid (row = 0, column = 0, columnspan = 3)
        self.block0.config (width = '500', height ='50', bg = '#2B3A4A')
        
        # button english
        self.btn1=Button(self.root, text="ENGLISH", command=self.englishBtn, bg='#2B3A4A', fg='white')
        self.btn1.grid(column=0, row=1)
        
        # button french
        self.btn2=Button(self.root, text="FRENCH", command=self.frenchBtn, bg='#2B3A4A', fg='white')
        self.btn2.grid(column=2, row=1)


        self.root.mainloop()

    # english btn function changes the word and bg color: red in active state or gray in inactive state
    def englishBtn(self):
        self.btn1.config(bg="red")
        self.btn2.config(bg="grey")
        ingles_label = Label( self.root, text = '<<HOUSE>>', font = 'Cambria 15', bg='#2B3A4A', fg='white')
        ingles_label.grid( row = 2, column = 1)

    # french btn function changes word and bg color: blue in active state, or gray in inactive state
    def frenchBtn(self):
        self.btn2.config(bg="blue")
        self.btn1.config(bg="grey")
        frances_label = Label( self.root, text = '<<MAISON>>', font = 'Cambria 15', bg='#2B3A4A', fg='white')
        frances_label.grid( row = 2, column = 1 )


app= changeLanguage()
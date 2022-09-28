# 4 Utilizando los widgets Menu y Notebook diseñar una pantalla de Menú/Solapas de la temática que desees.

#import tkinter 
from tkinter import*

# Create new instance Tk()
root=Tk()
root.iconbitmap ('logo.ico')
root.title ('Menu - Python')
root.resizable (0, 0)

# Create menu bar
menu_bar = Menu (root)
root.config (menu=menu_bar, width=500, height=300, bg='#2B3A4A')

# Archive menu
archiveMenu=Menu (menu_bar, tearoff=0) 
menu_bar.add_cascade (label="Archive", menu=archiveMenu) 
archiveMenu.add_command (label="New") #Item
archiveMenu.add_command (label="Save") #Item

# Save as submenu
saveAsMenu=Menu (menu_bar, tearoff=0) 
archiveMenu.add_cascade (label="Save as", menu=saveAsMenu) 
saveAsMenu.add_command (label="PDF") #Item
saveAsMenu.add_command (label="PNG") #Item
saveAsMenu.add_command (label="JPG") #Item

# separator
archiveMenu.add_separator () 

archiveMenu.add_command (label="Close") #Item
archiveMenu.add_command (label="Exit") #Item

# Edition menu
archiveEdition=Menu (menu_bar, tearoff=0)
menu_bar.add_cascade  (label="Edition", menu=archiveEdition) 
archiveEdition.add_command (label="Copy") #Item
archiveEdition.add_command  (label="Cut") #Item
archiveEdition.add_command (label="Paste") #Item

# Tools menu
archiveTools=Menu (menu_bar, tearoff=0)
menu_bar.add_cascade (label="Tools", menu=archiveTools) 
archiveTools.add_command (label="one") #Item
archiveTools.add_command (label="two") #Item
archiveTools.add_command (label="three") #Item
archiveTools.add_command (label="four") #Item

# Help menu
archiveHelp=Menu (menu_bar, tearoff=0)
menu_bar.add_cascade (label="Help", menu=archiveHelp) 
archiveHelp.add_command (label="License") #Item
archiveHelp.add_command (label="About") #Item

root.mainloop()

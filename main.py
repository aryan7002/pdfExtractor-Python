import tkinter as tk
import PyPDF2
from PIL import Image,ImageTk

root = tk.Tk()

canvas = tk.Canvas(root,width =600, height = 300)
canvas.grid(columnspan=3)

#Logo 
logo =Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column = 1, row = 0)

#Instruction
instruction = tk.Label(root,text="Select a PDF File on your computer",font='Rockwell')
instruction.grid(columnspan=3,column=0,row=1)

#Browse Button 
browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text ,font='Rockwell')
browse_text.set("Browse")
browse_btn.grid(column=1,row=2)
root.mainloop()
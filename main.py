from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from functions import display_logo, display_textbox, extract_images,display_icon

root = Tk()
root.geometry('+%d+%d'%(350,10)) #place GUI at x=350, y=10

#header area - logo & browse button
header = Frame(root, width=800, height=175, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

image_menu= Frame(root, width=800, height=60)
image_menu.grid(columnspan=3, rowspan=1, row=2)

What_img =Label(root,text="image 1 of 5" ,font=("shanti",10))
What_img.grid(row=2,column=1)

display_icon('arrow_l.png', 2, 0)
display_icon('arrow_r.png', 2, 2)


#header area - logo & browse button
save_img = Frame(root, width=800, height=60, bg="#c8c8c8")
save_img.grid(columnspan=3, rowspan=1, row=3)

copyText_btn = Button(root,text='copy text',font=("shanti",10),height=1,width=15)
saveAll_btn = Button(root,text='save all images',font=("shanti",10),height=1,width=15)
save_btn = Button(root,text='save image',font=("shanti",10),height=1,width=15)

copyText_btn.grid(row = 3,column = 0)
saveAll_btn.grid(row =3 ,column = 1)
save_btn.grid(row = 3 , column = 2)

#main content area - text and image extraction
main_content = Frame(root, width=800, height=250, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=2, row=4)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        #page_content = page_content.encode('cp1252')
        page_content = page_content.replace('\u2122', "'")

        #show text box on row 4 col 0
        display_textbox(page_content, 4, 0, root)

        #reset the button text back to Browse
        browse_text.set("Browse")

display_logo('logo.png', 0, 0)

#instructions
instructions = Label(root, text="Select a PDF file", font=("Raleway", 10), bg="white")
instructions.grid(column=2, row=0, sticky=SE, padx=75, pady=5)

#browse button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)

root.mainloop()
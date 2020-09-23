#all the imports
from tkinter import Tk,TRUE,FALSE,Label,Frame,Button,COMMAND,Image,mainloop,PhotoImage,FLAT,TOP,LEFT,BOTH
from base import export_func,import_func,run_func
from PIL import Image
from PIL import ImageTk

main=Tk()

#title
main.title("Filent")
main.geometry("700x400")

#icon
mainicon=Image.open('icon.png')
mainicon=mainicon.resize((94,94))
mainicon=ImageTk.PhotoImage(mainicon)
main.iconphoto(False,mainicon)

#background
image = Image.open('image.png')
image = image.resize((3840,2160))
img = ImageTk.PhotoImage(image)
mainframe=Label(image=img)

#button images
import_image=Image.open("import.png")
import_image=ImageTk.PhotoImage(import_image)

export_image=Image.open("export.png")
export_image=ImageTk.PhotoImage(export_image)

run_image=Image.open("Run.png")
run_image=ImageTk.PhotoImage(run_image)

#buttons
import_button=Button(mainframe,text="Import",width=60,relief=FLAT,padx=50,pady=50,image=import_image,bg="#585858",compound=TOP,activebackground="#585858",fg="#FFFFFF",command=import_func)
import_button.pack(side=LEFT,expand=TRUE)

export_buttion=Button(mainframe,text='Export',width=60,relief=FLAT,padx=50,pady=50,image=export_image,bg="#585858",compound=TOP,activebackground="#585858",fg="#FFFFFF",command=export_func)
export_buttion.pack(side=LEFT,expand=TRUE)

run_button=Button(mainframe,text="Run",width=60,relief=FLAT,padx=50,pady=50,image=run_image,bg="#585858",compound=TOP,activebackground="#585858",fg="#FFFFFF",command=run_func)
run_button.pack(side=LEFT,expand=TRUE)


#packing the mainframe(background)
mainframe.pack(fill=BOTH,expand=TRUE)

main.mainloop()
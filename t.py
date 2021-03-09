from PIL import Image, ImageTk
from tkinter import *
  
a = Tk()
img = Image.open("image/find.png")
image_ = ImageTk.PhotoImage(img)
 
scroll = Scrollbar(a, orient="vertical")
text = Text(a, width=25, height=15, wrap="none", yscrollcommand=scroll.set)
text.image_create("1.0", image=image_)
a.mainloop()
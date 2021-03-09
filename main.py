##### Importing The Requuired module ######
import tkinter as tk
from tkinter import Label, Message, StringVar, font,ttk,messagebox,filedialog,colorchooser
import speech_recognition as sr
import os

current_font_size=14
current_font_style='Arial'
weight='normal'
slant='roman'
url=''
under_line='normal'
text_changed = False 
f=False






root=tk.Tk()
root.title('Advance Notepad')
root.iconbitmap("image/logo.ico")
# root.overrideredirect(True)
# root.overrideredirect(False)
# root.attributes('-fullscreen',True)
# root.state('zoomed')
root.geometry("800x444")




######_____________   Creating The status barSection   _____________#######

status_bar=tk.Label(root,text='status bar',bg='#4281f5')
status_bar.pack(side=tk.BOTTOM,fill=tk.X)

######_____________   End The status barSection   _____________#######

######_____________creating The Menu_____________#######

main_menu=tk.Menu()
file=tk.Menu(main_menu,tearoff=0)
edit=tk.Menu(main_menu,tearoff=0)
format_=tk.Menu(main_menu,tearoff=0)
view=tk.Menu(main_menu,tearoff=0)
color_theme=tk.Menu(main_menu,tearoff=0)
help_=tk.Menu(main_menu,tearoff=0)
##########__________End The Main_menu___________########
def find_func(event=None):
    global f
    
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    if f==False:
        find_dialogue = tk.Toplevel()
        find_dialogue.geometry('450x250+500+200')
        find_dialogue.iconbitmap("image/ico.ico")

        find_dialogue.title('Find')
        find_dialogue.resizable(0,0)

        ## frame 
        find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
        find_frame.pack(pady=20)

        ## labels
        text_find_label = ttk.Label(find_frame, text='Find : ')
        text_replace_label = ttk.Label(find_frame, text= 'Replace')

        ## entry 
        find_input = ttk.Entry(find_frame, width=30)
        replace_input = ttk.Entry(find_frame, width=30)

        ## button 
        find_button = ttk.Button(find_frame, text='Find', command=find)
        replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

        ## label grid 
        text_find_label.grid(row=0, column=0, padx=4, pady=4)
        text_replace_label.grid(row=1, column=0, padx=4, pady=4)

        ## entry grid 
        find_input.grid(row=0, column=1, padx=4, pady=4)
        replace_input.grid(row=1, column=1, padx=4, pady=4)

        ## button grid 
        find_button.grid(row=2, column=0, padx=8, pady=4)
        replace_button.grid(row=2, column=1, padx=8, pady=4)
        f=True

        find_dialogue.mainloop()



######_____________   add Tollbar Function   _____________#######
def new_file(event=None):
    text_editor.delete(1.0,'end')
def open_file(event=None):
      global url
      url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select file",filetypes=(("TEXT FILE","*.txt"),("ALL FILES","*.*")))
      try:
        with open(url,'r') as file:
          content=file.read()
          text_editor.delete(1.0,tk.END)
          text_editor.insert(tk.INSERT,content)
          root.title(os.path.basename(url))

      except FileNotFoundError:
        return
      except:
        return

## save file 

def save_file(event=None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return 

## save as functionality 
def save_as(event=None):
    global url 
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return 

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        root.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return 

      
     
 
     

     
      
######_____________   End Tollbar Function   _____________#######



######_____________Add cascading_____________#######
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Colour Theme',menu=color_theme)
main_menu.add_cascade(label='Help',menu=help_)

def help_1():
    window=tk.Toplevel(bg="white")
    window.iconbitmap("image/logo.ico")
    window.geometry("444x444+500+250")
    window.resizable(0,0)

    icon=tk.PhotoImage(file="image/logo.png")
    l=Label(window,image=icon)
    l2=Label(window,text="Advance Notepad",bg="white",fg="#3486eb",font=("Comic Sans MS", 20, "bold"))
    l3=Label(window,text="__________________________________________________________________________",bg="white",fg="#3486eb")
    ico1=tk.PhotoImage(file="image/note.png")
    copy=Label(window,text="Â© Suraj Yadav.All right are reserved.",bg="white").place(x=160,y=188)
    luck=Label(window,image=ico1)
    main=Label(window,text="Python Programming Project",bg="white").place(x=160,y=168)
    main1=Label(window,text="This Dekstop Based Application is build by Suraj Yadav All basic ",bg="white").place(x=60,y=268)
    main2=Label(window,text="Functionality are incuded in this Project,The advance Fetures are- ",bg="white").place(x=60,y=284)
    main3=Label(window,text="1.  Voice Input ",bg="white").place(x=60,y=304)
    main4=Label(window,text="2.  Find/Replace Function",bg="white").place(x=60,y=324)
    main5=Label(window,text="2.  Background/Foreground color Buttom",bg="white").place(x=60,y=344)
    def destroy():
        window.destroy()
    ok=ttk.Button(window,text="OK",command=destroy).place(x=350,y=400)

    l.place(x=70,y=50)
    l2.place(x=190,y=70)
    l3.place(x=30,y=130)
    luck.place(x=50,y=150)

  
    
    window.mainloop()


help_.add_command(label="About Advance pad",command=help_1)


##########__________End Cascading___________########

######_____________Import The icons of File Menu_____________#######
new_icon=tk.PhotoImage(file="image/new.png")
open_icon=tk.PhotoImage(file="image/open.png")
new_icon=tk.PhotoImage(file="image/new.png")
save_icon=tk.PhotoImage(file="image/save.png")
save_as_icon=tk.PhotoImage(file="image/save_as.png")
exit_icon=tk.PhotoImage(file="image/exit.png")


##########__________End Import The icons of File Menu___________########

######_____________File Menu add command_____________#######
file.add_command(label="   New",image=new_icon,compound=tk.LEFT,accelerator='CRT+N',command=new_file)
file.add_command(label="   Open",image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
file.add_command(label="   Save",image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
file.add_command(label="   Save As",image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+shift+S',command=save_as)
file.add_command(label="   Exit",image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+shift+X',command=exit_func)


######_____________End File Menu add command_____________#######


######_____________Import The icons of edit Menu_____________#######
cut_icon=tk.PhotoImage(file="image/cut.png")
copy_icon=tk.PhotoImage(file="image/copy.png")
clear_all_icon=tk.PhotoImage(file="image/clear_all.png")
find_icon=tk.PhotoImage(file="image/find.png")
paste_icon=tk.PhotoImage(file="image/paste.png")
undo_icon=tk.PhotoImage(file="image/undo.png")
redo_icon=tk.PhotoImage(file="image/q.png")





##########__________End Import The icons of edit Menu___________########

def clear_all():
    text_editor.delete(1.0,tk.END)


######_____________   Add bar's Icon   _____________#######

toolbar_icon=tk.PhotoImage(file="image/tool_bar.png")
statusbar_icon=tk.PhotoImage(file="image/status_bar.png")


######_____________ End  Add bar's Icon   _____________#######

######_____________   Add bar's comand   _____________#######

# view.add_checkbutton(label="tool bar",image=toolbar_icon,compound=tk.LEFT)
# view.add_checkbutton(label="status bar",image=statusbar_icon,compound=tk.LEFT)


######_____________   End bar's comand   _____________#######

######_____________   Add Color Theam icon    _____________#######
font_color_icon=tk.PhotoImage(file="image/font_color.png")

red_icon=tk.PhotoImage(file="image/red.png")
night_blue_icon=tk.PhotoImage(file="image/night_blue.png")
monokai_icon=tk.PhotoImage(file="image/monokai.png")
light_plus_icon=tk.PhotoImage(file="image/light_plus.png")
light_default_icon=tk.PhotoImage(file="image/light_default.png")
dark_icon=tk.PhotoImage(file="image/dark.png")
# hacker_icon=tk.PhotoImage(file="image/hacker.png")


######_____________   End Color Theam icon    _____________#######

######_____________   Add Color Theam Command    _____________#######

def change_to_white():
    text_editor.config(bg="white",fg="black",insertbackground="black")
def change_to_light():
    text_editor.config(bg="#f2f1ed")

def change_to_dark():
    text_editor.config(bg="black",fg="white",insertbackground="white")

def change_to_monokai():
    text_editor.config(bg="#fce1a7",fg="black",insertbackground="black")
def change_to_pink():
    text_editor.config(bg="#fcd3ae",fg="black",insertbackground="black")
def change_to_hacker():
    text_editor.config(bg="black",fg="green",insertbackground="green")
def change_to_night_blue():
    text_editor.config(bg="#81b4f7",fg="black",insertbackground="black")
def change_to_select():
    color=colorchooser.askcolor()
    a= color[1].split("#")
    i = int(a[1], 16)
    # print(i)
    if int(i)<646464:
        text_editor.config(fg="white",insertbackground="white")

        

        

    
       

    text_editor.config(bg=color[1])
    print(color[1])






color_theme.add_command(label="Default",image=light_default_icon,compound=tk.LEFT,command=change_to_white)
color_theme.add_command(label="Default Plus ",image=light_plus_icon,compound=tk.LEFT,command=change_to_light)
color_theme.add_command(label="Dark ",image=dark_icon,compound=tk.LEFT,command=change_to_dark)
color_theme.add_command(label="monokai ",image=monokai_icon,compound=tk.LEFT,command=change_to_monokai)
color_theme.add_command(label="Light pink ",image=red_icon,compound=tk.LEFT,command=change_to_pink)
color_theme.add_command(label="night_blue ",image=night_blue_icon,compound=tk.LEFT,command=change_to_night_blue)
color_theme.add_command(label="Hacker ",image=dark_icon,compound=tk.LEFT,command=change_to_hacker)
color_theme.add_command(label="select ",image=font_color_icon,compound=tk.LEFT,command=change_to_select)




######_____________   End Color Theam Command    _____________#######

########________________________Creating tollbar_________________########## relief="groove"

# print(tk.font.families())

toll_bar=tk.Label(root,bg="#4281f5")
# toll_bar.config(fontsize='50')
toll_bar.pack(side=tk.TOP,fill=tk.X,ipady=10)

################################font_box
fonts=tk.font.families()
fontselect=StringVar()
font_box=ttk.Combobox(root,width=20,state='readonly',textvariable=fontselect,)
font_box['values']=fonts
font_box.current(17)
font_box.place(x=2,y=10)

#-----------------

###fontSize

font_size=tk.IntVar()

font_size_box=ttk.Combobox(root,width=20,state='readonly',textvariable=font_size)
font_size_box['values'] =tuple(range(6,81,2))
font_size_box.place(x=157,y=10)
font_size_box.current(4)


####buttons

bold_icon=tk.PhotoImage(file="image/bold.png")
italic_icon=tk.PhotoImage(file="image/italic.png")
underline_icon=tk.PhotoImage(file="image/underline.png")
align_center_icon=tk.PhotoImage(file="image/align_center.png")
align_left_icon=tk.PhotoImage(file="image/align_left.png")
align_right_icon=tk.PhotoImage(file="image/align_right.png")
voice_icon=tk.PhotoImage(file="image/voice.png")
listen_icon=tk.PhotoImage(file="image/listen.png")





bold_button=tk.Button(root,image=bold_icon,)
# bold_button.grid(row=0,column=3,padx=5)
bold_button.place(x=330-14,y=6)

italic_button=tk.Button(root,image=italic_icon)
italic_button.place(x=370-14,y=6)


underline_button=tk.Button(root,image=underline_icon)
underline_button.place(x=410-14,y=6)

font_color_button=tk.Button(root,image=font_color_icon)
font_color_button.place(x=450-14,y=6)



align_left_button=tk.Button(root,image=align_left_icon)
align_left_button.place(x=490-14,y=6)

align_center_button=tk.Button(root,image=align_center_icon)
align_center_button.place(x=530-14,y=6)

align_right_button=tk.Button(root,image=align_right_icon)
align_right_button.place(x=570-14,y=6)

voice_button=tk.Button(root,image=voice_icon)
voice_button.place(x=610-14,y=6)

######_____________   Creating The Text-editor Section   _____________#######

text_editor=tk.Text(root,font=('arial',14),undo=True)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(root)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
scroll_bar.config(command=text_editor.yview)

text_editor.pack(fill=tk.BOTH,expand=True)
text_editor.config(yscrollcommand=scroll_bar.set)

######_____________   Ending The Text-editor Section   _____________#######



######_____________Edit  Menu add command_____________#######
edit.add_command(label="   Cut",image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="   Copy",image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="   Paste",image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="   Clear All",image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+A+C',command=clear_all)

edit.add_command(label="   Undo",image=undo_icon,compound=tk.LEFT,accelerator='Ctrl+Z',command=text_editor.edit_undo)
edit.add_command(label="   Redo",image=redo_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=text_editor.edit_redo)
edit.add_command(label="   Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl+F",command=find_func)



######_____________End Edit  Menu add command_____________#######






######_____________   add Function On Font Section   _____________#######

def change_size(event=None):
    global current_font_size,current_font_style
    current_font_size=font_size_box.get()
    text_editor.config(font=(current_font_style,current_font_size,weight,slant))
def change_font(event=None):
    global current_font_size,current_font_style
    current_font_style=font_box.get()
    text_editor.config(font=(current_font_style,current_font_size,weight,slant))
    
    
    

font_size_box.bind("<<ComboboxSelected>>",change_size)
font_box.bind('<<ComboboxSelected>>',change_font)

######_____________  End Function On Font Section   _____________#######

######_____________  Creating Button Functinality _____________#######



def change_bold():
    global weight
    text_proparty=tk.font.Font(font=text_editor['font'])
    if(text_proparty.actual()['weight']=='normal'):
      text_editor.config(font=(current_font_style,current_font_size,'bold',slant,))
      
      weight='bold'
    if(text_proparty.actual()['weight']=='bold'):
      text_editor.config(font=(current_font_style,current_font_size,'normal',slant,under_line))
      
      weight='normal'



bold_button.config(command=change_bold)

def change_italic():
    global slant
    text_proparty=tk.font.Font(font=text_editor['font'])
    if(text_proparty.actual()['slant']=='roman'):
      text_editor.config(font=(current_font_style,current_font_size,weight,'italic',under_line))
      
      slant='italic'
    if(text_proparty.actual()['slant']=='italic'):
      text_editor.config(font=(current_font_style,current_font_size,'normal','roman',under_line))
      
      slant='roman'
italic_button.config(command=change_italic)


def change_underline():
    global under_line
    text_proparty=tk.font.Font(font=text_editor['font'])
    if(text_proparty.actual()['underline']==0):
      text_editor.config(font=(current_font_style,current_font_size,weight,'italic','underline'))
      
      under_line='underline'
    if(text_proparty.actual()['underline']==1):
      text_editor.config(font=(current_font_style,current_font_size,'normal','roman','normal'))
      
      under_line='normal'
underline_button.config(command=change_underline)

#fg color

def color_choser(event=None):
      color=colorchooser.askcolor()
      text_editor.config(fg=color[1])
font_color_button.config(command=color_choser)

def voice_input():
      # listen=ttk.Button(toll_bar,image=listen_icon)
      # listen.grid(row=0,column=10,padx=5)
      # sr.Microphone(device_index=1)
      try:
         
         r=sr.Recognizer()
         with sr.Microphone() as source:
           audio=r.listen(source)
           text=r.recognize_google(audio)
           text_editor.insert(tk.INSERT,text+" ")
      except:
        messagebox.showwarning("Connection Problem","Please Check Your Internet Connection or Try Again Latter")
        
     
  
voice_button.config(command=voice_input)

def right_align():
  text_content=text_editor.get(1.0,'end')
  text_editor.tag_config('right',justify=tk.RIGHT)
  text_editor.delete(1.0,'end')
  text_editor.insert(tk.INSERT,text_content,'right')

def left_align():
      text_content=text_editor.get(1.0,'end')
      text_editor.tag_config('left',justify=tk.LEFT)
      text_editor.delete(1.0,'end')
      text_editor.insert(tk.INSERT,text_content,'left')
def center_align():
      text_content=text_editor.get(1.0,'end')
      text_editor.tag_config('center',justify=tk.CENTER)
      text_editor.delete(1.0,'end')
      text_editor.insert(tk.INSERT,text_content,tk.CENTER)


align_right_button.config(command=right_align)
align_left_button.config(command=left_align)
align_center_button.config(command=center_align)


######_____________  Ending Button Functinality _____________#######


def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True 
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}',fg="white")
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)

## view check button 

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toll_bar.pack_forget()
        show_toolbar = False 
    else :
        text_editor.pack_forget()
        # status_bar.pack_forget()
        # toll_bar.pack(side=tk.TOP, fill=tk.X)
        toll_bar.pack(side=tk.TOP,fill=tk.X,ipady=10)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True 


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        text_editor.pack_forget()


        status_bar.pack(side=tk.BOTTOM,fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)


        show_statusbar = True 


view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_toolbar, image=toolbar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, image=statusbar_icon, compound=tk.LEFT, command=hide_statusbar)

root.config(menu=main_menu)
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-Alt-s>", save_as)
root.bind("<Control-q>", exit_func)
root.bind("<Control-f>", find_func)
root.bind("<Control-z>", text_editor.edit_undo)
root.bind("<Control-x>", text_editor.edit_redo)



root.mainloop()





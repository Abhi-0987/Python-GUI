from tkinter import *
from tkinter import ttk, font
from tkinter import messagebox
import random, string
import pyperclip

source=""
def complexity():
    global source
    com = len_var.get()
    if com==1:
        source = string.ascii_lowercase + string.digits
        R2['state']='disabled'
        R3['state']='disabled'
        R4['state']='disabled'
    elif com==2:
        source = string.ascii_uppercase + string.digits
        R1['state']='disabled'
        R3['state']='disabled'
        R4['state']='disabled'
    elif com==3:
        source = string.ascii_letters + string.digits
        R1['state']='disabled'
        R2['state']='disabled'
        R4['state']='disabled'
    elif com==4:
        source = string.printable
        R1['state']='disabled'
        R2['state']='disabled'
        R3['state']='disabled'

def reset():
    global source
    NameEntry.delete(0,'end')
    pass_length.set(0)
    GeneratedPass.delete(0,'end')
    R1['state']='abled'
    R2['state']='abled'
    R3['state']='abled'
    R4['state']='abled'
    source=""
    len_var.set(0)
    

def generate():
    global source
    length = pass_length.get()
    password = ""
    name=Namevar.get()
    if len(name)==0:
        messagebox.showinfo("Disclaimer","Please Enter Your Name")
    else:
        if len(source)==0:
            messagebox.showinfo("Disclaimer","Please Select Complexity")
        elif length>=8:
            for i in range(length):
                password+=random.choice(source)
            gen_pass.set(password)
        if length<8:
            messagebox.showinfo("Disclaimer","Minimum length must be 8")

def copycliptoboard():
    generated_pass = gen_pass.get()
    if len(generated_pass)==0:
        messagebox.showinfo('No Data','Ooppss!! The Password is\n not generated')
    else:
        pyperclip.copy(generated_pass)
        messagebox.showinfo('voilà!!!!','Congrats on creating your password..\n It is copied to Clipboard')

pass_gen= Tk()
pass_gen.title('Password Generator')
pass_gen.geometry('545x345')
pass_gen.resizable(0,0)
font.families()

frame = Frame(pass_gen,bg='black',width=550,height=55).grid(row=0,columnspan=3)

Title = Label(frame,text='PASSWORD GENERATOR',font=('Eras Medium ITC',20,'bold','italic'),bg='salmon3',justify='center',bd=7,relief=GROOVE,height=1,width=22)
Title.grid(padx=(70,0),row=0)

Namevar = StringVar()
Name = Label(text='NAME:',font=('Eras Medium ITC',15,'bold')).grid(row=1,column=0,sticky=W,padx=(50,0))
NameEntry = ttk.Entry(font=('Eras Medium ITC',15),textvariable=Namevar,width=15,style='M.TEntry')
NameEntry.grid(row=1,column=0,padx=(5,0),pady=(2,0))

pass_length = IntVar()
Length = Label(text='Select Length:',font=('Eras Medium ITC',15,'bold')).grid(row=2,column=0,sticky=W,padx=(5,0),pady=(5,0))
LengthEntry = ttk.Entry(font=('Eras Medium ITC',15),textvariable=pass_length,width=15,).grid(row=2,column=0,padx=(5,0),pady=(5,0))

labelframe = LabelFrame(pass_gen,text='Select The Complexity',width=323,height=70,bd=1,relief=SOLID).grid(row=3,column=0,sticky=W,padx=(5,0),pady=5)

frame2 = Frame(pass_gen,bg='black',width=175,height=240).grid(row=1,rowspan=6,sticky=E,columnspan=4,padx=(0,21),pady=(5,30))
frame3 = Frame(pass_gen,width=165,height=230).grid(row=1,rowspan=6,sticky=E,columnspan=4,padx=(0,26),pady=(5,30))
Notelabel = Label(text='NOTE',font=("Microsoft Himalaya",20)).grid(row=1,column=0,sticky=E,pady=(13,0),padx=(0,13))
Notetext = Label(text='Low: Password with  \nlowercase letters&digits\nFair: Password with  \nuppercase letters&digits',font=("Microsoft Himalaya",15))
Notetext.grid(row=1,rowspan=3,columnspan=2,sticky=E,pady=(5,0),padx=(325,11))

Notetext1 = Label(text='Strong: Password with   \nlowercase,Uppercase&digits\nVerystrong: Password with \nlowercase,Uppercase,digits\nand Special Charecters',font=("Microsoft Himalaya",15))
Notetext1.grid(row=3,rowspan=4,columnspan=2,sticky=E,padx=(363,0),pady=(6,0))

len_var = IntVar()
R1_name = Label(text='Weak',font=('Helvetica', 10)).grid(row=3,column=0,sticky=W,padx=(15,0),pady=(35,0))
R1 = ttk.Radiobutton(pass_gen,value=1,variable=len_var,command=complexity)
R1.grid(row=3,column=0,sticky=NW,padx=(25,0),pady=(27,0))

R2_name = Label(text='Fair',font=('Helvetica', 10)).grid(row=3,column=0,sticky=W,padx=(100,0),pady=(35,0))
R2 = ttk.Radiobutton(pass_gen,value=2,variable=len_var,command=complexity)
R2.grid(row=3,column=0,sticky=NW,padx=(105,0),pady=(27,0))

R3_name = Label(text='Strong',font=('Helvetica', 10)).grid(row=3,column=0,sticky=W,padx=(170,0),pady=(35,0))
R3 = ttk.Radiobutton(pass_gen,value=3,variable=len_var,command=complexity)
R3.grid(row=3,column=0,sticky=NW,padx=(185,0),pady=(27,0))

R4_name = Label(text='Very Strong',font=('Helvetica', 10)).grid(row=3,column=0,sticky=W,padx=(230,0),pady=(35,0))
R4 = ttk.Radiobutton(pass_gen,value=4,variable=len_var,command=complexity)
R4.grid(row=3,column=0,sticky=NW,padx=(255,0),pady=(27,0))

gen_pass = StringVar()
passgen = Label(text='Password:',font=('Eras Medium ITC',15,'bold')).grid(row=4,column=0,sticky=W,padx=(5,0),pady=(5,0))
GeneratedPass = ttk.Entry(font=('Eras Medium ITC',15),textvariable=gen_pass,justify='center',width=15)
GeneratedPass.grid(row=4,column=0,padx=(0,70),pady=(5,0))

genbtn = ttk.Button(text='GENERATE',style='E.TButton',command=generate).grid(row=5,column=0,sticky=W,padx=(70,0),pady=(5,0))
acceptbtn = ttk.Button(text='ACCEPT',style='E.TButton',command=copycliptoboard).grid(row=5,column=0,sticky=E,padx=(0,145),pady=(5,0))
Resetbtn = ttk.Button(text='RESET',style='E.TButton',command=reset).grid(row=6,column=0,padx=(0,70),pady=(5,0),ipadx=50)


style = ttk.Style()
style.configure('E.TButton',font=('Gill Sans MT', 15))



pass_gen.mainloop()

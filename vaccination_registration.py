from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import main
import vaccination_info
import traceback

#global variables
entry_name = ""
entry_mob = ""
entry_age = ""
entry_addhaar = ""
var = ""
vaccine_choose = ""
center_choose = ""
root = ""
dose_var = ""

def insert_record():
    global dose_var,entry_name,entry_mob,entry_age,entry_addhaar,var,vaccine_choose,center_choose
    present_date = f"{datetime.now().day}-{datetime.now().month}-{datetime.now().year}"
    present_time = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
     
    is_pass = True
    warn = ""

    if entry_name.get() == "" and entry_mob.get() == "" and entry_addhaar.get() == "" and entry_age.get() == "" and var.get() == "0" and vaccine_choose.get() == "" and dose_var.get() == "0" and center_choose.get() == "":
        warn = "Please fill all the fields"
        is_pass = False
    
    elif entry_name.get() == "":
        warn = "Name can't be empty"
        is_pass = False
            
    elif entry_mob.get() == "":
        warn = "Mobile no. can't be empty"
        is_pass = False

    elif entry_addhaar.get() == "":
        warn = "Addhaar can't be empty"
        is_pass = False

    elif entry_age.get() == "":
        warn = "Age no. can't be empty"
        is_pass = False
        
    elif  var.get() == "0":
        warn = "Select Gender"
        is_pass = False
   
    elif vaccine_choose.get() == "":
        warn = "Select Vaccine"
        is_pass = False
   

    elif dose_var.get() == "0":
        warn = "Select Dose"
        is_pass = False
   
    elif center_choose.get() == "":
        warn = "Select Center"
        is_pass = False

    elif len(entry_addhaar.get()) > 12 or len(entry_addhaar.get()) < 12:
        warn = "Enter the 12 digit addhaar no."
        is_pass = False
   
    elif len(entry_mob.get()) < 10 or len(entry_mob.get()) < 10:
        warn = "Enter the 10 digit Mobile no"
        is_pass = False

    elif int(entry_age.get()) < 18 or int(entry_age.get()) > 150:
        warn = "Enter valid age"
        is_pass = False
    
    if is_pass:
                try:
                    mob = int(entry_mob.get())
                    addh = int(entry_addhaar.get())
                    con = sqlite3.connect('database/vaccination_record.db')
                    cur = con.cursor()
                    cur.execute("INSERT INTO record VALUES (:name, :mob, :addhaar, :age, :gender, :vaccine_name, :dose,:center_name, :date, :time)",
                                {'name' : entry_name.get(),
                                 'mob' : mob,
                                 'addhaar' : addh,
                                 'age' : entry_age.get(),
                                 'gender' : var.get(),
                                 'vaccine_name' : vaccine_choose.get(),
                                 'dose' : dose_var.get(),
                                 'center_name' : center_choose.get(),
                                 'date' : present_date,
                                 'time' : present_time
                                 })
                    con.commit()
                    messagebox.showinfo('Confirmation','Record Sucessfully Saved')

                except ValueError as vp:
                    messagebox.showerror("warning","Please input valid no.")
            
                except Exception as ep:
                    messagebox.showerror("warning",'Addhaar must be Unique')


    else:
        messagebox.showerror('Error',warn)

def back_to_main():
    root.destroy()
    vaccination_info.run()


def run():
    global dose_var,root,entry_name,entry_mob,entry_age,entry_addhaar,var,vaccine_choose,center_choose
    root = Tk()
    root.title("Vaccination")

    width = 700
    height = 740
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable('False','False')
    root.config(bg="#ffffff")
    img = PhotoImage(file="icon/covid.png")
    root.iconphoto(root,img)
    
    img_btn = PhotoImage(file="icon/back.png")
    img_size = img_btn.subsample(20, 20)
    back_button = Button(root, image=img_size, command=back_to_main)
    back_button.grid(row=0, column=0)
    back_button.config(bg="#ffffff")
    back_button.config(borderwidth=0)
    back_button.config(activebackground="#ffffff")

    label_title=Label(root,text="Vaccination Registration")
    label_title.grid(row=1,column=3,pady=20,columnspan=4,sticky=W)
    label_title.config(bg="#ffffff",fg='#297d5d')
    label_title.config(font=("Papyrus",20,"bold"))

    label_name=Label(root,text="Full Name :")
    label_name.grid(row=3,column=2,pady=20)
    label_name.config(bg="#ffffff")
    label_name.config(font=("Papyrus",11))
    entry_name = Entry(root)
    entry_name.grid(row=3,column=3)
    entry_name.config(font=("Papyrus",11))

    label_mob=Label(root,text="Mob No. :")
    label_mob.grid(row=4,column=2,pady=20)
    label_mob.config(bg="#ffffff")
    label_mob.config(font=("Papyrus",11))
    entry_mob = Entry(root)
    entry_mob.grid(row=4,column=3)
    entry_mob.config(font=("Papyrus",11))


    label_addhaar=Label(root,text="Addhhar No. :")
    label_addhaar.grid(row=5,column=2,pady=20)
    label_addhaar.config(bg="#ffffff")
    label_addhaar.config(font=("Papyrus",11))
    entry_addhaar = Entry(root)
    entry_addhaar.grid(row=5,column=3)
    entry_addhaar.config(font=("Papyrus",11))


    label_age=Label(root,text="Age :")
    label_age.grid(row=6,column=2,pady=20)
    label_age.config(bg="#ffffff")
    label_age.config(padx=15)
    label_age.config(font=("Papyrus",11))
    entry_age = Entry(root)
    entry_age.grid(row=6,column=3)
    entry_age.config(font=("Papyrus",11))


    rb_void = Label(root,text="                          ")
    rb_void.grid(row=6,column=1)
    rb_void.config(bg="#ffffff")

    var = StringVar()
    rb_label = Label(root,text="Gender :")
    rb_label.grid(row=7,column=2)
    rb_label.config(bg="#ffffff")
    rb_label.config(pady=15)
    rb_label.config(font=("Papyrus",11))

    rb= Radiobutton(root, text="Male" ,variable=var, value="Male",borderwidth=0,font= ("Papyrus",11),padx = 20)
    rb.grid(row=7,column=3)
    rb.config(bg="#ffffff")
    rb.config(activebackground="#ffffff")
    rb.config(font=("Papyrus",11))

    rb1= Radiobutton(root, text="Female" ,variable=var, value="Female",borderwidth=0,font= ("Papyrus",11),padx = 20)
    rb1.grid(row=7,column=4)
    rb1.config(bg="#ffffff")
    rb1.config(activebackground="#ffffff")
    rb1.config(font=("Papyrus",11))

    rb2= Radiobutton(root, text="Other" ,variable=var, value="Other",borderwidth=0,font= ("Papyrus",11),padx = 20)
    rb2.grid(row=7,column=5)
    rb2.config(bg="#ffffff")
    rb2.config(activebackground="#ffffff")
    rb2.config(font=("Papyrus",11))
    var.set(0)

    label_vaccine=Label(root,text="Vaccine :")
    label_vaccine.grid(row=8,column=2,pady=20)
    label_vaccine.config(bg="#ffffff")
    label_vaccine.config(font=("Papyrus",11))

    vn=StringVar()
    vaccine_choose = ttk.Combobox(root,width=27,textvariable=vn,state="readonly")
    vaccine_choose['values'] =('Covishield','Covaxine','Sputnik V')
    vaccine_choose.grid(column=3,row=8)
    vaccine_choose.current()

    dose_var = StringVar()
    rb_dose_label = Label(root,text="Dose :")
    rb_dose_label.grid(row=9,column=2)
    rb_dose_label.config(bg="#ffffff")
    rb_dose_label.config(pady=15)
    rb_dose_label.config(font=("Papyrus",11))

    rb_dose_1= Radiobutton(root, text="1" ,variable=dose_var, value="1",borderwidth=0,font= ("Papyrus",11),padx = 20)
    rb_dose_1.grid(row=9,column=3)
    rb_dose_1.config(bg="#ffffff")
    rb_dose_1.config(activebackground="#ffffff")
    rb_dose_1.config(font=("Papyrus",11))

    rb_dose_2= Radiobutton(root, text="2" ,variable=dose_var, value="2",borderwidth=0,font= ("Papyrus",11),padx = 20)
    rb_dose_2.grid(row=9,column=4)
    rb_dose_2.config(bg="#ffffff")
    rb_dose_2.config(activebackground="#ffffff")
    rb_dose_2.config(font=("Papyrus",11))
    dose_var.set(0)

    label_center=Label(root,text="Center :")
    label_center.grid(row=10,column=2,pady=20)
    label_center.config(bg="#ffffff")
    label_center.config(font=("Papyrus",11))

    cn=StringVar()
    center_choose = ttk.Combobox(root,width=27,textvariable=cn,state="readonly")
    center_choose['values'] =('Peoples Collage of Nursing Center',
                              'GMC Hamidia',
                              'Memoral Hospital',
                              'Govt HSS Obedia School',
                              'JP Hospital',
                              'KNP Nursing Collage')
    center_choose.grid(column=3,row=10)
    center_choose.current()


    register_img = PhotoImage(file="icon/register.png")
    register_img_size = register_img.subsample(5,5)
    register_button = Button(root, image=register_img_size, command= insert_record)
    register_button.grid(column = 3,row = 11  )
    register_button.config(borderwidth=0)
    register_button.config(bg="#ffffff")
    register_button.config(activebackground="#ffffff")
       
    root.mainloop()

if __name__ == "__main__":
    run()

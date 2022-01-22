from tkinter import *
import tkinter as tk
import country_frame
import district_frame
import state_frame
import vaccination_info
from tkinter import messagebox


#global variables
var = ""
root = ""


def reset():
    global var
    return var.set(0)


def submit():
    global checkvar,var,root,submit_button
    open_frame = var.get()
    if checkvar.get() == 1:
        if open_frame == "Country":
            root.destroy()
            country_frame.run()   
        elif open_frame == "State":
            root.destroy()
            state_frame.run()
        elif open_frame == "District":
            root.destroy()
            district_frame.run()
        elif open_frame == "Vaccination":
            root.destroy()
            vaccination_info.run()
        else:
            messagebox.showwarning("Alert","Please Select the Option")

    else:
        messagebox.showwarning("Alert","Please Check the box")
def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Confirm Exit','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
            tk.messagebox.showinfo('Thank You!','Thank You For Using Our Application')
            root.destroy()

def run():
    global checkvar,var,root,submit_button
    root = tk.Tk()
    
    width = 800
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable('False','False')
    root.title("Covid-19 Tracker")
    root.configure(bg="#ffffff")
    f = ("Papyrus", 25, "bold")
    img = tk.PhotoImage(file="icon/covid.png")
    root.iconphoto(root,img)

    
    root.protocol("WM_DELETE_WINDOW", ExitApplication)

    title = tk.Label(text = "Coronavirus Tracker")

    # For Title image
    banner = tk.PhotoImage(file="icon/corona-virus.png")
    #banner_image = banner.subsample(3,3)
    bannerlabel = tk.Label(root, image=banner)
    bannerlabel.config(bd=0)
    bannerlabel.config(bg="#ffffff")
    bannerlabel.pack(pady=20)
    var = StringVar()
    checkvar = IntVar()
    frame= LabelFrame(root, text='Choose',borderwidth=0,font= ('Papyrus',10,"bold"))
    frame.pack(ipady=30,ipadx=20)
    frame.config(bg="#ffffff")

    rb = Radiobutton(frame, text="Country" ,variable=var, value="Country",borderwidth=0,font= ('Papyrus',10),padx = 20)
    rb.pack(anchor="w",ipadx=5,ipady=5)
    rb.config(bg="#ffffff")
    rb.config(activebackground="#ffffff")


    rb1 = Radiobutton(frame, text="State" ,variable=var, value="State",borderwidth=0,font= ('Papyrus',10),padx = 20)
    rb1.pack(anchor="w",ipadx=5,ipady=5)
    rb1.config(bg="#ffffff")
    rb1.config(activebackground="#ffffff")


    rb2 = Radiobutton(frame, text="District" ,variable=var, value="District",borderwidth=0,font= ('Papyrus',10),padx = 20)
    rb2.pack(anchor="w",ipadx=5,ipady=5)
    rb2.config(bg="#ffffff")
    rb2.config(activebackground="#ffffff")


    rb3= Radiobutton(frame, text="Vaccination" ,variable=var, value="Vaccination",borderwidth=0,font= ('Papyrus',10),padx = 20)
    rb3.pack(anchor="w",ipadx=5,ipady=5)
    rb3.config(bg="#ffffff")
    rb3.config(activebackground="#ffffff")

    check = Checkbutton(root,text= "Search result is applicable for india only",variable = checkvar, onvalue = 1, offvalue = 0)
    check.pack()
    check.config(bg="#ffffff")
    check.config(activebackground="#ffffff")
    check.config(font=("Papyrus",11))
    
    submit_img = tk.PhotoImage(file="icon/submit_button.png")
    submit_img_size = submit_img.subsample(7,7)
    submit_button = tk.Button(root,image=submit_img_size ,command=submit,borderwidth=2)
    submit_button.pack()
    submit_button.config(bg="#ffffff")
    submit_button.config(borderwidth=0)
    submit_button.config(activebackground="#ffffff")
    

    reset_img = tk.PhotoImage(file="icon/reset_button.png")
    reset_img_size = reset_img.subsample(7,7)
    reset_button = tk.Button(root,image=reset_img_size ,command=reset,borderwidth=2)
    reset_button.pack()
    reset_button.config(bg="#ffffff")
    reset_button.config(borderwidth=0)
    reset_button.config(activebackground="#ffffff")
    var.set(0)
    root.mainloop()



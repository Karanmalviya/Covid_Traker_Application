from tkinter import *
import sqlite3
import view_page
from tkinter import messagebox
import vaccination_info

#global varibles.
entry_name = ""
entry_mob = ""
root = ""

def back_to_main():
    root.destroy()
    vaccination_info.run()

def user_login():
    global entry_name,entry_mob,root
    userdata = ""
    try:
        con = sqlite3.connect('database/vaccination_record.db')
        cur = con.cursor()
        cur.execute("Select * from record where addhaar = :1 and mob = :2",(int(entry_name.get()),int(entry_mob.get())))
        
        userdata = cur.fetchone()
        cur.close()
        con.close()

        if userdata == None:
            messagebox.showerror("Alert","Data didn't match")
            return

    except Exception as ep:
        messagebox.showerror("Alert","Please Enter Addhaar or Mobile")
    else:
        messagebox.showinfo("Successfull Matached","Successfully Logged In")
        root.destroy()
        view_page.run(userdata)


def run():
    global entry_name,entry_mob,root
    root = Tk()
    root.title('Login')
    
    width = 600
    height = 370
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable('False','False')
    root.config(background='#FFFFFF')
    img = PhotoImage(file="icon/covid.png")
    root.iconphoto(root, img)
    void_space = Label(root,text="                    ")
    void_space.grid(row=0,column=1)
    void_space.config(bg="#ffffff")

    img_btn = PhotoImage(file="icon/back.png")
    img_size = img_btn.subsample(20, 20)
    back_button = Button(root, image=img_size, command=back_to_main)
    back_button.grid(row=0, column=0)
    back_button.config(bg="#ffffff")
    back_button.config(borderwidth=0)
    
    title = Label(root,text="Sign In for Vaccination")
    title.grid(row=1,column=3,pady=20)
    title.config(bg="#ffffff")
    title.config(font=("Papyrus",13,"bold"))
    title.config(fg='#297d5d')

    label_name=Label(root,text="Addhaar No. :")
    label_name.grid(row=3,column=2,pady=20)
    label_name.config(bg="#ffffff")
    label_name.config(font=("Papyrus",11))
    entry_name = Entry(root)
    entry_name.grid(row=3,column=3)
    entry_name.config(font=("Papyrus",11))
    entry_name.config(bd=2)


    label_mob=Label(root,text="Mob No. :")
    label_mob.grid(row=4,column=2,pady=20)
    label_mob.config(bg="#ffffff")
    label_mob.config(font=("Papyrus",11))
    entry_mob = Entry(root)
    entry_mob.grid(row=4,column=3)
    entry_mob.config(font=("Papyrus",11))
    entry_mob.config(bd=2)


    login_img = PhotoImage(file="icon/submit_button.png")
    login_img_size = login_img.subsample(5,5)
    login_button = Button(root, image=login_img_size, command= user_login)
    login_button.grid(column = 3,row = 5  )
    login_button.config(borderwidth=0)
    login_button.config(bg="#ffffff")
    login_button.config(activebackground="#ffffff")

    root.mainloop()

if __name__ == "__main__":
    run()

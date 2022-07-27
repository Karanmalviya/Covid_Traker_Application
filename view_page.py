from tkinter import *
import vaccination_info


# global variables
root = ""


def back_to_main():
    root.destroy()
    vaccination_info.run()


def run(data):
    global root
    root = Tk()
    root.title('Certificate')
    width = 700
    height = 470
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable('False','False')
    root.config(background='#FFFFFF')
    img = PhotoImage(file="icon/covid.png")
    root.iconphoto(root, img)

    img_btn = PhotoImage(file="icon/back.png")
    img_size = img_btn.subsample(20, 20)
    back_button = Button(root, image=img_size, command=back_to_main)
    back_button.grid(row=0, column=0)
    back_button.config(bg="#ffffff")
    back_button.config(borderwidth=0)

    void_space = Label(root,text="                    ")
    void_space.grid(row=0,column=1)
    void_space.config(bg="#ffffff")

    title = Label(root,text="Certificate for COVID -19 Vaccination")
    title.grid(row=0,column=3,columnspan=3,pady=10)
    title.config(bg="#ffffff")
    title.config(font=("Papyrus",13,'bold'))
    title.config(fg="#297d5d")


    b_title = Label(root,text="Beneficiary Details")
    b_title.grid(row=1,column=2)
    b_title.config(fg="#297d5d")
    b_title.config(bg="#ffffff")
    b_title.config(font=("Papyrus",11,'bold'))

    name,mob,add,age,gender,vac,dose,cen,date,time = data
    
    b_name_label = Label(root,text="Beneficiary Name : ")
    b_name_label.grid(row=2,column=2,sticky=W,pady=10)
    b_name_label.config(bg="#ffffff")
    b_name_label.config(font=("Papyrus",11))

    void_space1 = Label(root,text="                   ")
    void_space1.grid(row=2,column=3,sticky=W)
    void_space1.config(bg="#ffffff")
                 
    b_name_view = Label(root,text=f"{name}")
    b_name_view.grid(row=2,column=4,sticky=W)
    b_name_view.config(bg="#ffffff")
    b_name_view.config(font=("Papyrus",11))
                 
    b_age = Label(root,text="Age : ")
    b_age.grid(row=3,column=2,sticky=W)
    b_age.config(bg="#ffffff")
    b_age.config(font=("Papyrus",11))
                 
    b_age_view = Label(root,text=f"{age}")
    b_age_view.grid(row=3,column=4,sticky=W)
    b_age_view.config(bg="#ffffff")
    b_age_view.config(font=("Papyrus",11))
                 
    b_gender_label = Label(root,text="Gender : ")
    b_gender_label.grid(row=4,column=2,sticky=W)
    b_gender_label.config(bg="#ffffff")
    b_gender_label.config(font=("Papyrus",11))

    b_gender_view = Label(root,text=f"{gender}")
    b_gender_view.grid(row=4,column=4,sticky=W)
    b_gender_view.config(bg="#ffffff")
    b_gender_view.config(font=("Papyrus",11))

    b_id_label = Label(root,text="ID Verified : ")
    b_id_label.grid(row=5,column=2,sticky=W)
    b_id_label.config(bg="#ffffff")
    b_id_label.config(font=("Papyrus",11))

    b_id_view = Label(root,text=f"{add}")
    b_id_view.grid(row=5,column=4,sticky=W)
    b_id_view.config(bg="#ffffff")
    b_id_view.config(font=("Papyrus",11))

    v_title = Label(root,text="Vaccination Details")
    v_title.grid(row=7,column=2,sticky=W,pady=10)
    v_title.config(fg="#297d5d")
    v_title.config(bg="#ffffff")
    v_title.config(font=("Papyrus",11,'bold'))

        
    v_name = Label(root,text="Vaccine Name : ")
    v_name.grid(row=8,column=2,sticky=W)
    v_name.config(bg="#ffffff")
    v_name.config(font=("Papyrus",11))
                 
    v_name_view = Label(root,text=f"{vac}")
    v_name_view.grid(row=8,column=4,sticky=W)
    v_name_view.config(bg="#ffffff")
    v_name_view.config(font=("Papyrus",11))

    v_date = Label(root,text="Date of Dose : ")
    v_date.grid(row=9,column=2,sticky=W)
    v_date.config(bg="#ffffff")
    v_date.config(font=("Papyrus",11))

    v_date_view = Label(root,text=f"{dose} dose at {date}")
    v_date_view.grid(row=9,column=4,sticky=W)
    v_date_view.config(bg="#ffffff")
    v_date_view.config(font=("Papyrus",11))
                 
    v_center_label = Label(root,text="Vaccinated at : ")
    v_center_label.grid(row=10,column=2,sticky=W)
    v_center_label.config(bg="#ffffff")
    v_center_label.config(font=("Papyrus",11))             

    v_center_label_view = Label(root,text=f"{cen}")
    v_center_label_view.grid(row=10,column=4,sticky=W)
    v_center_label_view.config(bg="#ffffff")
    v_center_label_view.config(font=("Papyrus",11))
                 
    root.mainloop()
    

if __name__ == "__main__":
    run()
    

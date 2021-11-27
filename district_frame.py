import controller as use  
import tkinter as tk
from tkinter import ttk
import main
from tkinter import messagebox

#global varibles
root = ""
my_label = ""
n = ""
n1 = ""
state_choose = ""



def submit3():
    global n,n1,my_label,my_label1
    state_name = n.get()
    district_name = n1.get()
    if state_name == '' or district_name == '':
            messagebox.showerror("Alert","Please Select the Option")
    else:

            data = use.get_single_district_data_details(state_name, district_name)

            my_label1.configure(text=f"{district_name}", background='#FFFFFF',font=("Papyrus", 12))
            my_label1.config(font=("Papyrus", 12,"bold"))
            
            lbl_data = f"Active-case : {data['active']}\nConfirmed : {data['confirmed']}\nRecovered : {data['recovered']}\nDecrease : {data['deceased']}"
            my_label.configure(text=lbl_data, background='#FFFFFF',font=("Papyrus", 12))
            # lbl_title = "Name\tActive\tConfirmed\tRecovered"
            # ttk.Label(root, text=lbl_title,
            # font=("Times New Roman", 12)).grid(column=0,row=10, padx=10)

def combobox(e):
    global district_choose
    state_name = n.get()
    if state_name != '':
        obj2 = use.get_district_name_list(state_name)
        district_tuple = tuple(obj2)
        district_choose['values'] = district_tuple

def back_to_main():
    global root
    root.destroy()
    main.run()


def run():
    global n,n1,my_label,district_choose,root,my_label1
    root = tk.Tk()
    root.title('Distict Wise Cases')
    
    width = 600
    height = 470
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable('False','False')
    root.config(background = '#FFFFFF')
    img = tk.PhotoImage(file="icon/covid.png")
    root.iconphoto(root,img)
    img_btn = tk.PhotoImage(file="icon/back.png")
    img_size = img_btn.subsample(20,20)
    back_button = tk.Button(root, image=img_size, command= back_to_main)
    back_button.grid(row = 0 , column = 0)
    back_button.config(bg="#ffffff")
    back_button.config(borderwidth=0)
           
    label_t = tk.Label(root, text = "District Wise Search",background = '#ffffff', foreground ="#000000",font = ("Papyrus", 15),fg='#297d5d')
    label_t.grid(row = 0, column = 2)
    label_t.config(fg='#297d5d')

    ttk.Label(root, text = "Select the State :",background = '#FFFFFF',font = ("Papyrus", 12)).grid(column = 1,row = 5, padx = 10, pady = 25)
      
    # Combobox creation
    n = tk.StringVar()
    state_choose = ttk.Combobox(root, width = 27, textvariable = n,state='readonly')
      
    # Adding combobox drop down list
    state_choose['values'] = (
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Andaman and Nicobar Islands',
    'Bihar'	,
    'Chhattisgarh',
    'Delhi',
    'Goa'	,
    'Gujarat',	
    'Haryana',	
    'Himachal Pradesh' ,
    'Jharkhand',	
    'Karnataka',	
    'Kerala',	
    'Madhya Pradesh',
    'Maharashtra',	
    'Manipur',	
    'Meghalaya',	
    'Mizoram',		
    'Nagaland',	
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',	
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand', 
    'West Bengal',)
    state_choose.grid(column = 2, row = 5)
    state_choose.current()



    ttk.Label(root, text = "Select the District :",background = '#FFFFFF',
              font = ("Papyrus", 12)).grid(column = 1,
              row = 7, padx = 10, pady = 25)
    # Combobox creation of district
    n1 = tk.StringVar()
    district_choose = ttk.Combobox(root, width = 27, textvariable = n1,state='readonly')
      
    # Adding combobox drop down list
    district_choose['values'] = ()
    district_choose.grid(column = 2, row = 7)
    district_choose.current()

    district_choose.bind('<Button-1>', combobox)

    submit_img = tk.PhotoImage(file="icon/submit_button.png")
    submit_img_size = submit_img.subsample(6,6)
    submit_button1 = tk.Button(root, image=submit_img_size, command= submit3)
    submit_button1.grid(column = 2,row = 9  )
    submit_button1.config(borderwidth=0)
    submit_button1.config(bg="#ffffff")
    submit_button1.config(activebackground="#ffffff")

    my_label1 = tk.Label(root,bg="white")
    my_label1.grid(column=2,row=12)
    my_label1.configure(text=" ")
    
    my_label = tk.Label(root,bg="white")
    my_label.grid(column=2,row=16, padx=10, pady=20)
    my_label.configure(text=" ")

    root.mainloop()

import controller as use
import tkinter as tk
from tkinter import ttk
import main
from tkinter import messagebox



#global varibles
my_keys = ['active', 'confirmed', 'recovered', 'deceased']
listbox = ""
n = ""
root = ""


def submit2():
    global state_name
    if n.get() == '':
        messagebox.showerror("Alert","Please Select the option first")
    else:
        listbox.delete(0,tk.END)
        state_name = n.get()
        obj2 = use.get_district_data_details(state_name)
        cities = []
        for i in obj2:
            if type(i) == str:
                cities.append(" ")
                cities.append(f"             {i}")
                cities.append(" ")
            else:
                for j in i:
                    if j == "active":
                        cities.append(f"active : {i['active']}")
                    if j == "confirmed":
                        cities.append(f"confirmed : {i['confirmed']}")
                    if j == "recovered":
                        cities.append(f"recovered : {i['recovered']}")
                    if j == "deceased":
                        cities.append(f"deceased : {i['deceased']}")
        listbox.insert(tk.END, *cities)

def back_to_main():
    root.destroy()
    main.run()





def run():
    global root,n,listbox,state_name
    root = tk.Tk()
    root.title('StateWise Cases')
    
    width = 500
    height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable('False','False')
    root.config(bg="#ffffff")
    img = tk.PhotoImage(file="icon/covid.png")
    root.iconphoto(root,img)
    img_btn = tk.PhotoImage(file="icon/back.png")
    img_size = img_btn.subsample(20, 20)
    back_button = tk.Button(root, image=img_size, command=back_to_main)
    back_button.grid(row=0, column=0)
    back_button.config(bg="#ffffff")
    back_button.config(borderwidth=0)
    back_button.config(activebackground="#ffffff")


    label_t=tk.Label(root, text="State Wise Cases",background='#ffffff',fg='#297d5d', foreground="#000000",font=("Papyrus", 15))
    label_t.grid(row=0, column=2)
    label_t.config(fg='#297d5d')
    ttk.Label(root, text="Select the State :", background="#ffffff",font=("Papyrus", 10)).grid(column=1,row=5, padx=10, pady=25)

    # Combobox creation
    n = tk.StringVar()
    state_choose = ttk.Combobox(root, width=27, textvariable=n,state="readonly")

    # Adding combobox drop down list
    state_choose['values'] = (
        'Andhra Pradesh',
        'Arunachal Pradesh',
        'Assam',
        'Bihar',
        'Chhattisgarh',
        'Delhi',
        'Goa',
        'Gujarat',
        'Haryana',
        'Himachal',
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
        'West Bengal',
        'Andaman and Nicobar Islands')
    state_choose.grid(column=2, row=5)
    state_choose.current()


    submit_img = tk.PhotoImage(file="icon/submit_button.png")
    submit_img_size = submit_img.subsample(6,6)
    submit_button = tk.Button(root, image=submit_img_size, command=submit2)
    submit_button.grid(column=2, row=7)
    submit_button.config(borderwidth=0)
    submit_button.config(bg="#ffffff")
    submit_button.config(activebackground="#ffffff")

    yScroll = tk.Scrollbar(orient=tk.VERTICAL)
    yScroll.grid(row=10, column=3, sticky=tk.NW + tk.S)
    listbox = tk.Listbox(yscrollcommand=yScroll.set)
    listbox.grid(row=10, column=2, sticky=tk.N + tk.S + tk.E + tk.W)
    cities = ()
    listbox.insert(tk.END, *cities)
    listbox.config(borderwidth=0)
    yScroll['command'] = listbox.yview

    root.mainloop()

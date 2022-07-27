from tkinter import *
from tkinter import ttk
import main
import vaccination_registration
import login

#global variables
root = ""

def back_to_main():
    root.destroy()
    main.run()

    
def book_slot():
        root.destroy()
        vaccination_registration.run()
        
def view_book_slot():
       root.destroy()
       login.run()
        

def run():
    global root
    root = Tk()
    root.title("DashBoard")
    
    width = 550
    height = 250
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

    label_title=Label(root,text="Vaccination Booking")
    label_title.grid(row=0,column=3,pady=20,columnspan=4)
    label_title.config(bg="#ffffff")
    label_title.config(fg="#297d5d")

    label_title.config(font=("Papyrus",20,"bold"))

    void = Label(root,text="                          ")
    void.grid(row=3,column=1)
    void.config(bg="#ffffff")

    book_img = PhotoImage(file="icon/book_slot.png")
    book_img_size = book_img.subsample(6,6)
    book_slot_button = Button(root, image=book_img_size, command= book_slot)
    book_slot_button.grid(column = 3,row = 3  )
    book_slot_button.config(borderwidth=0)
    book_slot_button.config(bg="#ffffff")
    book_slot_button.config(activebackground="#ffffff")

    view_book_img = PhotoImage(file="icon/view_booking.png")
    view_book_img_size = view_book_img.subsample(6,6)
    view_booking_button = Button(root, image=view_book_img_size, command= view_book_slot)
    view_booking_button.grid(column = 4,row = 3  )
    view_booking_button.config(borderwidth=0)
    view_booking_button.config(bg="#ffffff")
    view_booking_button.config(activebackground="#ffffff")
    root.mainloop()
    
    
if __name__ == "__main__":
    run()

import socket
from tkinter import messagebox

def test_connection():
    try:
        socket.create_connection(('Google.com',80))
        return True
    except:
        messagebox.showerror("Internet lost","Internet Connection Not Found")
        return False
if test_connection():
    import main
    main.run()

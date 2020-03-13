from tkinter import *
from tkinter import messagebox

window = Tk()

window.iconbitmap(r'logo1.ico')
window.minsize('400' ,'200')
window.title("Dr.AIT UG Results")
window.configure(background="#fffdd0")
L1 = Label(window, text="Enter your USN:")
L1.pack(side = TOP, pady=20)

usn = StringVar()

btn = Button(window, text = 'Search').pack(side = BOTTOM, pady = 20)

E1 = Entry(window, bd =5, textvariable=usn)
E1.pack(side = BOTTOM, pady=20)
print(str(usn.get()))

window.mainloop()

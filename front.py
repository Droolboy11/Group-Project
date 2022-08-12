from tkinter import *
import ctypes
from functions import *

#window quality
ctypes.windll.shcore.SetProcessDpiAwareness(1)

main = Tk()
main.iconbitmap('D:\Aryan\Code\Group Project\school.ico')
main.title('SCHOOL MANAGEMENT SYSTEM')

#window size
main.state('zoomed')

#style
main.configure(background='#003865')

heading = Label(main, text='SCHOOL MANAGEMENT SYSTEM', font='Arial 50 bold underline', 
background='#003865',foreground='#D4F6CC')
heading.pack(anchor=CENTER, pady=10)

blank_space = Label(main, background='#003865')
blank_space.pack(pady=40)

student_btn = Button(main, text='Student Management', font='Helvetica 30 bold', fg='#EF5B0C',
command= lambda: StudentWindow(main))
student_btn.pack(anchor=CENTER, pady=25)

teacher_btn = Button(main, text='Teacher Management', font='Helvetica 30 bold', fg='#EF5B0C',
command= lambda: StaffWindow(main))
teacher_btn.pack(anchor=CENTER, pady=25)

infrastructure_btn = Button(main, text='Infrastructure Management', font='Helvetica 30 bold', fg='#EF5B0C',
command= lambda:Infrastructure(main))
infrastructure_btn.pack(anchor=CENTER, pady=25)

main.mainloop()
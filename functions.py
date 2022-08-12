from tkinter import ttk
from tkinter import *

def add(root,mode):
    window = Toplevel(root)
    window.title('SEARCH')
    window.geometry(f'{1080}x{290}')

    window.configure(background='#FEB139')
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)

    name = Label(window, text='Name:', pady=10)
    name_inp = Entry(window, font='Helvetica 20', pady=10)

    if mode == 'S':
        adm_no = Label(window, text='Admission no:', pady=10)
        adm_no_inp = Entry(window, font='Helvetica 20', pady=10)
        class_ = Label(window, text='Class:')
        class_inp = Entry(window, font='Helvetica 20')
        section = Label(window, text='Section:')
        section_inp = Entry(window, font='Helvetica 20')
        labels = [name, name_inp, adm_no, adm_no_inp, class_, class_inp, section, section_inp]
        
        for i in labels[::2]:
            i.configure(font='Helvetica 20', fg='#D61C4E', bg='#FEB139')

        for j in range(8):
            if j > 3:
                (labels[j]).grid(row=1, column=(j-4))
            else:
                (labels[j]).grid(row=0, column=j)

def searchwin(root, mode):
    window = Toplevel(root)
    window.title('SEARCH')
    window.geometry(f'{1080}x{290}')

    window.configure(background='#FEB139')
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    def search():
        pass

    def search():
        pass

    name = Label(window, text='Name:', font='Helvetica 30', fg='#D61C4E', bg='#FEB139')
    name.grid(row=0, column=0, sticky=EW, pady=10)

    name_inp = Entry(window, font='Helvetica 30')
    name_inp.grid(row=0, column=1)
    
    if mode == 'S':
        adm_no = Label(window, text='Admission no:', font='Helvetica 30', fg='#D61C4E', bg='#FEB139')
        adm_no.grid(row=1, column=0, sticky=EW)

        adm_no_inp = Entry(window, font='Helvetica 30')
        adm_no_inp.grid(row=1, column=1)

        S_search_btn = Button(window, text='SEARCH', font='Arial 20 bold', command= search)
        S_search_btn.grid(row=2, columnspan=2, pady=10)

    elif mode == 'T':
        subject = Label(window, text='Subject:', font='Helvetica 30', fg='#D61C4E', bg='#FEB139')
        subject.grid(row=1, column=0, sticky=EW)

        subject_inp = Entry(window, font='Helvetica 30')
        subject_inp.grid(row=1, column=1)

        T_search_btn = Button(window, text='SEARCH', font='Arial 20 bold', command= search)
        T_search_btn.grid(row=2, columnspan=2, pady=10)
    
    pass

def select(a, tree):
        """Returns value of selected item in treeview"""
        curItem = tree.focus()
        value = (tree.item(curItem, 'values'))
        return value

def StudentWindow(root):
    main = Toplevel(root)
    main.title('STUDENT MANAGEMENT SYSTEM')
    main.iconbitmap('D:\Aryan\Code\Group Project\student.ico')
    main.state('zoomed')

    #Style
    main.configure(background='#ECE5C7')
    s = ttk.Style()
    s.theme_use("clam")
    s.configure('Treeview.Heading', font='Bahnschrift 30 bold', rowheight=70) #Heading height
    s.configure('Treeview', font='Arial 20', rowheight=50, background="#ECE5C7", 
    fieldbackground="#ECE5C7") #Row Height
    s.configure('TButton', font='Arial 20 bold') #Buttons
    main.columnconfigure(0, weight=1)
    main.columnconfigure(1, weight=1)
    main.columnconfigure(2, weight=1)
    main.columnconfigure(3, weight=1)

    heading = Label(main, text='STUDENT MANAGEMENT SYSTEM', font='Arial 50 bold underline', 
    background='#ECE5C7',foreground='#D61C4E')
    heading.grid(row=0, columnspan=4, pady=20)

    tree = ttk.Treeview(main, columns=('c1','c2','c3','c4','c5'), show='headings', height=12, 
    selectmode='browse')
    
    #selected data
    tree.bind('<<TreeviewSelect>>', select('',tree))

    tree.column("# 1",anchor=CENTER, stretch=NO, width=215)
    tree.heading("# 1", text="Adm no")
    
    tree.column("# 2",anchor=CENTER, stretch=NO, width=600)
    tree.heading("# 2", text='Name')
    
    tree.column("# 3",anchor=CENTER, stretch=YES, width=230)
    tree.heading("# 3", text='Class')
    
    tree.column("# 4",anchor=CENTER, stretch=YES, width=250)
    tree.heading("# 4", text="Section")

    tree.column("# 5",anchor=CENTER, stretch=YES, width=500)
    tree.heading("# 5", text="Fees")

    tree.grid(row=1, columnspan=4)

    add_btn = ttk.Button(main, text='ADD', command= lambda: add(main,'S'))
    add_btn.grid(row=2, column=0, pady=10)

    update_btn = ttk.Button(main, text='UPDATE')
    update_btn.grid(row=2, column=1, pady=10)

    search_btn = ttk.Button(main, text='SEARCH', command= lambda: searchwin(main,'S'))
    search_btn.grid(row=2, column=2, pady=10)

    delete_btn = ttk.Button(main, text='DELETE')
    delete_btn.grid(row=2, column=3, pady=10)
    main.mainloop()

def StaffWindow(root):
    main = Toplevel(root)
    main.title('STAFF MANAGEMENT SYSTEM')
    main.iconbitmap(r'D:\Aryan\Code\Group Project\teacher.ico')
    main.state('zoomed')

    def class_teachers():
        window_ct = Toplevel(main)
        window_ct.title('CLASS TEACHERS')
        window_ct.state('zoomed')
        
        window_ct.configure(background='#ECE5C7')

        s_ct = ttk.Style()
        s_ct.theme_use("clam")
        s_ct.configure('Treeview.Heading', font='Bahnschrift 30 bold', rowheight=70) #Heading height
        s_ct.configure('Treeview', font='Arial 20', rowheight=50, background="#ECE5C7", 
        fieldbackground="#ECE5C7") #Row Height

        tree_ct = ttk.Treeview(window_ct, columns=('c1','c2','c3'), show='headings', height=17)

        tree_ct.column("# 1",anchor=CENTER, stretch=NO, width=600)
        tree_ct.heading("# 1", text="Name")
        
        tree_ct.column("# 2",anchor=CENTER, stretch=NO, width=600)
        tree_ct.heading("# 2", text='Subject')
        
        tree_ct.column("# 3",anchor=CENTER, stretch=YES, width=300)
        tree_ct.heading("# 3", text="Class")

        tree_ct.pack(pady=10)
    
    def group_d():
        window_d = Toplevel(main)
        window_d.title('CLASS TEACHERS')
        window_d.state('zoomed')
        
        window_d.configure(background='#ECE5C7')

        s = ttk.Style()
        s.theme_use("clam")
        s.configure('Treeview.Heading', font='Bahnschrift 30 bold', rowheight=70) #Heading height
        s.configure('Treeview', font='Arial 20', rowheight=50, background="#ECE5C7", 
        fieldbackground="#ECE5C7") #Row Height

        tree_d = ttk.Treeview(window_d, columns=('c1','c2'), show='headings', height=17)

        tree_d.column("# 1",anchor=CENTER, stretch=NO, width=600)
        tree_d.heading("# 1", text="Name")
        
        tree_d.column("# 2",anchor=CENTER, stretch=NO, width=600)
        tree_d.heading("# 2", text='Job')

        tree_d.pack(pady=10)

    #Style
    main.configure(background='#ECE5C7')
    s = ttk.Style()
    s.theme_use("clam")
    s.configure('Treeview.Heading', font='Bahnschrift 30 bold', rowheight=70) #Heading height
    s.configure('Treeview', font='Arial 20', rowheight=50, background="#ECE5C7", 
    fieldbackground="#ECE5C7") #Row Height
    s.configure('TButton', font='Arial 20 bold') #Buttons
    main.columnconfigure(0, weight=1)
    main.columnconfigure(1, weight=1)
    main.columnconfigure(2, weight=1)
    main.columnconfigure(3, weight=1)

    heading = Label(main, text='STAFF MANAGEMENT SYSTEM', font='Arial 50 bold underline', 
    background='#ECE5C7',foreground='#D61C4E')
    heading.grid(row=0, columnspan=3, pady=20)

    tree = ttk.Treeview(main, columns=('c1','c2','c3'), show='headings', height=11, 
    selectmode='browse')
    
    #selected data
    tree.bind('<<TreeviewSelect>>', select)

    tree.column("# 1",anchor=CENTER, stretch=NO, width=600)
    tree.heading("# 1", text="Name")
    
    tree.column("# 2",anchor=CENTER, stretch=NO, width=600)
    tree.heading("# 2", text='Subject')
    
    tree.column("# 3",anchor=CENTER, stretch=YES, width=600)
    tree.heading("# 3", text="Qualification")

    tree.grid(row=1, columnspan=3)

    ct_btn = ttk.Button(main, text='CLASS TEACHERS', command=class_teachers)
    ct_btn.grid(row=2, column=0, pady=10)

    grpd_btn = ttk.Button(main, text='GROUP-D WORKERS', command=group_d)
    grpd_btn.grid(row=2, column=1, pady=10)

    add_btn = ttk.Button(main, text='ADD', command= lambda: add(main, 'T'))
    add_btn.grid(row=2, column=2, pady=10)

    update_btn = ttk.Button(main, text='UPDATE')
    update_btn.grid(row=3, column=0, pady=10)

    search_btn = ttk.Button(main, text='SEARCH', command= lambda:searchwin(main, 'T'))
    search_btn.grid(row=3, column=1, pady=10)

    delete_btn = ttk.Button(main, text='DELETE')
    delete_btn.grid(row=3, column=2, pady=10)
    
    main.mainloop()

def Infrastructure(root):
    main = Toplevel(root)
    main.title('INFRASTRUCTURE')
    main.iconbitmap(r'D:\Aryan\Code\Group Project\infra.ico')
    main.state('zoomed')
    
    main.configure(background='#ECE5C7')
    main.columnconfigure(0, weight=1)

    heading = Label(main, text='INFRASTRUCTURE MANAGEMENT \nSYSTEM', font='Arial 50 bold underline', 
    background='#ECE5C7',foreground='#D61C4E')
    heading.grid(row=0, pady=10)



    main.mainloop()
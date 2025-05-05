from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3 as sq
from tkinter import messagebox
import datetime

window = Tk()
window.geometry("1360x700")
window.title("Library Management System")
icon = PhotoImage(file = "R:\\Library Management System\\logo.png")
window.iconphoto(True, icon)

frame = Frame(window)
frame.place(relx = 0.015, rely = 0.015)

img = ImageTk.PhotoImage(Image.open("R:\\Library Management System\\books_lib.jpg"))

label = Label(frame, image = img)
label.pack(padx = 15, pady = 15)

def Addbook():
    Newwin = Toplevel()
    Newwin.geometry("400x200")
    Newwin.title("Adding a book to Library")
    icon = PhotoImage(file = "R:\\Library Management System\\logo.png")
    Newwin.iconphoto(True, icon)

    connection = sq.connect("library.db")
    c = connection.cursor()
    
    c.execute("""CREATE TABLE if not exists books (bookid text,title text,author text)""")

    connection.commit()
    connection.close()
    
    bookid = Entry(Newwin, width = 30)
    bookid.grid(row = 0, column = 1,padx = 20,pady = 5)
    title = Entry(Newwin, width = 30)
    title.grid(row = 1, column = 1,padx = 20,pady = 5)
    author = Entry(Newwin, width = 30)
    author.grid(row = 2, column = 1,padx = 20,pady = 5)

    bookid_label = Label(Newwin, text = "Book ID :")
    bookid_label.grid(row = 0, column = 0, padx = 20, pady = 5)
    title_label = Label(Newwin, text = "Book Title :")
    title_label.grid(row = 1, column = 0, padx = 20, pady = 5)
    author_label = Label(Newwin, text = "Author :")
    author_label.grid(row = 2, column = 0, padx = 20,pady = 5)

    def submit():
        connection = sq.connect("library.db")
        c = connection.cursor()
    
        c.execute("INSERT INTO books VALUES (:bookid, :title, :author)",
                  {'bookid': bookid.get(),
                   'title': title.get(),
                   'author':author.get()
                   }
                  )
        connection.commit()
        connection.close()

        bookid.delete(0, END)
        title.delete(0, END)
        author.delete(0, END)

    def cancel():
        bookid.delete(0, END)
        title.delete(0, END)
        author.delete(0, END)
    
    submitbtn = Button(Newwin, text ="Submit", command = submit)
    submitbtn.grid(row = 3,
                   column = 0,
                   columnspan = 2,
                   ipadx = 100,
                   padx = 10,
                   pady = 5,
                   )

    cancelbtn = Button(Newwin, text ="Cancel", command = cancel)
    cancelbtn.grid(row = 4,
                   column = 0,
                   columnspan = 2,
                   ipadx = 100,
                   padx = 10,
                   pady = 5,
                   )

def Viewbook():
    Newwin = Toplevel()
    Newwin.geometry("800x400")
    Newwin.title("Viewing books in Library")
    icon = PhotoImage(file = "R:\\Library Management System\\logo.png")
    Newwin.iconphoto(True, icon)

    style = ttk.Style()

    style.theme_use('default')
    style.configure("Treeview",
                    background = "#D3D3D3",
                    foreground = "black",
                    rowheight = 25,
                    fieldbackground = "D3D3D3")
    style.map('Treeview',
              background = [('selected', "#347083")])
    tree_frame = Frame(Newwin)
    tree_frame.pack(pady=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)

    my_tree = ttk.Treeview(tree_frame,
                           yscrollcommand = tree_scroll.set,
                           selectmode = "extended")
    my_tree.pack()

    tree_scroll.config(command = my_tree.yview)
    my_tree['columns'] = ("Serial No","Book ID","Title","Author")

    my_tree.column("#0",width = 0,stretch = NO)
    my_tree.column("Serial No", anchor = W,width = 80)
    my_tree.column("Book ID", anchor = W,width = 80)
    my_tree.column("Title", anchor = W,width = 250)
    my_tree.column("Author", anchor  = W,width = 250)

    my_tree.heading("#0", text = '', anchor = W)
    my_tree.heading("Serial No", text = 'Serial No', anchor = W)
    my_tree.heading("Book ID", text = 'Book ID', anchor = W)
    my_tree.heading("Title", text = 'Title', anchor = W)
    my_tree.heading("Author", text = 'Author', anchor = W)
    
    
    connection = sq.connect("library.db")
    c = connection.cursor()
    
    c.execute('''SELECT rowid,* FROM books''')
    records = c.fetchall()

    for record in records:
        my_tree.insert(parent = '',index = 'end', text = '',values = (record[0],record[1],record[2],record[3]))

    connection.commit()
    connection.close()

def Updatebook():
    Newwin = Toplevel()
    Newwin.geometry("350x250")
    Newwin.title("Updating a book")
    icon = PhotoImage(file = "R:\\Library Management System\\logo.png")
    Newwin.iconphoto(True, icon)

    serial_no = Entry(Newwin, width = 30)
    serial_no.grid(row = 0, column = 1, padx = 20, pady = 5)
    bookid = Entry(Newwin, width = 30)
    bookid.grid(row = 1, column = 1, padx = 20, pady = 5)
    title = Entry(Newwin, width = 30)
    title.grid(row = 2, column = 1, padx = 20, pady = 5)
    author = Entry(Newwin, width = 30)
    author.grid(row = 3, column = 1, padx = 20, pady = 5)

    serial_label = Label(Newwin, text = "Serial No. :")
    serial_label.grid(row = 0, column = 0, padx = 20, pady = 5)
    bookid_label = Label(Newwin, text = "Book ID :")
    bookid_label.grid(row = 1, column = 0, padx = 20, pady = 5)
    title_label = Label(Newwin, text = "Book Title :")
    title_label.grid(row = 2, column = 0, padx = 20, pady = 5)
    author_label = Label(Newwin, text = "Author :")
    author_label.grid(row = 3, column = 0, padx = 20, pady = 5)

    def submit():
        connection = sq.connect("library.db")
        c = connection.cursor()
        c.execute("""UPDATE books SET bookid = :bookid,
            title = :title,
            author = :author
            WHERE rowid = :row""",
                  {'bookid':bookid.get(),
                   'title':title.get(),
                   'author':author.get(),
                   'row':serial_no.get(),
                   })
        connection.commit()
        connection.close()

        serial_no.delete(0,END)
        bookid.delete(0, END)
        title.delete(0, END)
        author.delete(0, END)
    def cancel():
        serial_no.delete(0,END)
        bookid.delete(0, END)
        title.delete(0, END)
        author.delete(0, END)
        
    submitbtn = Button(Newwin, text ="Submit", command = submit)
    submitbtn.grid(row = 4,
                   column = 0,
                   columnspan = 2,
                   ipadx = 100,
                   padx = 10,
                   pady = 10,
                   )

    cancelbtn = Button(Newwin, text ="Cancel", command = cancel)
    cancelbtn.grid(row = 5,
                   column = 0,
                   columnspan = 2,
                   ipadx = 100,
                   padx = 10,
                   pady = 10,
                   )

def Issuebook():
    Newwin = Toplevel()
    Newwin.geometry("350x250")
    Newwin.title("Issuing a book to Student")
    icon = PhotoImage(file = "R:\\Library Management System\\logo.png")
    Newwin.iconphoto(True, icon)

    Title_of_book = Entry(Newwin, width = 30)
    Title_of_book.grid(row = 0, column = 1, padx = 20, pady = 5)
    Student_name = Entry(Newwin, width = 30)
    Student_name.grid(row = 1, column = 1, padx = 20, pady = 5)
    Phone = Entry(Newwin, width = 30)
    Phone.grid(row = 2, column = 1, padx = 20, pady = 5)
    Address = Entry(Newwin, width = 30)
    Address.grid(row = 3, column = 1, padx = 20, pady = 5)

    Title_of_book_label = Label(Newwin, text = "Title of book :")
    Title_of_book_label.grid(row = 0, column = 0, padx = 20, pady = 5)
    Student_name_label = Label(Newwin, text = "Student Name :")
    Student_name_label.grid(row = 1, column = 0, padx = 20, pady = 5)
    Phone_label = Label(Newwin, text = "Phone :")
    Phone_label.grid(row = 2, column = 0, padx = 20, pady = 5)
    Address_label = Label(Newwin, text = "Address :")
    Address_label.grid(row = 3, column = 0, padx = 20, pady = 5)

    connection = sq.connect("library.db")
    c = connection.cursor()
    
    c.execute("""CREATE TABLE if not exists books_issued (Title_of_Book text,
        Student_Name text,
        Issued_Date TIMESTAMP,
        Return_Date TIMESTAMP,
        Phone text,
        Address text)""")

    connection.commit()
    connection.close()

    def submit():
        connection = sq.connect("library.db",detect_types = sq.PARSE_DECLTYPES | sq.PARSE_COLNAMES)
        c = connection.cursor()

        c.execute("""INSERT INTO books_issued (Title_of_Book,Student_Name,
                Issued_Date,
                Phone,
                Address) VALUES (:tob,:sn,:isd,:ph,:ad)""",
                  {'tob' : Title_of_book.get(),
                   'sn': Student_name.get(),
                   'isd': datetime.datetime.now(),
                   'ph': Phone.get(),
                   'ad': Address.get()
                   })

        connection.commit()
        connection.close()

        Title_of_book.delete(0,END)
        Student_name.delete(0,END)
        Phone.delete(0,END)
        Address.delete(0,END)

    def cancel():
        Title_of_book.delete(0,END)
        Student_name.delete(0,END)
        Phone.delete(0,END)
        Address.delete(0,END)

    submitbtn = Button(Newwin, text ="Submit", command = submit)
    submitbtn.grid(row = 4,
                   column = 0,
                   columnspan = 2,
                   ipadx = 100,
                   padx = 10,
                   pady = 10,
                   )
    cancelbtn = Button(Newwin, text ="Cancel", command = cancel)
    cancelbtn.grid(row = 5,
                   column = 0,
                   columnspan = 2,
                   ipadx = 100,
                   padx = 10,
                   pady = 10,
                   )

def Returnbook():
    Newwin = Toplevel()
    Newwin.geometry("1200x500")
    Newwin.title("Returning a book to Library")
    icon = PhotoImage(file = "R:\\Library Management System\\logo.png")
    Newwin.iconphoto(True, icon)

    style = ttk.Style()

    style.theme_use('default')
    style.configure("Treeview",
                    background = "#D3D3D3",
                    foreground = "black",
                    rowheight = 25,
                    fieldbackground = "D3D3D3")
    style.map('Treeview',
              background = [('selected', "#347083")])
    tree_frame = Frame(Newwin)
    tree_frame.pack(pady=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)

    my_tree = ttk.Treeview(tree_frame,
                           yscrollcommand = tree_scroll.set,
                           selectmode = "extended")
    my_tree.pack()

    tree_scroll.config(command = my_tree.yview)
    
    my_tree['columns'] = ("Serial No.","Title of Book","Student Name","Issued Date","Return Date","Phone","Address")

    my_tree.column("#0",width = 0,stretch = NO)
    my_tree.column("Serial No.", anchor = W,width = 55)
    my_tree.column("Title of Book", anchor = W,width = 200)
    my_tree.column("Student Name", anchor = W,width = 150)
    my_tree.column("Issued Date", anchor = W,width = 150)
    my_tree.column("Return Date", anchor  = W,width = 150)
    my_tree.column("Phone", anchor  = W,width = 150)
    my_tree.column("Address", anchor  = W,width = 250)

    my_tree.heading("#0", text = '', anchor = W)
    my_tree.heading("Serial No.", text = 'Serial No.', anchor = W)
    my_tree.heading("Title of Book", text = 'Title of Book', anchor = W)
    my_tree.heading("Student Name", text = 'Student Name', anchor = W)
    my_tree.heading("Issued Date", text = 'Issued Date', anchor = W)
    my_tree.heading("Return Date", text = 'Return Date', anchor = W)
    my_tree.heading("Phone", text = 'Phone', anchor = W)
    my_tree.heading("Address", text = 'Address', anchor = W)

    connection = sq.connect("library.db",detect_types = sq.PARSE_DECLTYPES | sq.PARSE_COLNAMES)
    c = connection.cursor()

    c.execute("SELECT oid,* FROM books_issued")
    records = c.fetchall()

    for record in records:
        my_tree.insert(parent = '',index = 'end', text = '',values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6]))

    connection.commit()
    connection.close()

    def Return_btn():
        connection = sq.connect("library.db",detect_types = sq.PARSE_DECLTYPES | sq.PARSE_COLNAMES)
        c = connection.cursor()

        c.execute("""UPDATE books_issued SET Return_Date = :rd WHERE oid = :oid""",
                  {'rd': datetime.datetime.now(),
                   'oid':serial_no.get()})

        connection.commit()
        connection.close()
        serial_no.delete(0,END)
    def select_record(e):
        serial_no.delete(0,END)
        selected = my_tree.focus()

        values = my_tree.item(selected,'values')

        serial_no.insert(0,values[0])

    def delete_all():
        user_response = messagebox.askyesno("Are you sure?",
                                            "All the existing data will be lost. Do you still want to continue?")

        if user_response == 1:
            connection = sq.connect("library.db")
            c = connection.cursor()

            c.execute("DROP TABLE books_issued")

            connection.commit()
            connection.close()
        else:
            pass

    my_tree.bind("<ButtonRelease-1>",select_record)
    data_frame = LabelFrame(Newwin,text = "Selected Record & Commands")
    data_frame.pack(fill = "x", expand = "yes",padx = 5)

    serial_no_label = Label(data_frame, text = "Serial No. :")
    serial_no_label.grid(row = 0, column = 0, padx = 10, pady = 10)

    serial_no = Entry(data_frame)
    serial_no.grid(row = 0, column = 1, padx = 10, pady = 10)

    return_btn = Button(data_frame, text ="Return",height = 1,width = 10, command = Return_btn)
    return_btn.grid(row = 1, column = 1, columnspan = 5,ipadx = 100,padx = 10, pady = 10)

    delete_all_records = Button(data_frame, text = "Delete All Records",height = 1,width = 10, command = delete_all)
    delete_all_records.grid(row = 2, column = 1, columnspan = 2,ipadx = 100,padx = 10, pady = 10)
#    my_tree.delete(*my_tree.get_children())

def Deletebook():
    Newwin = Toplevel()
    Newwin.geometry("400x200")
    Newwin.title("Deleting a book from Library")
    icon = PhotoImage(file = "R:\\Library Management System\\logo.png")
    Newwin.iconphoto(True, icon)

    serial_no = Entry(Newwin, width = 30)
    serial_no.grid(row = 0, column = 1,padx = 20,pady = 5)
    
    serial_label = Label(Newwin, text = "Serial No.")
    serial_label.grid(row = 0, column = 0,padx = 20,pady = 5)

    def deleterecord():
        connection = sq.connect("library.db")
        c = connection.cursor()

        c.execute("DELETE FROM books WHERE rowid =" + serial_no.get())

        serial_no.delete(0,END)
        
        connection.commit()
        connection.close()
    def canceldelete():
        serial_no.delete(0,END)

    def deleteall():
        user_response = messagebox.askyesno("Are you sure?",
                                            "All the existing data will be lost. Do you still want to continue?")

        if user_response == 1:
            connection = sq.connect("library.db")
            c = connection.cursor()

            c.execute("DROP TABLE books")

            connection.commit()
            connection.close()
        else:
            pass
        
        
    delete_button = Button(Newwin,
                           text = 'Delete',
                           height = 1,
                           width = 10,
                           command = deleterecord)
    delete_button.grid(row = 1,column = 0,columnspan = 2,ipadx = 100,padx = 10,pady = 5)

    cancel_button = Button(Newwin,
                           text = 'Cancel',
                           height = 1,
                           width = 10,
                           command = canceldelete)
    cancel_button.grid(row = 2,column = 0,columnspan = 2,ipadx = 100,padx = 10,pady = 5)

    delete_all_button = Button(Newwin,
                               text = 'Delete All records',
                               height = 1,
                               width = 10,
                               command = deleteall)
    delete_all_button.grid(row = 3,column = 0,columnspan = 2,ipadx = 100,padx = 10,pady = 5)
    

titleLabel = Label(window,
                   text = "Welcome to \nLibrary Management System",
                   font =("Arial",20,"bold")).pack(padx = 20, pady = 45)

Addbutton = Button(window,
                   text= "Add books",
                   height = 2,
                   width = 30,
                   command = Addbook,
                   font = ("ComicSans", 12,"bold")).pack(padx = 10, pady = 10)

Viewbutton = Button(window,
                    text = "View Books",
                    height = 2,
                    width = 30,
                    command = Viewbook,
                    font = ("ComicSans", 12,"bold")).pack(padx = 10, pady = 10)

Updatebutton = Button(window,
                      text = "Update Books",
                      height = 2,
                      width = 30,
                      command = Updatebook,
                      font = ("ComicSans", 12,"bold")).pack(padx = 10, pady = 10)

Issuebutton = Button(window,
                     text = "Issue Books",
                     height = 2,
                     width = 30,
                     command = Issuebook,
                     font = ("ComicSans", 12,"bold")).pack(padx = 10, pady = 10)

Returnbutton = Button(window,
                      text = "Return Books",
                      height = 2,
                      width = 30,
                      command = Returnbook,
                      font = ("ComicSans", 12,"bold")).pack(padx = 10, pady = 10)

Deletebutton = Button(window,
                      text = "Delete Books",
                      height = 2,
                      width = 30,
                      command = Deletebook,
                      font = ("ComicSans", 12,"bold")).pack(padx = 10, pady = 10)

Quitbutton = Button(window, text = "Quit",
                    height = 2,
                    width = 30,
                    command = window.destroy,
                    font = ("ComicSans", 12,"bold")).pack(padx = 10, pady = 10)

window.mainloop()
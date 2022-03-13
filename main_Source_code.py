from tkinter import *
import sqlite3
from tkinter import messagebox
import tkinter
#main frame
root = Tk()
root.geometry("400x690")
root.title("Sqlite3 Project")

#connect to db
def connectdb():
    try:
        global con, c
        con = sqlite3.connect('SHOP.db')
        c = con.cursor()
    except:
        messagebox.showwarning(
            "error", "Error while create or connecting to the database")

#create tabels
def createtb():
    try:
        connectdb()
        c.execute("""CREATE TABLE cashier (
        id integer primary key,
        name text,
        shift text
        )""")
        c.execute("""CREATE TABLE shelfer (
        id integer primary key,
        name text,
        shift text
        )""")
        c.execute("""CREATE TABLE boss (
        id integer primary key,
        name text
        )""")
        c.execute("""CREATE TABLE customer (
        id integer primary key,
        name text,
        address text,
        phone text
        )""")
        c.execute("""CREATE TABLE item (
        id integer primary key,
        name text,
        price integer
        )""")
        c.execute("""CREATE TABLE history_buy (
        id integer primary key,
        date integer,
        buyer integer,
        item integer,
        foreign key (item) references item(id),
        foreign key (buyer) references customer(id)
        )""")
        c.execute("""CREATE TABLE history_salary (
        id integer primary key,
        boss integer,
        salary integer,
        date integer,
        foreign key (boss) references boss(id)
        )""")
        con.commit()
        con.close()
        messagebox.showinfo("Congratulations", "tables was created")
    except:
        messagebox.showwarning("error", "Error while creating tables")

#delete all tabels
def deletetb():
    try:
        connectdb()
        c.execute('''DROP TABLE cashier''')
        c.execute('''DROP TABLE shelfer''')
        c.execute('''DROP TABLE boss''')
        c.execute('''DROP TABLE customer''')
        c.execute('''DROP TABLE item''')
        c.execute('''DROP TABLE history_buy''')
        c.execute('''DROP TABLE history_salary''')
        con.commit()
        con.close()
        messagebox.showinfo("Congratulations", "database was deleted")
    except:
        messagebox.showwarning("error", "Error while deleting database")

#insert record into tabels
def insertf():
    def aprove(queryx):
        connectdb()
        c.execute(queryx)
        con.commit()
        con.close()
        winsecond.destroy()

    def cashier():
        global winsecond
        winsecond = Toplevel(tkinsert)
        namevar = tkinter.StringVar()
        shiftvar = tkinter.StringVar()
        winsecond.title("Add Cashier")
        winsecond.geometry("200x200")
        Frame1 = Frame(winsecond)
        Frame1.grid(row=0)
        Frame2 = Frame(winsecond)
        Frame2.grid(row=1)
        Frame3 = Frame(winsecond)
        Frame3.grid(row=2)
        name_lab = Label(Frame1, text="Name : ").pack(
            side=LEFT, padx=5, pady=5)
        name_ent = Entry(Frame1, textvariable=namevar).pack(
            side=RIGHT, padx=5, pady=5)
        shift_lab = Label(Frame2, text="shift : ").pack(
            side=LEFT, padx=5, pady=5)
        shift_ent = Entry(Frame2, textvariable=shiftvar).pack(
            side=RIGHT, padx=5, pady=5)
        submit_but = Button(Frame3, text="Submit", command=lambda: aprove(f'''insert 
        into cashier(name,shift) values('{namevar.get()}','{shiftvar.get()}')''')).pack(padx=5, pady=5)

    def shelfer():
        global winsecond
        winsecond = Toplevel(tkinsert)
        namevar = tkinter.StringVar()
        shiftvar = tkinter.StringVar()
        winsecond.title("Add Shelfer")
        winsecond.geometry("200x200")
        Frame1 = Frame(winsecond)
        Frame1.grid(row=0)
        Frame2 = Frame(winsecond)
        Frame2.grid(row=1)
        Frame3 = Frame(winsecond)
        Frame3.grid(row=2)
        name_lab = Label(Frame1, text="Name : ").pack(
            side=LEFT, padx=5, pady=5)
        name_ent = Entry(Frame1, textvariable=namevar).pack(
            side=RIGHT, padx=5, pady=5)
        shift_lab = Label(Frame2, text="shift : ").pack(
            side=LEFT, padx=5, pady=5)
        shift_ent = Entry(Frame2, textvariable=shiftvar).pack(
            side=RIGHT, padx=5, pady=5)
        submit_but = Button(Frame3, text="Submit", command=lambda: aprove(f'''insert 
        into shelfer(name,shift) values('{namevar.get()}','{shiftvar.get()}')''')).pack(padx=5, pady=5)

    def customer():
        global winsecond
        winsecond = Toplevel(tkinsert)
        namevar = tkinter.StringVar()
        addressvar = tkinter.StringVar()
        phonevar = tkinter.StringVar()
        winsecond.title("Add Customer")
        winsecond.geometry("200x200")
        Frame1 = Frame(winsecond)
        Frame1.grid(row=0)
        Frame2 = Frame(winsecond)
        Frame2.grid(row=1)
        Frame3 = Frame(winsecond)
        Frame3.grid(row=2)
        Frame4 = Frame(winsecond)
        Frame4.grid(row=3)
        name_lab = Label(Frame1, text="Name : ").pack(
            side=LEFT, padx=5, pady=5)
        name_ent = Entry(Frame1, textvariable=namevar).pack(
            side=RIGHT, padx=5, pady=5)
        address_lab = Label(Frame2, text="address : ").pack(
            side=LEFT, padx=5, pady=5)
        address_ent = Entry(Frame2, textvariable=addressvar).pack(
            side=RIGHT, padx=5, pady=5)
        phone_lab = Label(Frame3, text="phone : ").pack(
            side=LEFT, padx=5, pady=5)
        phone_ent = Entry(Frame3, textvariable=phonevar).pack(
            side=RIGHT, padx=5, pady=5)
        submit_but = Button(Frame4, text="Submit", command=lambda: aprove(f'''insert 
        into customer(name,address,phone) values('{namevar.get()}','{addressvar.get()}','{phonevar.get()}')''')).pack(padx=5, pady=5)

    def item():
        global winsecond
        winsecond = Toplevel(tkinsert)
        namevar = tkinter.StringVar()
        pricevar = tkinter.StringVar()
        winsecond.title("Add Item")
        winsecond.geometry("200x200")
        Frame1 = Frame(winsecond)
        Frame1.grid(row=0)
        Frame2 = Frame(winsecond)
        Frame2.grid(row=1)
        Frame3 = Frame(winsecond)
        Frame3.grid(row=2)
        name_lab = Label(Frame1, text="Name : ").pack(
            side=LEFT, padx=5, pady=5)
        name_ent = Entry(Frame1, textvariable=namevar).pack(
            side=RIGHT, padx=5, pady=5)
        shift_lab = Label(Frame2, text="Price : ").pack(
            side=LEFT, padx=5, pady=5)
        shift_ent = Entry(Frame2, textvariable=pricevar).pack(
            side=RIGHT, padx=5, pady=5)
        submit_but = Button(Frame3, text="Submit", command=lambda: aprove(f'''insert 
        into item(name,price) values('{namevar.get()}','{pricevar.get()}')''')).pack(padx=5, pady=5)

    def boss():
        global winsecond
        winsecond = Toplevel(tkinsert)
        namevar = tkinter.StringVar()
        winsecond.title("Add Boss")
        winsecond.geometry("200x200")
        Frame1 = Frame(winsecond)
        Frame1.grid(row=0)
        Frame2 = Frame(winsecond)
        Frame2.grid(row=1)
        name_lab = Label(Frame1, text="Name : ").pack(
            side=LEFT, padx=5, pady=5)
        name_ent = Entry(Frame1, textvariable=namevar).pack(
            side=RIGHT, padx=5, pady=5)
        submit_but = Button(Frame2, text="Submit", command=lambda: aprove(f'''insert 
        into boss(name) values('{namevar.get()}')''')).pack(padx=5, pady=5)

    def history_buy():
        global winsecond
        winsecond = Toplevel(tkinsert)
        buyervar = tkinter.StringVar()
        itemvar = tkinter.StringVar()
        datevar = tkinter.StringVar()
        winsecond.title("Add Buy")
        winsecond.geometry("200x200")
        Frame1 = Frame(winsecond)
        Frame1.grid(row=0)
        Frame2 = Frame(winsecond)
        Frame2.grid(row=1)
        Frame3 = Frame(winsecond)
        Frame3.grid(row=2)
        Frame4 = Frame(winsecond)
        Frame4.grid(row=3)
        name_lab = Label(Frame1, text="Buyer ID : ").pack(
            side=LEFT, padx=5, pady=5)
        name_ent = Entry(Frame1, textvariable=buyervar).pack(
            side=RIGHT, padx=5, pady=5)
        address_lab = Label(Frame2, text="Item ID : ").pack(
            side=LEFT, padx=5, pady=5)
        address_ent = Entry(Frame2, textvariable=itemvar).pack(
            side=RIGHT, padx=5, pady=5)
        phone_lab = Label(Frame3, text="Date : ").pack(
            side=LEFT, padx=5, pady=5)
        phone_ent = Entry(Frame3, textvariable=datevar).pack(
            side=RIGHT, padx=5, pady=5)
        submit_but = Button(Frame4, text="Submit", command=lambda: aprove(f'''insert 
        into history_buy(date,buyer,item) values('{datevar.get()}','{buyervar.get()}','{itemvar.get()}')''')).pack(padx=5, pady=5)

    def history_salary():
        global winsecond
        winsecond = Toplevel(tkinsert)
        bossvar = tkinter.StringVar()
        salaryvar = tkinter.StringVar()
        datevar = tkinter.StringVar()
        winsecond.title("Add Salary")
        winsecond.geometry("200x200")
        Frame1 = Frame(winsecond)
        Frame1.grid(row=0)
        Frame2 = Frame(winsecond)
        Frame2.grid(row=1)
        Frame3 = Frame(winsecond)
        Frame3.grid(row=2)
        Frame4 = Frame(winsecond)
        Frame4.grid(row=3)
        name_lab = Label(Frame1, text="Boss ID : ").pack(
            side=LEFT, padx=5, pady=5)
        name_ent = Entry(Frame1, textvariable=bossvar).pack(
            side=RIGHT, padx=5, pady=5)
        address_lab = Label(Frame2, text="Salary : ").pack(
            side=LEFT, padx=5, pady=5)
        address_ent = Entry(Frame2, textvariable=salaryvar).pack(
            side=RIGHT, padx=5, pady=5)
        phone_lab = Label(Frame3, text="Date : ").pack(
            side=LEFT, padx=5, pady=5)
        phone_ent = Entry(Frame3, textvariable=datevar).pack(
            side=RIGHT, padx=5, pady=5)
        submit_but = Button(Frame4, text="Submit", command=lambda: aprove(f'''insert 
        into history_salary(boss,salary,date) values('{bossvar.get()}','{salaryvar.get()}','{datevar.get()}')''')).pack(padx=5, pady=5)
    tkinsert = Toplevel(root)
    tkinsert.title("Insert")
    tkinsert.geometry("200x255")
    cashier_but = Button(tkinsert, text="Cashier", command=cashier)
    shelfer_but = Button(tkinsert, text="Shelfer", command=shelfer)
    customer_but = Button(tkinsert, text="Customer", command=customer)
    item_but = Button(tkinsert, text="item", command=item)
    boss_but = Button(tkinsert, text="Boss", command=boss)
    history_buy_but = Button(tkinsert, text="History_buy", command=history_buy)
    history_salary_but = Button(
        tkinsert, text="History_salary", command=history_salary)
    cashier_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    shelfer_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    customer_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    item_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    boss_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    history_buy_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    history_salary_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)

#custom query
def custumq():
    querytext = tkinter.StringVar()

    def passdata():
        finnaly = ""
        connectdb()
        c.execute(querytext.get())
        queryresault = c.fetchall()
        for q in queryresault:
            for qq in q:
                finnaly += str(qq) + " "
            finnaly += "\n"
        messagebox.showinfo("Show Resault", finnaly)
        con.close()
        custumqwindow.destroy()
    custumqwindow = Toplevel(root)
    custumqwindow.title("Custom Query")
    custumqwindow.geometry("300x100")

    querybox_ent = Entry(custumqwindow, textvariable=querytext, width=50)
    pass_but = Button(custumqwindow, text="done", command=passdata)

    querybox_ent.pack(padx=10, pady=10)
    pass_but.pack(padx=20, pady=10, ipadx=30)

#insert default records in tabels
def insertdefault():
    connectdb()
    c.execute('''insert into cashier(name,shift) values('abbas','morning')''')
    c.execute('''insert into cashier(name,shift) values('hasan','afternoon')''')
    c.execute('''insert into cashier(name,shift) values('hossein','morning')''')
    c.execute('''insert into shelfer(name,shift) values('bagher','morning')''')
    c.execute('''insert into shelfer(name,shift) values('somayeh','afternoon')''')
    c.execute('''insert into shelfer(name,shift) values('mahdi','morning')''')
    c.execute(
        '''insert into customer(name,address,phone) values('gholam','isf-main street','+989552145588')''')
    c.execute(
        '''insert into customer(name,address,phone) values('saeeid','tehran-kashani','+989885551236')''')
    c.execute(
        '''insert into customer(name,address,phone) values('hamid','kerman-mahan','+9890022255555')''')
    c.execute('''insert into boss(name) values('ali')''')
    c.execute('''insert into item(name,price) values('meet',50)''')
    c.execute('''insert into item(name,price) values('onion',5)''')
    c.execute('''insert into item(name,price) values('carrot',4)''')
    c.execute('''insert into item(name,price) values('soda',10)''')
    c.execute('''insert into history_buy(buyer,item,date) values(1,1,20220111)''')
    c.execute('''insert into history_buy(buyer,item,date) values(2,2,20220110)''')
    c.execute('''insert into history_buy(buyer,item,date) values(3,4,20220109)''')
    c.execute(
        ''' insert into history_salary(boss,salary,date) values(1,3500,20211101)''')
    c.execute(
        ''' insert into history_salary(boss,salary,date) values(1,2500,20211201)''')
    c.execute(
        ''' insert into history_salary(boss,salary,date) values(1,3500,20220101)''')
    c.execute(
        ''' insert into history_salary(boss,salary,date) values(1,4500,20220106)''')
    con.commit()
    con.close()

#show primary and foriegn keys
def showkey():
    showkeywindow = Toplevel(root)
    showkeywindow.title("Shows Keys")
    showkeywindow.geometry("250x300")
    main_lab = LabelFrame(showkeywindow, text="Primary key")
    main_lab.pack()
    primary_lab = Label(
        main_lab, text="cashier : id\nshelfer : id\nboss : id\ncustomer : id\nitem : id\nhistory_buy : id\nhistory_salary : id",)
    primary_lab.pack()
    second_lab = LabelFrame(showkeywindow, text="Foriegn Key")
    second_lab.pack()
    foriegn_lab = Label(
        second_lab, text="history_buy :\nbuyer(id customer)\nitem(id item)\nhistory_salary :\nboss(id boss)")
    foriegn_lab.pack()

#show shift morning emplyees
def employeeshow():
    connectdb()
    textinfo = ''
    c.execute('''select * from cashier where shift ='morning' ''')
    rows_cashier = c.fetchall()
    c.execute('''select * from shelfer where shift='morning' ''')
    rows_shelfer = c.fetchall()
    for r in rows_cashier:
        textinfo += "Type = cashier\n"
        textinfo += f"ID = {r[0]}\nName = {r[1]}\nShift = {r[2]}\n"
        textinfo += "--------\n"
    textinfo += "========\n"
    for r in rows_shelfer:
        textinfo += "Type = shelfer\n"
        textinfo += f"ID = {r[0]}\nName = {r[1]}\nShift = {r[2]}\n"
        textinfo += "--------\n"
    messagebox.showinfo("Shift Morning", textinfo)
    con.close()

#show addresess and phones of meet buyers
def meetbuy():
    connectdb()
    textinfo = ''
    c.execute('''select customer.name,customer.address,customer.phone,item.name from 
    item inner join history_buy on item.id = history_buy.item 
    inner join customer on customer.id = history_buy.buyer 
    where item.name = 'meet' ''')
    meetbuyers = c.fetchall()
    for m in meetbuyers:
        textinfo += f"Name = {m[0]}\n"
        textinfo += f"Address = {m[1]}\n"
        textinfo += f"Phone = {m[2]}\n"
        textinfo += f"Item = {m[3]}\n"
        textinfo += "========\n"
    messagebox.showinfo("Meet Buyers", textinfo)
    con.close()

#show salary boss upper 3000
def showsalary():
    connectdb()
    textinfo = ''
    c.execute('''select boss.name,history_salary.date,history_salary.salary from
    boss inner join history_salary
    on boss.id = history_salary.boss
    where history_salary.salary > 3000
    and date between 20211212 and 20220113''')
    salaryup3000 = c.fetchall()
    for s in salaryup3000:
        textinfo += f"Name = {s[0]}\n"
        textinfo += f"Date = {s[1]}\n"
        textinfo += f"Salary = {s[2]}\n"
        textinfo += "========\n"
    messagebox.showinfo("Salary Upper 3000", textinfo)
    con.close()

#show records of tabels
def showrec():
    def showmessage(queryx):
        finnaly = ""
        queryy = f'''select * from {queryx}'''
        connectdb()
        c.execute(queryy)
        queryresault = c.fetchall()
        for q in queryresault:
            for qq in q:
                finnaly += str(qq) + " "
            finnaly += "\n"
        messagebox.showinfo("Show Resault", finnaly)
        con.close()
    tkinsert = Toplevel(root)
    tkinsert.title("Show Records")
    tkinsert.geometry("200x255")
    cashier_but = Button(tkinsert, text="Cashier",
                         command=lambda: showmessage("cashier"))
    shelfer_but = Button(tkinsert, text="Shelfer",
                         command=lambda: showmessage("shelfer"))
    customer_but = Button(tkinsert, text="Customer",
                          command=lambda: showmessage("customer"))
    item_but = Button(tkinsert, text="item",
                      command=lambda: showmessage("item"))
    boss_but = Button(tkinsert, text="Boss",
                      command=lambda: showmessage("boss"))
    history_buy_but = Button(tkinsert, text="History_buy",
                             command=lambda: showmessage("history_buy"))
    history_salary_but = Button(
        tkinsert, text="History_salary", command=lambda: showmessage("history_salary"))
    cashier_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    shelfer_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    customer_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    item_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    boss_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    history_buy_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)
    history_salary_but.pack(pady=5, padx=20, ipadx=10, fill=BOTH)

#define main frame items
intro_lab = Label(root, text="Welcome")
createdb_but = Button(
    root, text="Create or connect database 'shop'", command=connectdb)
createtb_but = Button(root, text="Create Tabels", command=createtb)
deletetb_but = Button(root, text="Delete Tabels", command=deletetb)
insertdefault_but = Button(
    root, text="Insert Default info", command=insertdefault)
insert_but = Button(root, text="Insert to database", command=insertf)
showrec_but = Button(root, text="Show Records", command=showrec)
custumq_but = Button(root, text="type Costum Query", command=custumq)
showkey_but = Button(
    root, text="show Primary and foreign key", command=showkey)
employeeshow_but = Button(
    root, text="show shift Morning Employee", command=employeeshow)
meetbuy_but = Button(root, text="Show info Buyers Meet", command=meetbuy)
showsalary_but = Button(
    root, text="Show Boss Salary Up 3000$ in moon ago", command=showsalary)
# align in
intro_lab.pack(padx=5, pady=5, fill=BOTH)
createdb_but.pack(padx=40, pady=5, ipady=10, fill=BOTH)
createtb_but.pack(padx=40, pady=5, ipady=10, fill=BOTH)
deletetb_but.pack(padx=40, pady=5, ipady=10, fill=BOTH)
insertdefault_but.pack(padx=40, ipady=10, pady=5, fill=BOTH)
custumq_but.pack(padx=40, ipady=10, pady=5, fill=BOTH)
insert_but.pack(padx=40, pady=5, ipady=10, fill=BOTH)
showrec_but.pack(padx=40, pady=5, ipady=10, fill=BOTH)
showkey_but.pack(padx=40, pady=5, ipady=10, fill=BOTH)
employeeshow_but.pack(padx=40, pady=5, ipady=10, fill=BOTH)
meetbuy_but.pack(padx=40, pady=5, ipady=10, fill=BOTH)
showsalary_but.pack(padx=40, pady=5, ipady=10, fill=BOTH)
root.mainloop()

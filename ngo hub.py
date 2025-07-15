import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime, timedelta
import mysql.connector as sql

root=tk.Tk()
root.geometry('500x600')
root.title('ngo hub')
root.configure(bg='#FBF5EA')

bg_color='#863E28'

user_image=tk.PhotoImage(file='user_image.png')
admin_image=tk.PhotoImage(file="admin_login.png")
create_image=tk.PhotoImage(file="create.png")
lock_image=tk.PhotoImage(file="locked.png")
unlock_image=tk.PhotoImage(file="unlocked.png")

def user_list():
    def go_to_admindashboard():
        ngo_fm.destroy()
        root.update()
        admin_dashboard()

    conn = sql.connect(host='localhost', password='ziyarawat@123', user='root', database="ngohub")
    cur = conn.cursor()
    cur.execute("SELECT * FROM userinfo")
    data = cur.fetchall()
    num=len(data)
    conn.close()
    ngo_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    heading_lb=tk.Label(ngo_fm,text='User List',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=1300)
    # columns = ['Name', 'Phone Number',dob,email,username]

    ngo_name_lb=tk.Label(ngo_fm,text='Name',bg=bg_color,fg="white",font=("times",15,"bold"))
    ngo_name_lb.place(x=0,y=50,width=170)
    a=80
    for i in range(num):
        ngo_lb=tk.Label(ngo_fm,text=data[i][0],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        ngo_lb.place(x=30,y=a)
        a=a+40

    emailid_lb=tk.Label(ngo_fm,text='Phone Number',bg=bg_color,fg="white",font=("times",15,"bold"))
    emailid_lb.place(x=150,y=50,width=280)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][1],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=230,y=a)
        a=a+40

    phn_lb=tk.Label(ngo_fm,text='Date Of Birth',bg=bg_color,fg="white",font=("times",15,"bold"))
    phn_lb.place(x=370,y=50,width=200)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][2],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=400,y=a)
        a=a+40

    category_lb=tk.Label(ngo_fm,text='Email ID\t',bg=bg_color,fg="white",font=("times",15,"bold"))
    category_lb.place(x=550,y=50,width=300)
    a=80
    for i in range(num):
        valuecategory_lb=tk.Label(ngo_fm,text=data[i][3],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecategory_lb.place(x=560,y=a)
        a=a+40
    city_lb=tk.Label(ngo_fm,text='Username\t',bg=bg_color,fg="white",font=("times",15,"bold"))
    city_lb.place(x=830,y=50,width=300)
    a=80
    for i in range(num):
        valuecity_lb=tk.Label(ngo_fm,text=data[i][4],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecity_lb.place(x=860,y=a)
        a=a+40
    login_btn=tk.Button(ngo_fm,text='Back',font=("times",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=go_to_admindashboard)
    login_btn.place(x=450,y=530,width=150,height=20)
    
    ngo_fm.pack(pady=5)
    ngo_fm.pack_propagate(False)
    ngo_fm.configure(width=1050,height=580,bg='#FBF5EA')

def volunteer_list():
    def go_to_admindashboard():
        ngo_fm.destroy()
        root.update()
        admin_dashboard()

    conn = sql.connect(host='localhost', password='ziyarawat@123', user='root', database="ngohub")
    cur = conn.cursor()
    cur.execute("SELECT * FROM volunteerlist")
    data = cur.fetchall()
    num=len(data)
    conn.close()
    ngo_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    heading_lb=tk.Label(ngo_fm,text='Volunteer List',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=1300)
    # columns = ['Name', 'Email ID', 'Phone Number', 'city', 'ngo', 'date']

    ngo_name_lb=tk.Label(ngo_fm,text='Name',bg=bg_color,fg="white",font=("times",15,"bold"))
    ngo_name_lb.place(x=0,y=50,width=230)
    a=80
    for i in range(num):
        ngo_lb=tk.Label(ngo_fm,text=data[i][0],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        ngo_lb.place(x=0,y=a)
        a=a+40

    emailid_lb=tk.Label(ngo_fm,text='\tEmail ID',bg=bg_color,fg="white",font=("times",15,"bold"))
    emailid_lb.place(x=200,y=50,width=280)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][1],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=250,y=a)
        a=a+40

    phn_lb=tk.Label(ngo_fm,text='\tPhone Number',bg=bg_color,fg="white",font=("times",15,"bold"))
    phn_lb.place(x=450,y=50,width=270)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][2],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=570,y=a)
        a=a+40

    category_lb=tk.Label(ngo_fm,text='City',bg=bg_color,fg="white",font=("times",15,"bold"))
    category_lb.place(x=700,y=50,width=200)
    a=80
    for i in range(num):
        valuecategory_lb=tk.Label(ngo_fm,text=data[i][3],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecategory_lb.place(x=730,y=a)
        a=a+40
    city_lb=tk.Label(ngo_fm,text='NGO\t',bg=bg_color,fg="white",font=("times",15,"bold"))
    city_lb.place(x=850,y=50,width=300)
    a=80
    for i in range(num):
        valuecity_lb=tk.Label(ngo_fm,text=data[i][4],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecity_lb.place(x=880,y=a)
        a=a+40
    date_lb=tk.Label(ngo_fm,text='Date',bg=bg_color,fg="white",font=("times",15,"bold"))
    date_lb.place(x=1100,y=50,width=200)
    a=80
    for i in range(num):
        valuedate_lb=tk.Label(ngo_fm,text=data[i][5],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuedate_lb.place(x=1150,y=a)
        a=a+40
    login_btn=tk.Button(ngo_fm,text='Back',font=("times",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=go_to_admindashboard)
    login_btn.place(x=530,y=530,width=150,height=20)
    
    ngo_fm.pack(pady=5)
    ngo_fm.pack_propagate(False)
    ngo_fm.configure(width=1300,height=580,bg='#FBF5EA')

def donation_list():
    def go_to_admindashboard():
        ngo_fm.destroy()
        root.update()
        admin_dashboard()

    conn = sql.connect(host='localhost', password='ziyarawat@123', user='root', database="ngohub")
    cur = conn.cursor()
    cur.execute("SELECT * FROM donationlist")
    data = cur.fetchall()
    num=len(data)
    conn.close()
    ngo_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    heading_lb=tk.Label(ngo_fm,text='Donation List',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=1300)
    # columns = ['Name', 'Email ID', 'Phone Number', 'city', 'ngo', 'amount']

    ngo_name_lb=tk.Label(ngo_fm,text='Name',bg=bg_color,fg="white",font=("times",15,"bold"))
    ngo_name_lb.place(x=0,y=50,width=230)
    a=80
    for i in range(num):
        ngo_lb=tk.Label(ngo_fm,text=data[i][0],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        ngo_lb.place(x=0,y=a)
        a=a+40

    emailid_lb=tk.Label(ngo_fm,text='\tEmail ID',bg=bg_color,fg="white",font=("times",15,"bold"))
    emailid_lb.place(x=200,y=50,width=280)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][1],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=250,y=a)
        a=a+40

    phn_lb=tk.Label(ngo_fm,text='\tPhone Number',bg=bg_color,fg="white",font=("times",15,"bold"))
    phn_lb.place(x=450,y=50,width=270)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][2],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=570,y=a)
        a=a+40

    category_lb=tk.Label(ngo_fm,text='City',bg=bg_color,fg="white",font=("times",15,"bold"))
    category_lb.place(x=700,y=50,width=200)
    a=80
    for i in range(num):
        valuecategory_lb=tk.Label(ngo_fm,text=data[i][3],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecategory_lb.place(x=730,y=a)
        a=a+40
    city_lb=tk.Label(ngo_fm,text='NGO\t',bg=bg_color,fg="white",font=("times",15,"bold"))
    city_lb.place(x=850,y=50,width=300)
    a=80
    for i in range(num):
        valuecity_lb=tk.Label(ngo_fm,text=data[i][4],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecity_lb.place(x=870,y=a)
        a=a+40
    date_lb=tk.Label(ngo_fm,text='Amount',bg=bg_color,fg="white",font=("times",15,"bold"))
    date_lb.place(x=1100,y=50,width=200)
    a=80
    for i in range(num):
        valuedate_lb=tk.Label(ngo_fm,text=data[i][5],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuedate_lb.place(x=1150,y=a)
        a=a+40
    login_btn=tk.Button(ngo_fm,text='Back',font=("times",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=go_to_admindashboard)
    login_btn.place(x=530,y=530,width=150,height=20)
    
    ngo_fm.pack(pady=5)
    ngo_fm.pack_propagate(False)
    ngo_fm.configure(width=1300,height=580,bg='#FBF5EA')

def update_ngodetails(name,email,phno,category,city,edate,currentname):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("update ngolist set name=%s,email=%s,phonenumber=%s,category=%s,city=%s,establishmentdate=%s where name=%s", (name,email,phno,category,city,edate,currentname))
    conn.commit()
    conn.close()

def give_ngodetails(currentname):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("SELECT * FROM ngolist WHERE name = %s", (currentname,))
    response=cur.fetchall()
    conn.close()
    return response

def delete_ngodetails(name):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("delete from ngolist where name=%s",(name,))
    conn.commit()
    conn.close()   

def delete_ngo():
    conn = sql.connect(host='localhost', password='ziyarawat@123', user='root', database="ngohub")
    cur = conn.cursor()
    cur.execute("SELECT name FROM ngolist")
    a= cur.fetchall()
    conn.close()
    data=[]
    for i in a:
        data.append(i[0])

    def go_to_manage():
        delngo_fm.destroy()
        root.update()
        manage_ngos()

    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')

    def check_input_validation():
        if name_ent.get()=='':
            message_box(message='NGO Name is Required')
        else:
            delete_ngodetails(name_ent.get())
            message_box("NGO Successfully Deleted!")

    delngo_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    heading_lb=tk.Label(delngo_fm,text='Delete NGO',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=480)

    back_btn=tk.Button(delngo_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=go_to_manage)
    back_btn.place(x=5,y=43)

    name_lb=tk.Label(delngo_fm,text="Select Ngo Name To Delete From List",font=("Helvetica",16,"bold"),fg=bg_color,bg='#FBF5EA')
    name_lb.place(x=40,y=130)
    name_ent=ttk.Combobox(delngo_fm,values=data,font=("Helvetica",16,"bold"))
    name_ent.place(x=70,y=190,width=300)
    name_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=name_ent))

    login_btn=tk.Button(delngo_fm,text='Delete',font=("Helvetica",16,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=check_input_validation)
    login_btn.place(x=150,y=300,width=150,height=40)
    
    delngo_fm.pack(pady=5)
    delngo_fm.pack_propagate(False)
    delngo_fm.configure(width=480,height=580,bg='#FBF5EA')

def add_ngodetails(name,email,phno,category,city,edate):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute(f"""insert into ngolist values('{name}','{email}','{phno}','{category}','{city}','{edate}')""")
    conn.commit()
    conn.close()

def ngoadmin():
    def go_to_admindashboard():
        ngo_fm.destroy()
        root.update()
        admin_dashboard()

    conn = sql.connect(host='localhost', password='ziyarawat@123', user='root', database="ngohub")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ngolist")
    data = cur.fetchall()
    num=len(data)
    conn.close()
    ngo_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    heading_lb=tk.Label(ngo_fm,text='NG0 List',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=1300)
    # columns = ['NGO Name', 'Email ID', 'Phone Number', 'Category', 'City', 'Establishment Date']

    ngo_name_lb=tk.Label(ngo_fm,text='NGO Name',bg=bg_color,fg="white",font=("times",15,"bold"))
    ngo_name_lb.place(x=0,y=50,width=230)
    a=80
    for i in range(num):
        ngo_lb=tk.Label(ngo_fm,text=data[i][0],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        ngo_lb.place(x=0,y=a)
        a=a+40

    emailid_lb=tk.Label(ngo_fm,text='\tEmail ID',bg=bg_color,fg="white",font=("times",15,"bold"))
    emailid_lb.place(x=200,y=50,width=280)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][1],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=250,y=a)
        a=a+40

    phn_lb=tk.Label(ngo_fm,text='\tPhone Number',bg=bg_color,fg="white",font=("times",15,"bold"))
    phn_lb.place(x=450,y=50,width=280)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][2],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=570,y=a)
        a=a+40

    category_lb=tk.Label(ngo_fm,text='Category',bg=bg_color,fg="white",font=("times",15,"bold"))
    category_lb.place(x=700,y=50,width=200)
    a=80
    for i in range(num):
        valuecategory_lb=tk.Label(ngo_fm,text=data[i][3],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecategory_lb.place(x=730,y=a)
        a=a+40
    city_lb=tk.Label(ngo_fm,text='City',bg=bg_color,fg="white",font=("times",15,"bold"))
    city_lb.place(x=900,y=50,width=200)
    a=80
    for i in range(num):
        valuecity_lb=tk.Label(ngo_fm,text=data[i][4],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecity_lb.place(x=970,y=a)
        a=a+40
    date_lb=tk.Label(ngo_fm,text='Establishment Date\t',bg=bg_color,fg="white",font=("times",15,"bold"))
    date_lb.place(x=1100,y=50)
    a=80
    for i in range(num):
        valuedate_lb=tk.Label(ngo_fm,text=data[i][5],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuedate_lb.place(x=1100,y=a)
        a=a+40
    login_btn=tk.Button(ngo_fm,text='Back',font=("times",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=go_to_admindashboard)
    login_btn.place(x=530,y=550,width=150,height=20)
    


    ngo_fm.pack(pady=5)
    ngo_fm.pack_propagate(False)
    ngo_fm.configure(width=1300,height=580,bg='#FBF5EA')

def manage_ngos():
    def go_to_add():
        dashboard_fm.destroy()
        root.update()
        add_ngo()
    def go_to_delete():
        dashboard_fm.destroy()
        root.update()
        delete_ngo()
    def go_to_update():
        dashboard_fm.destroy()
        root.update()
        update_ngo()   
    def go_to_admindashboard():
        dashboard_fm.destroy()
        root.update()
        admin_dashboard()
    dashboard_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(dashboard_fm,text='Manage NGOs',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=400)

    back_btn=tk.Button(dashboard_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=go_to_admindashboard)
    back_btn.place(x=5,y=43)
    
    add_btn=tk.Button(dashboard_fm,text='Add NGO',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_add)
    add_btn.place(x=70,y=120,width=250,height=50)
    delete_btn=tk.Button(dashboard_fm,text='Delete NGO',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_delete)
    delete_btn.place(x=70,y=190,width=250,height=50)
    update_btn=tk.Button(dashboard_fm,text='Update NGO',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_update)
    update_btn.place(x=70,y=260,width=250,height=50)

    dashboard_fm.pack(pady=30)
    dashboard_fm.pack_propagate(False)
    dashboard_fm.configure(width=400,height=450,bg='#FBF5EA')

def add_ngo():
    def go_to_manage():
        addngo_fm.destroy()
        root.update()
        manage_ngos()

    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')
                
    def check_input_validation():
        if name_ent.get()=='':
            name_ent.config(highlightcolor='red',highlightbackground='red')
            name_ent.focus()
            message_box(message='NGO Name is Required')
        elif contact_ent.get()=='':
            contact_ent.config(highlightcolor='red',highlightbackground='red')
            contact_ent.focus()
            message_box(message='NGO Phone Number is Required')
        elif edate_ent.get()=='':
            edate_ent.config(highlightcolor='red',highlightbackground='red')
            edate_ent.focus()
            message_box(message='Establishment date of NGO is Required')
        elif email_ent.get()=='':
            email_ent.config(highlightcolor='red',highlightbackground='red')
            email_ent.focus()
            message_box(message='NGO Email id is Required')
        elif category_ent.get()=='':
            category_ent.config(highlightcolor='red',highlightbackground='red')
            category_ent.focus()
            message_box(message='NGO category is Required')
        elif city_ent.get()=='':
            city_ent.config(highlightcolor='red',highlightbackground='red')
            city_ent.focus()
            message_box(message='NGO city is Required')
        else:
            add_ngodetails(name_ent.get(),email_ent.get(),contact_ent.get(),category_ent.get(),city_ent.get(),edate_ent.get())
            message_box("NGO Added Successfully")

    addngo_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(addngo_fm,text='Add NGO',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=480)
    
    name_lb=tk.Label(addngo_fm,text="Enter NGO name",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    name_lb.place(x=30,y=130)
    name_ent=tk.Entry(addngo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    name_ent.place(x=240,y=130,width=200)
    name_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=name_ent))

    email_lb=tk.Label(addngo_fm,text="Enter NGO email id",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    email_lb.place(x=20,y=170)
    email_ent=tk.Entry(addngo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    email_ent.place(x=240,y=170,width=200)
    email_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=email_ent))

    contact_lb=tk.Label(addngo_fm,text="Enter NGO phone number",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    contact_lb.place(x=10,y=220)
    contact_ent=tk.Entry(addngo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    contact_ent.place(x=240,y=220,width=200)
    contact_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=contact_ent))

    category_lb=tk.Label(addngo_fm,text="Enter NGO category",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    category_lb.place(x=20,y=270)
    category_ent=tk.Entry(addngo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    category_ent.place(x=240,y=270,width=200)
    category_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=category_ent))

    city_lb=tk.Label(addngo_fm,text="Enter NGO City",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    city_lb.place(x=20,y=320)
    city_ent=tk.Entry(addngo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    city_ent.place(x=240,y=320,width=200)
    city_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=city_ent))

    edate_lb=tk.Label(addngo_fm,text="Enter Establishment Date",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    edate_lb.place(x=10,y=370)
    edate_ent=tk.Entry(addngo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    edate_ent.place(x=240,y=370,width=200)
    edate_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=edate_ent))

    login_btn=tk.Button(addngo_fm,text='Update',font=("Helvetica",16,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=check_input_validation)
    login_btn.place(x=150,y=450,width=150,height=40)

    back_btn=tk.Button(addngo_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=go_to_manage)
    back_btn.place(x=5,y=43)

    addngo_fm.pack(pady=5)
    addngo_fm.pack_propagate(False)
    addngo_fm.configure(width=480,height=580,bg='#FBF5EA')

def update_ngo():
    conn = sql.connect(host='localhost', password='ziyarawat@123', user='root', database="ngohub")
    cur = conn.cursor()
    cur.execute("SELECT name FROM ngolist")
    a= cur.fetchall()
    conn.close()
    data=[]
    for i in a:
        data.append(i[0])
    def go_to_manage():
        updatengo_fm.destroy()
        root.update()
        manage_ngos()

    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')
    def check_ngo():
        if currentname_ent.get()=='':
            message_box(message='NGO name is Required')
        else:
            def check_input_validation():
                if name_ent.get()=='':
                    name_ent.config(highlightcolor='red',highlightbackground='red')
                    name_ent.focus()
                    message_box(message='NGO Name is Required')
                elif contact_ent.get()=='':
                    contact_ent.config(highlightcolor='red',highlightbackground='red')
                    contact_ent.focus()
                    message_box(message='NGO Phone Number is Required')
                elif edate_ent.get()=='':
                    edate_ent.config(highlightcolor='red',highlightbackground='red')
                    edate_ent.focus()
                    message_box(message='Establishment date of NGO is Required')
                elif email_ent.get()=='':
                    email_ent.config(highlightcolor='red',highlightbackground='red')
                    email_ent.focus()
                    message_box(message='NGO Email id is Required')
                elif category_ent.get()=='':
                    category_ent.config(highlightcolor='red',highlightbackground='red')
                    category_ent.focus()
                    message_box(message='NGO category is Required')
                elif city_ent.get()=='':
                    city_ent.config(highlightcolor='red',highlightbackground='red')
                    city_ent.focus()
                    message_box(message='NGO city is Required')
                else:
                    update_ngodetails(name_ent.get(),email_ent.get(),contact_ent.get(),category_ent.get(),city_ent.get(),edate_ent.get(),currentname_ent.get())
                    message_box("NGO Updated Successfully")
            data2=give_ngodetails(currentname_ent.get())
            heading_lb=tk.Label(updatengo_fm,text='Enter NGO details',bg=bg_color,fg="white",font=("times",24,"bold"))
            heading_lb.place(x=0,y=180,width=480)
        
            name_lb=tk.Label(updatengo_fm,text="Enter NGO name",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            name_lb.place(x=30,y=240)
            name_ent=tk.Entry(updatengo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            name_ent.place(x=240,y=240,width=200)
            name_ent.insert(tk.END,data2[0][0])
            name_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=name_ent))

            email_lb=tk.Label(updatengo_fm,text="Enter NGO email id",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            email_lb.place(x=20,y=270)
            email_ent=tk.Entry(updatengo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            email_ent.place(x=240,y=270,width=200)
            email_ent.insert(tk.END,data2[0][1])
            email_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=email_ent))

            contact_lb=tk.Label(updatengo_fm,text="Enter NGO phone number",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            contact_lb.place(x=10,y=300)
            contact_ent=tk.Entry(updatengo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            contact_ent.place(x=240,y=300,width=200)
            contact_ent.insert(tk.END,data2[0][2])
            contact_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=contact_ent))

            category_lb=tk.Label(updatengo_fm,text="Enter NGO category",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            category_lb.place(x=20,y=330)
            category_ent=tk.Entry(updatengo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            category_ent.place(x=240,y=330,width=200)
            category_ent.insert(tk.END,data2[0][3])
            category_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=category_ent))

            city_lb=tk.Label(updatengo_fm,text="Enter NGO City",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            city_lb.place(x=20,y=360)
            city_ent=tk.Entry(updatengo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            city_ent.place(x=240,y=360,width=200)
            city_ent.insert(tk.END,data2[0][4])
            city_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=city_ent))

            edate_lb=tk.Label(updatengo_fm,text="Enter Establishment Date",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            edate_lb.place(x=10,y=390)
            edate_ent=tk.Entry(updatengo_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            edate_ent.place(x=240,y=390,width=200)
            edate_ent.insert(tk.END,data2[0][5])
            edate_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=edate_ent))

            login_btn=tk.Button(updatengo_fm,text='Update',font=("Helvetica",16,"bold"),
                                bg=bg_color,fg='#FBF5EA',command=check_input_validation)
            login_btn.place(x=150,y=450,width=150,height=40)

    updatengo_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    heading_lb=tk.Label(updatengo_fm,text='Update NGO details',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=480)

    back_btn=tk.Button(updatengo_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=go_to_manage)
    back_btn.place(x=5,y=43)
    currentname_lb=tk.Label(updatengo_fm,text="Select Ngo Name To Update",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    currentname_lb.place(x=100,y=80)
    currentname_ent=ttk.Combobox(updatengo_fm,values=data,font=("Helvetica",13,"bold"))
    currentname_ent.place(x=70,y=110,width=300)
    currentname_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=currentname_ent))

    submit_btn=tk.Button(updatengo_fm,text='Submit',font=("Helvetica",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=check_ngo)
    submit_btn.place(x=180,y=140,height=20)

    line_lb=tk.Label(updatengo_fm,text="--"*39,font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    line_lb.place(x=0,y=160)

    updatengo_fm.pack(pady=5)
    updatengo_fm.pack_propagate(False)
    updatengo_fm.configure(width=480,height=580,bg='#FBF5EA')

def generate_random_dates():
    today = datetime.today()
    
    first_day_next_month = (today.replace(day=28) + timedelta(days=4)).replace(day=1)
    
    last_day_next_month = (first_day_next_month + timedelta(days=31)).replace(day=1) - timedelta(days=1)
    
    random_dates = [
        today + timedelta(days=random.randint(0, (last_day_next_month - today).days))
        for _ in range(3)
    ]
    
    return [date.strftime('%Y-%m-%d') for date in random_dates]

def check_admin_already_exist(username):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("SELECT username FROM admininfo WHERE username = %s", (username,))
    response=cur.fetchall()
    conn.close()

    return response

def check_password_right(password):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("SELECT password FROM userinfo WHERE password = %s", (password,))
    response=cur.fetchall()
    conn.close()

    return response

def admin_password_match(username,password):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("SELECT password FROM admininfo WHERE username = %s", (username,))
    db_password=cur.fetchall()[0][0]
    conn.close()
    if db_password==password:
        return 1
    return 0

def user_password_match(username,password):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("SELECT password FROM userinfo WHERE username = %s", (username,))
    db_password=cur.fetchall()[0][0]
    conn.close()
    if db_password==password:
        return 1
    return 0

def check_user_already_exist(username):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("SELECT username FROM userinfo WHERE username = %s", (username,))
    response=cur.fetchall()
    conn.close()

    return response

def give_userdetails(username):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("SELECT * FROM userinfo WHERE username = %s", (username,))
    response=cur.fetchall()
    conn.close()
    return response

def update_user_details(name,contact,dob,email,username,currentusername):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("update userinfo set name=%s,phnno=%s,dob=%s,email=%s,username=%s where username=%s", (name,contact,dob,email,username,currentusername))
    conn.commit()
    conn.close()

def update_password_sql(password,currentpass):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute("update userinfo set password=%s where password=%s", (password,currentpass))
    conn.commit()
    conn.close()

def add_volunteer(name,email,phno,address,ngo,date):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute(f"""insert into volunteerlist values('{name}','{email}','{phno}','{address}','{ngo}','{date}')""")
    conn.commit()
    conn.close()

def add_donation(name,email,phno,address,ngo,amount):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute(f"""insert into donationlist values('{name}','{email}','{phno}','{address}','{ngo}','{amount}')""")
    conn.commit()
    conn.close()

def add_user(name,phno,dob,email,username,password):
    conn=sql.connect(host='localhost',password='ziyarawat@123',user='root',database="ngohub")
    cur=conn.cursor()
    cur.execute(f"""insert into userinfo values('{name}','{phno}','{dob}','{email}','{username}','{password}')""")
    conn.commit()
    conn.close()

def confirmation_box(message):

    answer=tk.BooleanVar()
    answer.set(False)

    def action(ans):
        answer.set(ans)
        confirmation_box_fm.destroy()

    confirmation_box_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3,bg='#FBF5EA')
    message_lb=tk.Label(confirmation_box_fm,text=message,font=("Helvetica",15,"bold"),bg='#FBF5EA')
    message_lb.pack(pady=20)

    cancel_btn=tk.Button(confirmation_box_fm,text='Cancel',font=("Helvetica",15,"bold"),bd=0,
                         bg=bg_color,fg='#FBF5EA',command=lambda:action(False))
    cancel_btn.place(x=50,y=160)

    yes_btn=tk.Button(confirmation_box_fm,text='Yes',font=("Helvetica",15,"bold"),bd=0,bg=bg_color,
                      fg='#FBF5EA',command=lambda:action(True))
    yes_btn.place(x=190,y=160,width=80)

    confirmation_box_fm.place(x=100,y=120,width=320,height=220)
    

    root.wait_window(confirmation_box_fm)
    return answer.get()

def message_box(message):
    meessage_box_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3,bg='#FBF5EA')

    close_btn=tk.Button(meessage_box_fm,text='X',bd=0,font=("Helvetica",13,"bold"),
                        fg=bg_color,command=lambda:meessage_box_fm.destroy(),bg='#FBF5EA')
    close_btn.place(x=290,y=5)

    message_lb=tk.Label(meessage_box_fm,text=message,font=("Helvetica",15,"bold"),bg='#FBF5EA')
    message_lb.pack(pady=50)

    meessage_box_fm.place(x=100,y=120,width=320,height=200)

def main_page():
    def forward_to_user_login_page():
        main_page.destroy()
        root.update()
        user_login()

    def forward_to_admin_page():
        main_page.destroy()
        root.update()
        admin_login()
    
    def forward_to_create_page():
        main_page.destroy()
        root.update()
        create_account_page()

    main_page=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    heading_lb=tk.Label(main_page,text='Welcome To Ngo Hub',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=400)
    #user button
    user_login_btn=tk.Button(main_page,text="User Login",bg=bg_color,fg='white',font=("Helvetica",15,"bold"),
                             bd=0,command=forward_to_user_login_page)
    user_login_btn.place(x=120,y=125,width=200)
    user_login_img=tk.Button(main_page,image=user_image,bd=0,bg='#FBF5EA',command=forward_to_user_login_page)
    user_login_img.place(x=50,y=100)
    #admin button
    admin_login_btn=tk.Button(main_page,text="Admin Login",bg=bg_color,fg='white',font=("Helvetica",15,"bold"),
                              bd=0,command=forward_to_admin_page)
    admin_login_btn.place(x=120,y=225,width=200)
    admin_login_img=tk.Button(main_page,image=admin_image,bd=0,bg='#FBF5EA',command=forward_to_admin_page)
    admin_login_img.place(x=50,y=200)
    #create account button
    create_login_btn=tk.Button(main_page,text="Create Account",bg=bg_color,fg='white',font=("Helvetica",15,"bold"),
                               bd=0,command=forward_to_create_page)
    create_login_btn.place(x=120,y=325,width=200)
    create_login_img=tk.Button(main_page,image=create_image,bd=0,bg='#FBF5EA',command=forward_to_create_page)
    create_login_img.place(x=50,y=300)

    main_page.pack(pady=30)
    main_page.pack_propagate(False)
    main_page.configure(width=400,height=420,bg='#FBF5EA')

def ngolist():
    def go_to_userdashboard():
        ngo_fm.destroy()
        root.update()
        user_dashboard()

    conn = sql.connect(host='localhost', password='ziyarawat@123', user='root', database="ngohub")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ngolist")
    data = cur.fetchall()
    num=len(data)
    conn.close()
    ngo_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    heading_lb=tk.Label(ngo_fm,text='NG0 List',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=1300)
    # columns = ['NGO Name', 'Email ID', 'Phone Number', 'Category', 'City', 'Establishment Date']

    ngo_name_lb=tk.Label(ngo_fm,text='NGO Name',bg=bg_color,fg="white",font=("times",15,"bold"))
    ngo_name_lb.place(x=0,y=50,width=230)
    a=80
    for i in range(num):
        ngo_lb=tk.Label(ngo_fm,text=data[i][0],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        ngo_lb.place(x=0,y=a)
        a=a+40

    emailid_lb=tk.Label(ngo_fm,text='\tEmail ID',bg=bg_color,fg="white",font=("times",15,"bold"))
    emailid_lb.place(x=200,y=50,width=280)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][1],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=250,y=a)
        a=a+40

    phn_lb=tk.Label(ngo_fm,text='\tPhone Number',bg=bg_color,fg="white",font=("times",15,"bold"))
    phn_lb.place(x=450,y=50,width=280)
    a=80
    for i in range(num):
        valueemail_lb=tk.Label(ngo_fm,text=data[i][2],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valueemail_lb.place(x=570,y=a)
        a=a+40

    category_lb=tk.Label(ngo_fm,text='Category',bg=bg_color,fg="white",font=("times",15,"bold"))
    category_lb.place(x=700,y=50,width=200)
    a=80
    for i in range(num):
        valuecategory_lb=tk.Label(ngo_fm,text=data[i][3],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecategory_lb.place(x=730,y=a)
        a=a+40
    city_lb=tk.Label(ngo_fm,text='City',bg=bg_color,fg="white",font=("times",15,"bold"))
    city_lb.place(x=900,y=50,width=200)
    a=80
    for i in range(num):
        valuecity_lb=tk.Label(ngo_fm,text=data[i][4],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuecity_lb.place(x=970,y=a)
        a=a+40
    date_lb=tk.Label(ngo_fm,text='Establishment Date\t',bg=bg_color,fg="white",font=("times",15,"bold"))
    date_lb.place(x=1100,y=50)
    a=80
    for i in range(num):
        valuedate_lb=tk.Label(ngo_fm,text=data[i][5],bg='#FBF5EA',fg=bg_color,font=("arial",15,"bold"))
        valuedate_lb.place(x=1100,y=a)
        a=a+40
    login_btn=tk.Button(ngo_fm,text='Back',font=("times",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=go_to_userdashboard)
    login_btn.place(x=530,y=530,width=150,height=20)
    
    ngo_fm.pack(pady=5)
    ngo_fm.pack_propagate(False)
    ngo_fm.configure(width=1300,height=580,bg='#FBF5EA')

def donate():
    conn = sql.connect(host='localhost', password='ziyarawat@123', user='root', database="ngohub")
    cur = conn.cursor()
    cur.execute("SELECT name FROM ngolist")
    a= cur.fetchall()
    conn.close()
    data=[]
    for i in a:
        data.append(i[0])

    def go_to_userdashboard():
        donate_fm.destroy()
        root.update()
        user_dashboard()

    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')

    def check_input_validation():
        if name_ent.get()=='':
            name_ent.config(highlightcolor='red',highlightbackground='red')
            name_ent.focus()
            message_box(message='Full Name is Required')
        elif email_ent.get()=='':
            email_ent.config(highlightcolor='red',highlightbackground='red')
            email_ent.focus()
            message_box(message='Email ID is Required')
        elif phno_ent.get()=='':
            phno_ent.config(highlightcolor='red',highlightbackground='red')
            phno_ent.focus()
            message_box(message='Phone number is Required')
        elif address_ent.get()=='':
            address_ent.config(highlightcolor='red',highlightbackground='red')
            address_ent.focus()
            message_box(message='City Name is Required')
        elif organisation_ent.get()=='':
            message_box(message='NGO Name is Required')
        elif amount_ent.get()=='':
            amount_ent.config(highlightcolor='red',highlightbackground='red')
            amount_ent.focus()
            message_box(message='Amount is Required')
        else:
            add_donation(name=name_ent.get(),email=email_ent.get(),phno=phno_ent.get(),address=address_ent.get(),ngo=organisation_ent.get(),amount=amount_ent.get())
            message_box("Thank you for Donation!!")

    donate_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(donate_fm,text='Donate To Ngos',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=480)

    quote_lb=tk.Label(donate_fm,text="DONATE TO MAKE A DIFFERENCE!",font=("times",18,"bold"),fg=bg_color,bg='#FBF5EA')
    quote_lb.place(x=20,y=70)
  
    name_lb=tk.Label(donate_fm,text="Enter your name",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    name_lb.place(x=30,y=140)
    name_ent=tk.Entry(donate_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    name_ent.place(x=240,y=140,width=200)
    name_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=name_ent))

    email_lb=tk.Label(donate_fm,text="Enter your Email ID",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    email_lb.place(x=20,y=180)
    email_ent=tk.Entry(donate_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    email_ent.place(x=240,y=180,width=200)
    email_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=email_ent))

    phno_lb=tk.Label(donate_fm,text="Enter your Phone Number",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    phno_lb.place(x=10,y=220)
    phno_ent=tk.Entry(donate_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    phno_ent.place(x=240,y=220,width=200)
    phno_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=phno_ent))

    address_lb=tk.Label(donate_fm,text="Enter your City",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    address_lb.place(x=20,y=260)
    address_ent=tk.Entry(donate_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    address_ent.place(x=240,y=260,width=200)
    address_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=address_ent))

    organisation_lb=tk.Label(donate_fm,text="Select the Ngo to Donate ",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    organisation_lb.place(x=10,y=300)
    organisation_ent=ttk.Combobox(donate_fm,values=data,font=("Helvetica",13,"bold"))
    organisation_ent.place(x=240,y=300,width=200)

    amount_lb=tk.Label(donate_fm,text="Enter the Amount",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    amount_lb.place(x=10,y=340)
    amount_ent=tk.Entry(donate_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    amount_ent.place(x=240,y=340,width=200)
    amount_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=amount_ent))

    login_btn=tk.Button(donate_fm,text='DONATE',font=("Helvetica",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=check_input_validation)
    login_btn.place(x=150,y=420,width=150,height=40)
    
    back_btn=tk.Button(donate_fm,text='back',font=("Helvetica",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=go_to_userdashboard)
    back_btn.place(x=30,y=490,height=20)

    donate_fm.pack(pady=5)
    donate_fm.pack_propagate(False)
    donate_fm.configure(width=480,height=580,bg='#FBF5EA')

def volunteer():
    dates = generate_random_dates()
    conn = sql.connect(host='localhost', password='ziyarawat@123', user='root', database="ngohub")
    cur = conn.cursor()
    cur.execute("SELECT name FROM ngolist")
    a= cur.fetchall()
    conn.close()
    data=[]
    for i in a:
        data.append(i[0])

    def go_to_userdashboard():
        volunteer_fm.destroy()
        root.update()
        user_dashboard()

    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')

    def check_input_validation():
        if name_ent.get()=='':
            name_ent.config(highlightcolor='red',highlightbackground='red')
            name_ent.focus()
            message_box(message='Full Name is Required')
        elif email_ent.get()=='':
            email_ent.config(highlightcolor='red',highlightbackground='red')
            email_ent.focus()
            message_box(message='Email ID is Required')
        elif phno_ent.get()=='':
            phno_ent.config(highlightcolor='red',highlightbackground='red')
            phno_ent.focus()
            message_box(message='Phone number is Required')
        elif address_ent.get()=='':
            address_ent.config(highlightcolor='red',highlightbackground='red')
            address_ent.focus()
            message_box(message='City Name is Required')
        elif organisation_ent.get()=='':
            message_box(message='NGO Name is Required')
        elif datev_ent.get()=='':
            message_box(message='Date is Required')
        else:
            add_volunteer(name=name_ent.get(),email=email_ent.get(),phno=phno_ent.get(),address=address_ent.get(),ngo=organisation_ent.get(),date=datev_ent.get())
            message_box("Thank you for Volunteering!!")

    volunteer_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(volunteer_fm,text='Volunteer At Ngos',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=480)

    quote_lb=tk.Label(volunteer_fm,text="VOLUNTEERS MAKE IT WORK!",font=("times",18,"bold"),fg=bg_color,bg='#FBF5EA')
    quote_lb.place(x=30,y=70)
  
    name_lb=tk.Label(volunteer_fm,text="Enter your name",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    name_lb.place(x=30,y=140)
    name_ent=tk.Entry(volunteer_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    name_ent.place(x=240,y=140,width=200)
    name_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=name_ent))

    email_lb=tk.Label(volunteer_fm,text="Enter your Email ID",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    email_lb.place(x=20,y=180)
    email_ent=tk.Entry(volunteer_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    email_ent.place(x=240,y=180,width=200)
    email_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=email_ent))

    phno_lb=tk.Label(volunteer_fm,text="Enter your Phone Number",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    phno_lb.place(x=10,y=220)
    phno_ent=tk.Entry(volunteer_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    phno_ent.place(x=240,y=220,width=200)
    phno_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=phno_ent))

    address_lb=tk.Label(volunteer_fm,text="Enter your City",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    address_lb.place(x=20,y=260)
    address_ent=tk.Entry(volunteer_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    address_ent.place(x=240,y=260,width=200)
    address_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=address_ent))

    organisation_lb=tk.Label(volunteer_fm,text="Select the Ngo to Donate ",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    organisation_lb.place(x=10,y=300)
    organisation_ent=ttk.Combobox(volunteer_fm,values=data,font=("Helvetica",13,"bold"))
    organisation_ent.place(x=240,y=300,width=200)

    datev_lb=tk.Label(volunteer_fm,text="Select the Date:",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    datev_lb.place(x=30,y=340)
    datev_ent=ttk.Combobox(volunteer_fm,values=dates,font=("Helvetica",13,"bold"))
    datev_ent.place(x=240,y=340,width=200)
    datev_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=datev_ent))

    login_btn=tk.Button(volunteer_fm,text='VOLUNTEER',font=("Helvetica",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=check_input_validation)
    login_btn.place(x=150,y=420,width=150,height=40)
    
    back_btn=tk.Button(volunteer_fm,text='back',font=("Helvetica",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=go_to_userdashboard)
    back_btn.place(x=30,y=490,height=20)

    volunteer_fm.pack(pady=5)
    volunteer_fm.pack_propagate(False)
    volunteer_fm.configure(width=480,height=580,bg='#FBF5EA')
    
def update_user():
    def go_to_userdashboard():
        update_user_fm.destroy()
        root.update()
        user_dashboard()

    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')

    def check_username():
        if currentusername_ent.get()=='':
            currentusername_ent.config(highlightcolor='red',highlightbackground='red')
            currentusername_ent.focus()
            message_box(message='Username is Required')
        elif not check_user_already_exist(currentusername_ent.get()):
            currentusername_ent.config(highlightcolor='red',highlightbackground='red')
            currentusername_ent.focus()
            message_box('Username does not exists')
        else:
            data=give_userdetails(currentusername_ent.get())
            def check_input_validation():
                if name_ent.get()=='':
                    name_ent.config(highlightcolor='red',highlightbackground='red')
                    name_ent.focus()
                    message_box(message='Full Name is Required')
                elif contact_ent.get()=='':
                    contact_ent.config(highlightcolor='red',highlightbackground='red')
                    contact_ent.focus()
                    message_box(message='Phone Number is Required')
                elif dob_ent.get()=='':
                    dob_ent.config(highlightcolor='red',highlightbackground='red')
                    dob_ent.focus()
                    message_box(message='birthdate is Required')
                elif email_ent.get()=='':
                    email_ent.config(highlightcolor='red',highlightbackground='red')
                    email_ent.focus()
                    message_box(message='Email id is Required')
                elif username_ent.get()=='':
                    username_ent.config(highlightcolor='red',highlightbackground='red')
                    username_ent.focus()
                    message_box(message='Username is Required')
                else:
                    update_user_details(name=name_ent.get(),contact=contact_ent.get(),
                                        dob=dob_ent.get(),email=email_ent.get(),username=username_ent.get(),currentusername=currentusername_ent.get())
                    message_box("successfully updated")

            heading2_lb=tk.Label(update_user_fm,text='Enter Details to be Updated',bg=bg_color,fg="white",font=("times",20,"bold"))
            heading2_lb.place(x=0,y=200,width=480)

            name_lb=tk.Label(update_user_fm,text="Enter your name",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            name_lb.place(x=30,y=270)
            name_ent=tk.Entry(update_user_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            name_ent.place(x=240,y=270,width=230)
            name_ent.focus()
            name_ent.insert(tk.END,data[0][0])
            name_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=name_ent))

            contact_lb=tk.Label(update_user_fm,text="Enter your phone number",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            contact_lb.place(x=10,y=310)
            contact_ent=tk.Entry(update_user_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            contact_ent.place(x=240,y=310,width=230)
            contact_ent.insert(tk.END,data[0][1])
            contact_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=contact_ent))


            dob_lb=tk.Label(update_user_fm,text="Enter your birthdate",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            dob_lb.place(x=20,y=350)
            dob_ent=tk.Entry(update_user_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            dob_ent.place(x=240,y=350,width=230)
            dob_ent.insert(tk.END,data[0][2])
            dob_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=dob_ent))

            email_lb=tk.Label(update_user_fm,text="Enter your email id",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            email_lb.place(x=20,y=390)
            email_ent=tk.Entry(update_user_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            email_ent.place(x=240,y=390,width=230)
            email_ent.insert(tk.END,data[0][3],)
            email_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=email_ent))

            username_lb=tk.Label(update_user_fm,text="Enter your username",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
            username_lb.place(x=20,y=430)
            username_ent=tk.Entry(update_user_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2)
            username_ent.place(x=240,y=430,width=230)
            username_ent.insert(tk.END,data[0][4])
            username_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=username_ent))
        
            update_btn=tk.Button(update_user_fm,text='Update',font=("Helvetica",15,"bold"),
                                bg=bg_color,fg='#FBF5EA',command=check_input_validation)
            update_btn.place(x=150,y=500,width=150,height=40)
        

            
    update_user_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(update_user_fm,text='Update User Details',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=480)

    currentusername_lb=tk.Label(update_user_fm,text="Enter your username",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    currentusername_lb.place(x=40,y=100)
    currentusername_ent=tk.Entry(update_user_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    currentusername_ent.place(x=220,y=100,width=200)
    currentusername_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=currentusername_ent))

    submit_btn=tk.Button(update_user_fm,text='Submit',font=("Helvetica",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=check_username)
    submit_btn.place(x=150,y=140,height=20)

    line_lb=tk.Label(update_user_fm,text="--"*39,font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    line_lb.place(x=0,y=170)

    back_btn=tk.Button(update_user_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=go_to_userdashboard)
    back_btn.place(x=5,y=43)

    update_user_fm.pack(pady=5)
    update_user_fm.pack_propagate(False)
    update_user_fm.configure(width=480,height=580,bg='#FBF5EA')

def update_password():
    def go_to_userdashboard():
        update_password_fm.destroy()
        root.update()
        user_dashboard()
    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')

    def show_hide_password():
        if currentpass_ent['show']=='*':
            currentpass_ent.config(show='')
            show_hide_btn.config(image=unlock_image)
        else:
            currentpass_ent.config(show='*')
            show_hide_btn.config(image=lock_image)

    def check_password():
        if currentpass_ent.get()=='':
            currentpass_ent.config(highlightcolor='red',highlightbackground='red')
            currentpass_ent.focus()
            message_box(message='Password is Required')
        elif not check_password_right(currentpass_ent.get()):
            currentpass_ent.config(highlightcolor='red',highlightbackground='red')
            currentpass_ent.focus()
            message_box('Password Wrong!!')
        else: 
            def show_hide_password2():
                if pass_ent['show']=='*':
                    pass_ent.config(show='')
                    show_hide_btn.config(image=unlock_image)
                else:
                    pass_ent.config(show='*')
                    show_hide_btn.config(image=lock_image)

            def check_input_validation():
                if pass_ent.get()=='':
                    pass_ent.config(highlightcolor='red',highlightbackground='red')
                    pass_ent.focus()
                    message_box(message='Password is Required')
                else:
                    update_password_sql(password=pass_ent.get(),currentpass=currentpass_ent.get())
                    message_box("Password Updated Successfully!")

            heading_lb=tk.Label(update_password_fm,text='Change Password',bg=bg_color,fg="white",font=("times",24,"bold"))
            heading_lb.place(x=0,y=270,width=480)

            pass_lb=tk.Label(update_password_fm,text="Enter Your New Password",font=("Helvetica",18,"bold"),fg=bg_color,bg='#FBF5EA')
            pass_lb.place(x=70,y=340)
            pass_ent=tk.Entry(update_password_fm,font=("Helvetica",18,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                                    highlightbackground="gray",highlightthickness=2,show="*")
            pass_ent.place(x=80,y=380,width=300,height=30)
            pass_ent.focus()
            pass_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=pass_ent))

            show_hide_btn=tk.Button(update_password_fm,image=lock_image,bd=0,bg='#FBF5EA',command=show_hide_password2)
            show_hide_btn.place(x=400,y=370)

            submit_btn=tk.Button(update_password_fm,text='Update Password',font=("Helvetica",15,"bold"),
                                bg=bg_color,fg='#FBF5EA',command=check_input_validation)
            submit_btn.place(x=150,y=450)


    update_password_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(update_password_fm,text='Update Password',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=480)

    currentpass_lb=tk.Label(update_password_fm,text="Enter Your Current Password",font=("Helvetica",18,"bold"),fg=bg_color,bg='#FBF5EA')
    currentpass_lb.place(x=60,y=100)
    currentpass_ent=tk.Entry(update_password_fm,font=("Helvetica",18,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2,show="*")
    currentpass_ent.place(x=80,y=140,width=300,height=30)
    currentpass_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=currentpass_ent))

    show_hide_btn=tk.Button(update_password_fm,image=lock_image,bd=0,bg='#FBF5EA',command=show_hide_password)
    show_hide_btn.place(x=400,y=130)

    submit_btn=tk.Button(update_password_fm,text='Submit',font=("Helvetica",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=check_password)
    submit_btn.place(x=190,y=200,height=20)

    line_lb=tk.Label(update_password_fm,text="--"*39,font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    line_lb.place(x=0,y=230)

    back_btn=tk.Button(update_password_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=go_to_userdashboard)
    back_btn.place(x=5,y=43)


    update_password_fm.pack(pady=5)
    update_password_fm.pack_propagate(False)
    update_password_fm.configure(width=480,height=580,bg='#FBF5EA')

def user_dashboard():
    def go_to_updatepassword():
        dashboard_fm.destroy()
        root.update()
        update_password()

    def go_to_updatedetails():
        dashboard_fm.destroy()
        root.update()
        update_user()

    def go_to_volunteer():
        dashboard_fm.destroy()
        root.update()
        volunteer()

    def go_to_donate():
        dashboard_fm.destroy()
        root.update()
        donate()

    def go_to_ngolist():
        dashboard_fm.destroy()
        root.update()
        ngolist()
    def forward_to_main_page():
        ans=confirmation_box(message="DO You Want To Logout?")
        if ans:
            dashboard_fm.destroy()
            root.update()
            main_page()

    dashboard_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(dashboard_fm,text='User Dashboard',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=400)

    back_btn=tk.Button(dashboard_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=forward_to_main_page)
    back_btn.place(x=5,y=43)


    view_btn=tk.Button(dashboard_fm,text='View Ngos List',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_ngolist)
    view_btn.place(x=70,y=70,width=250,height=50)
    donate_btn=tk.Button(dashboard_fm,text='Donate to Ngos',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_donate)
    donate_btn.place(x=70,y=140,width=250,height=50)
    volunteer_btn=tk.Button(dashboard_fm,text='Volunteer at Ngos',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_volunteer)
    volunteer_btn.place(x=70,y=210,width=250,height=50)
    update_details_btn=tk.Button(dashboard_fm,text='Update Personal Details',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_updatedetails)
    update_details_btn.place(x=70,y=280,width=250,height=50)
    update_password_btn=tk.Button(dashboard_fm,text='Update Password',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_updatepassword)
    update_password_btn.place(x=70,y=350,width=250,height=50)

    dashboard_fm.pack(pady=30)
    dashboard_fm.pack_propagate(False)
    dashboard_fm.configure(width=400,height=450,bg='#FBF5EA')

def user_login():

    def forward_to_main_page():
        user_login_page_fm.destroy()
        root.update()
        main_page()

    def forward_to_create_page():
        user_login_page_fm.destroy()
        root.update()
        create_account_page()

    
    def show_hide_password():
        if password_ent['show']=='*':
            password_ent.config(show='')
            show_hide_btn.config(image=unlock_image)
        else:
            password_ent.config(show='*')
            show_hide_btn.config(image=lock_image)

    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')

    def check_input_validation():
        if username_ent.get()=='':
            username_ent.config(highlightcolor='red',highlightbackground='red')
            username_ent.focus()
            message_box(message='Username is Required')
        elif password_ent.get()=='':
            password_ent.config(highlightcolor='red',highlightbackground='red')
            password_ent.focus()
            message_box(message='Password is Required')
        elif not check_user_already_exist(username_ent.get()):
            username_ent.config(highlightcolor='red',highlightbackground='red')
            username_ent.focus()
            message_box('Username does not exists')
        else:
            a=user_password_match(username=username_ent.get(),password=password_ent.get())
            if a==1:
                user_login_page_fm.destroy()
                root.update()
                user_dashboard()
            else:
                password_ent.config(highlightcolor='red',highlightbackground='red')
                password_ent.focus()
                message_box("Password Wrong!")



    #user login page
    user_login_page_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(user_login_page_fm,text='User Login Page',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=400)
    
    #back button
    back_btn=tk.Button(user_login_page_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=forward_to_main_page)
    back_btn.place(x=5,y=43)


    user_icon_lb=tk.Label(user_login_page_fm,image=user_image,bg='#FBF5EA')
    user_icon_lb.place(x=150,y=50)

    #username label and button
    username_lb=tk.Label(user_login_page_fm,text="Enter the Username-",font=("Helvetica",15,"bold"),fg=bg_color,bg='#FBF5EA')
    username_lb.place(x=90,y=140)
    username_ent=tk.Entry(user_login_page_fm,font=("Helvetica",15,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                        highlightbackground="gray",highlightthickness=2)
    username_ent.place(x=90,y=190)
    username_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=username_ent))

    #password label and button
    password_lb=tk.Label(user_login_page_fm,text="Enter the Password-",font=("Helvetica",15,"bold"),fg=bg_color,bg='#FBF5EA')
    password_lb.place(x=90,y=240)
    password_ent=tk.Entry(user_login_page_fm,font=("Helvetica",15,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                        highlightbackground="gray",highlightthickness=2,show="*")
    password_ent.place(x=90,y=290)
    password_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=password_ent))
    

    #lock hide button
    show_hide_btn=tk.Button(user_login_page_fm,image=lock_image,bd=0,bg='#FBF5EA',command=show_hide_password)
    show_hide_btn.place(x=320,y=280)

    #login button
    login_btn=tk.Button(user_login_page_fm,text='Login',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=check_input_validation)
    login_btn.place(x=105,y=340,width=200,height=40)

    #create your account button
    create_account_btn=tk.Button(user_login_page_fm,text="⚠️\nCreate your account",fg=bg_color,bd=0,
                                bg='#FBF5EA',command=forward_to_create_page)
    create_account_btn.place(x=150,y=390)

    user_login_page_fm.pack(pady=30)
    user_login_page_fm.pack_propagate(False)
    user_login_page_fm.configure(width=400,height=450,bg='#FBF5EA')

def admin_dashboard():
    def go_to_volunteerlist():
        dashboard_fm.destroy()
        root.update()
        volunteer_list()
    def go_to_userlist():
        dashboard_fm.destroy()
        root.update()
        user_list()
    def go_to_donationlist():
        dashboard_fm.destroy()
        root.update()
        donation_list()
    def go_to_manage():
        dashboard_fm.destroy()
        root.update()
        manage_ngos()

    def go_to_ngolist():
        dashboard_fm.destroy()
        root.update()
        ngoadmin()

    def forward_to_main_page():
        ans=confirmation_box(message="DO You Want To Logout?")
        if ans:
            dashboard_fm.destroy()
            root.update()
            main_page()

    dashboard_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(dashboard_fm,text='Admin Dashboard',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=400)

    back_btn=tk.Button(dashboard_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=forward_to_main_page)
    back_btn.place(x=5,y=43)

    upadte_ngos_btn=tk.Button(dashboard_fm,text='Manage Ngos List',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_manage)
    upadte_ngos_btn.place(x=70,y=70,width=250,height=50)
    seedonation_btn=tk.Button(dashboard_fm,text='View Donations List',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_donationlist)
    seedonation_btn.place(x=70,y=140,width=250,height=50)
    seevolunteer_btn=tk.Button(dashboard_fm,text='View Volunteer List',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_volunteerlist)
    seevolunteer_btn.place(x=70,y=210,width=250,height=50)
    seeuser_details_btn=tk.Button(dashboard_fm,text='View User List',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_userlist)
    seeuser_details_btn.place(x=70,y=280,width=250,height=50)
    viewngo_btn=tk.Button(dashboard_fm,text='View Ngos',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=go_to_ngolist)
    viewngo_btn.place(x=70,y=350,width=250,height=50)
    
    dashboard_fm.pack(pady=30)
    dashboard_fm.pack_propagate(False)
    dashboard_fm.configure(width=400,height=450,bg='#FBF5EA')

def admin_login():

    def forward_to_main_page():
        admin_login_page_fm.destroy()
        root.update()
        main_page()
    def show_hide_password():
            if password_ent['show']=='*':
                password_ent.config(show='')
                show_hide_btn.config(image=unlock_image)
            else:
                password_ent.config(show='*')
                show_hide_btn.config(image=lock_image)

    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')

    def check_input_validation():
        if username_ent.get()=='':
            username_ent.config(highlightcolor='red',highlightbackground='red')
            username_ent.focus()
            message_box(message='Username is Required')
        elif password_ent.get()=='':
            password_ent.config(highlightcolor='red',highlightbackground='red')
            password_ent.focus()
            message_box(message='Password is Required')
        elif not check_admin_already_exist(username_ent.get()):
            username_ent.config(highlightcolor='red',highlightbackground='red')
            username_ent.focus()
            message_box('Admin does not exists')
        else:
            a=admin_password_match(username=username_ent.get(),password=password_ent.get())
            if a==1:
                admin_login_page_fm.destroy()
                root.update()
                admin_dashboard()
            else:
                password_ent.config(highlightcolor='red',highlightbackground='red')
                password_ent.focus()
                message_box("Password Wrong!")



    #admin login page
    admin_login_page_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    
    heading_lb=tk.Label(admin_login_page_fm,text='Admin Login Page',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=400)

    #back button
    back_btn=tk.Button(admin_login_page_fm,text='←',font=('bold',20),fg=bg_color,bd=0,bg='#FBF5EA',command=forward_to_main_page)
    back_btn.place(x=5,y=43)

    user_icon_lb=tk.Label(admin_login_page_fm,image=admin_image,bg='#FBF5EA')
    user_icon_lb.place(x=150,y=50)

    #username label and button
    username_lb=tk.Label(admin_login_page_fm,text="Enter the Username-",font=("Helvetica",15,"bold"),fg=bg_color,bg='#FBF5EA')
    username_lb.place(x=90,y=140)
    username_ent=tk.Entry(admin_login_page_fm,font=("Helvetica",15,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    username_ent.place(x=90,y=190)
    username_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=username_ent))

    #password label and button
    password_lb=tk.Label(admin_login_page_fm,text="Enter the Password-",font=("Helvetica",15,"bold"),fg=bg_color,bg='#FBF5EA')
    password_lb.place(x=90,y=240)
    password_ent=tk.Entry(admin_login_page_fm,font=("Helvetica",15,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2,show="*")
    password_ent.place(x=90,y=290)
    password_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=password_ent))

    #lock hide button
    show_hide_btn=tk.Button(admin_login_page_fm,image=lock_image,bd=0,bg='#FBF5EA',command=show_hide_password)
    show_hide_btn.place(x=320,y=280)

    #login button
    login_btn=tk.Button(admin_login_page_fm,text='Login',font=("Helvetica",15,"bold"),bg=bg_color,fg='#FBF5EA',command=check_input_validation)
    login_btn.place(x=105,y=340,width=200,height=40)

    admin_login_page_fm.pack(pady=30)
    admin_login_page_fm.pack_propagate(False)
    admin_login_page_fm.configure(width=400,height=450,bg='#FBF5EA')

def create_account_page():
    
    def forward_to_main_page():
        ans=confirmation_box(message="DO You Want To Leave\n This Page?")
        if ans:
            create_account_page_fm.destroy()
            root.update()
            main_page()
    
    def remove_highligth_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!="":
                entry.config(highlightcolor='gray',highlightbackground='gray')



    def check_input_validation():
        if name_ent.get()=='':
            name_ent.config(highlightcolor='red',highlightbackground='red')
            name_ent.focus()
            message_box(message='Full Name is Required')
        elif contact_ent.get()=='':
            contact_ent.config(highlightcolor='red',highlightbackground='red')
            contact_ent.focus()
            message_box(message='Phone Number is Required')
        elif dob_ent.get()=='':
            dob_ent.config(highlightcolor='red',highlightbackground='red')
            dob_ent.focus()
            message_box(message='birthdate is Required')
        elif email_ent.get()=='':
            email_ent.config(highlightcolor='red',highlightbackground='red')
            email_ent.focus()
            message_box(message='Email id is Required')
        elif username_ent.get()=='':
            username_ent.config(highlightcolor='red',highlightbackground='red')
            username_ent.focus()
            message_box(message='Username is Required')
        elif passw_ent.get()=='':
            passw_ent.config(highlightcolor='red',highlightbackground='red')
            passw_ent.focus()
            message_box(message='Password is Required')
        elif rpassw_ent.get()=='':
            rpassw_ent.config(highlightcolor='red',highlightbackground='red')
            rpassw_ent.focus()
            message_box(message='Re-Enter the password')
        elif passw_ent.get()!=rpassw_ent.get():
            rpassw_ent.config(highlightcolor='red',highlightbackground='red')
            rpassw_ent.focus()
            message_box(message='Re-entered password \n does not match')
        elif check_user_already_exist(username_ent.get()):
            message_box('Username already exists')
            
        else:
            add_user(name=name_ent.get(),phno=contact_ent.get(),dob=dob_ent.get(),email=email_ent.get(),username=username_ent.get(),password=passw_ent.get())
            message_box('Account successfully created')

    create_account_page_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    heading_lb=tk.Label(create_account_page_fm,text='Create Account',bg=bg_color,fg="white",font=("times",24,"bold"))
    heading_lb.place(x=0,y=0,width=480)

    #creating image
    create_icon_lb=tk.Label(create_account_page_fm,image=create_image,bg='#FBF5EA')
    create_icon_lb.place(x=200,y=50)
    #label and entry for entries
    name_lb=tk.Label(create_account_page_fm,text="Enter your name",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    name_lb.place(x=30,y=140)
    name_ent=tk.Entry(create_account_page_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    name_ent.place(x=240,y=140,width=200)
    name_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=name_ent))

    contact_lb=tk.Label(create_account_page_fm,text="Enter your phone number",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    contact_lb.place(x=10,y=180)
    contact_ent=tk.Entry(create_account_page_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    contact_ent.place(x=240,y=180,width=200)
    contact_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=contact_ent))

    dob_lb=tk.Label(create_account_page_fm,text="Enter your birthdate",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    dob_lb.place(x=20,y=220)
    dob_ent=tk.Entry(create_account_page_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    dob_ent.place(x=240,y=220,width=200)
    dob_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=dob_ent))

    email_lb=tk.Label(create_account_page_fm,text="Enter your email id",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    email_lb.place(x=20,y=260)
    email_ent=tk.Entry(create_account_page_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    email_ent.place(x=240,y=260,width=200)
    email_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=email_ent))

    username_lb=tk.Label(create_account_page_fm,text="Enter your username",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    username_lb.place(x=20,y=300)
    username_ent=tk.Entry(create_account_page_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    username_ent.place(x=240,y=300,width=200)
    username_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=username_ent))

    passw_lb=tk.Label(create_account_page_fm,text="Create account password",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    passw_lb.place(x=10,y=340)
    passw_ent=tk.Entry(create_account_page_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    passw_ent.place(x=240,y=340,width=200)
    passw_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=passw_ent))

    rpassw_lb=tk.Label(create_account_page_fm,text="Re-enter account password",font=("Helvetica",13,"bold"),fg=bg_color,bg='#FBF5EA')
    rpassw_lb.place(x=10,y=380)
    rpassw_ent=tk.Entry(create_account_page_fm,font=("Helvetica",13,"bold"),justify=tk.CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)
    rpassw_ent.place(x=240,y=380,width=200)
    rpassw_ent.bind('<KeyRelease>',lambda e:remove_highligth_warning(entry=rpassw_ent))


    login_btn=tk.Button(create_account_page_fm,text='Submit',font=("Helvetica",15,"bold"),
                        bg=bg_color,fg='#FBF5EA',command=check_input_validation)
    login_btn.place(x=150,y=420,width=150,height=40)

    home_btn=tk.Button(create_account_page_fm,text='Home',font=("Helvetica",12,"bold"),bg=bg_color,fg='#FBF5EA',command=forward_to_main_page)
    home_btn.place(x=200,y=480)


    create_account_page_fm.pack(pady=5)
    create_account_page_fm.pack_propagate(False)
    create_account_page_fm.configure(width=480,height=580,bg='#FBF5EA')

def written_page():
    def forward_to_main():
        main1_page.destroy()
        root.update()
        main_page()
    main1_page=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    main1_page.pack(pady=30)
    heading_lb=tk.Label(main1_page,text='We see the opportunity\nto make a difference',fg="green",font=("times",25,"bold"))
    heading_lb.place(x=0,y=0,width=390)
    heading2_lb=tk.Label(main1_page,text='What we do?',fg="black",font=("times",18,"bold"))
    heading2_lb.place(x=0,y=90,width=390)
    heading2_lb=tk.Label(main1_page,text='NGO hub is a platform dedicated to\nenable,empower and serve NGOs.\nWe connect NGOs to volunteers and\n donations.We connect NGOs to\neach other to inspire.'
    ,fg="black",font=("times",15))
    heading2_lb.place(x=0,y=130,width=390)
    button=tk.Button(main1_page,text="Get Involved",bg="#822D99",fg='white',font=("times",15,"bold"),
                               bd=0,command=forward_to_main)
    button.place(x=100,y=300,width=200)
    main1_page.pack_propagate(False)
    main1_page.configure(width=400,height=420)
written_page()
root.mainloop()


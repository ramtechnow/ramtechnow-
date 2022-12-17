from audioop import add
from cProfile import label
from calendar import c
import logging
from queue import Full
from re import A
from select import select
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import clear, position, update
from unittest import result
from wsgiref.simple_server import software_version
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="shriram",
    database="project1"
    )
mycursor=mydb.cursor()

root = Tk()

#---------------------------------------FrontpageFrame
def frontpage_frame():
    root.title("Employee Management System")
    root.geometry("1000x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")
    global img2
    img2 =PhotoImage(file=r"C:\Users\Sri Ram\Desktop\bg6.png")
    # img3=Label( root , image = img2) . place (x=0,y=0, anchor="nw")
    global my_canvas
    my_canvas =Canvas( root , width=1000 , height=1080)
    my_canvas.pack( fill = "both" , expand = True)
    my_canvas.create_image(625,250,image=img2,anchor="center")
     
    my_canvas.create_text ( 675 , 100 ,text = " Ram Technologies Pvt Ltd " , font = ( "elephant",25,"bold" ), fill = "orange" )
    global btnADMIN
    btnADMIN=Button(root,command=adminlogin_frame,text="Admin",width=20, font=("arial bold", 22), bg="yellow", fg="red",borderwidth=3)
    btnADMIN.place(x = 500 , y = 250)
    global btnEmployee
    btnEmployee=Button(root, command=onedetailview_frame ,text="Employee",width=20, font=("arial bold", 22), bg="aquamarine", fg="red",borderwidth=3)
    btnEmployee.place(x =500 , y = 400)
    
#---------------------------------------AdminLoginFrame    
def adminlogin_frame():
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="white")
    root.state("zoomed")
    
    Employeename=StringVar()
    password=StringVar()
    global AdminLogin_frame
    AdminLogin_frame=Frame(root,width=700,height=450,bg="white")
    AdminLogin_frame.place(x=350,y=150)
    img3 =PhotoImage(file=r"C:\Users\Sri Ram\Desktop\bg5.png")
    lblimg1=Label(AdminLogin_frame,image=img3,bg="black") 
    lblimg1.place(x=0,y=0)
    img4 =PhotoImage(file=r"C:\Users\Sri Ram\Desktop\1login.png")
    lblimg1=Label(AdminLogin_frame,image=img4,bg="white",borderwidth=4) 
    lblimg1.place(x=20,y=100)
    title = Label(AdminLogin_frame, text="Admin login",width=15, font=("lithograph", 25, "bold"), bg="red", fg="white")
    title.place(x=220,y=50)

    lblEmployee = Label(AdminLogin_frame, text="Username", font=("cornerstone", 16), bg="red", fg="white")
    lblEmployee.place(x=200,y=150)
    txtEmployee = Entry(AdminLogin_frame, textvariable=Employeename, font=("cornerstone", 16), width=25,bd=5)
    txtEmployee.insert(0,"admin")
    txtEmployee.place(x=320,y=150)

    lblpass = Label(AdminLogin_frame, text="Password", font=("cornerstone", 16), bg="red", fg="white")
    lblpass.place(x=200,y=230)
    txtpass = Entry(AdminLogin_frame, textvariable=password,show="*", font=("cornerstone", 16,), width=25,fg="black",bg="white",bd=5)
    txtpass.place(x=320,y=230)
    def showpass():
        p=txtpass.get()
        lbl=Label(AdminLogin_frame,width=30,text=f"{p}",font=("cornerstone", 13), bg="#66dcfa", fg="black")
        lbl.place(x=230,y=280)
    def Ladminlogin():
        username=txtEmployee.get()
        password=txtpass.get()
        if username=="" or password=="":
            messagebox.showerror("Error Input","Please give input username and password")
        elif username=="admin" and password=="welcome":
            adminpage_frame()
        elif username!="admin":
            messagebox.showerror("Error input","Incorrect username")
            txtEmployee.delete(0,END)
            txtEmployee.insert(0,"admin")
            txtpass.delete(0,END)
        else:
            txtpass.delete(0,END)
            messagebox.showerror("Error input","Incorrect password")
    btnlogin=Button(AdminLogin_frame, command=Ladminlogin ,text="Login",width=15, font=("cornerstone", 16), bg="blue", fg="white",bd=3).place(x=300,y=350)
    btnshowpass=Button(AdminLogin_frame,command=showpass,text="Show Password",width=12, font=("cornerstone", 10), bg="red", fg="white",bd=0).place(x=350,y=300)

    root.mainloop()

#---------------------------------------admin_page_frame
def adminpage_frame():
    AdminLogin_frame.destroy() 
    btnADMIN.destroy()
    btnEmployee.destroy()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")

    title = Label(root, text="Admin",width=10, font=("elephant", 25, "bold"), bg="indianred", fg="white")
    title.place(x=0,y=1)
    
    global btnadd
    btnadd=Button(root, command=entries_frame ,text="Add Employee",width=50, font=("cornerstone", 15), bg="cyan", fg="#000000",bd=2)
    btnadd.place(x=400,y=200)
    global btndelete
    btndelete=Button(root, command=Delete_frame ,text="Delete Employee",width=50, font=("cornerstone", 15), bg="red", fg="white",bd=2)
    btndelete.place(x=400,y=250)
    global btnupdate
    btnupdate=Button(root, command=update_frame ,text="Update Employee details",width=50, font=("cornerstone", 15), bg="orange", fg="white",bd=2)
    btnupdate.place(x=400,y=300)
    global btnview
    btnview=Button(root, command=onedetailview_frame ,text="View Employee details",width=50, font=("cornerstone", 15), bg="brown", fg="white",bd=2)
    btnview.place(x=400,y=350)
    global btnallview
    btnallview=Button(root, command=alldetails,text="All Employees details",width=50, font=("cornerstone", 15), bg="purple", fg="white",bd=2)
    btnallview.place(x=400,y=400)


#-------------------------------------entries_frame
def entries_frame():
    root1 = Tk()
    root1.title("Employee Management System")
    root1.geometry("1920x1080+0+0")
    root1.config(bg="maroon")
    root1.state("zoomed")

    name = StringVar()
    age = StringVar( )
    doj = StringVar()
    gender = StringVar()
    email = StringVar()
    contact = StringVar()
    position=StringVar()
    Employee_ID=StringVar()

    Entries_frame = Frame(root1, bg="maroon")
    Entries_frame.pack(side=TOP, fill=X)
    title = Label(Entries_frame, text="Add Employee", font=("bazooka", 18, "bold"), bg="maroon", fg="white")
    title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

    lblName = Label(Entries_frame, text="Name", font=("bazooka", 15), bg="maroon", fg="white")
    lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtName = Entry(Entries_frame, textvariable=name, font=("bazooka", 15), width=30)
    txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    lblAge = Label(Entries_frame, text="Age", font=("bazooka", 15), bg="maroon", fg="white")
    lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtAge = Entry(Entries_frame, textvariable=age, font=("bazooka", 15), width=30)
    txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    lbldoj = Label(Entries_frame, text="D.O.J", font=("bazooka", 15), bg="maroon", fg="white")
    lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    txtDoj = Entry(Entries_frame, textvariable=doj, font=("bazooka", 15), width=30)
    txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    lblEmail = Label(Entries_frame, text="Email", font=("bazooka", 15), bg="maroon", fg="white")
    lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtEmail = Entry(Entries_frame, textvariable=email, font=("bazooka", 15), width=30)
    txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    lblGender = Label(Entries_frame, text="Gender", font=("bazooka", 15), bg="maroon", fg="white")
    lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    comboGender = ttk.Combobox(Entries_frame, font=("bazooka", 15), width=28, textvariable=gender, state="readonly")
    comboGender['values'] = ("Male", "Female")
    comboGender.grid(row=3, column=1, padx=10, sticky="w")

    lblContact_no= Label(Entries_frame, text="Contact No", font=("bazooka", 15), bg="maroon", fg="white")
    lblContact_no.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtContact_no= Entry(Entries_frame, textvariable=contact, font=("bazooka", 15), width=30)
    txtContact_no.grid(row=3, column=3, padx=10, sticky="w")

    lblEmployee_ID = Label(Entries_frame, text="Employee ID", font=("bazooka", 15), bg="maroon", fg="white")
    lblEmployee_ID.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    txtEmployee_ID =Entry(Entries_frame, textvariable=Employee_ID, font=("bazooka", 15), width=30)
    txtEmployee_ID.grid(row=4, column=1, padx=10, sticky="w")

    lblPosition = Label(Entries_frame, text="Position", font=("bazooka", 15), bg="maroon", fg="white")
    lblPosition.grid(row=4, column=2, padx=10, pady=10, sticky="w")
    comboPosition = ttk.Combobox(Entries_frame, font=("bazooka", 15), width=28, textvariable=position, state="readonly")
    comboPosition["values"] = ("Marketing Manager", "Human Resource","Administrative Assistant","Product Manager","Sales Associate","Sales Manager","Business Analyst","Book Keeper","software Engineer")
    comboPosition.grid(row=4, column=3, padx=10, sticky="w")
    
    #---------------------------tree view
    tree_frame = Frame(root1, bg="maroon")
    tree_frame.place(x=0, y=400 , width=1400, height=1000)
    # tree_frame.grid(row=5,column=0,pady=10)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('cornerstone', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('cornerstone', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact_no")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employee_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll() 
    def clearall():
        txtName.delete(0,END)
        txtAge.delete(0,END)
        txtDoj.delete(0,END)
        comboGender.set("")
        txtEmail.delete(0,END)
        txtContact_no.delete(0,END)
        comboPosition.set("")
        txtEmployee_ID.delete(0,END)
    def add_details():
        sql="insert into employee_details (Employee_Id,Name,Age,DOJ,Email,Gender,Contact_No,Position) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(txtEmployee_ID.get(),txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact_no.get(),comboPosition.get())
        if txtEmployee_ID.get()=="" or txtName.get()=="" or txtAge.get()==""or txtDoj.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact_no.get()=="" or comboPosition.get()=="":
            messagebox.showerror("Input error","please fill all details")
            root.destroy()
            entries_frame()
            a=StringVar()
            if txtAge.get()==a:
                messagebox.showerror("Input Error","Give age in number") 
                root.destroy()
                entries_frame()
        else:
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data Inserted succesfully")
            displayAll()
            clearall()
    
    btnADD=Button(Entries_frame, command=add_details ,text="Add",width=20, font=("bazooka", 18), bg="green", fg="white",bd=3).grid(row=6,column=1,padx=10,pady=10)
    btnclear=Button(Entries_frame, command=clearall ,text="clear",width=20, font=("bazooka", 18), bg="orange", fg="white",bd=3).grid(row=6,column=2,padx=10,pady=10)
    #btncancel=Button(Entries_frame, command=root.quit ,text="cancel",width=20, font=("bazooka", 16), bg="red", fg="white",bd=3).grid(row=6,column=3,padx=20,pady=10)


#---------------------------------------delete_frame
def Delete_frame():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")

    id=StringVar()
    delete_frame= Frame(root, bg="firebrick",width=500,height=300)
    delete_frame.place(x=10,y=10)
    title = Label(delete_frame, text="Delete Employee", font=("bazooka", 25, "bold"), bg="firebrick", fg="white")
    title.place(x=10,y=10)

    lblid = Label(delete_frame, text="Enter Employee id", font=("bazooka", 16), bg="firebrick", fg="white")
    lblid.place(x=10,y=100)
    txtid = Entry(delete_frame, textvariable=id, font=("cornerstone", 16), width=30)
    txtid.place(x=200,y=100)

    tree_frame = Frame(root, bg="firebrick")
    tree_frame.place(x=0, y=450 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('cornerstone', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('cornerstone', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employee_details")
        global rows
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()
    def delete():
        sql1="select Employee_Id from employee_details"
        mycursor.execute(sql1)
        result=mycursor.fetchall()
        print(result)
        if txtid.get()=="":
            messagebox.showerror("Input error","Give input")
            root.destroy()
            Delete_frame()
        elif (txtid.get(),) in result:
            sql="delete from employee_details where Employee_Id=%s"
            value=(txtid.get(),)
            mycursor.execute(sql,value)
            mydb.commit()
            print("deleted successfully")
            displayAll()
            txtid.delete(0,END)
        else:
            messagebox.showerror("error input","Give valid Input")
            root.destroy()
            Delete_frame()

    btnconfirm=Button(delete_frame, command=delete ,text="Confirm",width=15, font=("bazooka", 15), bg="red", fg="white",bd=3).place(x=200,y=200)
    #btncancel=Button(delete_frame, command=root.quit ,text="Cancel",width=15, font=("bazooka", 15), bg="red", fg="white",bd=3).place(x=320,y=200)


#---------------------------------------Update_frame
def update_frame():
    #root = Tk()
    btnadd.destroy()
    btndelete.destroy()
    btnupdate.destroy()
    btnview.destroy()
    btnallview.destroy()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")

    lblid = Label(root, text="Select detail to update :", font=("bazooka", 18), bg="firebrick", fg="white")
    lblid.place(x=400,y=230)

    btnposition=Button(root, command=positionupdate_frame ,text="Position",width=25, font=("cornerstone", 15), bg="red", fg="white",bd=0)
    btnposition.place(x=600,y=300)
    btnEmail=Button(root, command=emailupdate_frame ,text="Email",width=25, font=("cornerstone", 15), bg="red", fg="white",bd=0)
    btnEmail.place(x=600,y=350)
    btnContact=Button(root, command=contactupdate_frame,text="Contact No.",width=25, font=("cornerstone", 15), bg="red", fg="white",bd=0)
    btnContact.place(x=600,y=400)

#---------------------------------------Position_update
def positionupdate_frame():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")

    position_frame= Frame(root, bg="firebrick")
    position_frame.pack(side=TOP, fill=X)
    position_update= Label(position_frame, text="Position Update", font=("bazooka", 18, "bold"), bg="firebrick", fg="white")
    position_update.grid(row=0, columnspan=15, padx=10, pady=20, sticky="W")

    Employee_id=StringVar()
    employee_id = Label(position_frame, text="Enter employee ID ", font=("bazooka", 15), bg="firebrick", fg="white")
    employee_id.grid(row=1, column=1, padx=10, pady=20, sticky="W")
    txtemployee_id = Entry(position_frame, textvariable=Employee_id, font=("bazooka", 15), width=30)
    txtemployee_id.grid(row=1, column=2, padx=10, sticky="w")

    old_position = Label(position_frame, text="Old Position ", font=("bazooka", 15), bg="firebrick", fg="white")
    old_position.grid(row=2, column=1, padx=10, pady=20, sticky="W")
    oldcomboposition = ttk.Combobox(position_frame, font=("bazooka", 15), width=28, textvariable=position, state="readonly")
    oldcomboposition["values"] = ("Marketing Manager", "Human Resource","Administrative Assistant","Product Manager","Sales Associate","Sales Manager","Business Analyst","Book Keeper","software Engineer")
    oldcomboposition.grid(row=2, column=2, padx=10, sticky="w")

    new_position = Label(position_frame, text="New Position ", font=("bazooka", 15), bg="firebrick", fg="white")
    new_position.grid(row=3, column=1, padx=10, pady=20, sticky="W")
    newcomboposition = ttk.Combobox(position_frame, font=("bazooka", 15), width=28, textvariable=position, state="readonly")
    newcomboposition["values"] = ("Marketing Manager", "Human Resource","Administrative Assistant","Product Manager","Sales Associate","Sales Manager","Business Analyst","Book Keeper","software Engineer")
    newcomboposition.grid(row=3, column=2, padx=10, sticky="w")

    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=400 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('cornerstone', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('cornerstone', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employee_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()
    def posupdate():
        sql1="select Employee_Id from employee_details"
        mycursor.execute(sql1)
        result=mycursor.fetchall()
        print(result)
        sql2="select Position from employee_details"
        mycursor.execute(sql2)
        result1=mycursor.fetchall()
        print(result1)
        try:
            if oldcomboposition.get()=="" or txtemployee_id.get()=="":
                messagebox.showerror("Error Input"," Give all input")
                root.destroy()
                posupdate()
            elif (oldcomboposition.get(),) in result1 and (txtemployee_id.get(),) in result:
                sql="update employee_details set Position=%s where Position=%s and Employee_Id=%s"
                val=(newcomboposition.get(),oldcomboposition.get(),txtemployee_id.get()) 
                result2=mycursor.execute(sql,val)
                mydb.commit()
                print("Updated successfully")
                messagebox.Message("Updated successfully")
                displayAll()
        except:
            messagebox.showerror("Error Input","Please give valid Employee ID and Position")
            root.destroy()
            posupdate()

    btnconfirm=Button(position_frame, command=posupdate ,text="Confirm",width=15, font=("bazooka", 15), bg="red", fg="white",bd=3).grid(row=4,columnspan=3,padx=10,pady=10)

#---------------------------------------email_update
def emailupdate_frame():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")

    Email_frame= Frame(root, bg="firebrick")
    Email_frame.pack(side=TOP, fill=X)
    Email_update= Label(Email_frame, text="Email Update", font=("bazooka", 18, "bold"), bg="firebrick", fg="white")
    Email_update.grid(row=0, columnspan=15, padx=10, pady=20, sticky="W")

    Employee_id=StringVar()
    employee_id = Label(Email_frame, text="Enter employee ID ", font=("bazooka", 15), bg="firebrick", fg="white")
    employee_id.grid(row=1, column=1, padx=10, pady=20, sticky="W")
    txtemployee_id = Entry(Email_frame, textvariable=Employee_id, font=("bazooka", 15), width=30)
    txtemployee_id.grid(row=1, column=2, padx=10, sticky="w")

    oldemail=StringVar()
    newemail=StringVar()

    old_Email = Label(Email_frame, text="Old Email ", font=("bazooka", 15), bg="firebrick", fg="white")
    old_Email.grid(row=2, column=1, padx=10, pady=20, sticky="W")
    txtoldemail = Entry(Email_frame, textvariable=oldemail, font=("bazooka", 15), width=30)
    txtoldemail.grid(row=2, column=2, padx=10, sticky="w")

    new_Email = Label(Email_frame, text="New Email ", font=("bazooka", 15), bg="firebrick", fg="white")
    new_Email.grid(row=3, column=1, padx=10, pady=20, sticky="W")
    txtnewemail = Entry(Email_frame, textvariable=newemail, font=("bazooka", 15), width=30)
    txtnewemail.grid(row=3, column=2, padx=10, sticky="w")

    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=400 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('cornerstone', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('cornerstone', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employee_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()

    def emailupdate():
        sql1="select Employee_Id from employee_details"
        mycursor.execute(sql1)
        result=mycursor.fetchall()
        print(result)
        sql2="select Email from employee_details"
        mycursor.execute(sql2)
        result1=mycursor.fetchall()
        print(result1)
        try:
            if txtoldemail.get()=="" or txtemployee_id.get()=="" or txtnewemail.get()=="":
                messagebox.showerror("Error Input"," Give all input")
                root.destroy()
                emailupdate()
            elif (txtoldemail.get(),) in result1 and (txtemployee_id.get(),) in result:
                sql="update employee_details set Email=%s where Email=%s and Employee_Id=%s"
                val=(txtnewemail.get(),txtoldemail.get(),txtemployee_id.get()) 
                result2=mycursor.execute(sql,val)
                mydb.commit()
                print("Updated successfully")
                messagebox.Message("Updated successfully")
                displayAll()
        except:
            messagebox.showerror("Error Input","Please give valid Employee ID and email")
            root.destroy()
            emailupdate()

    btnclear=Button(Email_frame, command=emailupdate ,text="Confirm",width=15, font=("bazooka", 15), bg="red", fg="white",bd=3).grid(row=4,columnspan=3,padx=10,pady=10)

#---------------------------------------contact_update
def contactupdate_frame():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")

    Contact_frame= Frame(root, bg="firebrick")
    Contact_frame.pack(side=TOP, fill=X)
    Contact_update= Label(Contact_frame, text="Contact Update", font=("bazooka", 18, "bold"), bg="firebrick", fg="white")
    Contact_update.grid(row=0, columnspan=15, padx=10, pady=20, sticky="W")

    Employee_id=StringVar()
    employee_id = Label(Contact_frame, text="Enter employee ID ", font=("bazooka", 15), bg="firebrick", fg="white")
    employee_id.grid(row=1, column=1, padx=10, pady=20, sticky="W")
    txtemployee_id = Entry(Contact_frame, textvariable=Employee_id, font=("bazooka", 15), width=30)
    txtemployee_id.grid(row=1, column=2, padx=10, sticky="w")

    oldContact=StringVar()
    newContact=StringVar()

    old_Contact = Label(Contact_frame, text="Old Contact No. ", font=("bazooka", 15), bg="firebrick", fg="white")
    old_Contact.grid(row=2, column=1, padx=10, pady=20, sticky="W")
    txtoldContact = Entry(Contact_frame, textvariable=oldContact, font=("bazooka", 15), width=30)
    txtoldContact.grid(row=2, column=2, padx=10, sticky="w")

    new_Contact = Label(Contact_frame, text="New Contact No.", font=("bazooka", 15), bg="firebrick", fg="white")
    new_Contact.grid(row=3, column=1, padx=10, pady=20, sticky="W")
    txtnewContact = Entry(Contact_frame, textvariable=newContact, font=("bazooka", 15), width=30)
    txtnewContact.grid(row=3, column=2, padx=10, sticky="w")

    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=400 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('cornerstone', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('cornerstone', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employee_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()

    def conupdate():
        sql1="select Employee_Id from employee_details"
        mycursor.execute(sql1)
        result=mycursor.fetchall()
        print(result)
        sql2="select Contact_No from employee_details"
        mycursor.execute(sql2)
        result1=mycursor.fetchall()
        print(result1)
        try:
            if txtoldContact.get()=="" or txtemployee_id.get()=="" or txtnewContact.get()=="":
                messagebox.showerror("Error Input"," Give all input")
                root.destroy()
                conupdate()
            elif (txtoldContact.get(),) in result1 and (txtemployee_id.get(),) in result:
                sql="update employee_details set Contact_No=%s where Contact_No=%s and Employee_Id=%s"
                val=(txtnewContact.get(),txtoldContact.get(),txtemployee_id.get()) 
                result2=mycursor.execute(sql,val)
                mydb.commit()
                print("Updated successfully")
                messagebox.Message("Updated successfully")
                displayAll()
        except:
            messagebox.showerror("Error Input","Please give valid Employee ID and contact details")
            root.destroy()
            conupdate()

    btnclear=Button(Contact_frame, command=conupdate ,text="Confirm",width=15, font=("bazooka", 15), bg="red", fg="white",bd=3).grid(row=4,columnspan=3,padx=10,pady=10)


#---------------------------------------view one detail
def onedetail_frame():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")

    onedetail_frame= Frame(root, bg="firebrick")
    onedetail_frame.pack(side=TOP, fill=X)
    lblone_detail= Label(onedetail_frame, text="Employee details", font=("cornerstone", 21, "bold"), bg="white", fg="dark violet")
    lblone_detail.grid(row=0, columnspan=15, padx=10, pady=20, sticky="W")

    employeeiD=StringVar()
    employee_iD = Label(onedetail_frame, text="Enter employee Id ", font=("cornerstone", 18), bg="blue", fg="white")
    employee_iD.grid(row=1, column=1, padx=10, pady=20, sticky="W")
    txtemployee_iD = Entry(onedetail_frame, textvariable=employeeiD, font=("cornerstone", 16), width=30)
    txtemployee_iD.grid(row=1, column=2, padx=10, sticky="w")

    btnview=Button(onedetail_frame, command=onedetailview_frame ,text="View",width=15, font=("cornerstone", 15), bg="red", fg="white",bd=3).grid(row=4,columnspan=3,padx=10,pady=10)

#---------------------------------------onedetailview_frame

def onedetailview_frame():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")

    # onedetailview_frame= Frame(root, bg="firebrick")
    # onedetailview_frame.pack(side=TOP, fill=X)
    lbl_one_detail= Label(root, text="Employee details", font=("bazooka", 21, "bold"), bg="firebrick", fg="white")
    lbl_one_detail.place(x=10,y=10)

    onedetail_frame= Frame(root, bg="firebrick",width=300,height=500)
    onedetail_frame.place(x=350,y=250)
    # lblone_detail= Label(onedetail_frame, text="Employee details", font=("cornerstone", 21, "bold"), bg="white", fg="dark violet")
    # lblone_detail.grid(row=0, columnspan=15, padx=10, pady=20, sticky="W")

    employeeiD=StringVar() 
    employee_iD = Label(onedetail_frame, text="Enter employee Id ", font=("bazooka", 15 ), bg="firebrick", fg="white")
    employee_iD.grid(row=1, column=1, padx=10, pady=20, sticky="W")
    txtemployee_iD = Entry(onedetail_frame, textvariable=employeeiD, font=("cornerstone", 15), width=30)
    txtemployee_iD.grid(row=1, column=2, padx=10, sticky="w")

    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=600 , width=1400, height=100)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('cornerstone', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('cornerstone', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)

    def displayAll():
        tv.delete(*tv.get_children())
        sql="SELECT * from employee_details where Employee_Id=%s"
        val=(txtemployee_iD.get(),)
        mycursor.execute(sql,val)
        rows=mycursor.fetchall()
        if txtemployee_iD.get()=="" or rows==[]:
            messagebox.showerror("Error Input","Give valid Employee ID")
            root.destroy()
            onedetailview_frame()
        else:                

            for i in rows:
                tv.insert("", END, values=i)
    btnview=Button(onedetail_frame, command=displayAll ,text="View",width=12, font=("bazooka", 12,"bold"), bg="red", fg="white",bd=3)
    btnview.grid(row=2,column=2,padx=10,pady=10)

    
#---------------------------------------All Employees detail

def alldetails():
    root1 = Tk()
    root1.title("Employee Management System")
    root1.geometry("1920x1080+0+0")
    root1.config(bg="firebrick")
    root1.state("zoomed")

    alldetails_frame= Frame(root1, bg="firebrick")
    alldetails_frame.pack(side=TOP, fill=X)

    lbl_all_details= Label(alldetails_frame, text="All Employees details", font=("cornerstone", 21, "bold"), bg="firebrick", fg="white")
    lbl_all_details.grid(row=0, columnspan=15, padx=10, pady=20, sticky="W")
    root1.title("Employee Management System")
    root1.geometry("1920x1080+0+0")
    root1.config(bg="firebrick")
    root1.state("zoomed")
    tree_frame = Frame(root1, bg="firebrick")
    tree_frame.place(x=0, y=80 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('cornerstone', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('cornerstone', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employee_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()
def treeframe():
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="firebrick")
    root.state("zoomed")
    tree_frame = Frame(root, bg="firebrick")
    tree_frame.place(x=0, y=80 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('cornerstone', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('cornerstone', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employee_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()
    
frontpage_frame()
root.mainloop()

from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self):
        self.load_gui()





    def load_gui(self):



        self.root=Tk()
        self.root.geometry('1530x790')
        self.root.title('Employee Management System')

        # variables
        self.name = StringVar()
        self.Designation = StringVar()
        self.email = StringVar()
        self.department = StringVar()
        self.address = StringVar()
        self.dob = StringVar()
        self.married_status = StringVar()
        self.doj = StringVar()
        self.idproofcomb = StringVar()
        self.idproofno = StringVar()
        self.gender = StringVar()
        self.phone = StringVar()
        self.country = StringVar()
        self.salary = StringVar()


        Heading=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',bg='white',fg='darkred',font=('times new roman',37,'bold'))
        Heading.place(x=0,y=0,width=1530,height=50)

        img=Image.open('wallpapers/logo.jpg')
        img=img.resize((50,50))
        self.photo_logo=ImageTk.PhotoImage(img)

        logo=Label(self.root,image=self.photo_logo)
        logo.place(x=270,y=0,width=50,height=50)


        img_frame=Frame(self.root,bg='white',bd=2,relief=RIDGE)
        img_frame.place(x=0,y=50,width=1530,height=160)

        img1 = Image.open('wallpapers/emp1.jpeg')
        img1 = img1.resize((510, 160))
        self.photo_img1 = ImageTk.PhotoImage(img1)

        photo1 = Label(img_frame, image=self.photo_img1)
        photo1.place(x=0, y=0, width=510, height=155)

        img2 = Image.open('wallpapers/emp2.jpeg')
        img2 = img2.resize((510, 160))
        self.photo_img2 = ImageTk.PhotoImage(img2)

        photo2 = Label(img_frame, image=self.photo_img2)
        photo2.place(x=510, y=0, width=510, height=155)

        img3 = Image.open('wallpapers/emp3.jpeg')
        img3 = img3.resize((510, 160))
        self.photo_img3 = ImageTk.PhotoImage(img3)

        photo3 = Label(img_frame, image=self.photo_img3)
        photo3.place(x=1020, y=0, width=510, height=155)

        #main frame
        Main_Frame=Frame(self.root,bg='white',bd=2,relief=RIDGE)
        Main_Frame.place(x=10,y=220,width=1500,height=560)

        #upper frame
        Upper_Frame=LabelFrame(Main_Frame,bg='white',text='Employee Information',fg='darkblue',bd=2,relief=RIDGE,font=('times new roman',12,'bold'))
        Upper_Frame.place(x=8,y=5,width=1480,height=270)

        #entery feilds and lables


        # 1.Department
        department=Label(Upper_Frame,text='Department: ',bg='white',font=('airial',12,'bold'))
        department.grid(row=0,column=0,padx=2,sticky=W)
        department_entry=ttk.Combobox(Upper_Frame,font=('arial',11,'bold'),width=17,state='readonly',textvariable=self.department)
        department_entry['values']=('Select Department','Software Engineer','HR','Manager')
        department_entry.current(0)
        department_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # 2.Designation
        designation = Label(Upper_Frame, text='Designation: ', bg='White', font=('airial', 12, 'bold'))
        designation.grid(row=1, column=0, padx=2, sticky=W)
        designation_entry = ttk.Entry(Upper_Frame, width=22, font=('airial', 11, 'bold'),textvariable=self.Designation)
        designation_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # 3.Address
        address = Label(Upper_Frame, text='Address: ', bg='White', font=('airial', 12, 'bold'))
        address.grid(row=2, column=0, padx=2, sticky=W)
        address_entry = ttk.Entry(Upper_Frame, width=22, font=('airial', 11, 'bold'),textvariable=self.address)
        address_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # 3.DOB
        dob = Label(Upper_Frame, text='DOB: ', bg='White', font=('airial', 12, 'bold'))
        dob.grid(row=3, column=0, padx=2, sticky=W)
        dob_entry = ttk.Entry(Upper_Frame, width=22, font=('airial', 11, 'bold'),textvariable=self.dob)
        dob_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # 4.ID proof
        id_combobox=ttk.Combobox(Upper_Frame,state='readonly',font=('airial', 12, 'bold'),width=17,textvariable=self.idproofcomb)
        id_combobox['values']=('Select Id Proof','Adhar Card','PAN Card','Voter Id')
        id_combobox.current(0)
        id_combobox.grid(row=4,column=0,padx=2,pady=10,sticky=W)
        id_entry=ttk.Entry(Upper_Frame,width=22,font=('airial',11,'bold'),textvariable=self.idproofno)
        id_entry.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        # 5.Name
        name=Label(Upper_Frame,text='Name: ',bg='White',font=('airial',12,'bold'))
        name.grid(row=0,column=2,padx=2,sticky=W)
        name_entry=ttk.Entry(Upper_Frame,width=22,font=('airial',11,'bold'),textvariable=self.name)
        name_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #6.Email
        email = Label(Upper_Frame, text='Email: ', bg='White', font=('airial', 12, 'bold'))
        email.grid(row=1, column=2, padx=2, sticky=W)
        email_entry = ttk.Entry(Upper_Frame, width=22, font=('airial', 11, 'bold'),textvariable=self.email)
        email_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #7.Married status
        married_sts = Label(Upper_Frame, text='Married Status: ', bg='White', font=('airial', 12, 'bold'))
        married_sts.grid(row=2, column=2, padx=2, sticky=W)
        married_sts_combobox=ttk.Combobox(Upper_Frame,state='readonly',width=17,font=('airial', 11, 'bold'),textvariable=self.married_status)
        married_sts_combobox['values']=('Married','Unmarried')
        married_sts_combobox.current(0)
        married_sts_combobox.grid(row=2,column=3,padx=2,sticky=W)

        #8.DOJ
        doj = Label(Upper_Frame, text='DOJ: ', bg='White', font=('airial', 12, 'bold'))
        doj.grid(row=3, column=2, padx=2, sticky=W)
        doj_entry = ttk.Entry(Upper_Frame, width=22, font=('airial', 11, 'bold'),textvariable=self.doj)
        doj_entry.grid(row=3, column=3, padx=2, pady=10, sticky=W)

        #9.Gender
        gender = Label(Upper_Frame, text='Gender: ', bg='White', font=('airial', 12, 'bold'))
        gender.grid(row=4, column=2, padx=2, sticky=W)
        gender_combobox = ttk.Combobox(Upper_Frame, state='readonly', width=17, font=('airial', 11, 'bold'),textvariable=self.gender)
        gender_combobox['values'] = ('Male', 'Female')
        gender_combobox.current(0)
        gender_combobox.grid(row=4, column=3, padx=2, sticky=W)

        #10.Phone Number
        phone = Label(Upper_Frame, text='Phone No.: ', bg='White', font=('airial', 12, 'bold'))
        phone.grid(row=0, column=4, padx=2, sticky=W)
        phone_entry = ttk.Entry(Upper_Frame, width=22, font=('airial', 11, 'bold'),textvariable=self.phone)
        phone_entry.grid(row=0, column=5, padx=2, pady=10, sticky=W)

        #11.Country
        country = Label(Upper_Frame, text='Country: ', bg='White', font=('airial', 12, 'bold'))
        country.grid(row=1, column=4, padx=2, sticky=W)
        country_entry = ttk.Entry(Upper_Frame, width=22, font=('airial', 11, 'bold'),textvariable=self.country)
        country_entry.grid(row=1, column=5, padx=2, pady=10, sticky=W)

        #12.Salary
        salary = Label(Upper_Frame, text='Salary(CTC): ', bg='White', font=('airial', 12, 'bold'))
        salary.grid(row=2, column=4, padx=2, sticky=W)
        salary_entry = ttk.Entry(Upper_Frame, width=22, font=('airial', 11, 'bold'),textvariable=self.salary)
        salary_entry.grid(row=2, column=5, padx=2, pady=10, sticky=W)


        #mask image
        mask_img = Image.open('wallpapers/mask.jpg')
        mask_img = mask_img.resize((240, 220))
        self.mask_im = ImageTk.PhotoImage(mask_img)
        mask = Label(Upper_Frame, image=self.mask_im)
        mask.place(x=1000, y=10, width=240, height=220)


        #Button Frame
        button_Frame = Frame(Upper_Frame, bg='white', bd=2, relief=RIDGE)
        button_Frame.place(x=1290, y=20, width=170, height=210)

        #buttons
        save=Button(button_Frame,text='Save',bg='blue',fg='white',width=13,font=('airial', 15, 'bold'),command=self.add_data)
        save.grid(row=0,column=0,padx=1,pady=5)

        update = Button(button_Frame, text='Update', bg='blue', fg='white', width=13, font=('airial', 15, 'bold'),command=self.update_date)
        update.grid(row=1, column=0, padx=1, pady=5)

        delete = Button(button_Frame, text='Delete', bg='blue', fg='white', width=13, font=('airial', 15, 'bold'),command=self.delete_data)
        delete.grid(row=2, column=0, padx=1, pady=5)

        clr = Button(button_Frame, text='Clear', bg='blue', fg='white', width=13, font=('airial', 15, 'bold'),command=self.reset_data)
        clr.grid(row=3, column=0, padx=1, pady=5)

        # down frame
        Down_Frame = LabelFrame(Main_Frame, bg='white', text='Employee Information Table', fg='darkblue', bd=2,
                                relief=RIDGE, font=('times new roman', 12, 'bold'))
        Down_Frame.place(x=8, y=280, width=1480, height=270)

        #Search Frame
        search_Frame = Frame(Down_Frame, bg='white', bd=2, relief=RIDGE)
        search_Frame.place(x=10, y=10, width=1460, height=40)

        #search Lable
        search_by=Label(search_Frame,text='Search By:',bg='red',fg='white',font=('airial', 15, 'bold'))
        search_by.grid(row=0,column=0,padx=2,pady=5)

        #search combobox
        self.search_combo=StringVar()
        search=ttk.Combobox(search_Frame,state='readonly',width=17,font=('airial', 12, 'bold'),textvariable=self.search_combo)
        search['values']=('Select','Phone No.:','Id number:')
        search.current(0)
        search.grid(row=0,column=1,padx=2,pady=5)

        #text entry box
        self.search=StringVar()
        text=Entry(search_Frame,width=17,font=('airial', 12, 'bold'),bd=2,relief=RIDGE,textvariable=self.search)
        text.grid(row=0,column=2,padx=4,pady=5)

        #buttons

        #search button
        src_btn=Button(search_Frame,text='Search',font=('airial', 11, 'bold'),width=13,bg='blue',fg='white',command=self.search_data)
        src_btn.grid(row=0,column=3,padx=8,pady=(2,2))

        #Showall button
        showall_btn = Button(search_Frame, text='Show All', font=('airial', 11, 'bold'), width=13, bg='blue', fg='white',command=self.fetch_data)
        showall_btn.grid(row=0, column=4, padx=8, pady=(2, 2))

        #table frame
        table_frame=Frame(Down_Frame,bd=3,relief=RIDGE)
        table_frame.place(x=6,y=60,width=1460,height=180)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,columns=('name','degi','email','dep','add','dob','marrid','doj',
                                        'idproofcomb','idproofno','gender','phone','country','salary',),
                                    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi', text='Designation')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('dep', text='Department')
        self.employee_table.heading('add', text='Address')
        self.employee_table.heading('dob', text='DOB')
        self.employee_table.heading('marrid', text='Married Status')
        self.employee_table.heading('doj', text='DOJ')
        self.employee_table.heading('idproofcomb', text='ID Proof')
        self.employee_table.heading('idproofno', text='ID No.')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('phone', text='Phone No.')
        self.employee_table.heading('country', text='Country')
        self.employee_table.heading('salary', text='Salary(CTC)')

        self.employee_table['show']='headings'

        self.employee_table.column('name', width=100)
        self.employee_table.column('degi', width=100)
        self.employee_table.column('email', width=100)
        self.employee_table.column('dep', width=100)
        self.employee_table.column('add', width=100)
        self.employee_table.column('dob', width=100)
        self.employee_table.column('marrid', width=100)
        self.employee_table.column('doj', width=100)
        self.employee_table.column('idproofcomb', width=100)
        self.employee_table.column('idproofno', width=100)
        self.employee_table.column('gender', width=100)
        self.employee_table.column('phone', width=100)
        self.employee_table.column('country', width=100)
        self.employee_table.column('salary', width=100)


        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        self.root.mainloop()

        #function to save the data
    def add_data(self):
        if self.department.get()=="" or self.email.get()=="":
            messagebox.showerror('Error!,All Feilds Are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Swift@87',database='employee')
                my_cursor=conn.cursor()
                my_cursor.execute('INSERT INTO employee_information VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                self.name.get(),
                self.Designation.get() ,
                self.email.get(),
                self.department.get() ,
                self.address.get(),
                self.dob.get() ,
                self.married_status.get(),
                self.doj.get() ,
                self.idproofcomb.get(),
                self.idproofno.get(),
                self.gender.get(),
                self.phone.get() ,
                self.country.get() ,
                self.salary.get()

                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Sucessfull!!',f'data saved',parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

    #fetch_data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Swift@87', database='employee')
        my_cursor = conn.cursor()
        my_cursor.execute('SELECT * FROM employee_information')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.name.set(data[0]),
        self.Designation.set(data[1]),
        self.email.set(data[2]),
        self.department.set(data[3]),
        self.address.set(data[4]),
        self.dob.set(data[5]),
        self.married_status.set(data[6]),
        self.doj.set(data[7]),
        self.idproofcomb.set(data[8]),
        self.idproofno.set(data[9]),
        self.gender.set(data[10])
        self.phone.set(data[11]),
        self.country.set(data[12]),
        self.salary.set(data[13])

    def update_date(self):
        if self.department.get()=="" or self.email.get()=="":
            messagebox.showerror('Error!,All Feilds Are Required')
        else:
            try:
                update=messagebox.askyesno('Update','Are You Sure?')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Swift@87',database='employee')
                    my_cursor=conn.cursor()
                    my_cursor.execute('UPDATE employee_information SET name=%s,designation=%s,email=%s,department=%s,'
                                      'address=%s,dob=%s,married_status=%s,doj=%s,id_proof=%s,gender=%s,phone_no=%s,country=%s,salary=%s WHERE id_no=%s',(
                                        self.name.get(),
                                        self.Designation.get(),
                                        self.email.get(),
                                        self.department.get(),
                                        self.address.get(),
                                        self.dob.get(),
                                        self.married_status.get(),
                                        self.doj.get(),
                                        self.idproofcomb.get(),

                                        self.gender.get(),
                                        self.phone.get(),
                                        self.country.get(),
                                        self.salary.get(),
                                        self.idproofno.get()


                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Sucess','Your Data is sucessfully Updated',parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)


    #delete data
    def delete_data(self):
        if self.idproofno=="":
            messagebox.showerror('Error!,All Feilds Are Required')
        else:
            try:
                delete=messagebox.askyesno("Delete","Are You sure?")
                if delete>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Swift@87', database='employee')
                    my_cursor = conn.cursor()
                    my_cursor.execute('DELETE FROM employee_information WHERE id_no=%s',(self.idproofno.get(),))
                else:
                    if not delete:
                        return


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('sucess','data deleted sucessfully!!')
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
    def reset_data(self):
        self.name.set(""),
        self.Designation.set(""),
        self.email.set("")
        self.department.set('select dapartment'),
        self.address.set(""),
        self.dob.set(""),
        self.married_status.set("Married"),
        self.doj.set(""),
        self.idproofcomb.set("Select Id Proof"),
        self.idproofno.set(""),
        self.gender.set("Male"),
        self.phone.set(""),
        self.country.set(""),
        self.salary.set("")

    def search_data(self):
        if self.search_combo=='':
            messagebox.showerror('Error','Please Select valid option')
        elif self.search=='':
            messagebox.showerror('Error','Please enter valid Id No')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Swift@87',
                                               database='employee')
                my_cursor = conn.cursor()
                my_cursor.execute('SELECT * FROM employee_information WHERE ' +str(self.search_combo.get())+"LIKE '%" + str(self.search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)





obj=Employee()
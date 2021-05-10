from tkinter import *
from tkinter import font as tkfont
from tkinter import ttk
from db import Database
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

database = Database("student.db")


class MainApp():
    def __init__(self, master):
        self.master = master
        self.master.title("Student management system")
        self.master.geometry("1800x1000")
        self.init_dashboard()
        self.bottom_frame = None

    def add_student(self):
        self.bottom_frame = Frame(self.master, bg='gray91', height=790, width=1800)
        self.bottom_frame.place(x=0, y=210)
        self.student_label = Label(self.bottom_frame, text='Add Student Info', font='msserif 15', bg='gray93').place(
            x=225, y=0)

        sidf = Frame(self.bottom_frame, height=1, width=1)
        sid = Entry(sidf)

        snf = Frame(self.bottom_frame, height=1, width=1)
        sn = Entry(snf)

        sdobf = Frame(self.bottom_frame, height=1, width=1)
        sdob = Entry(sdobf)

        sid.insert(0, 'Student ID')
        sn.insert(0, 'Student Name')
        sdob.insert(0, 'DOB')

        def on_entry_click1(event):
            if sid.get() == 'Student ID':
                sid.delete(0, END)
                sid.insert(0, '')

        def on_entry_click2(event):
            if sn.get() == 'Student Name':
                sn.delete(0, END)
                sn.insert(0, '')

        def on_entry_click3(event):
            if sdob.get() == 'DOB':
                sdob.delete(0, END)
                sdob.insert(0, '')

        def on_exit1(event):
            if sid.get() == '':
                sid.insert(0, 'Student ID')

        def on_exit2(event):
            if sn.get() == '':
                sn.insert(0, 'Student Name')

        def on_exit3(event):
            if sdob.get() == '':
                sdob.insert(0, 'DOB')

        sid.bind('<FocusIn>', on_entry_click1)
        sn.bind('<FocusIn>', on_entry_click2)
        sdob.bind('<FocusIn>', on_entry_click3)
        sid.bind('<FocusOut>', on_exit1)
        sn.bind('<FocusOut>', on_exit2)
        sdob.bind('<FocusOut>', on_exit3)

        sid.pack(ipady=4, ipadx=15)
        sn.pack(ipady=4, ipadx=15)
        sdob.pack(ipady=4, ipadx=15)
        sidf.place(x=220, y=42)
        snf.place(x=435, y=42)
        sdobf.place(x=650, y=42)

        def add_student_to_db():
            if sid.get() == 'Student ID' or sn.get() == 'Student Name' or sdob.get() == 'DOB':
                messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
            elif sid.get() == '' or sn.get() == '' or sdob.get() == '':
                messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
            else:
                if database.check_student(str(sid.get())):
                    database.update_student(str(sid.get()), sn.get(), sdob.get())
                else:
                    database.insert_student(str(sid.get()), sn.get(), sdob.get())
                database.select_student()

        self.button_add_student = Button(self.bottom_frame, text='Add Student', bg='white', fg='cyan4',
                                         font='timenewroman 11', activebackground='green',
                                         command=add_student_to_db).place(x=235, y=100)

    def add_course(self):
        self.bottom_frame = Frame(self.master, bg='gray91', height=790, width=1800)
        self.bottom_frame.place(x=0, y=210)
        self.course_label = Label(self.bottom_frame, text='Add Course Info', font='msserif 15', bg='gray93').place(
            x=225, y=0)

        cidf = Frame(self.bottom_frame, height=1, width=1)
        cid = Entry(cidf)

        cnf = Frame(self.bottom_frame, height=1, width=1)
        cn = Entry(cnf)

        ccf = Frame(self.bottom_frame, height=1, width=1)
        cc = Entry(ccf)

        cid.insert(0, 'Course ID')
        cn.insert(0, 'Course Name')
        cc.insert(0, 'Course Credit')

        def on_entry_click1(event):
            if cid.get() == 'Course ID':
                cid.delete(0, END)
                cid.insert(0, '')

        def on_entry_click2(event):
            if cn.get() == 'Course Name':
                cn.delete(0, END)
                cn.insert(0, '')

        def on_entry_click3(event):
            if cc.get() == 'Course Credit':
                cc.delete(0, END)
                cc.insert(0, '')

        def on_exit1(event):
            if cid.get() == '':
                cid.insert(0, 'Course ID')

        def on_exit2(event):
            if cn.get() == '':
                cn.insert(0, 'Course Name')

        def on_exit3(event):
            if cc.get() == '':
                cc.insert(0, 'Course Credit')

        cid.bind('<FocusIn>', on_entry_click1)
        cn.bind('<FocusIn>', on_entry_click2)
        cc.bind('<FocusIn>', on_entry_click3)
        cid.bind('<FocusOut>', on_exit1)
        cn.bind('<FocusOut>', on_exit2)
        cc.bind('<FocusOut>', on_exit3)

        cid.pack(ipady=4, ipadx=15)
        cn.pack(ipady=4, ipadx=15)
        cc.pack(ipady=4, ipadx=15)
        cidf.place(x=220, y=42)
        cnf.place(x=435, y=42)
        ccf.place(x=650, y=42)

        def add_course_to_db():
            if cid.get() == 'Course ID' or cn.get() == 'Course Name' or cc.get() == 'Course Credit':
                messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
            elif cid.get() == '' or cn.get() == '' or cc.get() == '':
                messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
            else:
                if database.check_course(str(cid.get())):
                    database.update_course(cid.get(), cn.get(), cc.get())
                else:
                    database.insert_course(cid.get(), cn.get(), cc.get())
                database.select_course()

        self.button_add_course = Button(self.bottom_frame, text='Add Course', bg='white', fg='cyan4',
                                        font='timenewroman 11', activebackground='green',
                                        command=add_course_to_db).place(x=235, y=100)

    def add_mark(self):
        self.bottom_frame = Frame(self.master, bg='gray91', height=790, width=1800)
        self.bottom_frame.place(x=0, y=210)
        self.mark_label = Label(self.bottom_frame, text='Add Mark', font='msserif 15', bg='gray93').place(
            x=225, y=0)

        sidf = Frame(self.bottom_frame, height=1, width=1)
        sid = Entry(sidf)

        cidf = Frame(self.bottom_frame, height=1, width=1)
        cid = Entry(cidf)

        gf = Frame(self.bottom_frame, height=1, width=1)
        g = Entry(gf)

        sid.insert(0, 'Student ID')
        cid.insert(0, 'Course ID')
        g.insert(0, 'Grade')

        def on_entry_click1(event):
            if sid.get() == 'Student ID':
                sid.delete(0, END)
                sid.insert(0, '')

        def on_entry_click2(event):
            if cid.get() == 'Course ID':
                cid.delete(0, END)
                cid.insert(0, '')

        def on_entry_click3(event):
            if g.get() == 'Grade':
                g.delete(0, END)
                g.insert(0, '')

        def on_exit1(event):
            if sid.get() == '':
                sid.insert(0, 'Student ID')

        def on_exit2(event):
            if cid.get() == '':
                cid.insert(0, 'Course ID')

        def on_exit3(event):
            if g.get() == '':
                g.insert(0, 'Grade')

        sid.bind('<FocusIn>', on_entry_click1)
        cid.bind('<FocusIn>', on_entry_click2)
        g.bind('<FocusIn>', on_entry_click3)
        sid.bind('<FocusOut>', on_exit1)
        cid.bind('<FocusOut>', on_exit2)
        g.bind('<FocusOut>', on_exit3)

        sid.pack(ipady=4, ipadx=15)
        cid.pack(ipady=4, ipadx=15)
        g.pack(ipady=4, ipadx=15)
        sidf.place(x=220, y=42)
        cidf.place(x=435, y=42)
        gf.place(x=650, y=42)

        def add_mark_to_db():
            if sid.get() == 'Student ID' or cid.get() == 'Course ID' or g.get() == 'Grade':
                messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
            elif sid.get() == '' or cid.get() == '' or g.get() == '':
                messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
            else:
                if database.check_mark(str(sid.get()), str(cid.get())):
                    database.update_mark(sid.get(), cid.get(), g.get())
                else:
                    database.insert_mark(sid.get(), cid.get(), g.get())
                database.select_mark()

        self.button_add_course = Button(self.bottom_frame, text='Add Mark', bg='white', fg='cyan4',
                                        font='timenewroman 11', activebackground='green',
                                        command=add_mark_to_db).place(x=235, y=100)

    def show_student(self):
        self.bottom_frame = Frame(self.master, bg='gray91', height=790, width=1800)
        self.bottom_frame.place(x=0, y=210)
        self.student_label = Label(self.bottom_frame, text='Student Information', font='msserif 15', bg='gray93').place(
            x=225, y=0)
        table_frame = Frame(self.bottom_frame, bd=4, relief=RIDGE, bg="royal blue")
        table_frame.place(x=200, y=75, width=790, height=525)

        scrool_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scrool_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,
                                          columns=("student_name", "date_of_birth"),
                                          xscrollcommand=scrool_x.set, yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM, fill=X)
        scrool_y.pack(side=RIGHT, fill=Y)
        scrool_x.config(command=self.student_table.xview)
        scrool_y.config(command=self.student_table.yview)

        self.student_table.heading("student_name", text="Student Name")
        self.student_table.heading("date_of_birth", text="Date of birth")
        self.student_table["show"] = "headings"

        self.student_table.column("student_name", width=100)
        self.student_table.column("date_of_birth", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_student_data()

    def fetch_student_data(self):
        self.rows = database.select_student()
        if len(self.rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for self.row in self.rows:
                self.student_table.insert("", END, values=self.row)

    def show_course(self):
        self.bottom_frame = Frame(self.master, bg='gray91', height=790, width=1800)
        self.bottom_frame.place(x=0, y=210)
        table_frame = Frame(self.bottom_frame, bd=4, relief=RIDGE, bg="royal blue")
        table_frame.place(x=200, y=75, width=790, height=525)
        self.course_label = Label(self.bottom_frame, text='Course Information', font='msserif 15', bg='gray93').place(
            x=225, y=0)

        scrool_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scrool_y = Scrollbar(table_frame, orient=VERTICAL)
        self.course_table = ttk.Treeview(table_frame,
                                         columns=("course_name", "course_credit"),
                                         xscrollcommand=scrool_x.set, yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM, fill=X)
        scrool_y.pack(side=RIGHT, fill=Y)
        scrool_x.config(command=self.course_table.xview)
        scrool_y.config(command=self.course_table.yview)

        self.course_table.heading("course_name", text="Course Name")
        self.course_table.heading("course_credit", text="Course Credit")
        self.course_table["show"] = "headings"

        self.course_table.column("course_name", width=100)
        self.course_table.column("course_credit", width=100)

        self.course_table.pack(fill=BOTH, expand=1)
        self.fetch_course_data()

    def fetch_course_data(self):
        self.rows = database.select_course()
        if len(self.rows) != 0:
            self.course_table.delete(*self.course_table.get_children())
            for self.row in self.rows:
                self.course_table.insert("", END, values=self.row)

    def show_mark(self):
        self.bottom_frame = Frame(self.master, bg='gray91', height=790, width=1800)
        self.bottom_frame.place(x=0, y=210)
        course_list = database.select_all_courses()
        nb = ttk.Combobox(self.bottom_frame, values=course_list, state='readonly', width=22)
        nb.place(x=40, y=75)
        nb.current(0)
        table_frame = Frame(self.bottom_frame, bd=4, relief=RIDGE, bg="royal blue")
        table_frame.place(x=200, y=75, width=790, height=525)
        self.mark_label = Label(self.bottom_frame, text='Mark Information', font='msserif 15', bg='gray93').place(
            x=225, y=0)

        scrool_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scrool_y = Scrollbar(table_frame, orient=VERTICAL)
        self.mark_table = ttk.Treeview(table_frame,
                                       columns=("student_name", "grade"),
                                       xscrollcommand=scrool_x.set, yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM, fill=X)
        scrool_y.pack(side=RIGHT, fill=Y)
        scrool_x.config(command=self.mark_table.xview)
        scrool_y.config(command=self.mark_table.yview)

        self.mark_table.heading("student_name", text="Student Name")
        self.mark_table.heading("grade", text="Grade")
        self.mark_table["show"] = "headings"

        self.mark_table.column("student_name", width=100)
        self.mark_table.column("grade", width=100)

        self.mark_table.pack(fill=BOTH, expand=1)

        def get_student_mark():
            self.rows = database.select_student_mark_from_course(nb.get())
            if len(self.rows) != 0:
                self.mark_table.delete(*self.mark_table.get_children())
                for self.row in self.rows:
                    self.mark_table.insert("", END, values=self.row)

        get_marks = Button(self.bottom_frame, text='Get Marks', bg='blue', fg='white', font='timenewroman 9',
                           activeforeground='black', command=get_student_mark).place(x=50, y=105)

    def show_average_gpa(self):
        self.bottom_frame = Frame(self.master, bg='gray91', height=790, width=1800)
        self.bottom_frame.place(x=0, y=210)
        table_frame = Frame(self.bottom_frame, bd=4, relief=RIDGE, bg="royal blue")
        table_frame.place(x=400, y=75, width=790, height=525)
        self.average_label = Label(self.bottom_frame, text='Average GPA', font='msserif 15', bg='gray93').place(
            x=400, y=0)

        scrool_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scrool_y = Scrollbar(table_frame, orient=VERTICAL)
        self.average_table = ttk.Treeview(table_frame,
                                          columns=("student_name", "average_gpa"),
                                          xscrollcommand=scrool_x.set, yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM, fill=X)
        scrool_y.pack(side=RIGHT, fill=Y)
        scrool_x.config(command=self.average_table.xview)
        scrool_y.config(command=self.average_table.yview)

        self.average_table.heading("student_name", text="Student Name")
        self.average_table.heading("average_gpa", text="Average GPA")
        self.average_table["show"] = "headings"

        self.average_table.column("student_name", width=100)
        self.average_table.column("average_gpa", width=100)

        self.average_table.pack(fill=BOTH, expand=1)
        self.fetch_average_data()

    def fetch_average_data(self):
        self.rows = database.average_gpa()
        if len(self.rows) != 0:
            self.average_table.delete(*self.average_table.get_children())
            for self.row in self.rows:
                self.average_table.insert("", END, values=self.row)

    def sort_gpa(self):
        self.bottom_frame = Frame(self.master, bg='gray91', height=790, width=1800)
        self.bottom_frame.place(x=0, y=210)
        table_frame = Frame(self.bottom_frame, bd=4, relief=RIDGE, bg="royal blue")
        table_frame.place(x=400, y=75, width=790, height=525)
        self.sort_label = Label(self.bottom_frame, text='Sort GPA', font='msserif 15', bg='gray93').place(
            x=400, y=0)
        scrool_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scrool_y = Scrollbar(table_frame, orient=VERTICAL)
        self.sort_table = ttk.Treeview(table_frame,
                                       columns=("student_name", "average_gpa"),
                                       xscrollcommand=scrool_x.set, yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM, fill=X)
        scrool_y.pack(side=RIGHT, fill=Y)
        scrool_x.config(command=self.sort_table.xview)
        scrool_y.config(command=self.sort_table.yview)

        self.sort_table.heading("student_name", text="Student Name")
        self.sort_table.heading("average_gpa", text="Average GPA")
        self.sort_table["show"] = "headings"

        self.sort_table.column("student_name", width=100)
        self.sort_table.column("average_gpa", width=100)

        self.sort_table.pack(fill=BOTH, expand=1)
        self.fetch_sort_data()

    def fetch_sort_data(self):
        self.rows = database.sort_gpa()
        if len(self.rows) != 0:
            self.sort_table.delete(*self.sort_table.get_children())
            for self.row in self.rows:
                self.sort_table.insert("", END, values=self.row)

    def exit(self):
        q = messagebox.askyesno("Exit", "Do you really want to exit ?")
        if (q):
            self.master.destroy()

    def init_dashboard(self):
        self.frame1 = Frame(self.master, bg='#0f624c', height=60, width=1800)
        self.frame1.place(x=0, y=0)
        self.label1 = Label(self.frame1, text='DASHBOARD', fg='White', bg='#0f624c', font=('Arial', 30, 'bold'))
        self.label1.place(x=800, y=5)
        self.frame2 = Frame(self.master, bg='white', height=150, width=1800)
        self.frame2.place(x=0, y=60)
        self.button1 = Button(self.frame2, text='Add Student', fg='white', bg='blue', height=5, width=20,
                              font=('Arial', 11, 'bold'), activebackground='white',
                              activeforeground='black',
                              bd=3, relief='flat', cursor='hand2', command=self.add_student)
        self.button1.grid(row=0, column=0, sticky="w", padx=4, pady=5, )
        self.button2 = Button(self.frame2, text='Add Courses', fg='white', bg='blue', height=5, width=20,
                              font=('Arial', 11, 'bold'), activebackground='white',
                              activeforeground='black',
                              bd=3, relief='flat', cursor='hand2', command=self.add_course)
        self.button2.grid(row=0, column=1, sticky="w", padx=4, pady=10, )
        self.button3 = Button(self.frame2, text='Add Marks', fg='white', bg='blue', height=5, width=20,
                              font=('Arial', 11, 'bold'), activebackground='white',
                              activeforeground='black',
                              bd=3, relief='flat', cursor='hand2', command=self.add_mark)
        self.button3.grid(row=0, column=2, sticky="w", padx=4, pady=10, )
        self.button4 = Button(self.frame2, text='View Student', fg='white', bg='blue', height=5, width=20,
                              font=('Arial', 11, 'bold'), activebackground='white',
                              activeforeground='black',
                              bd=3, relief='flat', cursor='hand2', command=self.show_student)
        self.button4.grid(row=0, column=3, sticky="w", padx=4, pady=10, )
        self.button5 = Button(self.frame2, text='View Courses', fg='white', bg='blue', height=5, width=20,
                              font=('Arial', 11, 'bold'), activebackground='white',
                              activeforeground='black',
                              bd=3, relief='flat', cursor='hand2', command=self.show_course)
        self.button5.grid(row=0, column=4, sticky="w", padx=4, pady=10, )
        self.button6 = Button(self.frame2, text='View Marks', fg='white', bg='blue', height=5, width=20,
                              font=('Arial', 11, 'bold'), activebackground='white',
                              activeforeground='black',
                              bd=3, relief='flat', cursor='hand2', command=self.show_mark)
        self.button6.grid(row=0, column=5, sticky="w", padx=4, pady=10, )
        self.button7 = Button(self.frame2, text='View Average GPA', fg='white', bg='blue', height=5, width=20,
                              font=('Arial', 11, 'bold'), activebackground='white',
                              activeforeground='black',
                              bd=3, relief='flat', cursor='hand2', command=self.show_average_gpa)
        self.button7.grid(row=0, column=6, sticky="w", padx=4, pady=10, )
        self.button8 = Button(self.frame2, text='Sort', fg='white', bg='blue', height=5, width=20,
                              font=('Arial', 11, 'bold'), activebackground='white',
                              activeforeground='black',
                              bd=3, relief='flat', cursor='hand2', command=self.sort_gpa)
        self.button8.grid(row=0, column=7, sticky="w", padx=4, pady=10, )
        self.button9 = Button(self.frame2, text='Exit', fg='white', bg='blue', height=5, width=20,
                              font=('Arial', 11, 'bold'), activebackground='white',
                              activeforeground='black',
                              bd=3, relief='flat', cursor='hand2', command=self.exit)
        self.button9.grid(row=0, column=8, sticky="w", padx=4, pady=10)


if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()

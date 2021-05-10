import sqlite3
import datetime


class Database:
    def __init__(self, filename):
        self.db = sqlite3.connect(filename)
        self.cursorObj = self.db.cursor()

    def insert_student(self, student_id, student_name, student_dob):
        self.data = [(int(student_id), student_name, student_dob)]
        self.cursorObj.executemany("INSERT INTO student VALUES(?,?,?)", self.data)
        self.db.commit()

    def update_student(self, student_id, student_name, student_dob):
        self.cursorObj.execute(
            "update student set student_name='{}',date_of_birth='{}' where student_id='{}'".format(student_name,
                                                                                                   student_dob,
                                                                                                   int(student_id)))
        self.db.commit()

    def check_student(self, student_id):
        self.cursorObj.execute("select * from student where student_id=" + student_id)
        results = self.cursorObj.fetchone()
        if (results):
            return True
        else:
            return False

    def select_student(self):
        self.cursorObj.execute("SELECT * FROM student")
        rows = self.cursorObj.fetchall()
        return rows

    def insert_course(self, course_id, course_name, course_credit):
        self.data = [(int(course_id), course_name, course_credit)]
        self.cursorObj.executemany("INSERT INTO course VALUES(?,?,?)", self.data)
        self.db.commit()

    def update_course(self, course_id, course_name, course_credit):
        self.cursorObj.execute(
            "update course set course_name='{}',course_credit='{}' where course_id='{}'".format(course_name,
                                                                                                course_credit,
                                                                                                int(course_id, )))
        self.db.commit()

    def check_course(self, course_id):
        self.cursorObj.execute("select * from course where course_id=" + course_id)
        results = self.cursorObj.fetchone()
        if results:
            return True
        else:
            return False

    def select_course(self):
        self.cursorObj.execute("SELECT * FROM course")
        rows = self.cursorObj.fetchall()
        return rows

    def insert_mark(self, student_id, course_id, grade):
        self.data = [(int(student_id), int(course_id), float(grade))]
        self.cursorObj.executemany("INSERT INTO mark (student_id,course_id,grade)VALUES(?,?,?)", self.data)
        self.db.commit()

    def update_mark(self, student_id, course_id, grade):
        self.cursorObj.execute(
            "update mark set grade='{}' where student_id='{}'".format(float(grade), int(student_id)))

        self.db.commit()

    def check_mark(self, student_id, course_id):
        self.cursorObj.execute(
            "select * from mark where student_id='{}' and course_id='{}'".format(student_id, course_id))
        results = self.cursorObj.fetchone()
        if results:
            return True
        else:
            return False

    def select_mark(self):
        self.cursorObj.execute("SELECT * FROM mark")
        rows = self.cursorObj.fetchall()
        print(rows)

    def select_all_courses(self):
        self.cursorObj.execute("SELECT course_name FROM course")
        rows = self.cursorObj.fetchall()
        self.db.commit()
        course_list=[]
        for row in rows:
            course_list.append(row[0])
        return course_list

    def select_student_mark_from_course(self,course_name):
        self.cursorObj.execute("SELECT student_name,grade FROM course,mark,student WHERE mark.student_id="
                               "student.student_id and mark.course_id=course.course_id and course.course_id"
                               "=(select course.course_id from course where course.course_name='{}')".format(course_name))
        rows = self.cursorObj.fetchall()
        self.db.commit()
        return rows

    def average_gpa(self):
        self.cursorObj.execute("SELECT student_name, AVG(grade) as average_grade "
                               "from mark, student where student.student_id = mark.student_id group by mark.student_id")
        rows = self.cursorObj.fetchall()
        self.db.commit()
        return rows

    def sort_gpa(self):
        self.cursorObj.execute("SELECT student_name, AVG(grade) as average_grade "
                               "from mark, student where student.student_id = mark.student_id group by mark.student_id order by AVG(grade) asc")
        rows = self.cursorObj.fetchall()
        self.db.commit()
        return rows


def main():
    db = Database(filename='student.db')
    # db.get_information_bill(1)
    # db.total_amount_of_water_by_area()
    print(db.select_student())


if __name__ == '__main__':
    main()

import time
import curses
from curses import textpad
import math

menu = ['AddStudent', 'AddCourse', 'AddMark', 'ShowStudent', 'ShowCourse', 'ShowMark', 'StudentAverageGpa',
        'SortDescendingOrder', 'Exit']


class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def get_student_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def set_student_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def __eq__(self, other):
        return self.id == other.id

    def get_key(self):
        return self.get_student_id()

    def displayStudentInformation(self):
        print("Student Id: %d, Student name: %s, Student dob: %s" % (self.id, self.name, self.dob))


class Course:
    def __init__(self, courseId, courseName, noOfCredit):
        self.courseId = courseId
        self.courseName = courseName
        self.noOfCredit = noOfCredit

    def get_course_id(self):
        return self.courseId

    def get_course_name(self):
        return self.courseName

    def get_course_credit(self):
        return self.noOfCredit

    def set_course_name(self, courseName):
        self.courseName = courseName

    def set_course_id(self, courseId):
        self.courseId = courseId

    def set_course_credit(self, noOfCredit):
        self.noOfCredit = noOfCredit

    def __eq__(self, other):
        return self.courseId == other.courseId

    def get_key(self):
        return self.get_course_id()

    def displayCourseInformation(self):
        print(
            "CourseId: {}, Course name: {}, Course credit: {}".format(self.courseId, self.courseName, self.noOfCredit))


class Mark:
    def __init__(self, studentId, courseId, grade):
        self.studentId = studentId
        self.courseId = courseId
        self.grade = grade

    def get_student_id(self):
        return self.studentId

    def get_course_id(self):
        return self.courseId

    def get_grade(self):
        return self.grade

    def set_student_id(self, studentId):
        self.studentId = studentId

    def set_course_id(self, courseId):
        self.courseId = courseId

    def set_grade(self, grade):
        self.grade = grade

    def __eq__(self, other):
        return self.get_student_id() == other.get_student_id() and self.get_course_id() == other.get_course_id()

    def displayStudentMark(self, studentName):
        print("Student Id: {}, Student Name: {}, Student Mark: {} ".format(self.studentId, studentName, self.grade))


def showMarkInformationForSpecificCourse(courseName, students, courses, grades, stdscr):
    courseId = ""
    studentName = ""
    studentGrade = ""
    x = 0
    y = 5
    num = 0
    for i in range(len(courses)):
        if courses[i].get_course_name() == courseName:
            courseId = courses[i].get_course_id()
            break

    for j in range(len(grades)):
        if int(grades[j].get_course_id()) == int(courseId):
            for k in range(len(students)):
                if int(students[k].get_student_id()) == int(grades[j].get_student_id()):
                    stdscr.addstr(y + num, x, "Student name: " + str(students[k].get_name()) + ' Student grade: ' + str(
                        grades[j].get_grade()))
                    num += 2
                    break


def findStudentAverageMark(studentId, marks, courses):
    studentGrades = []
    studentCredit = []
    totalCredit = 0
    totalMark = 0

    for i in range(len(marks)):
        if int(marks[i].get_student_id()) == int(studentId):
            studentGrades.insert(len(studentGrades) - 1, marks[i].get_grade())
            for j in range(len(courses)):
                if (int(courses[j].get_course_id()) == int(marks[i].get_course_id())):
                    studentCredit.insert(len(studentCredit) - 1, int(courses[j].get_course_credit()))
                    break
        else:
            continue
    for i in range(len(studentGrades)):
        totalMark += studentGrades[i] * studentCredit[i]
    for i in range(len(studentCredit)):
        totalCredit += int(studentCredit[i])
    averageGpa = totalMark / totalCredit
    return averageGpa


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def main(stdscr):
    students = []
    courses = []
    grades = []
    averageGpa = []
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0
    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 0:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            m = 0
            stdscr.addstr(2, 0, "id")
            studentId = int(stdscr.getstr(3, 0).decode())
            stdscr.addstr(4, 0, "name")
            studentName = stdscr.getstr(5, 0).decode()
            stdscr.addstr(6, 0, 'dob')
            dob = stdscr.getstr(7, 0).decode()
            stdscr.addstr(9, 0, str(studentId))
            student = Student(studentId, studentName, dob)
            if (len(students) == 0):
                students.append(student)

            for j in range(len(students)):
                if (student == students[j]):
                    students[j] = student
                    m = 1
                    break
                if (m == 0):
                    students.append(student)
            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 1:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            m = 0
            stdscr.addstr(2, 0, "id")
            courseId = int(stdscr.getstr(3, 0).decode())
            stdscr.addstr(4, 0, "name")
            courseName = stdscr.getstr(5, 0).decode()
            stdscr.addstr(6, 0, 'noOfCredit')
            noOfCredit = int(stdscr.getstr(7, 0).decode())
            course = Course(courseId, courseName, noOfCredit)
            if (len(courses) == 0):
                courses.append(course)
            for j in range(len(courses)):
                if (course == courses[j]):
                    courses[j] = course
                    m = 1
                    break
                if (m == 0):
                    courses.append(course)
            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 2:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            m = 0
            stdscr.addstr(2, 0, "studentId")
            studentId = stdscr.getstr(3, 0).decode()
            stdscr.addstr(4, 0, "courseId")
            courseId = stdscr.getstr(5, 0).decode()
            stdscr.addstr(6, 0, 'mark')
            mark = float(stdscr.getstr(7, 0).decode())
            mark = math.floor(mark)
            grade = Mark(studentId, courseId, mark)
            if (len(grades) == 0):
                grades.append(grade)
            for j in range(len(grades)):
                if (grades[j] == grade):
                    grades[j] = grade
                    m = 1
                    break
                if (m == 0):
                    grades.append(grade)
            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 3:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            stdscr.addstr(2, 0, "studentId")
            studentId = int(stdscr.getstr(3, 0).decode())
            for i in range(0, len(students)):
                if (students[i].get_student_id() == studentId):
                    stdscr.addstr(6, 0,
                                  "StudentId: " + str(students[i].get_student_id()) + " Student name: " + students[
                                      i].get_name() + " Dob: " + students[i].get_dob())
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 4:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            stdscr.addstr(2, 0, "courseId")
            courseId = int(stdscr.getstr(3, 0).decode())
            for i in range(0, len(courses)):
                if (courses[i].get_course_id() == courseId):
                    stdscr.addstr(6, 0, "CourseId: " + str(courses[i].get_course_id()) + " Course name: " + courses[
                        i].get_course_name() + " Credit: " + str(courses[i].get_course_credit()))
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 5:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            stdscr.addstr(2, 0, "courseName")
            courseName = stdscr.getstr(3, 0).decode()
            showMarkInformationForSpecificCourse(courseName, students, courses, grades, stdscr)
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 6:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            stdscr.addstr(2, 0, "studentId")
            studentId = int(stdscr.getstr(3, 0).decode())
            stdscr.addstr(5, 0, "student average marks: ")
            averageMark = findStudentAverageMark(studentId, grades, courses)
            averageGpa.insert(len(averageGpa) - 1, [studentId, averageMark])
            stdscr.addstr(7, 0, str(averageMark))
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 7:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            averageGpa.sort(key=lambda x: x[1], reverse=True)
            y = 2
            x = 0
            for i in range(len(averageGpa)):
                stdscr.addstr(y + i * 2, x, "StudentId: " + str(averageGpa[i][0]) + " Student AveragGpa: " +
                str(averageGpa[i][1]))

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 8:
            break

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)

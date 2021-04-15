from domains import *
from input import *
from output import *
import curses
import time
import math
import zipfile
import os


def main(stdscr):
    menu = ['AddStudent', 'AddCourse', 'AddMark', 'ShowStudent', 'ShowCourse', 'ShowMark', 'StudentAverageGpa',
            'SortDescendingOrder', 'Decompress File', 'Exit']
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
            studentId, studentName, dob = add_students(stdscr)
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

            with open("student.txt", "r+") as sf:
                m = 0
                for student in students:
                    for line in sf.readlines():
                        if str(line[0]) == str(student.get_student_id()) in line:
                            m = 1
                            break
                        else:
                            continue
                    if m == 1:
                        m = 0
                        continue
                    else:
                        sf.write(f"{student.get_student_id()} -- {student.get_name()} -- {student.get_dob()} \n")

            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 1:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            m = 0
            courseId, courseName, noOfCredit = add_courses(stdscr)
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

            with open("course.txt", "r+") as sf:
                m = 0
                for course in courses:
                    for line in sf.readlines():
                        if str(line[0]) == str(course.get_course_id()) in line:
                            m = 1
                            break
                        else:
                            continue
                    if m == 1:
                        m = 0
                        continue
                    else:
                        sf.write(f"{course.get_course_id()}--{course.get_course_name()} \n")

            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 2:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            m = 0
            studentId, courseId, mark = add_marks(stdscr)
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
            with open("mark.txt", "r+") as sf:
                m = 0
                for grade in grades:
                    for line in sf.readlines():
                        if str(line[0]) == str(grade.get_student_id()) and line.split("--")[1] == str(
                                grade.get_course_id()):
                            m = 1
                            break
                        else:
                            continue
                    if m == 1:
                        m = 0
                        continue
                    else:
                        sf.write(f"{course.get_course_id()}--{course.get_course_name()} \n")

                stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 3:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            studentId = add_student_id(stdscr)
            with open("student.txt", "r") as sf:
                m = 0
                for line in sf.readlines():
                    if str(line[0]) == str(studentId):
                        x = line.split("--")
                        stdscr.addstr(6, 0,
                                      "StudentId: " + str(x[0]) + " Student name: " + x[1] + " Dob: " + x[2])
                        break
                    else:
                        continue

            # for i in range(0, len(students)):
            #     if (students[i].get_student_id() == studentId):
            #         stdscr.addstr(6, 0,
            #                       "StudentId: " + str(students[i].get_student_id()) + " Student name: " + students[
            #                           i].get_name() + " Dob: " + students[i].get_dob())
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 4:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            stdscr.addstr(2, 0, "courseId")
            courseId = int(stdscr.getstr(3, 0).decode())
            with open("course.txt", "r") as sf:
                m = 0
                for line in sf.readlines():
                    if str(line[0]) == str(courseId) in line:
                        x = line.split("--")
                        stdscr.addstr(6, 0,
                                      "CourseId: " + str(x[0]) + " Course name: " + str(x[1]) + " Credit: " + str(x[2]))
                        break
                    else:
                        continue
            # for i in range(0, len(courses)):
            #     if (courses[i].get_course_id() == courseId):
            #         stdscr.addstr(6, 0, "CourseId: " + str(courses[i].get_course_id()) + " Course name: " + courses[
            #             i].get_course_name() + " Credit: " + str(courses[i].get_course_credit()))
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
            studentId = add_student_id(stdscr)
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
                stdscr.addstr(y + i * 2, x, "StudentId: " + str(averageGpa[i][0]) + " Student AverageGpa: " +
                              str(averageGpa[i][1]))

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 8:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'We will decompress file into .dat')
            file_list = ['student.txt', 'course.txt', 'mark.txt']
            with zipfile.ZipFile('students.dat', 'w') as new_zip:
                for file_name in file_list:
                    new_zip.write(file_name)

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 9:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'We will load data from compress file')
            if os.path.isfile('students.dat'):
                zip_file = zipfile.ZipFile('students.dat', 'r')
                zip_file.extractall()
                if os.path.isfile('student.txt'):
                    f = open('student.txt', 'r').read().splitlines()
                    m = 4
                    for student in f:
                        stdscr.addstr(m, 0, student)
                        m += 1

            stdscr.getch()


        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 10:
            break

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)

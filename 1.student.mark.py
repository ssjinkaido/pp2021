courses = {}
students = []
marks = []


def enterNumberOfStudents():
    numberOfStudents = int(input("Enter the number of students: \n"))
    return numberOfStudents


def enterStudentsInfo():
    studentId = input("Enter student Id \n")
    studentName = input("Enter student name \n")
    studentDob = input("Enter student date of birth \n")
    return studentId, studentName, studentDob


def enterNumberOfCourses():
    numberOfCourses = int(input("Enter the number of courses \n"))
    return numberOfCourses


def enterCoursesInfo():
    courseId = input("Enter course Id \n")
    courseName = input("Enter course name \n")
    return courseId, courseName


# def enterStudentsMark(students, courses, marks):
#     courseId = (input("Enter the course Id \n"))
#     courseName = courses[courseId]
#     studentId = input("Enter the studentId \n")
#     studentName = students[studentId][0]
#     mark = float(input("Enter student marks \n"))
#     for i in range(len(marks)):
#         for item in marks[i].items():
#             for key,value in item.items():
#                 if(key==courseName and value[0]==studentName):
#                     marks[i][courseName][studentName].update(mark)

def enterStudentsMarks(students, course, marks):
    marks.append({course: {}})
    for i in range(len(students)):
        mark = float(input("Enter student marks \n"))
        marks[len(marks) - 1][course].update({students[i]["name"]: mark})


def showCoursesInfo(courses):
    print("Courses Info: ")
    for key, value in courses.items():
        print(value)


def showStudentsInfo(students):
    print("Student Info: ")
    for i in range(len(students)):
        print("Student Id " + "Student name " + "Student date of birth ")
        for value in students[i].items():
            print(value[1])


def showMarksInfo(marks, courseName, studentName):
    for i in range(len(marks)):
        for key, value in marks[i].items():
            for keyy, valuee in value.items():
                if (key == courseName and keyy == studentName):
                    print(valuee)


if __name__ == "__main__":

    numberOfStudents = enterNumberOfStudents()
    print(numberOfStudents)
    for i in range(numberOfStudents):
        studentId, studentName, studentDob = enterStudentsInfo()
        students.append({"id": studentId, "name": studentName, "dob": studentDob})

    numberOfCourses = enterNumberOfCourses()
    for i in range(0, numberOfCourses):
        courseId, courseName = enterCoursesInfo()
        courses[courseId] = courseName

    y = input("continue press y, not continue press n")
    while (y == "y"):
        s = input("enter m for marks input other to cancel")
        if (s == "m"):
            courseId = input("Enter the courseId: ")
            courseName = courses[courseId]
            enterStudentsMarks(students, courseName, marks)
        else:
            break

    print(marks)
    showCoursesInfo(courses)
    showStudentsInfo(students)
    courseName = input("Enter the name of the course: ")
    studentName = (input("Enter the name of the student: "))
    showMarksInfo(marks, courseName, studentName)

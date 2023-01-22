from classes import *

firstProgrammer = Programmer("Khalid",100029,"Python")
secondProgrammer = Programmer("Ali",106964,"C++")

firstStudent = Student("Ahmed",203456,"C++")
secondStudent = Student("Mohammed",202548,"Python")

print(firstProgrammer.write_info())
print("--"*10)
print(secondProgrammer.write_info())
print("--"*10)
print(firstStudent.write_info())
print("--"*10)
print(secondStudent.write_info())

def showContents(fileName):
    try:
        file = open(fileName, "r", encoding="utf-8")
    except:
        raise TypeError("'str' object cannot be interpreted as an integer")
    finally:
        print(f"Content is saved")
    content = file.read()
    file.close()
    return content

print(showContents("programmer.txt"))

print("--"*10)

print(showContents("student.txt"))
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
        raise TypeError("please provide the path")
    content = file.read()
    file.close()
    return content

try:
    print(showContents("programmer.txt"))
except:
    print("something went wrong!!")
else:
    print("successful")
finally:
    print("completed")

print("--"*10)

try:
    print(showContents("student.txt"))
except:
    print("something went wrong!!")
else:
    print("successful")
finally:
    print("completed")

from classes import *

programer1 = Programer("ali",1111111,"Java")
programer2 = Programer("ahmed", 222222, "Python")

student1 = Student("saad", 333333,"Php")
student2 = Student("saud", 444444, "Swift")

programer1.programer_info()
programer2.programer_info()

student1.programer_info()
student2.programer_info()

def printFile(file):
    print("*"*20)
    print(file)
    print()
    file = open(file, "r", encoding="utf-8")
    content = file.read()
    file.close()
    return content

try :
    printFile("programmers.txt")
    printFile("students.txt")
except :
    print("there is an error")
else :
    print("succesfully")
finally :
    print("completed")





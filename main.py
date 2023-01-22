from classes import Programmer , Student

def readFile(file):
    file = open(file , "r" , encoding='utf-8')
    content = file.read()
    file.close()
    return content


print()
_programmer = Programmer("Ali" , 23300 ,"Python")
_student = Student("Saad" , 30040 ,"Java")
print(_programmer.write_info())
print(_student.write_info())





try:
    print("----------------------------------")
    print(readFile("programmers.txt"))
    print(readFile("students.txt"))
    print("----------------------------------") 
except TypeError:
    print("Error Argment")
except Exception as e:
    print(e.__doc__)
finally:
    print("completed")
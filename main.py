import the_classes   
from the_classes import Programmer  
from the_classes import Student  

print(Programmer.write_info)
print(Student.write_info)


Programmer1 = Programmer("Mohammed",54673, "Python")
Student1 = Student("Nora", 6363, "CSS")


print(Programmer1.write_info())
print("_____________________________________")
print(Student1.write_info())
print("_____________________________________")


def File_Function(file_name):
    try:
        file = open(file_name, "r", encoding="utf-8")
    except:
        raise TypeError("Something went wrong !!")
    finally:
        print(f" Completing Process ... ")
    cat = file.read()
    file.close() 
    return cat

print(File_Function("programmer.txt"))
print("_____________________________________")
print(File_Function("student.txt"))
print("_____________________________________")





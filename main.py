import Class
try:
    programmer1=Class.Programmer("sara",383922,'Python')
    student1=Class.Student("salem", 290777 ,"C++")
except:
    print("somthing wrong!")
else:
    print("succesful.")
finally:
    print("completed")
programmer1.write_info()
student1.write_info()

student1=Class.Student("salem", 290777 ,"C++")
programmer1=Class.Programmer("Sara", 354635454 ,"Python")
programmer2=Class.Programmer("Nourah",34455856895, "C")
student2=Class.Student("Mohammed", 290777, "C#")
programmer1.write_info()
student1.write_info()
def read_file(file_name):
    contant=' '
    file=open(file_name,"r",encoding='utf-8')
    contant=file.read()
    file.close()
    return contant
print(read_file("student.txt"))
print(read_file("programmers.txt"))
try:
    programmer1=Class.Programmer("sara",383922,'Python')

except:
    print("somthing wrong!")
else:
    print("succesful.")
finally:
    print("completed")
programmer1.write_info()
student1.write_info()

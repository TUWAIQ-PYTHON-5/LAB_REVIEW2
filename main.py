import classes


programmer1 = classes.Programmer("Nada Albaty" , 1091586642, "Python")
programmer2 = classes.Programmer("Doha Dajem" , 1024375435, "Java")

Student1 = classes.Student("Maha Abdullah" , 1173658493, "C++")
Student2 = classes.Student("Noura Saleh" , 1098763526, "Flutter")


print(programmer1.write_info())
print(programmer2.write_info())
print(Student1.write_info())
print(Student2.write_info())


def read_file (file_name :str):
    content =""
    file= open (file_name,"r", encoding="utf-8")
    content = file.read()
    file.close()
    return content

try:
    read_file("programmers.txt")

except :
    print("somthing worng !!!")
else :
    print("Succesful !! ")
finally:
    print("compleated !!")


print(read_file("students.txt"))

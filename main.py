import classes 

programmer1 = classes.programmer ("Dooha Dajam", 438805742 , "Python")
programmer2 = classes.programmer("Nada albuti", 438805743 , "Python ")
student1 = classes.student("Razan Saeed", 43880056, " Java")
student2 = classes.student("Layan Saeed", 4388047,"C++")

print(programmer1.write_info())
print(programmer2.write_info())
print(student1.write_info())
print(student2.write_info())
print(programmer1.write_info())

def read_file ( file_name :str) :

    content = ''
    file = open(file_name, "r", encoding="utf-8")
    content= file.read()
    file.close()
    return content


try :
    
    print (read_file("programmers.txt"))


except TypeError :
    
    print("There was an error in the type")

except :
    
    print("somthing wrong !")

finally:
    print("coompleted")

print (read_file('students.txt'))

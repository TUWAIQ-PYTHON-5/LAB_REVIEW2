import classes  
programmer1=classes.Programmer("Raghad",77777,"python")

programmer2=classes.Programmer("Sarah",95479,"C#")

student1=classes.Student("Assel",88888,"java")

student2=classes.Student("Norah",687888,"C++")

print(student1.write_info())
print(student2.write_info())
print(programmer1.write_info())
print(programmer2.write_info())




def read_file(file_name):
    
    file =open(file_name,"r",encoding="utf-8")
    content=file.read()
    file.close()
    return content

try:
  print( read_file("programmers.txt"))
  print( read_file("students.txt"))
  
except:
    print("something wrong !")

else:
    print("successful")
finally:
    print("completed")


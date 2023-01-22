import classes

try:
    programmer1=classes.Programmer("amal",383922,'C#')
except:
    print("somthing wrong!")
else:
    print("succesful.")
finally:
    print("completed")
student1=classes.Student("salem",290777,"PYTHON")


student1.write_info()

def read_file(file_name :str):
    content=''
    file=open(file_name,"a+",encoding='utf-8')
    content=file.read()
    file.close()
    return content
programmer1.write_info() 
print(read_file("students.txt"))
print(read_file("programmers.txt"))
print(programmer1.get_name(),programmer1.get_programmer_id(),programmer1.get_languge())







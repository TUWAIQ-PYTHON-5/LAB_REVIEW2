import Classes

try:
    programmer1=Classes.Programmer("amal",383922,'C#')
except:
    print("somthing wrong!")
else:
    print("succesful.")
finally:
    print("completed")
student1=Classes.Student("salem",290777,"PYTHON")


student1.write_info()

def read_file(file_name :str):
    content=''
    file=open(file_name,"r+",encoding='utf-8')
    content=file.read()
    file.close()
    return content
programmer1.write_info()

print(read_file("students.txt"))
print(read_file("programmers.txt"))
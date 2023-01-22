
from classes import programmer
from classes import student



programmer1= programmer("sara",6546,"python")
print (programmer1.write_info())
student2 =student( "amal",3453,"c++")
print (student2.write_info())
 

print(programmer1.write_info())
print ("_" * 30)
print(student2.write_info())
print("_" * 30)

def file_function(file_name):
    try:
        file = open (file_name, 'r', encoding="utf-8")
    except :
        raise ValueError ("something went wrong!!")
    finally :
        print (f"complete process  .. ")
    cat = file.read
    file.close()
    return cat 

print (file_function("programmers.txt"))
print ("*"* 30)
print(file_function("student.txt"))
print ("*"* 30)
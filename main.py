import tow

def read_file(file_name :str):
    programmers=''
    file = open("programmers.txt", "r", encoding="utf-8")
    programmers=file.readline()
    file.close()
    return programmers



object_programmer=tow.Programmer("amal",10221,"c#")
object_student=tow.Student("hend",10987,"c++")
object_programmer.write_info()
object_student.write_info()
print(read_file("programmers.txt"))



import classes

try:
    programmer=classes.programmer("amal", 10222, "c")

except:
    print("somthing error")

else:
    print("succesful")
finally:
    print("complit")
student= classes.student("salem", 2099,"python")

student.write_info()

def read_file(file_name :str):
    content=''
    file=open(file_name,"a+",encoding='utf-8')
    content=file.read()
    file.close()
    return content
programmer.write_info()

print(read_file("students.txt"))
print(read_file("programmers.txt"))



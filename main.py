import classes


try:
    p1=classes.attribute("mohammed",3333,"python")
except:
    print("somthing wrong!")
else:
    print("succesful!")
finally:
    ("completed")
p2=classes.subclass('ali',111,"java")

p1.write_info()
p2.write_info()

def read_file(file_name):

    content = " "
    file = open(file_name, "a", encoding="utf-8")
    file.close()
    return content

print(read_file('programmers.txt'))
print(read_file('student.txt'))


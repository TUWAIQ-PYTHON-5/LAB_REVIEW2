import Classes

programmer1=Classes.programmer("ahmed",141,"c#")
student1=Classes.student("mohammed",415,"python")


programmer1.write_info()
student1.write_info()


def read_file(file_name):

    file=open(file_name,"r",encoding="utf-8")
    content=file.read()
    file.close()

try:
    read_file("prgrammers.txt")
except:
    print("something wrong!")
else:
    print("succesful")

finally:
    print("completed")


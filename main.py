from classes import Programmer, Student

def read_files(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            return content
    except:
        print("An error occured while reading the file")
        return None

try:
    programmer1=Programmer('Mohammed','983','java')
    programmer1.write_info()
    print(programmer1.print_info())

    student1=Student('Yazeed','12kl','JS')
    student1.write_info()
    print(student1.print_info())

    print(read_files('student'))

    student1.__studentID = "Not an int"
except TypeError as e:
    print("An error occured:", e)

try:
    #just write file name with out extend
    read_files('student_info.txt')
except Exception as e:
    print("An error occured:", e)
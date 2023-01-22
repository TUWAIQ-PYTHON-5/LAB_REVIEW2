from Classes import Programmer , student





prog1 = Programmer("mhammed" , 172 , "php")
std1 = student("ahmed", 122 , "JS")

prog1.write()
std1.write()




def readFile(fileName : str):
    file = open(fileName , "r" , encoding="utf-8")
    content = file.read()
    print("OJbect : " , content)
    file.close()


# prog1 = Programmer("mhammed" , 127 , "php")
# std1 = student("ahmed", 122 , "JS")
# prog1.write()
# std1.write()
# readFile("student.txt")
# readFile("example.txt")    
try:
    readFile("programmer.txt")
    readFile("student.txt")
except:
    print("somthing error") 
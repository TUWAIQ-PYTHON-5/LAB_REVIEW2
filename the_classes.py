class Programmer():
    type = "Programmer"
    def __init__(self, name : str, programmer_id : int, programming_language : str):
      
        self.__name = name 
        try:
            self.__programmer_id = programmer_id
        except ValueError:
            print("type is not int")
        self.__programming_language = programming_language

#____________________
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
#____________________
    def set_programmer_id(self, programmer_id):
        self.__programmer_id = programmer_id
    
    def get_programmer_id(self):
        return self.__programmer_id
#_______________________
    
    def set_language(self, programming_language):
        self.__programming_language = programming_language
    
    def get_language(self):
        return self.__programming_language
#_______________________

    def write_info(self):
        file = open("programmer.txt", "a+", encoding="utf-8")
        file.write(f"{self.__name} \t {self.__programmer_id} \t {self.__programming_language} ") 
        return ("Programmer information has been recorded")
        file.close()

################### subclass #######################
class Student(Programmer):

    type="Students"

    def __init__(self, name : str, student_id : int, programming_language : str):
        self.__name = name 
        try:
            self.__student_id = student_id
        except ValueError:
            print("type is not int")
        self.__programming_language = programming_language


    def write_info(self):
        file = open("student.txt", "w", encoding="utf-8")
        file.write(f"{self.__name} \t {self.__student_id} \t {self.__programming_language} ") 
        return ("Student information has been recorded")
        file.close()


#____________________
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
#____________________
    def set_programmer_id(self, student_id):
        self.__student_id = student_id
    
    def get_programmer_id(self):
        return self.__student_id
#_______________________
    
    def set_language(self, programming_language):
        self.__programming_language = programming_language
    
    def get_language(self):
        return self.__programming_language
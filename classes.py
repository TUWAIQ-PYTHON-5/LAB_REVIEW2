class Programmer:
    type = "programmer"
    def __init__(self,name:str,programmer_id:int,language:str):
        self.__name = name
        try:
            self.__programmer_id = programmer_id
        except ValueError:
            print("The input was not a valid integer.")
        self.__language = language
        
    def write_info(self):
        file = open("programmer.txt","a+",encoding="utf-8")
        file.write(f"-{self.__name}-\t-{self.__programmer_id}-\t-{self.__language}-\n")
        file.close()
        return f"Programmer information has been recorded"

    #name
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    #programmer_id
    def set_programmer_id(self, programmer_id):
        self.__programmer_id = programmer_id
    
    def get_programmer_id(self):
        return self.__programmer_id

    #language
    def set_language(self, language):
        self.__language = language
    
    def get_language(self):
        return self.__language
    
    
class Student(Programmer):
    type = "student"
    def __init__(self,name:str,student_id:int,language:str):
        self.__name = name
        try:
            self.__student_id = student_id
        except ValueError:
            print("The input was not a valid integer.")
        self.__language = language
    
        #name
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    #student_id
    def set_student_id(self, student_id):
        self.__student_id = student_id
    
    def get_student_id(self):
        return self.__student_id

    #language
    def set_language(self, language):
        self.__language = language
    
    def get_language(self):
        return self.__language

    def write_info(self):
        file = open("student.txt","a+",encoding="utf-8")
        file.write(f"-{self.__name}-\t-{self.__student_id}-\t-{self.__language}-\n")
        file.close()
        return f"Programmer information has been recorded"
class Programmer:

    type ="programmer"
    def __init__(self, name : str, programmer_ID : int, programming_language : str):
            self.__name = name 
            self.__programmer_ID = programmer_ID
            self.__programming_language = programming_language
    
    def set_name(self, name):
            self.__name = name
        
    def get_name(self):
            return self.__name
    
    def set_programmer_ID(self,programmer_ID):
        if type(programmer_ID) != int:
            raise ValueError("Please provide a valid number")
        
        self.__programmer_ID = programmer_ID

    def get_programmer_ID(self):
        return self.__programmer_ID
    
    def set_programming_language(self,programming_language):
        self.__programming_language = programming_language

    def get_programming_language(self):
        return self.__programming_language


    def write_info(self):
        file =open("programmers.txt", "a", encoding="utf-8")
        file.write(f"{self.__name}\t\t{self.__programmer_ID}\t\t{self.__programming_language}\n") 
        file.close()
        return "Programmer information has been recorded"



class Student(Programmer):
    type ="Student"
    def __init__(self, name : str, student_ID : int, programming_language : str):
        super().__init__(name,student_ID,programming_language)
        self.__student_ID = student_ID

    def set_student_ID (self, student_ID):
         if type(student_ID) != int:
             raise ValueError("Please provide a valid number")
         self.__student_ID = student_ID
    
    
    def get_student_ID(self):
         return self.__student_ID

    def write_info(self):
        file = open("students.txt", "a", encoding="utf-8")
        file.write(f"{self.get_name()}\t\t{self.__student_ID}\t\t{self.get_programming_language()}\n") 
        file.close()
        return "Programmer information has been recorded"






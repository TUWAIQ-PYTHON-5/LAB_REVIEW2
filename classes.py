class programmer():
    type = "programmer"

    def __init__(self, name : str, programmer_ID : int, programming_language : str):
        self.__name=name
        self.__programmer_ID =  programmer_ID
        self.__programming_language = programming_language
        

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.__name


    def set_programmer_ID(self, programmer_ID):
        if type(self.__programmer_ID) != int:
            raise TypeError ("the programming id must be integer")
        self.programmer_ID = programmer_ID

    def get_programmer_ID(self):
        return self.__programmer_ID   


    def set_programming_language(self, programming_language):
        self.programming_language = programming_language
    def get_programming_language(self):
        return self.__programming_language



    def write_info(self): 
        file=open("programmers.txt",'a+',encoding="utf-8")
        
        try:
            file.writelines(f"{self.__name}\t\t {self.__programmer_ID}\t\t {self.__programming_language}\n")
        except:
            print('error')
        file.close()
        return ("Programmer information has been recorded")

class student(programmer):
    type = "student"
    def __init__(self, name : str, student_ID : int, programming_language : str):
        super().__init__(name, student_ID, programming_language)
        
        self.__student_ID = student_ID

    def set_student_ID(self, student_ID):
        self.__student_ID = student_ID
    def get_student_ID(self):
        return self.__student_ID   

    def write_info(self): 
        file=open("student.txt",'a+',encoding="utf-8")
        file.write( f"{self.get_name()} \t{self.__student_ID}\t{self.__programming_language}\n")
        file.close()
        return ("student information has been recorded")

    
        
    
     

    
    
    
    

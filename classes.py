class programmer :
    type = "programmer"
    
    def __init__(self, name : str, programmer_ID : int , programming_language : str) -> None :
        
        self.__name = name 
        self.__programmer_ID = programmer_ID
        self.__programming_language = programming_language

# encabsulate the name

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

# encabsulate the programmer_ID

    def set_programmer_ID(self, programmer_ID):
        
        # To check the type of programmer_ID 
        if type(programmer_ID != 0 ) :
            raise ValueError ("The programmer ID must be int")

        self.__programmer_ID = programmer_ID
    
    def get_programmer_ID(self):
        return self.__programmer_ID


# encabsulate the programming_language

    def set_programming_language(self, programming_language):
        self.__programming_language = programming_language
    
    def get_programming_language(self):
        return self.__programming_language


#method1

    def write_info(self) :
        
        file = open("programmers.txt", "a", encoding="utf-8")
        file.write(f"{self.__name}\t\t{self.__programmer_ID}\t\t{self.__programming_language}"+"\n")
        file.close()
        return "Programmer information has been recorded"


# sub class

class student(programmer):

    type = "student"
    
    def __init__(self, name : str, student_ID : str, programming_language : int ):
        super().__init__(name, student_ID , programming_language)

        self.__student_ID = student_ID

    # student
    def set_student_ID(self, student_ID):
        
        # To check the type of student_ID 
        if type(student_ID != 0 ) :
            raise ValueError ("The student ID must be int")

        self.__student_ID = student_ID
    
    def get_student_ID(self):
        return self.__student_ID

# method2

    def write_info(self) :

        file = open("students.txt", "a", encoding="utf-8")
        file.write(f"{self.get_name()}\t\t{self.__student_ID}\t\t{self.get_programming_language()}"+"\n")
        file.close()
        return "Student information has been recorded"



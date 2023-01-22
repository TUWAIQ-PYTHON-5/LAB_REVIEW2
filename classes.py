class Programer :
    type = "programer"
    def __init__(self, name : str, programerID : int, programerLanguage : str) :
        self.__name = name
        self.__programerID = programerID
        self.__programerLanguage = programerLanguage

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_programerID(self, programerID):
        if programerID != int :
            raise TypeError("Only integers are allowed") 
        self.__programerID = programerID
    
    def get_programerID(self):
        return self.__programerID
    
    def set_programerLanguage(self, programerLanguage):
        self.__programerLanguage = programerLanguage
    
    def get_programerLanguage(self):
        return self.__programerLanguage
    
    def programer_info(self) :
        
        self.set_name(self.get_name())
        try :
            self.set_programerID(self.get_programerID())
        except :
              raise TypeError("Only integers are allowed") 
        self.set_programerLanguage(self.get_programerLanguage())

        file = open("programmers.txt", "a+", encoding="utf-8")
        file.write(f"-name-{self.__name}\t-programmer ID-{self.__programerID}\t-Programming language-{self.__programerLanguage}\n")
        file.close()
        print("Programmer information has been recorded")



# programer1 = Programer("ali", 111111, "Python")
# programer2 = Programer("ahmed", 222222, "Java")

# programer1.programer_info()
# programer2.programer_info()




class Student(Programer) :
    type = "student" 
    def __init__(self, name : str, programerID : int, programerLanguage : str) :
        super().__init__(name, programerID, programerLanguage)
    
    def programer_info(self) :
        self.set_name(self.get_name())
        try :
            self.set_programerID(self.get_programerID())
        except :
              raise TypeError("Only integers are allowed")
        self.set_programerLanguage(self.get_programerLanguage())

        file = open("students.txt", "a+", encoding="utf-8")
        file.write(f"-name-{self.get_name()}\t-programmer ID-{self.get_programerID()}\t-Programming language-{self.get_programerLanguage()}\n")
        print("Programmer information has been recorded")
        file.close()
        
    
# student1 = Student("saad", 333333, "Php")
# studrnt2 = Student("saud", 444444, "Swift")

# student1.programer_info()
# studrnt2.programer_info()

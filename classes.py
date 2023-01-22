class attribute():
    type = "programer"
    def __init__(self,name:str,programer_id:int,program_language:str):
        self.__name=name
        self.__programer_id=programer_id
        self.__program_language=program_language
        
        

    def set_name (self,name):
        self.__name=name

    def get_name(self):
        return self.__name

    def set_programer_id (self,programer_id):
        self.__programer_id=programer_id

        if programer_id != int:
            raise TypeError ("error type is not integr")

    def get_programer_id(self):
        return self.__programer_id

    def set_program_language (self,program_language):
        self.__program_language=program_language

    def get_program_language(self):
        return self.__program_language
        
########################################################################
    def write_info(self):
      
        

        file = open('programmers.txt', "a", encoding="utf-8")
        file.write(f"{self.get_name()}/t {self.get_programer_id()}/t{self.get_program_language()}")
        file.close()
        return "Programmer information has been recorded"

class subclass(attribute):

    type = "student"
    def __init__(self,name:str,student_id:int,program_language:str):
        super().__init__(name,student_id,program_language)
        self.__student_id=student_id
        
        


    def set_student_id (self,student_id):
        self.__student_id=student_id

        if student_id != int:
            raise TypeError ("error type is not integr")

    def get_student_id(self):
        return self.__student_id


    def write_info(self):
        

        file = open('student.txt', "a", encoding="utf-8")
        file.write(f"{self.get_name()}/n {self.get_student_id()}/n{self.get_program_language()}")
        file.close()
        return "Programmer information has been recorded"    
        


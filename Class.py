class Programmer:
    type="programmer"
    def __init__(self, name : str, programmer_ID : int,  language: str):
        self.__name =name
        self.__programmer_ID =programmer_ID
        self.__language =language 
    def set_name(self,name):
        self.__name=name
    def get_name(self):
         return self.__name
    def set_programmer_ID(self, programmer_ID):
        if not type(programmer_ID) == int:
            raise ValueError("Please provide a valid programmer ID")
        return self.__programmer_ID
        self.__programmer_ID = programmer_ID
    def get_programmer_ID(self):
        return self.__programmer_ID
    def language(self,language):
        self.__programing_language=language
    def get_language(self):
         return self.__language

    def write_info(self):
        file = open("programmers.txt", "a+", encoding='utf-8')
        file.write(f"{self.__name} \t\t {self.__programmer_ID} \t\t {self.__language}") 
        file.close()
        return "Programmer information has been recorded"
class Student(Programmer):
    type="Students"
    def __init__(self, name: str, student_ID: int, language: str):
        super().__init__(name, student_ID, language)
        self.__student_ID =student_ID

    def set_student_ID(self, student_ID):
        if not type(student_ID) == int:
            raise ValueError("Please provide a valid a student ID")
    
        self.__student_ID = student_ID

    def get_student_ID(self):
        return self.__student_ID
    
    def write_info(self):
        file = open("student.txt", "a+", encoding='utf-8')
        file.write(f"{self.get_name()}\t\t{self.get_student_ID}\t\t {self.get_language()}") 
        file.close()
        x="Programmer information has been recorded"
        return x
    
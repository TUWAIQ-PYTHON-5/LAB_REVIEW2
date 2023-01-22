class Programmer:
    Type = 'Programmer'
    def __init__(self,name:str,programmerID:int,programmingLanguage:str):
    
        self.set_name(name)
        self.set_programmerID(programmerID)
        self.set_programmingLanguage(programmingLanguage)

    def set_name(self,name:str):
        self.__name = name.upper()
    def get_name(self):
        return self.__name

    def set_programmerID(self,programmerID:int):
        if type(programmerID) != int:
            raise TypeError('ID Type is Wrong')

        self.__programmerID = programmerID
    def get_programmerID(self):
        return self.__programmerID
    
    def set_programmingLanguage(self,programmingLanguage:str):
        self.__programmingLanguage = programmingLanguage
    def get_programmingLanguage(self):
        return self.__programmingLanguage

    #Methods
    def write_info(self):
        programmer_file_info=open('programmer_info.txt','a+',encoding='utf-8')
        programmer_file_info.write(f'Programmer Name is : {self.get_name()} \t\t Programmer ID is : {self.get_programmerID()} \t\t Programming Language is : {self.get_programmingLanguage()} \n')
        programmer_file_info.close()
        return f'Programmer information has been recorded'

    def print_info(self):
        return f'Programmer Name is : {self.get_name()} \t\t Programmer ID is : {self.get_programmerID()} \t\t Programming Language is : {self.get_programmingLanguage()} '

     
##########################################################################################

class Student(Programmer):
    Type='Student'
    def __init__(self, name: str, studentID:int, programmingLanguage: str):
        super().__init__(name, studentID, programmingLanguage)
        self.set_name(name)
        self.set_studentID(studentID)
        self.set_programmingLanguage(programmingLanguage)
    
    def set_studentID(self,studentID):
        if type(studentID) != int:
            raise TypeError('ID Type is Wrong')
        self.__studentID = studentID
    def get_studentID(self):
        return self.__studentID

    #Methods
    def write_info(self):
        student_file_info=open('student_info.txt','a+',encoding='utf-8')
        student_file_info.write(f'Student Name is : {self.get_name()} \t\t Student ID is : {self.get_studentID()} \t\t Programming Language is : {self.get_programmingLanguage()} \n')
        student_file_info.close()
        return f'student information has been recorded'
    
    def print_info(self):
        return f'Student Name is : {self.get_name()} \t\t Student ID is : {self.get_programmerID()} \t\t Programming Language is : {self.get_programmingLanguage()} '


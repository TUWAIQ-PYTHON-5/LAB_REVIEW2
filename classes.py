
class Programmer():
    Type="programmer"
    def __init__(self,name : str ,programmer_id :int ,languge :str ):
        self.__name=name
        self.__programmer_id=programmer_id
        self.__languge= languge
    
    def set_name(self, name):
        self.__name=name
    def get_name(self):
        return self.__name
    
    
    def set_programmer_id(self,programmer_id):
        if type(self.__programmer_id) != int:
            raise TypeError("the programmer ID must be integer")
        self._programmer_id=programmer_id
    def get_programmer_id(self):
        
        return self.__programmer_id

    def set_languge(self,languge):
        self.__languge= languge
    def get_languge(self):
        return self.__languge
        file.close()
    def write_info(self):
        file=open('programmers.txt',"a",encoding='utf-8')
        try:
            file.writelines(f"{self.__name}\t\t {self.__programmer_id}\t\t {self.__languge}\n")
        except:
            

        
         return "Programmer information has been recorded"
class Student(Programmer):
    Type='student'
    def __init__(self, name: str, student_id: int, languge: str):
        super().__init__(name, student_id, languge)
        self.__student_id=student_id

    def set_student_id(self,student_id):
        self.__student_id=student_id
    def get_student_id(self):
        return self.__student_id

    def write_info(self):
        file=open('students.txt',"a",encoding='utf-8')
        file.write(f"{self.get_name()}\t\t {self.__student_id}\t\t {self.get_languge()}\n")
        file.close()
        return "Student information has been recorded"
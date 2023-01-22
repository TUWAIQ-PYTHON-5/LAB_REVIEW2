class Programmer:
    type="programmer" 
    def __init__(self,name,programmer_id,programming_language):
        
        self.__name=name 
        self.__programmer_id=programmer_id
        self.__programming_language =programming_language

    def set_name(self,name):
            self.__name = name

    def get_name(self):
            return self.__name  

    def set_programmer_id(self,programmer_id):
       if  type(programmer_id)!=int:
           raise TypeError("Enter numbers")
       self.__programmer_id = programmer_id

    def get_programmer_id(self):
            return self.__programmer_id         

    def set_programming_language(self,programming_language):
            self.__programming_language = programming_language

    def get_programming_language(self):
            return self.__programming_language



    def write_info(self):
        file=open("programmers.txt","a",encoding="utf-8")
        file.write(f"{self.get_name()}\t\t {self.get_programmer_id()}\t\t{self.get_programming_language()}\t\t")
        file.close()
        return "Programmer information has been recorded"
        

         
class Student(Programmer):
    type= "student"
    def __init__(self,name,student_id,programming_language):
        super().__init__(name,student_id,programming_language) 
        self.__student_id=student_id
        

    def set__student_id(self,student_id):
        self.__student_id = student_id
        if  type(student_id)!=int:
          raise TypeError("Enter numbers!")

    def get__student_id(self):
            return self.__student_id      


    def write_info(self):
        file=open("students.txt","a",encoding="utf-8")
        file.write(f"{self.get_name()}\t\t {self.get__student_id()}\t\t {self.get_programming_language()}\t\t")
        file.close()
        return "Programmer information has been recorded"
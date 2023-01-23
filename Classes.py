class programmer():
    Type="programmer"

    def __init__(self, name: str, ID_programmer  :int, programming_language: str):

        self.__name = name
        self.__ID_programmer = ID_programmer
        self.__programming_language = programming_language

    def set_name(self,name):
        self__name = name

    def get_name(self, name):
        return self . __name



    def set_ID_programmer(self,ID_programmer):
        if type(ID_programmer) != int:
            raise TypeError("the type is not int")
        self.__ID_programmer = ID_programmer

    def get_ID_programmer(self, ID_programmer):
        return self . __ID_programmer



    def set_programming_language(self,programming_language):
        self__programming_language = programming_language

    def get_programming_language(self, programming_language):
        return self . __programming_language


    

    def write_info(self):
        file_1 = open("write programmer info.txt", "a", encoding="utf-8")
        try:
            file_1.writelines(f"{self.get_name()} / {self.get_ID_programmer()} / {self.get_programming_language()} \n")
        except:
            print('error')
        file_1.close()
        return "Programmer information has been recorded"

class student(programmer):
    def __init__(self, name : str , student_id : int  , programmin_language):
        super().__init__(name, student_id , programmin_language )
        self.__student_id=student_id

    def set_student_id(self,student_id):
        self.__student_id=student_id
    def get_student_id(self):
        return self.__student_id

    def write_info(self):
        file_name =open('student.txt'  , "a" , encoding="utf-8") 
        try:
            file_name.writelines(f"{self.get_name()} / {self.get_ID_programmer()} / {self.get_programming_language()} \n")
        except:
            print('error')
        file_name = open("student.txt", "r", encoding="utf-8")
        
        file_name.close()
import os

class Programmer :


    def __init__(self , name , ID_programmer , programmin_language) -> None:
        self.__name = name
        self.__ID_programmer = ID_programmer
        self.__programming_language = programmin_language


    def set_name(self, name : str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_ID_programmer(self, ID_programmer : str):
        if type(ID_programmer) != int:
            raise ValueError("enter correct Id")
        else:
            self.__ID_programmer = ID_programmer    
            
        

    def get_ID_programmer(self):
        return self.__ID_programmer


    def set_programming_language(self, programming_language : str):
        self.__programming_language = programming_language

    def get_programming_language(self):
        return self.__programming_language

    def write(self ): 
        file_name =open('programmer.txt'  , "a" , encoding="utf-8") 
        file_name.writelines(f"{self.get_name()} / {self.get_ID_programmer()} / {self.get_programming_language()} \n ")
        file_name = open("programmer.txt", "r", encoding="utf-8")
        
        file_name.close()

        return "Programmer information has been recorded"  
class student(Programmer):
    def __init__(self, name : str , ID_programmer : int  , programmin_language):
        super().__init__(name, ID_programmer , programmin_language )
        

    def write(self):
        file_name =open('student.txt'  , "a" , encoding="utf-8") 
        file_name.writelines(f"{self.get_name()} / {self.get_ID_programmer()} / {self.get_programming_language()} \n ")
        file_name = open("student.txt", "r", encoding="utf-8")
        
        file_name.close()
             

        
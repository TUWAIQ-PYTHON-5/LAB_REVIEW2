
class Programmer():

    kind="programmer"

    def __init__(self , name : str , programmerID : int , language : str):
        self.__name = name
        self.__language = language
        try:
            if not type(programmerID) is int: #check type of programmerID 
                raise TypeError("Type Error")
            else:
                self.__programmerID = programmerID
        except Exception :
            pass

    def set_name(self , name):
         self.__name = name

    def get_name(self):
        return self.__name 
#-------------------------------------------------
    def set_programmerID(self , programmerID):

              self.__programmerID = programmerID
            
    def get_programmerID(self):
        return self.__programmerID 
#------------------------------------------------
    def set_lang(self , language):
            self.__language = language

    def get_lang(self):
            return self.__language


#-----------------------------------------------
    def write_info(self):
        try:
            file = open("programmers.txt", 'a+', encoding='utf-8')
            file.write(f"{self.__name} \t {self.__programmerID} \t {self.__language} \t")
            file.close()
            return "Programmer information has been recorded"
        except Exception as e:
            return "ID of Programmers must be Intger : " + e.__doc__
        
     
#-----------------------------------------------

class Student(Programmer):


    kind = "student"
    def __init__(self, name: str, studentID: int, language: str ):
        super().__init__(name, studentID, language)

        try:
            if not type(studentID) is int:
                    raise TypeError("Type Error")
            else:
                    self.__studentID = studentID
        except Exception as e:
            pass
            
    def set_studentID(self , studentID):
            self.__studentID = studentID

    def get_studentID(self):
          return  self.__studentID

    
    def write_info(self):
        try:
            file = open("students.txt", 'a+', encoding='utf-8')
            file.write(f"{self.get_name()} \t {self.__studentID} \t {self.get_lang()} \t")
            file.close()
            return "Student information has been recorded"
        except Exception as e:
            return "ID of student must be Intger : " +e.__doc__


    
        
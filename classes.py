
class programmer :
    type = "programmer"
    def __init__(self, name , programmer_id , programmer_languge):
        self.__name = name
        try:
          self.__programmer_id = programmer_id
        except ValueError:
            print ("type is not int")  
        self.__programmer_languge= programmer_languge


        
    def set_name (self,name):
        self.__name= name 
    def get_name (self):
        return self.__name
#-------------------------------------------
    def set_programmer_id(self,programmer_id):
         self.__programmer_id = programmer_id
    def get_programmer_id(self):
         return self.__programmer_id
 #-------------------------------------------
    def set_programmer_languge(self,programmer_languge):
         self.__programmer_languge = programmer_languge
    def get_programmer_id(self):
         return self.__programmer_languge
#-------------------------------------------


    def write_info(self) :
        file_name =open('programmers.txt'  , "a+" , encoding="utf-8") 
        file_name.write( f"{self.__name}\t\t{self.__programmer_id}\t\t{self.__programmer_languge}")
        file_name.close()
        return ("programmer information has been recorded")
         
        
class student (programmer):
    tybe = "student" 
    def __init__(self, name, student_id, programmer_languge):
        super().__init__(name, student_id, programmer_languge)
        
        self.__name = name
        try:
          self.__student_id = student_id
        except ValueError:
            print ("type is not int")  
        self.__programmer_languge= programmer_languge

    def set_name (self,name):
        self.__name = name 
    def get_name (self):
        return self.__name
#-------------------------------------------
    def set_programmer_id(self, student_id):
         self.__student_id = student_id
    def get_programmer_id(self):
         return self.__student_id
 #-------------------------------------------
    def set_programmer_languge(self,programmer_languge):
         self.__programmer_languge = programmer_languge
    def get_programmer_id(self):
         return self.__programmer_languge

    def write_info(self) :
        file_name =open('student.txt'  , "a+" , encoding="utf-8") 
        file_name.write( f"{self.__name}\t\t{self.__student_id}\t\t{self.__programmer_languge}")
        file_name.close()
        
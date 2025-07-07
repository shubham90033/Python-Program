
class MyClass:
    def __init__(self,value):
        self.value = value
        print("Object created with value:", self.value)
    
    def __name(self):
        print("private function")
    
    def public(self):          # encaptulation
        
        self.__ran=20           # private variable
        
        self.__name()

    def getdata(self):                      # we can say getter
        print(self.__ran)

    def setdata(self):                      # setter we can set the private the variable


        self.__ran=int(input("enter the new val which u want change"))        # change the value of private variable
        print("new __ran value",self.__ran)




obj = MyClass(10)       # object of class 

obj.public()
obj.getdata()
obj.setdata()
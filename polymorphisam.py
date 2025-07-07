# POLYMORPHISAM
  #over ride
class Parent:
    def show_message(self):
        print("This is the parent class method.")

class Child(Parent):
    def show_message(self):
        super().show_message()  # Calls the parent class method
        print("This is the child class method (Overridden).")







class MathOperations:
    def add(self, a, b, c=0,d=0,e=0):
        return a + b + c + d + e
    
    def mul(self,a,b,c , d=1, e=1):
        print("multiplication")
        return a * b *c * d *e
    
 
obj = MathOperations()
print(obj.add(1,2,3))
print(obj.add(1,6,3))
print(obj.mul(1,2,3))
print(obj.mul(1,6,3,2))


child_obj = Child()
child_obj.show_message()

  #using function

class add():
    a=10
    b=20
    print(a+b)

add()


#Abstraction Using Abstract Class

from abc import ABC,abstractmethod 
class Animal:
    @abstractmethod
    def sound(self):
        pass
class dog:
    def sound(self):
        print("dog barks")
obj=dog()
obj.sound()



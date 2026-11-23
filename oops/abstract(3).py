from abc import ABC ,abstractmethod
class student(ABC):
     @abstractmethod
     def information(self):
          pass
class teacher(student):
     def information(self):
          print("student information..")

object=teacher()
object.information()
from abc import ABC ,abstractmethod
class student:
    @abstractmethod
    def info(self):
        pass
class principla:
    def info(self):
        print("student name...")
o=principla()
o.info()
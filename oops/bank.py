from abc import ABC ,abstractmethod
class bank(ABC):
    @abstractmethod
    def deposit(self):
        pass
class sbi(bank):
    def deposit(self):
        print("money deposit  in SBI")
    
class HDFC(bank):
    def deposit(self):
        print("money deposit in HDFC.")

object=sbi()
object.deposit()

obj=HDFC()
obj.deposit()


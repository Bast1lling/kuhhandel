from enum import Enum

class Money(Enum):
    ZERO = 0
    TEN = 10
    FIFTY = 50
    ONE_HUNDRED = 100
    TWO_HUNDRED = 200
    FIVE_HUNDRED = 500

    def __str__(self):
        return str(self.value)
    
    def __int__(self):
        return self.value
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.value == other.value    

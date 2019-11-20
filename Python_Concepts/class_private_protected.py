
class A:
    def __init__(self):
        self.x = 1   # public variable
        self._y = 2  # Private variable programmer should refrain from using
        self.__z = 3  # Protected variable

    def getY(self):
        return self._y

    def getZ(self):
        return self.__z

a = A()

print(a.x)
print(a.getY())
print(a.getZ())
print("-"*20)
print(a.x)
print(a._y)  # warning to access private variable
# print(a.__z)   # Error to access protected variable

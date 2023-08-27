from singleton import SingletonClass



class number(metaclass=SingletonClass):
    _num = None
    def __init__(self, num):
        print("here")
        self._num = num

    def get_num(self):
        return self._num

    def set_num(self, value):
        if isinstance(value, int):
            self._num = value




obj1 = number(1)
print(obj1.get_num())

print("**** **** "*10)
obj2 = number(2)
print(obj1.get_num())
print(obj2.get_num())
obj2.set_num(3)

print("**** **** "*10)
print(obj1.get_num())
print(obj2.get_num())


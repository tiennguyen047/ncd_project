
"""this module is singleton design pattern
"""
class SingletonClass(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # print("create new instance for {} object". format(cls.__name__))
            cls._instances[cls] = super(SingletonClass, cls).__call__(*args, **kwargs)
        # else:
            # print("object instance {} is created, return {}".format(cls.__name__, cls.__dict__))
        return cls._instances[cls]
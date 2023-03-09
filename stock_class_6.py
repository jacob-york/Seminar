from expects_impl_7 import *
from generic_expects_impl_8 import *
from variable_param_impl_9 import *


class A:

    def __init__(self, integer=None, string=None):
        self._integer = integer
        self._string = string

    def get_integer(self):
        return self._integer

    def set_integer(self, new_integer):
        self._integer = new_integer

    def get_string(self):
        return self._string

    def set_string(self, new_string):
        self._string = new_string

    def all_integers(self, param1, param2, param3):
        # some code...
        pass

    def all_strings(self, param1, param2, param3):
        # some code...
        pass


def main():
    my_class = A()
    my_class.set_integer("Hello World!")
    my_class.set_string(5)


# entry point
if __name__ == "__main__":
    main()

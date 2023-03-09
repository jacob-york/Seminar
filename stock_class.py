from expects_impl import *
from generic_expects_impl import *


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


def main():
    my_class = A()
    my_class.set_integer("Hello World!")
    my_class.set_string(5)


# entry point
if __name__ == "__main__":
    main()

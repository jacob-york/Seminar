from g_expects_impl import *
from i_generic_expects import *
# from dummy_expects import *


class A:

    def __init__(self, integer=None, string=None):
        self._integer = integer
        self._string = string

    @property
    def integer(self):
        return self._integer

    @integer.setter
    def integer(self, new_integer):
        self._integer = new_integer

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, new_string):
        self._string = new_string

    def all_integers(self, integer1, integer2, integer3):
        # some code...
        pass

    def all_strings(self, string1, string2, string3):
        # some code...
        pass


def main():
    my_class = A()
    my_class.integer = "Hello World!"
    my_class.string = 5


# entry point
if __name__ == "__main__":
    main()

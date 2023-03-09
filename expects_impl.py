"""Type restriction with decorators."""


def expects_int(function):
    def inner(self, arg):
        if not isinstance(arg, int):
            raise TypeError(
                "\"" + str(arg) + "\" of type " + str(type(arg)) + " must be of type int."
            )
        function(self, arg)
    return inner


def expects_string(function):
    def inner(self, arg):
        if not isinstance(arg, str):
            raise TypeError(
                "\"" + str(arg) + "\" of type " + str(type(arg)) + " must be of type string."
            )
        function(self, arg)
    return inner

"""Type restriction with decorators."""


def expects_int(setter_method):
    def inner(self, arg):
        if not isinstance(arg, int):
            raise TypeError(
                "\"" + str(arg) + "\" of type " + str(type(arg)) + " must be of type int."
            )
        setter_method(self, arg)
    return inner


def expects_string(setter_method):
    def inner(self, arg):
        if not isinstance(arg, str):
            raise TypeError(
                "\"" + str(arg) + "\" of type " + str(type(arg)) + " must be of type string."
            )
        setter_method(self, arg)
    return inner

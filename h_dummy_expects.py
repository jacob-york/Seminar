def expects(setter_method, param_type):
    def inner(self, arg):
        if not isinstance(arg, param_type):
            raise TypeError(
                "\"" + str(arg) + "\" of type " + str(type(arg)) + " must be of type int."
            )
        setter_method(self, arg)
    return inner

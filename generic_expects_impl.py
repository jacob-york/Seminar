"""Generic expects implementation"""


def expects(param_type):

    def decorator(function):
        def inner(self, arg):
            if not isinstance(arg, param_type):
                raise TypeError(
                    "\"" + str(arg) + "\" of type " + str(type(arg)) + " must be of type " + str(param_type) + "."
                )
            function(self, arg)
        return inner

    return decorator

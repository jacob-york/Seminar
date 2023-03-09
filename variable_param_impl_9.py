def expects(*param_types):
    def decorator(function):
        """Used with METHOD definitions to restrict the parameter to param_type.
        Does not support functions."""
        def inner(self, *args):
            for i in range(len(param_types)):
                if not isinstance(args[i], param_types[i]):
                    raise TypeError(
                        "\"" + str(args[i]) +
                        "\" of type " + str(type(args[i])) +
                        " must be of type " + str(param_types[i]) + "."
                    )
            function(self, *args)
        return inner
    return decorator

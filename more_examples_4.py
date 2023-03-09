def append_a(function):
    def inner(param1, param2):
        return function(param1, param2) + "s"

    return inner


def append_s(function):
    def inner(param1, param2):
        return function(param1, param2) + "a"

    return inner


@append_a  # decorators can be stacked
@append_s  # executes bottom-up
def concatenate(param1, param2):
    return str(param1) + str(param2)

# equivalent to:
# concatenate = append_a(concatenate)
# concatenate = append_s(concatenate)


print(concatenate("water", "fall"))    # console output: waterfallas

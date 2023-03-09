# simple decorator:
def decorator(function):
    def return_func(param1, param2):  # return_func is conventionally called "inner" or "wrapper."
        return function(param2, param1)

    return return_func

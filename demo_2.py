from decorator_impl import decorator


# consider the following:

def my_function(param1, param2):
    return param1 + param2


print(my_function("water", "fall"))     # console output: "waterfall"

my_function = decorator(my_function)    # applying decorator; This decorator modifies my_function **post-definition**:

print(my_function("water", "fall"))     # console output: "fallwater"

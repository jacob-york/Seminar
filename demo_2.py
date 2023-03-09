from decorator_impl_3 import decorator


# consider the following:

def concatenate(param1, param2):
    return param1 + param2


print(concatenate("water", "fall"))     # console output: "waterfall"

concatenate = decorator(concatenate)    # applying decorator; This decorator modifies my_function **post-definition**:

print(concatenate("water", "fall"))     # console output: "fallwater"

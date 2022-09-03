# In Python you can have a variable within a function that has the same name as a variable outside of
# that function.
# However despite having the same name those variables are not the same variable.


# Variables created within functions.
# Have a local scope while variables that are created outside of functions have a global scope

example = "hello world"  # global


def loc_ex():
    example = "this"  # local
    return example


print(loc_ex())
print(example)

# The first is that local variables cannot be used by code in the global scope.
# The second point is that global variables can be accessed by code in a local scope.
# The third point is that code in the local scope of one function can't use variables from another functions
def loc_ex1():
    global fruit
    fruit = "pear"
    print(fruit)

fruit = "apple"
loc_ex1()
print(fruit)
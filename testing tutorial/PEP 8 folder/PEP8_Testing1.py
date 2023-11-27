# for getting the score card and how standard our code is 
# python -m pylint fileName  --> run this command to terminal for checking


"""Module providing a function printing add."""
def add_numbers(x,y):
    '''
    this function adds two numbers and return result
    >>> add_numbers(5,5)
    10
    >>> add_numbers(5,6)
    11
    '''
    result=x+y
    return result
print(add_numbers(5,6))
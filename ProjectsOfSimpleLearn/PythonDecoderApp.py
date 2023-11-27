def log_message(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(r"C:\Users\phaldar\Downloads\records.txt", 'a') as file:
            file.write(result + '\n')
        return result
    return wrapper

@log_message
def a_function_that_returns_a_string():
    return "A string"

@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"

# Example Usage
a_function_that_returns_a_string()
a_function_that_returns_a_string_with_newline("Hello, world!")
a_function_that_returns_another_string("Custom message")

def outer_functions(origi):
    message= msg
    def inner_function():
        return origi()
    return inner_function

hi_func = outer_functions('hi')
bye_func = outer_functions('bye')

hello_func()
  
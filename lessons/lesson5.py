# def simple_decorator (func):
#     def wrapper ():
#         print ('перед вызовом!!')

#         func()

#         print ('после вызова!!')
#     return wrapper
# @simple_decorator
# def say_hello ():
#     print ('Привет!!')

# @simple_decorator
# def test ():
#     print ('Тест')

# test()

def greeting_decorator (func):
    def wrapper (name):
        print (f'Привет {name}')
        func (name)
    return wrapper

@greeting_decorator 
def greeting (name):
    print (f'как дела {name}!!')
greeting('John Dee')

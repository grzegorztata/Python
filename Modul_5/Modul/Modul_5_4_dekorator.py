""" def say_hello():
    greeting = "Hello stranger!"
    return greeting """

def say_louder(func):  # w dekoratorze używamy 'funkcja w funkcji'
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@say_louder
def say_hello():
    greeting = "Hello stranger!"
    return greeting

print(say_hello())  # HELLO STRANGER!  == say_hello = say_louder(say_hello)
say_hello = say_louder(say_hello)
print(say_hello())
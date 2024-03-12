'''
lambda functions are small anonymous functions, they can take any number of arguments but have only one expression

They are best used as an anonymous function within another function.


'''

def multiplier(n):
    return lambda a : a * n

doubler = multiplier(2)

tripler  = multiplier(3)

print(doubler(22))

print(tripler(11))
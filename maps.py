'''
normally we implement a loop to go through data but instead we can use map() to iterate through something , this is
particularly useful when aplying a transform to each object in the iteration  and transform them into a new
iterable map

In functional programming, computations are done by combining functions that take arguments and return a concrete
value (or values) as a result. These functions don’t modify their input arguments and don’t change the program’s
state. They just provide the result of a given computation. These kinds of functions are commonly known as pure
functions.

Mapping consists of applying a transformation function to an iterable to produce a new iterable. Items in the new
iterable are produced by calling the transformation function on each item in the original iterable.

Filtering consists of applying a predicate or Boolean-valued function to an iterable to generate a new iterable.
Items in the new iterable are produced by filtering out any items in the original iterable that make the predicate
function return false.

Reducing consists of applying a reduction function to an iterable to produce a single cumulative value.

'''

# Old way
numbers = [10, 11, 2, 44, 21]

squared = []

for n in numbers:
    squared.append(n*n)

print(f"original values {numbers}, squared {squared}")

#new way
def square(value):
    return value**2

squared = map(square, numbers)

print(f"the type of the new structure is {type(squared)} and the values {list(squared)}")

# Note that the return value from the map is an iterable object and exposed by list()

#by way of further example, lets do some conversations, remembering that we would pass the iteration to a concrete function
# int is an example of that

nums_as_strings = ['1', '4', '11', '12', '4']

converted = map(int, nums_as_strings)

print(list(converted))

#because we are using functions that return something from a single expression we can use lambda here

numbers = [19,3,4,1,15,3]

squared = map(lambda num: num **2, numbers)

print(list(squared))

# it is possible to run multiple iterabels in map

first_array = [3,4,2,1,3]
second_array= [10,11,12,13,14,15]
print("looking into the additional array")

result = map(pow, first_array, second_array)
print(list(result))

#this is also useful for string manipulation
names = ['bob', 'harry', 'lucy', 'james']

make_nice = map(str.capitalize, names)

print(list(make_nice))

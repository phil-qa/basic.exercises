'''
The basic idea is to provide something similar to switch in other languages, the use of this is apredominant in late
binding, runtime allocation. A dispatch table is a list of pointers to functions
'''

# normal
thing = "this"

if thing == "blue":
    print("thing is blue")
elif thing == "green":
    print("thing is green")
elif thing == "white":
    print("thing is white")
elif thing == "this":
    print("thing is this")


# alternately
def blue_thing():
    print("the thing is blue")

def green_thing():
    print("the thing is green")

def white_thing():
    print("the thing is white")

def this_thing():
    print("the thing is this")


table = {
    "blue": blue_thing,
    "green": green_thing,
    "white": white_thing,
    "this": this_thing
}

table['this']()
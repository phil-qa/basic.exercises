def str_reverse(s):
    """
    Reverse a string
    """
    if s == "":
        return ""
    else:
        return s[-1]+str_reverse(s[:-1])


string = "this is a test"

print(str_reverse(string))
import re

file_object = open("uk-500.csv", 'r')
# print(file_object.read())
expression = r'([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})'
# read a couple of lines
for line in file_object:
    search = re.compile('.')
    #print(line)
    print(search.match(line))

file_object.close()




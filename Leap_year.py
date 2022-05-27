'''
Leap year conditions :
1. every year divisible by 4
2. except every year that is evenly divisible by 100
3. unless the year is also evenly divisible by 400
'''

response = None


while response != "enough":
    response = input("What year shall I check :")
    if response.isnumeric():
        year = int(response)

        is_div_4 = year % 4 == 0
        is_div_100 = year % 100 == 0
        is_div_400 = year % 400 == 0

        if is_div_4 and (not is_div_100 or is_div_400):
            print("Leap year")
        else:
            print("Not a leap year")

print('Bye')

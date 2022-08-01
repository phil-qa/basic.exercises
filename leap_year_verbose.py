'''
Get a year from a user
Return a message to the user if it is a leap year
where the conditions are
A leap year is evenly divisible by 4
Except every year that is evenly divisible be 100
unless the year is evenly divisible by 200
'''


# is it divisible by 4
def is_divisible_by_four(number_to_test):
    '''
    Function to check to see if a number can be divisible by 4
    :param number_to_test: integer
    :return: boolean False if it is not divisible by 4 True if it is
    '''
    return number_to_test % 4 == 0


# is it divisible by 100
def is_divisible_by_one_hundred(number_to_test):
    return number_to_test % 100 == 0


# is it divisible by 200
def is_divisible_by_two_hundred(number_to_test):
    return number_to_test % 200 == 0


def is_a_leap_year(year):
    return is_divisible_by_four(year) and (
                not is_divisible_by_one_hundred(user_input) or is_divisible_by_two_hundred(year))


user_input = None

while user_input != 'enough':
    user_input = input('What year to look at please: ')
    if user_input == 'enough':
        print("Bye we love you")
        break
    else:
        user_input = int(user_input)

    print("It is a leap year" if is_a_leap_year(user_input) else "It is not a Leap year")

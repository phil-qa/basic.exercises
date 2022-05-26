def print_out(text_to_print):
    print(text_to_print)


def divide(numbers):
    total = numbers[0]
    for number in numbers[1:]:
        total /= number
    return total


def multiply(numbers):
    total = numbers[0]
    for number in numbers[1:]:
        total *= number
    return total


def add(numbers):
    total = numbers[0]
    for number in numbers[1:]:
        total += number
    return total


def subtract(numbers):
    total = numbers[0]
    for number in numbers[1:]:
        total -= number
    return total


def get_numbers():
    numbers = []
    numbers.append(float(input("Give me a number")))
    numbers.append(float(input("Give me another number")))
    return numbers


def build_printout(numbers, result, operator):
    out_string = ""
    for number in numbers:
        out_string += f" {str(number)} {operator}"
    return out_string[:len(out_string) - 1] + f"= {result}"

operator = None
while operator !="stop":
    operator = input("which operator to use")
    if operator != "stop":
        legit_entries = ['-','+','/','*']
        if operator in legit_entries:
            numbers = get_numbers()
            if (operator == '+'):
                print(build_printout(numbers, add(numbers), '+'))
            elif (operator == '-'):
                print(build_printout(numbers, subtract(numbers), '-'))
            elif (operator == '/'):
                print(build_printout((numbers, divide(numbers), '/')))
            elif (operator == '*'):
                print(build_printout(numbers, multiply(numbers), '*'))
        else:
            print("I didnt understand the input")



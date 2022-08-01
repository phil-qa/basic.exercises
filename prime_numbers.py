def is_prime_number(value):
    if value > 1:
        for number in range(2, value):
            result = value % number
            if result == 0:
                return False
        return True

def get_next_prime(value):
    index = value
    while True:
        index += 1
        if is_prime_number(index):
            return index

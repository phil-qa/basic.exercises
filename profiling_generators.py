from memory_profiler import memory_usage, profile


@profile
def get_squares_v1(min_val, max_val):
    squares_list = []
    for num in range(min_val, max_val + 1):
        squares_list.append(num**2)
    return squares_list

@profile
def get_squares_v2(min_val, max_val):
    for num in range(min_val, max_val +1 ):
        yield num ** 2

@profile
def get_squares_v3(min_val, max_val):
    return(num ** 2 for num in range(min_val, max_val + 1))

if __name__=='__main__':
    min = 1
    max = 100000
    get_squares_v3(min,max)
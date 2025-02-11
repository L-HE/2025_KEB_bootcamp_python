#4 Make my_pow custom function instead of ** operator, power function and make it work
#from wsgiref.util import request_uri

def my_pow(b, e) -> float:
    """
    A function that receives a base and exponent and returns the power result in the form of the real number
    :param b: base number
    :param e: exponent
    :return: the power result in the form of the real number
    """
    result = 1
    for k in range(e):
        result = result * b
    return result


def is_prime(number) -> bool:
    """
    A function that determines whether a prime number is present
    and returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if number >= 2:
        i = 2
        while i <= int(my_pow(number, 0.5)) :
            if number % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

# test
#print(my_pow(2, 4))

# main
numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

#packing, unpacking
if n1 > n2:
    n1, n2 = n2, n1
if n1 < 2 :
    print("Cannot find prime number.")
else:
    number = n1
    while number <= n2:
        if is_prime(number):
           print(number, end=' ')
        number = number + 1
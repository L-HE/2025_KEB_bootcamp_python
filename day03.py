# Assignment Day 02
# v1.4) Make my_pow custom function instead of ** operator, power function and make it work.
import math


def my_pow(b, e) -> float:
    """
    A user-defined function that receives a base and exponent and returns the power result in the form of a real number
    :param b: base number
    :param e: exponent
    :return: the power result in the form of a real number
    """
    if e < 0:
        b = 1 / b
        e = e * -1

    result = 1

    i = int(e)
    f = e - i

    for _ in range(i):  # for k in range(e):
        result = result * b

    if f > 0:
        result = result * math.exp(f * math.log(b))

    return result


print(my_pow(10, -2))
print(my_pow(2, 9))
print(my_pow(16, 0.5))
print(my_pow(10, 3))
print(my_pow(25, 0.5))  # ieee 754

# print(math.exp(1))
# print(math.e)
# print(math.log(16, 2))
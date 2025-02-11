def is_prime(number) -> bool:
    """
    A function that determines whether a prime number is present
    and returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if number >= 2:
        i = 2
        while i <= int(number**0.5) :
            if number % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

# main
help(is_prime)

number = int(input ("Input number: "))

if is_prime(number):
    print(f"{number} is prime number")
else:
    print(f"{number} is NOT prime number")
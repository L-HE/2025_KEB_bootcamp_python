def is_prime(number) -> bool:
    """
    A function that determines whether a prime number is present
    and returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if number >= 2:
        for i in range(2, int(number**0.5) + 1):          #n**0.5 => n의 0.5제곱
            if number % i == 0:
                return False
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
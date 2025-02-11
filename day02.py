import math

number = int(input ("Input number: "))
is_prime = True
if number >= 2:
    for i in range(2, int(math.sqrt(number)) + 1):          #n**0.5 => n의 0.5제곱
        if number % i == 0:
            is_prime = False            #count = count + 1
            break                       #숫자가 커질수록 break의 의미가 커진다
        print(i, end=' ')
else:
    is_prime = False

if is_prime:                            #if count == 0:
    print(f"{number} is prime number")
else:
    print(f"{number} is NOT prime number")
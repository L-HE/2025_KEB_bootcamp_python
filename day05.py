# Assignment02
# v3.1) Factorial


def factorial_loop(num) -> int:
    answer = 1
    for i in range(2, num + 1):
        answer = answer * i
    return answer


def factorial_recursion(num) -> int:
    if num == 0:
        return 1
    else:
        return num * factorial_recursion(num - 1)


num = int(input('Insert a number: '))
print(f'{num}! = {factorial_loop(num)}')
print(f'{num}! = {factorial_recursion(num)}')
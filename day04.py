# Assignment
# v2.7) 2중 데코레이터 적용. time_decorator + description_decorator -> factorial 함수에 적용.

#시간을 기록할 수 있는 모듈
import  time


def description_decorator(func):
    """
    dd
    """
    def inner(*arg):
        """
        inner
        """
        print(func.__name__)
        print(func.__doc__)
        r = func(*arg)
        return r
    return inner


def time_decorator(func):
    """
    td
    """
    def wrapper(*arg):
        """
        wrapper
        """
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'duration time: {e - s}sec')
        return r
    return  wrapper


# @time_decorator
# @description_decorator
def factorial_repetition(num) -> int :
    """
    f_r
    """
    result = 1
    for i in range(2, num + 1):
        result = result * i
    return result

number = int(input())
dd = time_decorator(description_decorator(factorial_repetition))
print(f"{number}! = {dd(number)}")
# print(f"{number}! = {factorial_repetition(number)}")


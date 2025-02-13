# SOLID
# S : 단일 책임의 원칙
# Open Closed Principle : 개방 폐쇄 원칙 (확장에는 열려있고 수정에는 닫혀있는 원칙)

#시간을 기록할 수 있는 모듈
import  time


def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'duration time: {e - s}sec')
        return r
    return  wrapper


@time_decorator
def factorial_repetition(num) -> int :
    result = 1
    for i in range(2, num + 1):
        result = result * i
    return result

number = int(input())
#s = time.time()
print(f"{number}! = {factorial_repetition(number)}")
#e = time.time()
#print(e-s)
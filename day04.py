# SOLID
# S : 단일 책임의 원칙
# Open Closed Principle : 개방 폐쇄 원칙 (확장에는 열려있고 수정에는 닫혀있는 원칙)


def factorial_repetition(num) -> int :
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

number = int(input())
print(f"{number}! = {factorial_repetition(number)}")
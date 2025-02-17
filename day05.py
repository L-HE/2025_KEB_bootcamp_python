# Assignment3
# v3.2) Fibonacci Number with memoization


def fibonacci_loop(num) -> int:
    """
    반복문을 통해, 입력받은 수를 피보나치 수로 변환해주는 함수
    :param num: 입력받은 수
    :return: 입력받은 수에 해당하는 피보나치 수
    """
    flist = [0, 1]
    if num <= 1:
        return flist[num]
    else:
        for i in range(2, num + 1):
            flist.append(flist[i - 2] + flist[i - 1])
        return flist[num]


def fibonacci_recursion(num) -> int:
    """
    재귀함수와 memoization을 이용해, 입력받은 수를 피보나치 수로 변환하는 함수
    :param num: 입력받은 수
    :return: 입력받은 수에 해당하는 피보나치 수
    """
    memo = {}

    if num in memo:
        return memo[num]
    elif num <= 1:
        return num
    else:
        memo = {num : fibonacci_recursion(num - 2) + fibonacci_recursion(num - 1)}
        return memo[num]


num = int(input("Insert a number: "))
print(fibonacci_loop(num))
print(fibonacci_recursion(num))
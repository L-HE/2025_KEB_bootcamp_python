# Assignment01
# v3.0) Countdown

def countdown_loop(num):
    for i in range(num + 1):
        if (num - i) != 0:
            print(num - i)
        else:
            print("Boom")

def countdown_recursion(num):
    if num == 0:
        print("Boom")
    else:
        print(num)
        return countdown_recursion(num - 1)


num = int(input('Press a number that you want to countdown: '))
countdown_loop(num)
countdown_recursion(num)

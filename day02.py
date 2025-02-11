#for dan in range(2, 10, 1): #함수는 아니고 제네레이터임 / 2부터 9까지, 1씩 증가하며 반복 / 중괄호를 안씀 들여쓰기로 구분
#    for i in range(1, 10, 1):          #증가값은 기본 1 / 시작값은 기본 0
#        print(f"{dan} * {i} = {dan*i}") #f"string" 최신 문법

dan = int(input("Input dan : "))
for i in range(1, 10):
    print(f"{dan} * {i} = {dan*i}")
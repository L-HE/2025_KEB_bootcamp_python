#Assignment
#   v1.8) 다음 코드에서 dictionary를 제거하고 list만 사용하여 동일하게 동작하도록 코드를 수정하시오.
import random


def print_menu(num):
    """
    Functions that output menus in order according to the numbers entered
    :param num:
    :return:
    """
    print(f'{drinks[num-1]}에 어울리는 안주는 {foods[num-1]} 입니다\n')


drinks = ['위스키', '와인', '소주', '고량주']
foods = ['초콜릿', '치즈', '삼겹살', '양꼬치']

drinks.append('사케')
foods.append('광어회')
foods[0] = '낙곱새'

while True:
    menu = int(input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : '))
    if 1 <= menu <= len(drinks) :
        print_menu(menu)
    elif menu == len(drinks) + 1:
        ran_menu = random.randint(0, len(drinks) - 1)
        print(f'{drinks[ran_menu]}에 어울리는 안주는 {foods[ran_menu]} 입니다\n')
    elif menu == len(drinks) + 2:
        print(f'다음에 또 오세요')
        break
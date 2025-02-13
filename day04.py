#Assignment
#   v2.0) hint. 가격을 추가, 영수증을 출력
import random

# d_s_p = {"위스키":['초콜릿', 50_000]}
# print(d_s_p["위스키"][1])                #해봐


def print_menu(num):
    """
    Functions that output menus in order according to the numbers entered
    :param num: number of drink
    :return: string of sentence selecting drinks and foods
    """
    print(f'{drinks[num-1]}에 어울리는 안주는 {foods[num-1]} 입니다\n')


drinks = ['위스키', '와인', '소주', '고량주']
foods = ['초콜릿', '치즈', '삼겹살', '양꼬치']
prices = [50_000, 30_000, 5_000, 7_500]

drinks.append('사케')
drinks.append('데킬라')
foods.append('광어회')
foods.append('소금')
foods[0] = '낙곱새'
prices.append(25_000)
prices.append(37_000)

menu_list = '다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]} '
menu_list = menu_list + f'{len(drinks) + 1}) 아무거나 {len(drinks) + 2}) 종료 :    '

while True:
    menu = int(input(menu_list))
    if 1 <= menu <= len(drinks) :
        print_menu(menu)
    elif menu == len(drinks) + 1:
        ran_menu = random.randint(0, len(drinks) - 1)
        print(f'{drinks[ran_menu]}에 어울리는 안주는 {foods[ran_menu]} 입니다\n')
    elif menu == len(drinks) + 2:
        print(f'다음에 또 오세요')
        break
    else:
        print(f'잘못 입력하셨습니다. 다시 입력해주세요.\n')
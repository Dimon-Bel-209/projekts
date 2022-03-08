import math
from colorama import init
init()
from colorama import Fore, Back, Style
# основная часть кода
# ввод примера для вычислительных действаий
print(Fore.CYAN)
example = input('Действие: ')
x = list(example)

def se(a):
    print(Fore.CYAN)
    example = input('Действие: ')
    x = list(example)
    if example == 'pi':
        print(Fore.GREEN)
        print(math.pi)
    elif example != 'pi':
        print(Fore.GREEN)
        print(eval(example))
# определение действия для подщёта
while len(x) > 0:
    se(example)
else:
    print()   

input() 
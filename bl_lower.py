#bl_lower - функции вспомогательные для GUI и upper
import GUI
#Проверка ввода пустой строки
def checking_empty_str(name):
    while name == '':
        name = input('Вы ничего не ввели, попробуйте снова > ')
    return name

def print_list(lst,action):
    print(f'Список {action}: ')
    for elem in lst:
        print(elem)
    print()
#bl_lower - функции вспомогательные для GUI и upper
import GUI
#Проверка ввода пустой строки
def checking_empty_str(name):
    while name == '':
        name = input('Вы ничего не ввели, попробуйте снова > ')
    return name

#Проверка ввода первичных данных
def checking_input(name,lst):
    while name not in lst:
        if name == 'quit':
            quit()
        elif name == '':
            name = input('Вы ничего не ввели, попробуйте снова > ')
        else:
            name = input('Вы ввели неверный запрос, попробуйте снова > ')
    return name
def print_list(lst,action):
    print(f'Список {action}: ')
    for elem in lst:
        print(elem)
    print()
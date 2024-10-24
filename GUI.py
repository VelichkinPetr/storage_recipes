#GUI - Ввод данных и Вывод сообщений на экран
import os.path
from datetime import datetime
import bl_lower
import bl_upper

#имена всех вариантов данных с которыми может работать пользователь
list_name_action = ['catalog','recipe']
#список имен всех возможных функций
list_name_function = ['create','list','search','ingred','delete','sort','read','append','help','catalog','recipe']
#список значений для сортировки
list_sort = ['1','2']

#Общая информация для пользователя
def info():
    print(bl_lower.blue(f'Добро пожаловать!\n'
                        f'Это консольное приложение для хранения и работы с кулинарными рецептами.\n'
                        f'Для завершения работы приложения, введите \'{bl_lower.yellow('quit')}\'\n'))

#Подсказка для пользователя о функция доступных с конкретными данными
def get_help(action:str):
    if action == 'catalog':
        print(bl_lower.blue('\nДоступные функции для работы с Каталогом:\n'
              f'{bl_lower.yellow('recipe')} - перейти к работе с рецептами\n'
              f'{bl_lower.yellow('create')} - создать каталог\n'
              f'{bl_lower.yellow('list')} - получить список всех каталогов\n'
              f'{bl_lower.yellow('search')} - найти каталог по его названию\n'
              f'{bl_lower.yellow('delete')} - удалить каталог\n'
              f'{bl_lower.yellow('help')} - вызов справки\n'
              f'{bl_lower.yellow('quit')} - завершение работы приложения'))
    elif action == 'recipe':
        print(bl_lower.blue('\nДоступные функции для работы с Рецептами:\n'
              f'{bl_lower.yellow('catalog')} - перейти к работе с каталогами\n'
              f'{bl_lower.yellow('append')} - добавление рецепта\n'
              f'{bl_lower.yellow('search')} - найти рецепт по его наименованию\n'
              f'{bl_lower.yellow('ingred')} - найти рецепт по его ингредиентам\n'
              f'{bl_lower.yellow('read')} - вывод всех рецептов в каталоге\n'
              f'{bl_lower.yellow('sort')} - вывод всех рецептов в каталоге\n'
              f'{bl_lower.yellow('delete')} - удалить рецепт\n'
              f'{bl_lower.yellow('help')} - вызов справки\n'
              f'{bl_lower.yellow('quit')} - завершение работы приложения'))

#Создание директории для хранения каталогов
def path_dir_catalog() -> str:
    path_catalog = input('Введи директорию, где будут храниться каталоги > ')
    while not os.path.isdir(path_catalog):
        if path_catalog == 'quit':
            bl_upper.quit_program()
        elif path_catalog == '':
            path_catalog = checking_empty_str(path_catalog)
        else:
            path_catalog = input(bl_lower.red('Такой директории не существует, попробуйте снова > '))
    dir_name = r'\storage_recipe'
    path_dir = path_catalog+dir_name
    return path_dir


#Ввод и проверка имени объекта взаимодействия
def action_name() -> str:
    action = input(f'\nС чем хотите работать({bl_lower.yellow('catalog, recipe')}) > ')
    action = checking_input(action,list_name_action)
    return action

#Ввод и проверка имени функции
def function_name(action:str)-> str:
    function = input(f'\nВыберите действие с {bl_lower.yellow(action)} > ')
    function = checking_input(function,list_name_function)
    return function

#Проверка ввода на пустую строку
def checking_empty_str(name:str) -> str:
    if name == 'quit':
        bl_upper.quit_program()
    while name == '':
        name = input(bl_lower.red('Вы ничего не ввели, попробуйте снова > '))
        if name == 'quit':
            bl_upper.quit_program()
    return name

#Проверка ввода начальных данных или выход из программы
def checking_input(name:str,lst:list[str]) -> str:
    while name not in lst:
        if name == 'quit':
            bl_upper.quit_program()
        elif name == '':
            name = input(bl_lower.red('Вы ничего не ввели, попробуйте снова > '))
        else:
            name = input(bl_lower.red('Вы ввели неверный запрос, попробуйте снова > '))
    return name

#Печать списка
def print_list(lst:list[str]):
    print()
    for elem in lst:
        print(elem)

#Проверка ввода имени каталога и пути его создания:
def name_new_catalog() -> str:
    name_catalog = input('\nВведи имя каталога > ')
    name_catalog = checking_empty_str(name_catalog)
    return name_catalog

#Ввод и проверка нового рецепта
def new_recipe()-> list[str]:
    string = []
    name = input('\nНазвание рецепта > ')
    name = checking_empty_str(name)
    string.append('Название:'+name)

    composition = input('Состав > ')
    composition = checking_empty_str(composition)
    string.append('Состав:'+composition)

    description = input('Описание > ')
    description = checking_empty_str(description)
    string.append('Описание:'+description)

    time = input('Время приготовления[мин] > ')
    time = checking_empty_str(time)
    string.append('Время приготовления[мин]:'+time)
    string.append(f'Время создания:{datetime.now()}')
    return string

#Ввод и проверка имени рецепта для поиска
def name_recipe() -> str:
    recipe_name=input(f'\nВведи имя рецепта > ')
    recipe_name=checking_empty_str(recipe_name)
    return recipe_name

#Ввод и проверка
def get_index_sort() -> int:
    print(f'Для сортировки по Времени приготовления,    введите {bl_lower.yellow('1')}\n'
          f'               по Времени создания рецепта, введите {bl_lower.yellow('2')}')
    name_sort=input(f'\nСортировка по > ')
    name_sort = checking_input(name_sort,list_sort)
    if name_sort == '1':
        name_sort = 3
    elif name_sort == '2':
        name_sort = 4
    return name_sort

#Выбор направления сортировки
def get_sort_up_or_down() -> bool:
    print(f'Для сортировки по Возрастанию, введите {bl_lower.yellow('1')} \n'
          f'               по Убыванию,    введите {bl_lower.yellow('2')} ')
    name_sort = input(f'\nСортировка по > ')
    name_sort = checking_input(name_sort, list_sort)
    if name_sort == '1':
        name_sort = False
    elif name_sort == '2':
        name_sort = True
    return name_sort

#Вывод сортированного списка
def print_sort_list(list_name:list[str],list_column:list[str],list_sort:list[str]):
    for i in range(len(list_sort)):
        if list_sort[i] in list_column:
            index = list_column.index(list_sort[i])
            print(list_name[index], '\t', list_sort[i])

#Ввод ингредиентов для поиска рецепта
def name_search_ingredient() -> str:
    ingredient_name = input(f'\nВведи ингредиент для поиска > ')
    ingredient_name = checking_empty_str(ingredient_name)
    return ingredient_name

def show_succesful_message(text:str):
    print(bl_lower.green(text))

def show_error_message(text: str):
    print(bl_lower.red(text))

#Ввод начальных данных
def input_(path:str) -> str:
    name = name_new_catalog()
    format_file = '.txt'
    path_catalog = path + '\\' + name + format_file
    return path_catalog
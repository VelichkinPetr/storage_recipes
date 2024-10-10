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
                        f'Для вызова справки, введите \'{bl_lower.yellow('help')}\'\n'
                        f'Для возврата к выбору, введите \'{bl_lower.yellow('back')}\'\n'
                        f'Для выхода из приложения, введите \'{bl_lower.yellow('quit')}\'\n'))

#Подсказка для пользователя о функция доступных с конкретными данными
def get_help(action):
    if action == 'catalog':
        print(bl_lower.blue('\nДоступные функции для работы с Каталогом:\n'
              f'{bl_lower.yellow('create')} - создать каталог\n'
              f'{bl_lower.yellow('list')} - получить список всех каталогов\n'
              f'{bl_lower.yellow('search')} - найти каталог по его названию\n'
              f'{bl_lower.yellow('delete')} - удалить каталог.'))
    elif action == 'recipe':
        print(bl_lower.blue('\nДоступные функции для работы с Рецептами:\n'
              f'{bl_lower.yellow('append')} - добавление рецепта\n'
              f'{bl_lower.yellow('search')} - найти рецепт по его наименованию\n'
              f'{bl_lower.yellow('read')} - вывод всех рецептов в каталоге\n'
              f'{bl_lower.yellow('delete')} - удалить рецепт.'))

#Создание диретории для хранения каталогов
def path_dir_catalog():
    path_catalog = input('Введи директорию, где будут храниться каталоги > ')
    if path_catalog == 'quit':
        bl_upper.quit_program()
    path_catalog = checking_empty_str(path_catalog)
    while not os.path.isdir(path_catalog):
        path_catalog = input(bl_lower.red('Такой директории не существет, попробуйте снова > '))
    dir_name = r'\storage_recipe'
    path_dir = path_catalog+dir_name
    return path_dir

#Проверка ввода имени объекта взаимодействия
def action_name():
    action = input(f'\nС чем хотите работать({bl_lower.yellow('catalog, recipe')}) > ')
    action = checking_input(action,list_name_action)
    return action

#Проверка ввода имени функции
def function_name(action):
    function = input(f'\nВыберите действие с {bl_lower.yellow(action)} > ')
    function = checking_input(function,list_name_function)
    return function

def checking_empty_str(name):
    while name == '':
        name = input(bl_lower.red('Вы ничего не ввели, попробуйте снова > '))
    return name

def checking_input(name,lst):
    while name not in lst:
        if name == 'quit':
            bl_upper.quit_program()
        elif name == '':
            name = input(bl_lower.red('Вы ничего не ввели, попробуйте снова > '))
        else:
            name = input(bl_lower.red('Вы ввели неверный запрос, попробуйте снова > '))
    return name

#Печать списка
def print_list(lst):
    print()
    for elem in lst:
        print(elem)

#Проверка ввода имени каталога и пути его создания:
def name_new_catalog():
    name_catalog = input('\nВведи имя каталога > ')
    name_catalog = checking_empty_str(name_catalog)
    return name_catalog

def new_recipe():
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

    time = input('Время приготовления > ')
    time = checking_empty_str(time)
    string.append('Время приготовления:'+time)
    string.append('Время создания:'+str(datetime.now()))
    return string

def name_recipe():
    recipe_name=input(f'\nВведи имя рецепта > ')
    recipe_name = checking_empty_str(recipe_name)
    return recipe_name



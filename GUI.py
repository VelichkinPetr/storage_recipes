#GUI - Ввод данных и Вывод сообщений на экран
from datetime import datetime



#имена всех вариантов данных с которыми может работать пользователь
list_name_action = ['catalog','recipe']
#список имен всех возможных функций
list_name_function = ['create','list','search','delete','read','append','help','back']

#Общая информация для пользователя
def info():
    return print('Добро пожаловать!\n'
      'Это консольное приложение для хранения и работы с кулинарными рецептами.\n'
      'Для вызова справки, введите \'help\'\n'
      'Для возврата к выбору, введите \'back\'\n'
      'Для выхода из приложения, введите \'quit\'\n')

#Подсказка для пользователя о функция доступных с конкретными данными
def get_help(action):
    if action == 'catalog':
        print('\nДоступные функции для работы с Каталогом:\n'
              'create - создать каталог\n'
              'list - получить список всех каталогов\n'
              'search - найти каталог по его названию\n'
              'delete - удалить каталог.')
    elif action == 'recipe':
        print('\nДоступные функции для работы с Рецептами:\n'
              'append - добавление рецепта\n'
              'search - найти рецепт по его наименованию\n'
              'read - вывод всех рецептов в каталоге\n'
              'delete - удалить рецепт.')

#Создания папки, в которой будут храниться каталоги
def path_dir_catalog():
    path_catalog = input('Введи директорию, где будут храниться каталоги > ')
    path_catalog = checking_empty_str(path_catalog)
    dir_name = r'\storage_recipe'
    path_dir = path_catalog+dir_name
    return path_dir

#Проверка ввода имени объекта взаимодействия
def action_name():
    action = input('\nС чем хотите работать(catalog, recipe) > ')
    action = checking_input(action,list_name_action)
    return action

#Проверка ввода имени функции
def function_name(action):
    function = input(f'\nВыберите действие с {action} > ')
    function = checking_input(function,list_name_function)
    return function

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

#Печать списка
def print_list(lst,action):
    print()
    if lst != '':
        print(f'Список {action}: ')
        for elem in lst:
            print(elem)
    else:
        print('Пуст')

#Проверка ввода имени каталога и пути его создания:
def name_new_catalog():
    name_catalog = input('\nВведи имя каталога > ')
    name_catalog = checking_empty_str(name_catalog)
    return name_catalog

#Запрос нового рецепта
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

#Запрос названия рецепта, для поиска
def name_recipe():
    recipe_name=input(f'\nВведи имя рецепта > ')
    recipe_name = checking_empty_str(recipe_name)
    return recipe_name



#GUI - Ввод данных и Вывод сообщений на экран

#Общая информация для пользователя
def info():
    return print('Добро пожаловать!\n'
      'Это консольное приложение для хранения и работы с кулинарными рецептами.\n'
      'Для вызова справки, введите \'help\'\n'
      'Для выхода из приложения, введите \'quit\'\n')

#Подсказка для пользователя о функция доступных с конкретными данными
def my_help(action):
    if action == 'catalog':
        print('Доступные функции для работы с Каталогом:\n'
              'create_catalog - создать каталог\n'
              'catalog_list - получить список всех каталогов\n'
              'search_catalog - найти каталог по его названию\n'
              'delete_catalog - удатиль каталог\n'
              'recipes_in_catalog - чтение каталога - вывод всех рецептов в нем.\n')
    elif action == 'recipe':
        print('Доступные функции для работы с Рецептами:\n'
              'append_recipe - добавление рецепта\n'
              'search_recipe - найти рецепт по его наименованию\n'
              'delete_recipe - удатиль рецепт.\n')
def path_dir_catalog():
    path_catalog = input('Введи директорию, где будут храниться каталоги > ')
    while path_catalog == '':
        path_catalog = input('Вы ничего не ввели, попробуйте снова path > ')
    dir_name = r'\storage_recipe'
    path_dir=path_catalog+dir_name
    return path_dir

#Импорт списков констант
from bl_lower import list_name_function, list_name_action, list_format
#Проверка ввода имени объекта взаимодействия
def action_name():
    action = input('С чем хотите работать(catalog, recipe) > ')
    while action not in list_name_action:
        if action == 'quit':
            quit()
        elif action == '':
            action = input('Вы ничего не ввели, попробуйте снова a > ')
        else:
            action = input('Вы ввели неверный запрос, попробуйте снова a > ')
    return action

#Проверка ввода имени функции
def function_name(action):
    function = input(f'Выберите действие с {action} > ')
    while function not in list_name_function:
        if function == 'quit':
            quit()
        elif function == '':
            function = input('Вы ничего не ввели, попробуйте снова f > ')
        else:
            function = input('Вы ввели неверный запрос, попробуйте снова f > ')
    return function

#Проверка ввода формата каталога
def format_catalog():
    format_catalog = input('Введи расширение каталога > ')
    while format_catalog not in list_format:
        if format_catalog == '':
            format_catalog = input('Вы ничего не ввели, попробуйте снова format > ')
        else:
            format_catalog = input('Вы ввели неверный запрос, попробуйте снова format > ')
    return format_catalog
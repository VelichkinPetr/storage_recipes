#GUI - Ввод данных и Вывод сообщений на экран

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

#Проверка ввода имени каталога и пути его создания:
def name_new_catalog():
    name_catalog=input('Введи имя каталога > ')
    while name_catalog=='':
        name_catalog = input('Вы ничего не ввели, попробуйте снова catalog > ')
    return name_catalog

def path_dir_catalog():
    path_catalog = input('Введи директорию, где будут храниться каталоги > ')
    while path_catalog == '':
        path_catalog = input('Вы ничего не ввели, попробуйте снова path > ')
    dir_name = r'\storage_recipe'
    path_dir=path_catalog+dir_name
    return path_dir

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


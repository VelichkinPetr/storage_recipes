#GUI - Ввод данных и Вывод сообщений на экран

#Общая информация для пользователя
def info():
    return print('Добро пожаловать!\n'
      'Это консольное приложение для хранения и работы с кулинарными рецептами.\n'
      'Для вызова справки, введите \'help\'\n'
      'Для выхода из приложения, введите \'quit\'\n')

def path_dir_catalog():
    path_catalog = input('Введи директорию, где будут храниться каталоги > ')
    while path_catalog == '':
        path_catalog = input('Вы ничего не ввели, попробуйте снова path > ')
    dir_name = r'\storage_recipe'
    path_dir=path_catalog+dir_name
    return path_dir

#Импорт списков констант
from bl_lower import list_name_function, list_name_action
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
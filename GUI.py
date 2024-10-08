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
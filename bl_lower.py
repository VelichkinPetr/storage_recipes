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

#Ввод данных для получения пути к каталогу
def input_(path):
    name = GUI.name_new_catalog()
    format_file = '.txt'
    path_catalog = path + '\\' + name + format_file
    return name,format_file,path_catalog
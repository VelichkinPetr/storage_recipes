#bl_lower - функции вспомогательные для GUI и upper
import GUI
import os
import datetime

#Ввод начальных данных
def input_(path):
    name = GUI.name_new_catalog()
    format_file = '.txt'
    path_catalog = path + '\\' + name + format_file
    return name,format_file,path_catalog
#Проверка существования файла
def checking_file(name,format_file,path_catalog):
    if not os.path.isfile(path_catalog):
        print(red(f'Файл {name + format_file} не найден'))

#Проверка существования файла и его содержимого
def check_error_isfile(path):
    name, format_file, path_catalog = input_(path)
    if os.path.isfile(path_catalog):
        file = open(path_catalog, 'r+')
        file.seek(0)
        if len(file.read()) != 0:
            file.close()
            return path_catalog
        else:
            print(red(f'Файл {name + format_file} пуст'))
    else:
        print(red(f'Файл {name + format_file} не найден'))

#Генерация списка количества рецептов в файле и даты его создания
def get_len_and_date_file(path,lst):
    list_len_and_date = []
    if len(lst) != 0:
        for catalog in lst:
            file = open(path + r'\\' + catalog, 'r')
            len_catalog = 0
            for line in file:
                if 'Название' in line:
                    len_catalog += 1
            date_catalog = datetime.datetime.fromtimestamp(os.path.getctime(path + r'\\' + catalog))
            list_len_and_date.append(f'\tРецептов:{len_catalog},\tДата создания:{date_catalog}')
    return list_len_and_date

#Получение списка столбцов из каталога
def get_list_column(lst,index_column):
    lst_matrix = []
    for line in lst:
        row = line.split(';')
        lst_matrix.append(row)

    list_column = []
    for i in range(len(lst_matrix)):
        index_start = lst_matrix[i][index_column].index(':') + 1
        name_recipe = lst_matrix[i][index_column][index_start:]
        list_column.append(name_recipe)
    return list_column

#Цветовая окраска выводимых сообщений
def blue(text):
    return f'\033[34m{text}'

def red(text):
    return f'\033[31m{text}\033[34m'

def yellow(text):
    return f'\033[33m{text}\033[34m'

def green(text):
    return f'\033[32m{text}\033[34m'

#Преобразование искомого(ых) ингредиента(ов) в список
def get_list_search_ingredient(search_ingredient):
    if len(search_ingredient)>1:
        list_search_ingredient = search_ingredient.replace(' ','').split(',')
    else:
        list_search_ingredient=search_ingredient
    return list_search_ingredient

#Преобразование Списка составов в Матрицу ингредиентов
def get_matrix_ingredient(lst_composition):
    matrix_ingredient=[]
    for i,line in enumerate(lst_composition):
        if len(line)>1:
            row = lst_composition[i].split(',')
            for i in range(len(row)):
                row[i]=row[i].strip()
        else:
            row=lst_composition[i]
        matrix_ingredient.append(row)
    return matrix_ingredient
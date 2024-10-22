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
        return False
    else:
        return True
def checking_file_is_empty(path_catalog):
    if os.stat(path_catalog).st_size == 0:
        print(red(f'Файл пуст'))
        return True
    else:
        return False

#Получене пути к каталогу
def take_path_catalog(path):
    name, format_file, path_catalog = input_(path)
    if checking_file(name,format_file,path_catalog):
        if not checking_file_is_empty(path_catalog):
            return path_catalog

#Преобразование файла в список строк
def get_list_str_from_file(path_catalog):
    file = open(path_catalog, 'r+')
    file.seek(0)
    lst = []
    for string in file:
        lst.append(string[:-1])
    file.close()
    return lst

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

#Проверка ингридиентов в каталоге
def ingredient_in_catalog(lst,ingredient):
    if lst != []:
        GUI.print_list(lst)
    else:
        print(red(f'Ингредиентов \'{ingredient}\' нет в каталоге'))

#Проверка рецепта в каталоге
def recipe_in_catalog(recipe_search,lst_name):
    if recipe_search in lst_name:
        return True
    else:
        print(red(f'Рецепта {recipe_search} нет в каталоге'))
        return False
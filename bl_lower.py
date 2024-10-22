#bl_lower - функции вспомогательные для GUI и upper
import GUI
import os
import datetime

#Проверка существования файла
def checking_file(path_catalog :str) -> bool:
    if os.path.isfile(path_catalog):
        return True
    return False

#Проверка что файл пуст
def checking_file_is_empty(path_catalog:str) -> bool:
    if os.stat(path_catalog).st_size == 0:
        return True
    return False

#Преобразование файла в список строк
def get_file_contents(path_catalog:str) -> list[str]:
    file = open(path_catalog, 'r+')
    file.seek(0)
    lines = []
    for string in file:
        lines.append(string[:-1])
    file.close()
    return lines

#Генерация списка количества рецептов в файле и даты его создания
def get_len_and_date_file(path:str,list_dir:list[str]) -> list[str]:
    list_len_and_date = []
    if len(list_dir) != 0:
        for catalog in list_dir:
            file = open(path + r'\\' + catalog, 'r')
            len_catalog = 0
            for line in file:
                if 'Название' in line:
                    len_catalog += 1
            date_catalog = datetime.datetime.fromtimestamp(os.path.getctime(path + r'\\' + catalog))
            list_len_and_date.append(f'\tРецептов:{len_catalog},\tДата создания:{date_catalog}')
    return list_len_and_date

#Получение списка столбцов из каталога
def get_list_column(list_lines_file: str,index_column:int) -> list[str]:
    lst_matrix = []
    for line in list_lines_file:
        row = line.split(';')
        lst_matrix.append(row)

    list_column = []
    for i in range(len(lst_matrix)):
        index_start = lst_matrix[i][index_column].index(':') + 1
        name_recipe = lst_matrix[i][index_column][index_start:]
        list_column.append(name_recipe)
    return list_column

#Цветовая окраска выводимых сообщений
def blue(text:str) -> str:
    return f'\033[34m{text}'

def red(text:str) -> str:
    return f'\033[31m{text}\033[34m'

def yellow(text:str) -> str:
    return f'\033[33m{text}\033[34m'

def green(text:str) -> str:
    return f'\033[32m{text}\033[34m'

#Преобразование искомого(ых) ингредиента(ов) в список
def get_list_search_ingredient(search_ingredient:str) -> list[str]:
    if len(search_ingredient)>1:
        list_search_ingredient = search_ingredient.replace(' ','').split(',')
    else:
        list_search_ingredient=search_ingredient
    return list_search_ingredient

#Преобразование Списка составов в Матрицу ингредиентов
def get_matrix_ingredient(lst_composition:list[str]) -> list[list[str]]:
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
def recipe_in_catalog(recipe_search:str,lst_name:list[str]) -> bool:
    if recipe_search in lst_name:
        return True
    return False

#Запись рецепта в каталог
def write_recipe(path_catalog:str,app_recipe:str):
    with open(path_catalog, 'a+') as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write('\n' + app_recipe)
            file_object.close()
        else:
            file_object.write(app_recipe)
            file_object.close()

#Получение искомого рецепта
def get_recipe(recipe_search,list_names,list_lines_file):
    for i, name_recipe in enumerate(list_names):
        if recipe_search == name_recipe:
            index_search_name = i
            found_recipe = ';\n'.join(list_lines_file[index_search_name].split(';'))
            return found_recipe

#Удаление рецепта
def del_recipe(recipe_search,list_names,list_lines_file,path_catalog):
    for i, string in enumerate(list_names):
        if recipe_search == string:
            index_search_name = i
            del list_lines_file[index_search_name]
            file = open(path_catalog, 'w')
            file.writelines('\n'.join(list_lines_file))
            file.close()
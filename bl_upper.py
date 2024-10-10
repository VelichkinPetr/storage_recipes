#bl_upper - функции самого приложения
import os
import GUI
import bl_lower

#Создание директории для каталогов
def create_catalog_dir(path):
    if not os.path.isdir(path):
        return os.mkdir(path+'\\')

#Функции работы с каталогами
def create_catalog(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if os.path.isfile(path_catalog):
        print('Такой файл уже существует')
    else:
        new_catalog = open(path_catalog,'w')
        print('Файл успешно создан!')

def get_catalog_list(path,action):
    list_catalog = os.listdir(path)
    GUI.print_list(list_catalog,action)
    return list_catalog
#search_catalog
#delete_catalog
#recipes_in_catalog

#Функции работы с рецептами
#append_recipe
#search_recipe
#delete_recipe



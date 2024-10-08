#bl_upper - функции самого приложения
import os
import core



#Функции работы с каталогами
def create_catalog(action):
    import GUI
    path_dir=core.path
    name = GUI.name_new_catalog()
    format_file = GUI.format_catalog()

    if not os.path.isdir(path_dir):
        os.mkdir(path_dir+'\\')
    path_new_dir=path_dir+'\\'

    path_catalog=path_new_dir+name+format_file
    if os.path.isfile(path_catalog):
        print('Такой файл уже существует')
    else:
        new_catalog=open(path_catalog,'w')
        print('Файл успешно создан!')
    return path_catalog

#search_catalog
#delete_catalog
#recipes_in_catalog

#Функции работы с рецептами
#append_recipe
#search_recipe
#delete_recipe



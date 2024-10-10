#bl_lower - функции вспомогательные для GUI и upper
import GUI
import os
#Ввод данных для получения пути к каталогу
def input_(path):
    name = GUI.name_new_catalog()
    format_file = '.txt'
    path_catalog = path + '\\' + name + format_file
    return name,format_file,path_catalog

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
            print(f'Файл {name + format_file} пуст')
    else:
        print(f'Файл {name + format_file} не найден')
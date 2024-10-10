#bl_upper - функции самого приложения
import os
import GUI
import bl_lower

#Создание директории для каталогов
def create_catalog_dir(path):
    if not os.path.isdir(path):
        return os.mkdir(path+'\\')

def quit_program():
    print('Пока!')
    quit()
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

def search_catalog(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if os.path.isfile(path_catalog):
        print(f'Файл {name+format_file} найден')
    else:
        print(f'Файл {name+format_file} не найден')

def delete_catalog(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if os.path.isfile(path_catalog):
        os.remove(path)
        print(f'Файл успешно удален!')
    else:
        print(f'Файл {name + format_file} не найден')

#Функции работы с рецептами
def append_recipe(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if os.path.isfile(path_catalog):
        app_recipe = ';'.join(GUI.new_recipe())
        with open(path_catalog,'a+') as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data)>0:
                file_object.write('\n' + app_recipe)
                file_object.close()
            else:
                file_object.write(app_recipe)
                file_object.close()
            print(f'Рецепт успешно записан!')
    else:
        print(f'Файл {name + format_file} не найден')

def get_names_recipes(check_error):
    if isinstance(check_error,str):
        path_catalog = check_error
        file = open(path_catalog, 'r+')
        file.seek(0)
        lst = []
        lst_name = []
        for string in file:
            lst.append(string[:-1])
        file.seek(0)
        for i in range(len(lst)):
            index_name = lst[i].index(';')
            name_recipe = lst[i][9:index_name]
            lst_name.append(name_recipe)
        GUI.print_list(lst_name)
        return lst_name,lst,path_catalog


def search_recipe(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if os.path.isfile(path_catalog):
        file = open(path_catalog, 'r+')
        file.seek(0)
        lst = []
        lst_name = []
        for string in file:
            lst.append(string[:-1])
        if len(lst[0]) > 0:
            for i in range(len(lst)):
                index_name = lst[i].index(';')
                name_recipe = lst[i][9:index_name]
                lst_name.append(name_recipe)
            recipe_search = GUI.name_recipe()
            if recipe_search in lst_name:
                for i, string in enumerate(lst_name):
                    if recipe_search == string:
                        index_search_name = i
                        new_lst_search = ';\n'.join(lst[index_search_name].split(';'))
                        print(new_lst_search)
            else:
                print(f'Рецепта {recipe_search} нет в каталоге {name}')
        else:
            print(f'Файл {name + format_file} пуст')
    else:
        print(f'Файл {name + format_file} не найден')
#search_recipe
#delete_recipe



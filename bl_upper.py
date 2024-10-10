#bl_upper - функции самого приложения
import os
import GUI
import bl_lower

#Создание директории для каталогов
def create_catalog_dir(path):
    if not os.path.isdir(path):
        return os.mkdir(path+'\\')

def quit_program():
    print(bl_lower.green('Пока!'))
    quit()
#Функции работы с каталогами
def create_catalog(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if os.path.isfile(path_catalog):
        print(bl_lower.yellow('Такой файл уже существует'))
    else:
        new_catalog = open(path_catalog,'w')
        print(bl_lower.green('Файл успешно создан!'))

def get_catalog_list(path):
    list_dir = os.listdir(path)
    list_len_and_date = bl_lower.get_len_and_date_file(path,list_dir)
    if len(list_len_and_date)!=0:
        list_catalog = []
        for i in range(len(list_dir)):
            list_catalog.append(list_dir[i] + list_len_and_date[i])
        GUI.print_list(list_catalog)
    else:
        print(bl_lower.red(f'Каталогов нет!'))

def search_catalog(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if os.path.isfile(path_catalog):
        print(bl_lower.green(f'Файл {name+format_file} найден'))
    else:
        print(bl_lower.red(f'Файл {name+format_file} не найден'))

def delete_catalog(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if os.path.isfile(path_catalog):
        os.remove(path)
        print(bl_lower.green(f'Файл успешно удален!'))
    else:
        print(bl_lower.red(f'Файл {name + format_file} не найден'))

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
            print(bl_lower.green(f'Рецепт успешно записан!'))
    else:
        print(bl_lower.red(f'Файл {name + format_file} не найден'))

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

def search_recipe(names_recipes):
    if names_recipes != None:
        lst_name,lst,path_catalog = names_recipes
        recipe_search = GUI.name_recipe()
        if recipe_search in lst_name:
            for i, string in enumerate(lst_name):
                if recipe_search == string:
                    index_search_name = i
                    new_lst_search = ';\n'.join(lst[index_search_name].split(';'))
                    print(new_lst_search)
                    return new_lst_search,lst
        else:
            print(bl_lower.red(f'Рецепта {recipe_search} нет в каталоге'))

def delete_recipe(names_recipes):
    if names_recipes != None:
            lst_name,lst,path_catalog = names_recipes
            recipe_search = GUI.name_recipe()
            if recipe_search in lst_name:
                for i, string in enumerate(lst_name):
                    if recipe_search == string:
                        index_search_name = i
                        del lst[index_search_name]
                        file=open(path_catalog,'w')
                        file.writelines('\n'.join(lst))
                        print(bl_lower.green(f'Рецепт успешно удален!'))
            else:
                print(bl_lower.red(f'Рецепта {recipe_search} нет в каталоге'))



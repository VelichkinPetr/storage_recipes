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

def get_names_recipes(lst_file):
    if isinstance(lst_file,list):
        lst = lst_file
        lst_name=[]
        for i in range(len(lst)):
            index_name = lst[i].index(';')
            name_recipe = lst[i][9:index_name]
            lst_name.append(name_recipe)
        return lst_name,lst
    elif isinstance(lst_file,str):
        return lst_file,''

def search_recipe(names_recipes):
    if isinstance(names_recipes[0], list):
        lst=names_recipes[1]
        lst_name = names_recipes[0]
        recipe_search = GUI.name_recipe()
        if recipe_search in lst_name:
            for i, string in enumerate(lst_name):
                if recipe_search == string:
                    index_search_name = i
                    new_lst_search = ';\n'.join(lst[index_search_name].split(';'))
                    return new_lst_search
        else:
            new_lst_search = f'Рецепта {recipe_search} нет в каталоге'
            return new_lst_search,'',''
    elif isinstance(names_recipes[0],str):
        return names_recipes
#search_recipe
#delete_recipe



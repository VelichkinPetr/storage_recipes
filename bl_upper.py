#bl_upper - функции самого приложения
import os
import GUI
import bl_lower

#Создание директории для каталогов
def create_catalog_dir(path):
    if not os.path.isdir(path):
        return os.mkdir(path+'\\')

#Выход из программы
def quit_program():
    print(bl_lower.green('Пока!'))
    quit()

#Функции работы с каталогами
#Создание каталога
def create_catalog(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if os.path.isfile(path_catalog):
        print(bl_lower.yellow('Такой файл уже существует'))
    else:
        new_catalog = open(path_catalog,'w')
        new_catalog.close()
        print(bl_lower.green('Файл успешно создан!'))

#Получение списка каталогов
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

#Поиск каталога
def search_catalog(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if bl_lower.checking_file(name,format_file,path_catalog):
        print(bl_lower.green(f'Файл {name+format_file} найден'))


def delete_catalog(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if bl_lower.checking_file(name,format_file,path_catalog):
        os.remove(path)
        print(bl_lower.green(f'Файл успешно удален!'))


#Функции работы с рецептами
#Добавление рецептов в каталог
def append_recipe(path):
    name,format_file,path_catalog = bl_lower.input_(path)
    if bl_lower.checking_file(name,format_file,path_catalog):
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
    

#Получение списка рецептов в каталоге
def get_names_recipes(path_catalog):
    if isinstance(path_catalog,str):
        lst = bl_lower.get_list_str_from_file(path_catalog)

        index_column=0
        lst_name=bl_lower.get_list_column(lst,index_column)
        GUI.print_list(lst_name)
        return lst_name,lst,path_catalog

#Поиск рецепта
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

#Удаление рецепта
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
                        file.close()
                        print(bl_lower.green(f'Рецепт успешно удален!'))
            else:
                print(bl_lower.red(f'Рецепта {recipe_search} нет в каталоге'))

#Сортировка по Времени приготовления и создания
def sorting_file_by_column(check_error):
    if isinstance(check_error,str):
        path_catalog = check_error
        file = open(path_catalog, 'r+')
        file.seek(0)

        lst = []
        for string in file:
            lst.append(string[:-1])
        file.close()

        index_column = GUI.get_index_sort()
        lst_name = bl_lower.get_list_column(lst,0)
        lst_column=bl_lower.get_list_column(lst,index_column)

        sort_up_or_down=GUI.get_sort_up_or_down()
        lst_sort = sorted(lst_column,reverse=sort_up_or_down)

        GUI.print_sort_list(lst_name,lst_column,lst_sort)

#Поиск рецепта по ингредиентам
def search_recipe_ingredient(check_error):
    if isinstance(check_error,str):
        path_catalog = check_error
        file = open(path_catalog, 'r+')
        file.seek(0)

        lst = []
        for string in file:
            lst.append(string[:-1])

        search_ingredient = GUI.name_search_ingredient()
        lst_composition = bl_lower.get_list_column(lst, 1)

        # Создание списка рецептов с искомыми ингредиентами
        list_search_ingredient = bl_lower.get_list_search_ingredient(search_ingredient)
        matrix_ingredient = bl_lower.get_matrix_ingredient(lst_composition)
        list_recipe = []
        for search in list_search_ingredient:
            for i in range(len(matrix_ingredient)):
                for j in range(len(matrix_ingredient[i])):
                    if search in matrix_ingredient[i][j] and lst[i] not in list_recipe:
                        list_recipe.append(lst[i])
        if list_recipe != []:
            file.close()
            GUI.print_list(list_recipe)
        else:
            file.close()
            print(bl_lower.red(f'Ингредиентов \'{search_ingredient}\' нет в каталоге'))


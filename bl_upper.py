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
    GUI.show_succesful_message('Пока!')
    quit()

#Функции работы с каталогами
#Создание каталога
def create_catalog(path_catalog:str):
    if bl_lower.checking_file(path_catalog):
        GUI.show_error_message('Такой файл уже существует')
    else:
        new_catalog = open(path_catalog,'w')
        new_catalog.close()
        GUI.show_succesful_message('Файл успешно создан!')

#Получение списка каталогов
def get_catalog_list(path:str):
    list_dir = os.listdir(path)
    list_len_and_date = bl_lower.get_len_and_date_file(path,list_dir)
    if len(list_len_and_date)!=0:
        list_catalog = []
        for i in range(len(list_dir)):
            list_catalog.append(list_dir[i] + list_len_and_date[i])
        GUI.print_list(list_catalog)
    else:
        GUI.show_error_message('Каталогов нет!')

#Поиск каталога
def search_catalog(path_catalog:str):
    if bl_lower.checking_file(path_catalog):
        GUI.show_succesful_message('Файл найден')
    else:
        GUI.show_error_message('Файл не найден')

#Удаление каталога
def delete_catalog(path_catalog:str):
    if bl_lower.checking_file(path_catalog):
        os.remove(path_catalog)
        GUI.show_succesful_message('Файл успешно удален!')
    else:
        GUI.show_error_message(f'Файл не найден')

#Функции работы с рецептами
#Добавление рецептов в каталог
def append_recipe(path_catalog:str):
    if bl_lower.checking_file(path_catalog):
        app_recipe = ';'.join(GUI.new_recipe())
        bl_lower.write_recipe(path_catalog,app_recipe)
        GUI.show_succesful_message('Рецепт успешно записан!')
    else:
        GUI.show_error_message(f'Файл не найден')

#Получение списка рецептов в каталоге
def get_names_recipes(path_catalog: str):
    if bl_lower.checking_file(path_catalog):
        if not bl_lower.checking_file_is_empty(path_catalog):
            list_lines_file = bl_lower.get_file_contents(path_catalog)
            list_names=bl_lower.get_list_column(list_lines_file,0)
            GUI.print_list(list_names)
            return list_names,list_lines_file,path_catalog
        else:
            GUI.show_error_message(f'Файл пуст')
    else:
        GUI.show_error_message(f'Файл не найден')

#Поиск рецепта
def search_recipe(names_recipes):
    if names_recipes != None:
        list_names,list_lines_file,path_catalog = names_recipes
        recipe_search = GUI.name_recipe()
        if bl_lower.recipe_in_catalog(recipe_search, list_names):
            found_recipe = bl_lower.get_recipe(recipe_search,list_names,list_lines_file)
            print(found_recipe)
        else:
            GUI.show_error_message(f'Рецепта {recipe_search} нет в каталоге')

#Удаление рецепта
def delete_recipe(names_recipes):
    if names_recipes != None:
        list_names,list_lines_file,path_catalog = names_recipes
        recipe_search = GUI.name_recipe()
        if bl_lower.recipe_in_catalog(recipe_search,list_names):
            bl_lower.del_recipe(recipe_search,list_names,list_lines_file,path_catalog)
            GUI.show_succesful_message(f'Рецепт успешно удален!')
        else:
            GUI.show_error_message(f'Рецепта {recipe_search} нет в каталоге')

#Сортировка по Времени приготовления и создания
def sorting_file_by_column(path_catalog:str):
    if isinstance(path_catalog, str):
        list_lines_file = bl_lower.get_file_contents(path_catalog)
        lst_name = bl_lower.get_list_column(list_lines_file, 0)

        index_column = GUI.get_index_sort()
        lst_column=bl_lower.get_list_column(list_lines_file,index_column)

        sort_up_or_down=GUI.get_sort_up_or_down()
        lst_sort = sorted(lst_column,reverse=sort_up_or_down)

        GUI.print_sort_list(lst_name,lst_column,lst_sort)

#Поиск рецепта по ингредиентам
def search_recipe_ingredient(path_catalog:str):
    if isinstance(path_catalog, str):
        list_lines_file = bl_lower.get_file_contents(path_catalog)

        lst_composition = bl_lower.get_list_column(list_lines_file, 1)
        matrix_ingredient = bl_lower.get_matrix_ingredient(lst_composition)

        search_ingredient = GUI.name_search_ingredient()
        list_search_ingredient = bl_lower.get_list_search_ingredient(search_ingredient)

        # Создание списка рецептов с искомыми ингредиентами
        list_recipe = []
        for search in list_search_ingredient:
            for i in range(len(matrix_ingredient)):
                for j in range(len(matrix_ingredient[i])):
                    if search in matrix_ingredient[i][j] and list_lines_file[i] not in list_recipe:
                        list_recipe.append(list_lines_file[i])
        bl_lower.ingredient_in_catalog(list_recipe,search_ingredient)


#бесконечный цикл работы приложения, в котором мы спрашиваем у пользователя, что он хочет сделать и хочет ли вообще дальше работать
import bl_upper
import bl_lower
import GUI

def core():
    GUI.info()#начальная информация

    path = GUI.path_dir_catalog()
    bl_upper.create_catalog_dir(path)#создание директории для каталогов

    action = GUI.action_name()
    GUI.get_help(action)#вывод функций для выбранного объекта работы

    function = GUI.function_name(action)
    while True:
        if action == 'catalog':
            if function == 'recipe':
                action = function
                GUI.get_help(action)
                function = GUI.function_name(action)
            else:
                if function == 'quit':
                    bl_upper.quit_program()
                elif function == 'help':
                    GUI.get_help(action)
                elif function == 'create':
                    bl_upper.create_catalog(path)
                elif function == 'list':
                    bl_upper.get_catalog_list(path)
                elif function == 'search':
                    bl_upper.search_catalog(path)
                elif function == 'delete':
                    bl_upper.delete_catalog(path)
                function = GUI.function_name(action)
        elif action == 'recipe':
            if function == 'catalog':
                action = function
                GUI.get_help(action)
                function = GUI.function_name(action)
            else:
                if function == 'quit':
                    bl_upper.quit_program()
                elif function == 'help':
                    GUI.get_help(action)
                elif function == 'append':
                    bl_upper.append_recipe(path)
                elif function == 'read':
                    bl_upper.get_names_recipes( bl_lower.take_path_catalog(path) )
                elif function == 'sort':
                    bl_upper.sorting_file_by_column( bl_lower.take_path_catalog(path) )
                elif function == 'search':
                    bl_upper.search_recipe( bl_upper.get_names_recipes( bl_lower.take_path_catalog(path) ) )
                elif function == 'ingred':
                    bl_upper.search_recipe_ingredient( bl_lower.take_path_catalog(path) )
                elif function == 'delete':
                    bl_upper.delete_recipe( bl_upper.get_names_recipes( bl_lower.take_path_catalog(path) ) )
                function = GUI.function_name(action)


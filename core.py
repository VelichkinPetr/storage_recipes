#бесконечный цикл работы приложения, в котором мы спрашиваем у пользователя, что он хочет сделать и хочет ли вообще дальше работать
import bl_upper
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
                    bl_upper.create_catalog(GUI.input_(path))
                elif function == 'list':
                    bl_upper.get_catalog_list(path)
                elif function == 'search':
                    bl_upper.search_catalog(GUI.input_(path))
                elif function == 'delete':
                    bl_upper.delete_catalog(GUI.input_(path))
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
                    bl_upper.append_recipe(GUI.input_(path))
                elif function == 'read':
                    bl_upper.get_names_recipes(GUI.input_(path))
                elif function == 'sort':
                    bl_upper.sorting_recipe(GUI.input_(path))
                elif function == 'search':
                    bl_upper.search_recipe(bl_upper.get_names_recipes(GUI.input_(path)))
                elif function == 'ingred':
                    bl_upper.search_recipe_ingredient(GUI.input_(path))
                elif function == 'delete':
                    bl_upper.delete_recipe(bl_upper.get_names_recipes(GUI.input_(path)))
                function = GUI.function_name(action)


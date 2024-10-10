#бесконечный цикл работы приложения, в котором мы спрашиваем у пользователя, что он хочет сделать и хочет ли вообще дальше работать
import bl_upper
import bl_lower
import GUI

def core():
    GUI.info()

    path = GUI.path_dir_catalog()
    bl_upper.create_catalog_dir(path)

    action = GUI.action_name()
    GUI.get_help(action)

    function = GUI.function_name(action)
    while action != 'end':
        if action == 'catalog':
            if function == 'back':
                action = GUI.action_name()
                GUI.get_help(action)
                function = GUI.function_name(action)
            else:
                if function == 'quit':
                    quit()
                elif function == 'help':
                    GUI.get_help(action)
                elif function == 'create':
                    bl_upper.create_catalog(path)
                elif function == 'list':
                    bl_upper.get_catalog_list(path,action)
                elif function == 'search':
                    bl_upper.search_catalog(path)
                elif function == 'delete':
                   bl_upper.delete_catalog(path)
                function = GUI.function_name(action)
        elif action == 'recipe':
            if function == 'back':
                action = GUI.action_name()
                GUI.get_help(action)
                function = GUI.function_name(action)
            else:
                if function == 'quit':
                    quit()
                elif function == 'help':
                    GUI.get_help(action)
                elif function == 'append':
                    bl_upper.append_recipe(path)
                elif function == 'read':
                    bl_upper.get_names_recipes(bl_lower.check_error_isfile(path))
                elif function == 'search':
                    bl_upper.search_recipe(bl_upper.get_names_recipes(bl_lower.check_error_isfile(path)))
                elif function == 'delete':
                    print()
                function = GUI.function_name(action)


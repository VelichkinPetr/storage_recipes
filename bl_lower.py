#bl_lower - функции вспомогательные для GUI и upper
import bl_upper

#список имен всех возможных функций
list_name_function=['create_catalog','catalog_list','search_catalog','delete_catalog','recipes_in_catalog','append_recipe','search_recipe','delete_recipe','help','back']
#имена всех вариантов данных с которыми может работать пользователь
list_name_action=['catalog','recipe']
#список всех возможных форматов
list_format=['.txt','.rtf','.doc','.docx']

from GUI import action_name, function_name
#список всех возможных функций
list_function=['create_catalog','catalog_list','search_catalog','delete_catalog','recipes_in_catalog','append_recipe','search_recipe','delete_recipe','help']

#Функция ищет функцию по ее имени и запускает ее
def use_function(action,function):
    if function == 'back':
        print()
        action = action_name()
        function = function_name(action)
        value_func = None
    else:
        index_name = list_name_function.index(function)
        print()
        value_func=list_function[index_name](action)
        function = function_name(action)
    return action,function,value_func
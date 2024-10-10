#bl_lower - функции вспомогательные для GUI и upper
import bl_upper



from GUI import action_name, function_name, my_help
#список всех возможных функций
list_function=[bl_upper.create_catalog,bl_upper.catalog_list,'search_catalog','delete_catalog','recipes_in_catalog','append_recipe','search_recipe','delete_recipe',my_help]

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

def print_list(lst,action):
    print(f'Список {action}: ')
    for elem in lst:
        print(elem)
    print()
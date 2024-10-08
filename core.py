#бесконечный цикл работы приложения, в котором мы спрашиваем у пользователя, что он хочет сделать и хочет ли вообще дальше работать
from bl_lower import use_function
import GUI
GUI.info()
path= GUI.path_dir_catalog()
def core(action,function):
    while action != 'end':
        if action == 'catalog':
            action,function,use_func=use_function(action,function)
        elif action == 'recipe':
            action,function,use_func=use_function(action,function)
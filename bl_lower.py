#bl_lower - функции вспомогательные для GUI и upper
import GUI

#Ввод данных для получения пути к каталогу
def input_(path):
    name = GUI.name_new_catalog()
    format_file = '.txt'
    path_catalog = path + '\\' + name + format_file
    return name,format_file,path_catalog
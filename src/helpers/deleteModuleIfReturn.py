
def deleteModuleIfReturn(): del getattr(__import__('sys'), 'modules')['src.algorithms_menu.menu_RSA']

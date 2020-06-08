
def deleteModuleIfReturn(algName): del getattr(__import__('sys'), 'modules')['src.algorithms_menu.menu_' + algName]

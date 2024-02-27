import modules.screen as sc
import ui.title as t
from tabulate import tabulate

def menuMain():
    sc.clean_screen()
    t.headerMain()
    options = [['1.' ,'Activos'], ['2.','Personal'], ['3.','Zonas'], ['4.','Asignacion de Activos'], ['5.','Reportes'], ['6.','Movimientos de Activos'], ['7.','Salir']]
    print(tabulate(options, tablefmt='grid'))
    op = input('\n>> ')
    if (op == '1'):
        menuActivos()
    elif (op == '2'):
        pass
    elif (op == '3'):
        pass
    elif (op == '4'):
        pass
    elif (op == '5'):
        pass
    elif (op == '6'):
        pass
    elif (op == '7'):
        pass
    else:
        print('opcion no registrada......')
        
    sc.pause_screen()

def menuActivos():
    sc.clean_screen()
    t.headerActivo()
    options = [['1.' ,'Agregar'], ['2.','Editar'], ['3.','Eliminar'], ['4.','Buscar'], ['5.','Regresar al Menu Principal']]
    print(tabulate(options, tablefmt='grid'))
    sc.pause_screen()

def menuPersonal():
    sc.clean_screen()
    t.headerPersonal()
    options = [['1.' ,'Agregar'], ['2.','Editar'], ['3.','Eliminar'], ['4.','Buscar'], ['5.','Regresar al Menu Principal']]
    print(tabulate(options, tablefmt='grid'))
    sc.pause_screen()

def menuZonas():
    sc.clean_screen()
    t.headerZonas()
    options = [['1.' ,'Agregar'], ['2.','Editar'], ['3.','Eliminar'], ['4.','Buscar'], ['5.','Regresar al Menu Principal']]
    print(tabulate(options, tablefmt='grid'))
    sc.pause_screen()
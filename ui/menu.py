import modules.screen as sc
import modules.activos as mas 
import modules.personal as mp
import modules.zonas as mz
import modules.asignaciones as ma
import modules.reportes as mr
import modules.movactivos as mm
import ui.title as t
from tabulate import tabulate

def menuMain():
    sc.clean_screen()
    t.headerMain()
    options = [['1.' ,'Activos'], ['2.','Personal'], ['3.','Zonas'], ['4.','Asignacion de Activos'], ['5.','Reportes'], ['6.','Movimientos de Activos'], ['7.','Salir']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if (op == '1'):
        menuActivos()
    elif (op == '2'):
        menuPersonal()
    elif (op == '3'):
        menuZonas()
    elif (op == '4'):
        menuAsignacion()
    elif (op == '5'):
        menuReportes()
    elif (op == '6'):
        menuMovActi()
    elif (op == '7'):
        sc.clean_screen()
        print('Gracias por utilizar nuestro sistema.....')
        sc.pause_screen()
    else:
        sc.clean_screen()
        print('Opcion no registrada......')
        sc.pause_screen()
        menuMain()

def menuActivos():
    sc.clean_screen()
    t.headerActivo()
    options = [['1.' ,'Agregar'], ['2.','Editar'], ['3.','Eliminar'], ['4.','Buscar'], ['5.','Regresar al Menu Principal']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if (op == '1'):
        mas.addActi()
    elif (op == '2'):
        mas.modifyActi()
    elif (op == '3'):
        mas.delActi()
    elif (op == '4'):
        mas.searchActi()
    elif (op == '5'):
        menuMain()
    else:
        sc.clean_screen()
        print('Opcion no registrada......')
        sc.pause_screen()
        menuActivos()

def menuPersonal():
    sc.clean_screen()
    t.headerPersonal()
    options = [['1.' ,'Agregar'], ['2.','Editar'], ['3.','Eliminar'], ['4.','Buscar'], ['5.','Regresar al Menu Principal']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if (op == '1'):
        mp.addPer()
    elif (op == '2'):
        mp.modifyPer()
    elif (op == '3'):
        mp.delPer()
    elif (op == '4'):
        mp.searchPer()
    elif (op == '5'):
        menuMain()
    else:
        sc.clean_screen()
        print('Opcion no registrada......')
        sc.pause_screen()
        menuPersonal()

def menuZonas():
    sc.clean_screen()
    t.headerZonas()
    options = [['1.' ,'Agregar'], ['2.','Editar'], ['3.','Eliminar'], ['4.','Buscar'], ['5.','Regresar al Menu Principal']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if (op == '1'):
        mz.addZone()
    elif (op == '2'):
        mz.modifyZone()
    elif (op == '3'):
        mz.delZone()
    elif (op == '4'):
        mz.searchZone()
    elif (op == '5'):
        menuMain()
    else:
        sc.clean_screen()
        print('Opcion no registrada......')
        sc.pause_screen()
        menuPersonal()

def menuAsignacion():
    sc.clean_screen()
    t.headerAsignacion()
    options = [['1.' ,'Crear Asignacion'], ['2.','Buscar Asignacion'], ['3.','Regresar Menu Princiapl']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if (op == '1'):
        ma.createAsig()
    elif (op == '2'):
        ma.searchAsig()
    elif (op == '3'):
        menuMain()
    else:
        sc.clean_screen()
        print('Opcion no registrada......')
        sc.pause_screen()
        menuAsignacion()

def menuReportes():
    sc.clean_screen()
    t.headerReportes()
    options = [['1.' ,'Listar todos los Activos'], ['2.','Listar Activos por Categoria'], ['3.','Listar Activos dados de baja por daño'], ['4.','Listar Archivos y Asignaciones'], ['5.','Listar Historial de Movimiento de Activo'], ['6.','Regresar al Menu Principal']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if (op =='1'):
        mr.listAllActi()
    elif (op == '2'):
        mr.listActiCat()
    elif (op == '3'):
        mr.listActiDama()
    elif (op == '4'):
        mr.listActiAsig()
    elif (op == '5'):
        mr.listHistoMov()
    elif (op == '6'):
        menuMain()
    else:
        sc.clean_screen()
        print('Opcion no registrada......')
        sc.pause_screen()
        menuReportes()

def menuMovActi():
    sc.clean_screen()
    t.headerMain()
    options = [['1.' ,'Retorno de Activo'], ['2.','Dar de Baja Activo'], ['3.','Cambiar Asignacion de Activo'], ['4.','Enviar a Garantia Activo'], ['5.','Regresar al Menu Principal']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if (op == '1'):
        mm.returnActi()
    elif (op == '2'):
        mm.cancelActi()
    elif (op == '3'):
        mm.changeAsig()
    elif (op == '4'):
        mm.sendWarran()
    elif (op == '5'):
        menuMain()
    else:
        sc.clean_screen()
        print('Opcion no registrada......')
        sc.pause_screen()
        menuMovActi()

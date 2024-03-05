import modules.screen as scr
import modules.jsonfiles as file 
import ui.title as t
from tabulate import tabulate

activos_data = file.read_file('activos.json')
asig_data = file.read_file('asignaciones.json')

#Funcion para menu de tipo de listado
def menutypelist():
    scr.clean_screen()
    t.headerMenuTypeList()
    option = [['1.' ,'Categoria Equipo de Computo'], ['2.','Tipo de Equipo de Computo']]
    print(tabulate(option, tablefmt='youtrack'))
    op = input('\n>> ')
    return op

#Funcion para tipo de categoria
def menuCat():
    scr.clean_screen()
    op = menutypelist()
    if  op == '1':
        op = '0'
        return op
    elif op == '2':
        scr.clean_screen()
        t.headerMenuCat()
        options = [['1.' ,'CPU'], ['2.','MONITOR'], ['3.','TECLADO'], ['4.','MOUSE']]
        print(tabulate(options, tablefmt='youtrack'))
        op = input('\n>> ')
        return op
    else:
        menuCat()

#Funcion para listar todos los activos
def listAllActi():
    scr.clean_screen()
    kys = ['Codigo', 'Nombre', 'Transacción', 'Formulario', 'Marca', 'Categoría', 'Tipo', 'Valor und', 'Proveedor', 'Nro serial', 'Responsable', 'Estado']
    rows = []  # Lista para contener filas de la tabla
    for key, value in activos_data.items(): 
        row = []  # Lista para contener valores de una fila
        for v in value.values():
            if isinstance(v, dict):
                pass
            else:
                row.append(str(v))  # Añadir el valor a la fila
        rows.append(row)  # Añadir la fila a la lista de filas
    # Imprimir la tabla una vez que se haya construido todas las filas
    print(tabulate(rows, headers=kys, tablefmt='fancy_grid'))
    scr.pause_screen()

#Funcion para activos por categoria
def listActiCat(cat):
    tipo = ''
    if cat == '1':
        tipo = 'CPU'
    if cat == '2':
        tipo = 'Monitor'
    if cat == '3':
        tipo = 'Teclado'
    if cat == '4':
        tipo = 'Mouse'
    if cat == '1' or cat == '2' or cat == '3' or cat == '4':
        scr.clean_screen()
        kys = ['Codigo', 'Nombre', 'Transacción', 'Formulario', 'Marca', 'Categoría', 'Tipo', 'Valor und', 'Proveedor', 'Nro serial', 'Responsable', 'Estado']
        rows = []  # Lista para contener filas de la tabla
        for key, value in activos_data.items(): 
            row = []  # Lista para contener valores de una fila
            if value['tipo'] == tipo:  # Check the condition here
                for v in value.values():
                    if isinstance(v, dict):
                        pass
                    else:
                        row.append(v)  # Añadir el valor a la fila
                rows.append(row)  # Añadir la fila a la lista de filas
                # Imprimir la tabla una vez que se haya construido todas las filas
        print(tabulate(rows, headers=kys, tablefmt='fancy_grid'))
        scr.pause_screen()
    elif cat == '0':
        listAllActi()  

#Funcion para listar activos dados de baja
def listActiDama():
    scr.clean_screen()
    kys = ['Codigo', 'Nombre', 'Transacción', 'Formulario', 'Marca', 'Categoría', 'Tipo', 'Valor und', 'Proveedor', 'Nro serial', 'Responsable', 'Estado']
    rows = []  
    for key, value in activos_data.items(): 
        if value['estado'] in ['2', '3']:  
            row = [] 
            for v in value.values():
                if isinstance(v, dict):
                    pass
                else:
                    row.append(v)
            rows.append(row) 
    print(tabulate(rows, headers=kys, tablefmt='fancy_grid'))
    scr.pause_screen()

#Funcion para listar activos y asignaciones
def listActiAsig():
    pass

#Funcion para listar historial de movimientos de un activo
def listHistoMov():
    pass
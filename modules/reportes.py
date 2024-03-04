import modules.screen as scr
import modules.jsonfiles as file 
import ui.title as t
from tabulate import tabulate

activo_data = file.read_file('activos.json')
asig_data = file.read_file('asignaciones.json')

def menuCat():
    scr.clean_screen()
    def menutypelist():
        t.headerMenuTypeList()
        option = [['1.' ,'Categoria Equipo de Computo'], ['2.','Tipo de Equipo de Computo']]
        print(tabulate(option, tablefmt='youtrack'))
        op = input('\n>> ')
        return op
    op = menutypelist()
    if  op == '1':
            pass
    elif op == '2':
        scr.clean_screen()
        t.headerMenuCat()
        options = [['1.' ,'CPU'], ['2.','MONITOR'], ['3.','TECLADO'], ['4.','MOUSE']]
        print(tabulate(options, tablefmt='youtrack'))
        op = input('\n>> ')
        return op
    else:
        menutypelist()

def listAllActi():
    kys = ['Codigo','Nombre','CodTransaccion','Formulario','Marca','Categoria','Tipo','Valor Unitario','Proveedor','Nro Serial','Resposable','Estado']
    info = []
    for key, value in activo_data.items(): 
        if key != 'historial':
            value = str(value)
            info.append(value)
    print(tabulate([[info]], headers=kys, tablefmt='grid'))
    scr.pause_screen()

def listActiCat():
    cat = menuCat()
    print("Datos que contienen '{}' en la clave:".format(cat))
    for clave, valor in activo_data.items():
        print(clave, ":", valor)
    scr.pause_screen()


def listActiDama():
    pass

def listActiAsig():
    pass

def listHistoMov():
    pass
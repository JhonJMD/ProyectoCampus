import modules.screen as scr
import modules.jsonfiles as file
import ui.title as t
from tabulate import tabulate

def menuNameZone(zona : dict, filedata : dict):
    scr.clean_screen()
    t.headerMenuNameZonas()
    options = [['1.' ,'Apolo'], ['2.','Artemis'], ['3.','Sputnik']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if op == '1':
        namezone = 'Apolo'
    elif op == '2':
        namezone = 'Artemis'
    elif op =="3":
        namezone = 'Sputnik'
    else:
        print('Opcion ingresada invalida....')
        scr.pause_screen()
        menuNameZone()
    for value in filedata.values():
        if value['nombrezona'] == namezone:
            isNameEquals = True
    if isNameEquals == False:
        zona['nombrezona'] = namezone
    else:
        print('La zona ingresada ya se encuentra registrada')
        scr.pausa_screen()
        menuNameZone(zona, filedata)

def addZone():
    isFind = False
    is_add_zone = True
    while is_add_zone: 
        scr.clean_screen()
        file.check_file('zonas.json') 
        filedata = file.read_file('zonas.json') #carga el contenido del archivo a filedata
        zona =  {     
            'nrozona' : '',
            'nombrezona' : '',
            'totalcapacidad' : 0 
        }
        while True:
            try:
                nrozona = int(input('Ingrese el numero de la Zona (0 para salir): '))
            except ValueError:
                print('El dato ingresado no es valido')
                scr.pause_screen()
            else:
                if nrozona == 0:
                    is_add_zone = False 
                    break
                nrozona = str(nrozona).zfill(3)
                if len(filedata) == 0:
                    zona['nrozona'] = nrozona
                else:
                    for key in filedata.keys():
                        if key == nrozona:
                            isFind = True
                if isFind == False:
                    zona['nrozona'] = nrozona
                    menuNameZone(zona, filedata)
                    zona['totalcapacidad'] = 33
                    filedata.update({nrozona : zona}) #Actualiza el filedata con el contenido dado
                    file.update_file('zonas.json', filedata) #Actualiza el archivo json con el nuevo activo
                    #Bucle para decidir si se agrega otro activo o no 
                    while True:
                        scr.clean_screen()
                        yes_or_not = input('¿Desea registrar otro activo? s(sí) -- ENTER(no): ')
                        if yes_or_not == ('s' or 'S'):
                            break
                        elif yes_or_not == '':
                            is_add_zone = False
                            break
                    break
                else:
                    print('Ya esta registrado este numero de Zona')
                    scr.pause_screen()

addZone()

def modifyZone():
    pass

def delZone():
    pass

def searchZone():
    pass

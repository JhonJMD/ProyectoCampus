import modules.screen as scr
import modules.jsonfiles as file
import ui.title as t
from tabulate import tabulate

#Funcion menu de zonas
def menuNameZone(zona : dict, filedata : dict):
    isNameEquals = False
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
        scr.pause_screen()
        menuNameZone(zona, filedata)

#Funcion para agregar zonas
def addZone():
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
            isFind = False
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
                        yes_or_not = input('¿Desea registrar otra zona? s(sí) -- ENTER(no): ')
                        if yes_or_not == ('s' or 'S'):
                            break
                        elif yes_or_not == '':
                            is_add_zone = False
                            break
                    break
                else:
                    print('Ya esta registrado este numero de Zona')
                    scr.pause_screen()

#Funcion para modificar zonas
def modifyZone():
    modify_running = True
    while modify_running:
        scr.clean_screen()
        file.check_file('zonas.json') #Chequea si el archivo existe y si no lo crea
        filedata = file.read_file('zonas.json') #Carga el archivo a una variable python
        if len(filedata) == 0: #Revisa si hay contenido o no dentro del archivo
            print('No se encuentra ningúna zona registrada')
            break
        while True:
            scr.clean_screen()
            code_to_modify = input('Ingrese el codigo de la zona que desea modificar (ENTER para salir): ').zfill(3)
            
            if code_to_modify == '':
                modify_running = False
                return
            if code_to_modify in filedata.keys(): #Si el codigo está registrado empieza el proceso
                zone_dict = filedata[code_to_modify] 
                for key, value in zone_dict.items(): 
                    scr.clean_screen()
                    #Imprime los valores que se pueden modificar y quita algunos que no.
                    if (key != 'nrozona') and (key != 'nombrezona'):
                        print(f'{key} : {value}')
                        print('')
                        while True:
                            modify_or_not = str(input('¿Desea modificar esta información? s(sí) - n(no): ')).upper()
                            if modify_or_not == 'S':
                                new_value = input(f'Ingrese la nueva información para "{key}": ')
                                zone_dict[key] = new_value
                                break  
                            elif modify_or_not == 'N':
                                break
                break                
            else:
                print('El codigo no se encuentra registrado')
                scr.pause_screen()  
        file.update_file('zonas.json', filedata)  
        scr.clean_screen()
        print('Se ha modificado la información exitosamente')
        question = '¿Desea modificar otra zona? s(sí) -- n(no): '
        while True:
            yes_or_not = input(question).upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                modify_running = False
                break

#Fucion para eliminar zonas
def delZone():
    del_zone = True
    while del_zone:
        scr.clean_screen()
        file.check_file('zonas.json')
        filedata = file.read_file('zonas.json')  
        if len(filedata) == 0: #Si no hay activos registrados no entra al proceso de eliminación
            print('No hay zonas registradas')
            scr.pause_screen()
            del_zone = False
            break
        while True:
            scr.clean_screen()   
            code_to_del = input('Ingrese el codigo de la zona que desea eliminar (ENTER para salir): ').zfill(3)
            if code_to_del == '':
                return  
            if code_to_del in filedata.keys():
                for key, value in filedata[code_to_del].items():
                    if key == 'nombrezona':
                        print(f'{key} : {value}')
                break
            else:
                print('El codigo ingresado no se encuentra registrado')
                scr.pause_screen()    
        while True:
            print('')
            yes_or_not = input('Seguro que desea eliminar esta zona? s(sí) - n(no): ').upper()
            if yes_or_not == 'S':
                filedata.pop(code_to_del)
                file.update_file('zonas.json', filedata)
                break
            elif yes_or_not == 'N':
                break
        while True:
            scr.clean_screen()
            yes_or_not = input('¿Desea eliminar otra zona? s(sí) - n(no): ').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                del_zone = False
                break

#Funcion para buscar zonas
def searchZone():
    search_running = True
    while search_running:
        scr.clean_screen()
        info = []
        kys = ['Número','Nombre','Capacidad']
        file.check_file('zonas.json')
        filedata = file.read_file('zonas.json')
        while True:
            scr.clean_screen()
            code_to_search = input('Ingrese el codigo de la zona a buscar (ENTER para salir): ').zfill(3)
            if code_to_search == '':
                search_running = False
                return
            #Imprimir toda la información del codigo ingresado
            if code_to_search in filedata.keys(): #Si el codigo está registrado empieza el proceso
                for key, value in filedata[code_to_search].items(): 
                    value = str(value)
                    info.append(value)
                print(tabulate([info], headers=kys, tablefmt='fancy_grid'))
                scr.pause_screen()
                break       
            else:
                scr.clean_screen()
                print('El codigo ingresado no se encuentra registrado, verifiquelo nuevamente')
                scr.pause_screen()
        scr.clean_screen()
        while True:
            yes_or_not = input('¿Desea buscar otra zona? s(sí) -- n(no): ').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                search_running = False
                break

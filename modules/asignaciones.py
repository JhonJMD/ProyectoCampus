import modules.jsonfiles as file
import modules.screen as scr
from tabulate import tabulate
import datetime



#Función para crear asignaciones
def createAsig():
    dd = ''
    mm = ''
    yy = ''
    create_asig = True
    while create_asig:
        scr.clean_screen()
        file.check_file('asignaciones.json') #Crear archivo asignaciones
        asigdata = file.read_file('asignaciones.json') #Cargar archivo asignaciones
        personadata = file.read_file('personal.json') #Cargar archivo personal
        activdata = file.read_file('activos.json') #Cargar archivo activos
        zonedata = file.read_file('zonas.json')
        asignacion = {
            'nro asignacion' : '',
            'fecha asignacion' : (),
            'tipo asignacion' : '',
            'asignado a' : {},
            'activo/s asignado' : []
        }
        while True:
            try:
                scr.clean_screen()
                nro_asig = int(input('Ingrese el número de asignación (0 para salir): '))
                nro_asig = str(nro_asig)
                asignacion['nro asignacion'] = nro_asig
                if nro_asig == '0':
                    return
                if nro_asig in asigdata.keys():
                    print('Este número de asignación ya se encuentra registrado')
                    scr.pause_screen()
                else: 
                    break
            except:
                print('Por favor digite un valor válido para el número de asignación')
                scr.pause_screen()
        print('A continuación va a agregar la fecha de asignacion')
        scr.pause_screen()
        while True:
            #Validación de que el día sea un día válido de un mes
            try:
                scr.clean_screen()
                dd = int(input('Ingrese el día de asignación: '))  
                if dd in range(32):
                    break
                else:
                    print('Por favor ingrese un día válido')
                    scr.pause_screen()
            except:
                print('Por favor ingrese un día válido')
                scr.pause_screen()
        while True:
            #Validación de que el mes sea un mes valido del año
            try:
                scr.clean_screen()
                mm = int(input('Ingrese el mes de asignación: '))
                if mm in range(13):
                    break
                else:
                    print('Por favor ingrese un mes válido')
                    scr.pause_screen()
            except:
                print('Por favor ingrese un mes válido')
                scr.pause_screen()
        while True:
            #Validación de que el año sea menor o igual a el año en el que estamos
            try:
                scr.clean_screen()
                yy = int(input('Ingrese el año de asignación: '))
                if yy <= 2024:
                    break
                else:
                    print('Por favor ingrese un año válido')
                    scr.pause_screen()
            except:
                print('Por favor ingrese un año válido')
                scr.pause_screen()
        asignacion['fecha asignacion'] = f'{dd}/{mm}/{yy}' #Toma las variables anteriores para validar que el usuario ingrese una fecha correcta
        while True:
            scr.clean_screen()
            tipo = input('Ingrese "P" si el tipo de asignación es a persona o "Z" si es a una zona: ').upper()
            if tipo == 'P': #Valida que ingrese el dato correcto y le asigna el tipo de asig
                asignacion['tipo asignacion'] = 'Persona'
                break
            elif tipo == 'Z':
                asignacion['tipo asignacion'] = 'Zona'
                break
            else:
                print('Por favor ingrese un dato válido ("P" o "Z")')
        if tipo == 'P': #Empieza un bucle para ingresar la persona a la que se le asigna activos
            add_person = True
            while add_person:
                scr.clean_screen()
                isidcorrect = True
                while isidcorrect:
                    scr.clean_screen()
                    id = input('Ingres el ID de la persona a la que se asigna el activo: ')
                    if len(asigdata) != 0:
                        for item in asigdata:
                            #Verifica que la persona no tenga activos asignados
                            if id in item['asignado a']:
                                print('Esta persona ya cuenta con un activo asignado\nSi desea reasignarle otro primero retorne el activo que ya está asignado y pase a asignarle el nuevo')
                                scr.pause_screen()
                    else:
                        break
                #Se asegura de que el id ingresado sea el que la persona desea realmente asignar
                if id in personadata.keys():
                    name = personadata[id].get('nombre')
                    yesornot = input(f'El ID ingresado corresponde a {name}... ¿Está seguro que desea asignarlo? s(sí) - n(no): ').upper()
                    if yesornot == 'S':
                        asignacion['asignado a'].update({id : name})
                        scr.clean_screen()
                        print('Asignado exitosamente!')
                        break
                    if yesornot == 'N':
                        pass
                else:
                    print('El ID no se encuentra registrado, vuelva a intentarlo')
                    scr.pause_screen()
        if tipo == 'Z': #Empieza el bucle para ingresar la zona a la que se le asigna activos
            add_zone = True
            while add_zone:
                scr.clean_screen()
                is_zone_correct = True
                while is_zone_correct: 
                    scr.clean_screen()
                    zone = input('Ingrese el codigo de la zona a la que desea asignar activos: ')
                    if zone in zonedata.keys():
                        zone_name = zonedata[zone].get('nombrezona')
                        asignacion['asignado a'] = zone_name
                        scr.clean_screen()
                        print('¡La zona fue asignada correctamente!')
                        is_zone_correct = False
                        add_zone = False
                    else:
                        print('La zona no se encuentra registrada')
                        scr.pause_screen()
        if tipo == 'Z': #Empieza el bucle necesario para ingresar activos a una zona 
            nroId = 0
            add_acti_zone = True
            while add_acti_zone:
                scr.clean_screen()
                active = input('Ingrese el codigo del activo a asignar: ')
                if (active in activdata.keys()) and (activdata[active]['estado'] == '0'):
                    name = activdata[active].get('nombre') #Guarda el nombre del activo ingresado
                    tipo = activdata[active].get('tipo') #Guarda el tipo del activo ingresado
                    scr.clean_screen()
                    print(f'nombre : {name}\ntipo : {tipo}')
                    areyousure = input('¿Seguro que desea asignar este activo? s(sí) - n(no): ').upper()
                    if areyousure == 'S':
                        scr.clean_screen()
                        asignacion['activo/s asignado'].append(active) #Actualiza el diccionario de asignacion
                        activdata[active]['estado'] = '1' #Cambia el estado del activo a "asignado"
                    if areyousure == 'N':
                        scr.pause_screen()  
                else: #Si el activo tuvo algún error
                    scr.clean_screen()
                    print('El activo ingresado posee alguno de estos problemas:\n*No se encuentra registrado\n*Ya se encuentra asignado\n*Se encuentra en reparacion y/o garantía\n*No se encuentra disponible debido a alguna falla ')
                    print('Verifique el estado del activo en la sección buscar activo')
                    scr.pause_screen() 
                file.update_file('activos.json', activdata)              
                asigdata.update({nro_asig: asignacion})
                file.update_file('asignaciones.json', asigdata)
                nroId+=1
                movement = {
                    'nroId': str(nroId).zfill(3),
                    'fecha': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'tipoMov': '1', 
                    'idRespMov': '123'  
                }
                activdata[active]['historial'].update(movement)
                file.update_file('activos.json', activdata)   
                
                while True:
                    scr.clean_screen()
                    yes_or_not = input('¿Desea registrar otro activo? s(sí) -- n(no): ').upper()
                    if yes_or_not == 'S':
                        break
                    elif yes_or_not == 'N':
                        add_acti_zone = False
                        break              
        if tipo == 'P': #Empieza el bucle necesario para ingresar activos a una persona
            nroId_2 = 0
            add_acti = True
            tipos = []
            while add_acti:
                scr.clean_screen()
                activo = input('Ingrese el codigo del activo a asignar: ')    
                if (activo in activdata.keys()) and (activdata[activo]['estado'] == '0'): #Valida que el activo se encuentre registrado y no asignado
                    if activdata[activo]['tipo'] not in tipos: #Valida que el tipo de activo que se desea asignar no se encuentre ya asignado a esta persona
                        tipos.append(activdata[activo]['tipo']) #Si no se encuentra registrado, lo registra a la lista para luego volver a validar
                        name = activdata[activo].get('nombre')
                        tipo = activdata[activo].get('tipo')
                        scr.clean_screen
                        print(f'nombre : {name}')
                        print(f'tipo : {tipo}')
                        areyousure = input('¿Seguro que desea asignar este activo? s(sí) - n(no): ').upper()
                        if areyousure == 'S':
                            scr.clean_screen()
                            asignacion['activo/s asignado'].append(activo)
                            activdata[activo]['estado'] = '1'
                        if areyousure == 'N':
                            scr.pause_screen()
                    else: #Si la persona ya tiene un activo de este tipo asignado
                        scr.clean_screen()
                        print('Esta persona ya tiene un activo de este tipo asignado, asigne otro tipo de activo o regrese al menu')
                        scr.pause_screen()
                else: #Si el activo tuvo algún error
                    scr.clean_screen()
                    print('El activo ingresado posee alguno de estos problemas:\n*No se encuentra registrado\n*Ya se encuentra asignado\n*Se encuentra en reparacion y/o garantía\n*No se encuentra disponible debido a alguna falla ')
                    print('Verifique el estado del activo en la sección buscar activo')
                    scr.pause_screen()                        
                while True:
                    scr.clean_screen()
                    yes_or_not = input('¿Desea registrar otro activo? s(sí) -- n(no): ').upper()
                    if yes_or_not == 'S':
                        break
                    elif yes_or_not == 'N':
                        add_acti = False
                        break
        file.update_file('activos.json', activdata)              
        asigdata.update({nro_asig: asignacion})
        file.update_file('asignaciones.json', asigdata)
        nroId_2+=1
        movement = {
            'nroId': str(nroId).zfill(3),
            'fecha': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'tipoMov': '1', 
            'idRespMov': '123'  
        }
        activdata[active]['historial'].update(movement)
        file.update_file('activos.json', activdata)   
        while True:
            scr.clean_screen()
            yes_or_not = input('¿Desea registrar otra asignación? s(sí) -- n(no): ').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                create_asig = False
                break                                

def searchAsig():
    search_running = True
    while search_running:
        scr.clean_screen()
        info = []
        kys = ['Nro asignación','Fecha','Tipo','Asignado a','Activo/s asignado/s']
        file.check_file('asignaciones.json')
        filedata = file.read_file('asignaciones.json')
        while True:
            scr.clean_screen()
            code_to_search = input('Ingrese el número de asignación a buscar (ENTER para salir): ')
            if code_to_search == '':
                search_running = False
                return
            #Imprimir toda la información del codigo ingresado
            if code_to_search in filedata.keys(): #Si el codigo está registrado empieza el proceso
                for key, value in filedata[code_to_search].items(): 
                    value = str(value)
                    info.append(value)
                print(tabulate([info], headers=kys, tablefmt='grid'))
                scr.pause_screen()
                break       
            else:
                scr.clean_screen()
                print('El codigo ingresado no se encuentra registrado, verifiquelo nuevamente')
                scr.pause_screen()
        scr.clean_screen()
        while True:
            yes_or_not = input('¿Desea buscar otra asignación? s(sí) -- n(no): ').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                search_running = False
                break


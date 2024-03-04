import modules.jsonfiles as file 
import modules.screen as scr
import datetime

nroId = 0

def returnActi():
    global nroId
    return_acti = True
    while return_acti:
        file.check_file('activos.json')
        acti_data = file.read_file('activos.json')
        persona_data = file.read_file('personal.json')
        asig_data = file.read_file('asignaciones.json')
        while True:
            scr.clean_screen()
            code_to_return = input('Ingrese el codigo del activo que desea retornar: ')
            if code_to_return not in acti_data.keys():
                print('El activo no se encuentra registrado, por favor verifique en la sección de activos del menú principal') 
                scr.pause_screen()           
            else:
                state = acti_data[code_to_return]['estado'] 
                if state == '1':
                    print('El activo ya ha sido retornado.')
                    scr.pause_screen()
                else:
                    nroId+=1
                    acti_data[code_to_return]['estado'] = '1'
                    movement = {
                        'nroId': str(nroId).zfill(3),
                        'fecha': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'tipoMov': '2', 
                        'idRespMov': '123'  
                    }
                    acti_data[code_to_return]['historial'].update(movement)
                    file.update_file('activos.json', acti_data)   
                    print(f'Activo {code_to_return} retornado exitosamente.')
                    scr.pause_screen()
            while True:
                scr.clean_screen()
                yes_or_not = input('¿Desea retornar otro activo? s(sí) -- ENTER(no): ').upper()
                if yes_or_not == ('S'):
                    break
                elif yes_or_not == '':
                    return_acti = False
                    break 

def cancelActi():
    global nroId
    cancel_acti = True
    while cancel_acti:
        file.check_file('activos.json')
        acti_data = file.read_file('activos.json')
        persona_data = file.read_file('personal.json')
        asig_data = file.read_file('asignaciones.json')
        while True:
            scr.clean_screen()
            code_to_cancel = input('Ingrese el código del activo que desea dar de baja: ')
            if code_to_cancel not in acti_data.keys():
                print('El activo no se encuentra registrado, por favor verifique en la sección de activos del menú principal') 
                scr.pause_screen()           
                break
            else:
                state = acti_data[code_to_cancel]['estado'] 
                if state == '2':
                    print('El activo ya ha sido dado de baja.')
                    scr.pause_screen()
                    break
                else:
                    state = acti_data[code_to_cancel]['estado'] 
                    if state == '2':
                        print('El activo ya ha sido dado de baja')
                        scr.pause_screen()
                    else:
                        nroId+=1
                        acti_data[code_to_cancel]['estado'] = '2'
                        movement = {
                            'nroId': str(nroId).zfill(3),
                            'fecha': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            'tipoMov': '2', 
                            'idRespMov': '123'  
                        }
                        acti_data[code_to_cancel]['historial'].update(movement)
                        file.update_file('activos.json', acti_data)
                        print(f'Activo {code_to_cancel} dado de baja exitosamente.')
                        scr.pause_screen()
                    while True:
                        scr.clean_screen()
                        yes_or_not = input('¿Desea dar de baja otro activo? s(sí) -- ENTER(no): ').upper()
                        if yes_or_not == ('S'):
                            break
                        elif yes_or_not == '':
                            cancel_acti = False
                            break 

def changeAsig():
    global nroId
    change_acti = True
    while change_acti:
        file.check_file('activos.json')
        acti_data = file.read_file('activos.json')
        persona_data = file.read_file('personal.json')
        asig_data = file.read_file('asignaciones.json')
        while True:
            scr.clean_screen()
            code_to_change = input('Ingrese el código del activo que desea cambiar de asignación: ')
            if code_to_change not in acti_data.keys():
                print('El activo no se encuentra registrado, por favor verifique en la sección de activos del menú principal') 
                scr.pause_screen()           
                break
            else:
                state = acti_data[code_to_change]['estado']
                if state == '3':
                    print('El activo se encuentra en reparación o garantía, no se puede cambiar de asignación.')
                    scr.pause_screen()
                elif state == '2':
                    print('El activo ha sido dado de baja, no se puede cambiar de asignación.')
                    scr.pause_screen()
                else:
                    nroId+=1
                    while True:
                        new_assignment = input('Ingrese el nuevo destinatario del activo: ')
                        if new_assignment not in persona_data.keys() and new_assignment not in asig_data.keys():
                            print('El destinatario especificado no existe en la base de datos.')
                            scr.pause_screen()
                        else:
                            break
                    movement = {
                        'NroId': str(nroId).zfill(3),
                        'Fecha': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'tipoMov': '4',
                        'idRespMov': '123'
                    }
                    acti_data[code_to_change]['historial'].update(movement)
                    file.update_file('activos.json', acti_data)
                    print(f'Asignación del activo {code_to_change} cambiada exitosamente.')
                    scr.pause_screen()
                while True:
                    scr.clean_screen()
                    yes_or_not = input('¿Desea reasignar otro activo? s(sí) -- ENTER(no): ').upper()
                    if yes_or_not == ('S'):
                        break
                    elif yes_or_not == '':
                        change_acti = False
                        break 

def sendWarran():
    global nroId
    send_warran = True
    while send_warran:
        file.check_file('activos.json')
        acti_data = file.read_file('activos.json')
        persona_data = file.read_file('personal.json')
        asig_data = file.read_file('asignaciones.json')
        while True:
            scr.clean_screen()
            code_to_warran = input('Ingrese el código del activo que desea enviar a garantía: ')
            if code_to_warran not in acti_data.keys():
                print('El activo no se encuentra registrado, por favor verifique en la sección de activos del menú principal') 
                scr.pause_screen()           
            else:
                state = acti_data[code_to_warran]['estado']
                if state == '3':
                    print('El activo ya se encuentra en garantía.')
                    scr.pause_screen()
                else:
                    nroId+=1
                    acti_data[code_to_warran]['estado'] = '3'
                    movement = {
                        'NroId': str(nroId).zfill(3),
                        'Fecha': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'tipoMov': '3',
                        'idRespMov': '123',  
                    }
                    acti_data[code_to_warran]['historial'].update(movement)
                    file.update_file('activos.json', acti_data)  
                    print(f'Activo {code_to_warran} enviado a garantía correctamente.')
                    scr.pause_screen()
            while True:
                scr.clean_screen()
                yes_or_not = input('¿Desea reasignar otro activo? s(sí) -- ENTER(no): ').upper()
                if yes_or_not == ('S'):
                    break
                elif yes_or_not == '':
                    send_warran = False
                    break

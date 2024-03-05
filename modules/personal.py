import modules.screen as scr
import modules.jsonfiles as file
from tabulate import tabulate



#Función par añadir persona al archivo json
def addPer():
    is_add_per = True
    while is_add_per: 
        scr.clean_screen()
        file.check_file('personal.json') 
        filedata = file.read_file('personal.json') #carga el contenido del archivo a filedata
        persona =  {    
            'id' : '',
            'nombre' : '',
            'email' : '',
            'telefonos' : {
                'movil' : '',
                'casa' : '',
                'personal' : '',
                'oficina' : '' 
            }       
        }
        id = input('Ingrese el ID de la persona a registrar (ENTER para salir): ')
        if id == '':
            return
        if id in filedata.keys(): #Verificar si el codigo ya se encuentra registrado
            print('Este codigo ya se encuentra registrado, si desea editarlo vaya a la sección de editar activos')
            scr.pause_screen()
        else:      
            persona['id'] = id 
            persona['nombre'] = input('Ingrese el nombre de la persona: ')
            persona['email'] = input(f"Ingrese el email de {persona['nombre']}: ")
            while True:
                try:
                    scr.clean_screen()
                    persona['telefonos']['movil'] = int(input('Ingrese el número de telefono movil: '))
                    break
                except:
                    print('Ingrese un número de telefono válido')
                    scr.pause_screen()
            while True: #Cada while True y su try / Except es para validar que el usuario digite un número de telefono correcto
                try:
                    persona['telefonos']['casa'] = int(input('Ingrese el número de telefono de la casa (Enter si no ingresa): '))
                    break
                except:
                    print('Ingrese un número de telefono válido')
                    scr.pause_screen()
            while True:
                try:
                    persona['telefonos']['personal'] = int(input('Ingrese el número de telefono personal (Enter si no ingresa): '))
                    break
                except:
                    print('Ingrese un número de telefono válido')
                    scr.pause_screen()
            while True:
                try:
                    persona['telefonos']['oficina'] = input('Ingrese el número de telefono de oficina (Enter si no ingresa): ')  
                    break
                except:
                    print('Ingrese un número de telefono válido')
                    scr.pause_screen()
            scr.clean_screen()
            filedata.update({id : persona}) #Actualiza el filedata con el contenido dado
            file.update_file('personal.json', filedata) #Actualiza el archivo json con el nuevo activo
        #Bucle para decidir si se agrega otro activo o no 
        while True:
            scr.clean_screen()
            yes_or_not = input('¿Desea registrar otra persona? s(sí) -- ENTER(no): ')
            if yes_or_not == ('s' or 'S'):
                break
            elif yes_or_not == '':
                is_add_per = False
                break
        
#Función para modificar personal
def modifyPer():
    modify_running = True
    while modify_running:
        scr.clean_screen()
        file.check_file('personal.json') #Chequea si el archivo existe y si no lo crea
        filedata = file.read_file('personal.json') #Carga el archivo a una variable python
        if len(filedata) == 0: #Revisa si hay contenido o no dentro del archivo
            print('No se encuentra ningún activo registrado')
            break
        while True:
            scr.clean_screen()
            id_to_modify = input('Ingrese el codigo del activo que desea modificar (ENTER para salir): ')
            if id_to_modify == '':
                return
            if id_to_modify in filedata.keys(): #Si el codigo está registrado empieza el proceso
                person_dict = filedata[id_to_modify] 
                for key, value in person_dict.items(): 
                    scr.clean_screen()
                    #Imprime los valores que se pueden modificar y quita algunos que no.
                    if key != 'id':
                        if isinstance(value, dict): #Si el contenido de la llave es un diccionario entonces imprime 
                            for k, v in value.items(): #Cada llave y valor dentro de ese sub diccionario
                                scr.clean_screen()
                                print(f'{key}')
                                print(f'{k} : {v}')
                                print('')
                                while True:
                                    modify_or_not = input('¿Desea modificar esta información? s(sí) - n(no): ').upper()
                                    if modify_or_not == 'S':
                                        new_value = input(f'Ingrese la nueva información para "{k}": ')
                                        person_dict[key][k] = new_value
                                        break  
                                    elif modify_or_not == 'N':
                                        break 
                            break            
                        else:
                            scr.clean_screen()
                            print(f'{key} : {value}')
                            print('')
                            while True:
                                modify_or_not = input('¿Desea modificar esta información? s(sí) - n(no): ').upper()
                                if modify_or_not == 'S':
                                    new_value = input(f'Ingrese la nueva información para "{key}": ')
                                    person_dict[key] = new_value
                                    break  
                                elif modify_or_not == 'N':
                                    break
                break                
            else:
                print('El codigo no se encuentra registrado')
                scr.pause_screen()  
        file.update_file('personal.json', filedata)  
        scr.clean_screen()
        print('Se ha modificado la información exitosamente')
        question = '¿Desea modificar otro activo? s(sí) -- n(no): '
        while True:
            yes_or_not = input(question).upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                modify_running = False
                break

#Función para eliminar personal
def delPer():
    del_per = True
    while del_per:
        asigdata = file.read_file('asignaciones.json')
        scr.clean_screen()
        file.check_file('personal.json')
        filedata = file.read_file('personal.json')  
        if len(filedata) == 0: #Si no hay activos registrados no entra al proceso de eliminación
            print('No hay activos registrados')
            scr.pause_screen()
            del_per = False
            break
        while True:
            scr.clean_screen()   
            persondel = input('Ingrese el ID de la persona que desea eliminar (ENTER para salir): ')
            if persondel == '':
                return  
            for key, value in asigdata.items():
                if value['tipo asignacion'] == 'Persona':
                    if persondel in value['asignado a'].keys():
                        print('Esta persona no se puede eliminar porque tiene activos asignados, por favor verifique que no tenga nada asignado')
                        scr.pause_screen()
                        return
            if persondel in filedata.keys():
                for key, value in filedata[persondel].items():
                    if key == 'id' or key == 'nombre':
                        print(f'{key} : {value}')
                break
            else:
                print('El ID ingresado no se encuentra registrado')
                scr.pause_screen()    
        while True:
            print('')
            yes_or_not = input('Seguro que desea eliminar esta persona? s(sí) - n(no): ').upper()
            if yes_or_not == 'S':
                filedata.pop(persondel)
                file.update_file('personal.json', filedata)
                break
            elif yes_or_not == 'N':
                break
        while True:
            scr.clean_screen()
            yes_or_not = input('¿Desea eliminar otra persona? s(sí) - n(no): ').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                del_per = False
                break
                
#Función para buscar personal
def searchPer():
    search_running = True
    while search_running:
        scr.clean_screen()
        info = []
        kys = ['ID','Nombre','Email','Tel movil','Tel casa','Tel personal','Tel oficina'] #Headers de la tabla
        file.check_file('personal.json')
        filedata = file.read_file('personal.json')
        while True:
            scr.clean_screen()
            code_to_search = input('Ingrese el ID de la persona a buscar (ENTER para salir): ')
            if code_to_search == '':
                search_running = False
                return
            #Imprimir toda la información del codigo ingresado
            if code_to_search in filedata.keys(): #Si el codigo está registrado empieza el proceso
                for key, value in filedata[code_to_search].items(): 
                        if isinstance(value, dict): #Si el contenido de la llave es un diccionario
                            for k, v in value.items(): #Recorre cada llave y valor del subdiccionario
                                info.append(v) #Y lo guarda en un valor aparte del diccionario principal "telefonos"
                        if key != 'telefonos': #No deja que se imrpima el diccionario "Telefonos" en la tabla sino solo los valores que contiene
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
            yes_or_not = input('¿Desea buscar otro activo? s(sí) -- n(no): ').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                search_running = False
                break


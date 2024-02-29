import modules.screen as scr
import modules.jsonfiles as file



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
            persona['email'] = input(f'Ingrese el email de {persona['nombre']}: ')
            persona['telefonos']['movil'] = input('Ingrese el número de telefono movil: ')
            persona['telefonos']['casa'] = input('Ingrese el número de telefono de la casa (Enter si no ingresa): ')
            persona['telefonos']['personal'] = input('Ingrese el número de telefono personal (Enter si no ingresa): ')
            persona['telefonos']['oficina'] = input('Ingrese el número de telefono de oficina (Enter si no ingresa): ')  
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
                        if isinstance(value, dict):
                            for k, v in value.items():
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

def delPer():
    pass

def searchPer():
    pass

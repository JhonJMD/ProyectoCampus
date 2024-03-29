import modules.jsonfiles as file
import modules.screen as scr
from tabulate import tabulate

#Función para agregar el contenido al diccionario de activos en el archivo json 
def addActi():
    is_add_active = True
    while is_add_active: 
        scr.clean_screen()
        file.check_file('activos.json') 
        filedata = file.read_file('activos.json') #carga el contenido del archivo a filedata
        activo = {
            'codigo' : '',
            'nombre' : '',
            'transaccion' : '327',
            'formulario': '966217823',
            'marca': 'Compumax',
            'categoria ': 'Equipo de computo',
            'tipo': '',
            'valor und': 0.0,
            'proveedor': 'Compumax',
            'nro serial': '35465454554156454',
            'responsable': 'CampusLands',
            'estado': '0',
            'historial': {}
        }
        while True:
            scr.clean_screen()
            while True:
                scr.clean_screen()
                tipo = input('Ingrese el tipo de activo (1.cpu, 2.mouse, 3.teclado, 4.monitor, 5.Salir: ')
                if tipo == '1' or tipo == '2' or tipo == '3' or tipo == '4' or tipo == '5': #Verifica los tipos de maquina de computo que hay
                    break
            if tipo == '5':
                return
            if tipo == '1':
                activo['tipo'] = 'CPU'
                while True:
                    try:
                        codCampus = int(input('Ingrese el codigo (solo parte númerica) del activo a registrar: ')) #Se recibe la parte númerica del codigo a registrar
                        activo['codigo'] = f'CPU{codCampus}' #Agrega automaticamente el codigo "CPU" y se le suma el codigo agregado
                        codCampus = f'CPU{codCampus}'
                        break
                    except:
                        print('Codigo invalido, vuelva a intentarlo')
                        scr.pause_screen()   
            if tipo == '2':
                activo['tipo'] = 'Mouse'
                while True:
                    try:
                        codCampus = int(input('Ingrese el codigo (solo parte númerica) del activo a registrar: ')) #Se recibe la parte númerica del codigo
                        activo['codigo'] = f'MO{codCampus}' #Agrega automaticamente el codigo "MO" y se le suma el codigo agregado
                        codCampus = f'MO{codCampus}' #Guarda el codigo en una variable
                        break
                    except:
                        print('Codigo invalido, vuelva a intentarlo')
                        scr.pause_screen()   
            if tipo == '3':
                activo['tipo'] = 'Teclado'
                while True:
                    try:
                        codCampus = int(input('Ingrese el codigo (solo parte númerica) del activo a registrar: ')) #Se recibe la parte númerica del codigo
                        activo['codigo'] = f'TE{codCampus}' #Agrega automaticamente el codigo "TE" y se le suma el codigo ingresado
                        codCampus = f'TE{codCampus}' #Guarda el codigo en una variable 
                        break
                    except:
                        print('Codigo invalido, vuelva a intentarlo')
                        scr.pause_screen()   
            if tipo == '4':
                activo['tipo'] = 'Monitor'
                while True:
                    try:
                        codCampus = int(input('Ingrese el codigo (solo parte númerica) del activo a registrar: ')) #Se recibe la parte númerica del codigo 
                        activo['codigo'] = f'MON{codCampus}' #Agrega automaticamente el codigo "MON" y se le suma el código ingresado
                        codCampus = f'MON{codCampus}' #Guarda el codigo en una variable 
                        break
                    except:
                        print('Codigo invalido, vuelva a intentarlo')
                        scr.pause_screen()
            
            if codCampus in filedata.keys(): #Verificar si el codigo ya se encuentra registrado
                print('Este codigo ya se encuentra registrado, si desea editarlo vaya a la sección de editar activos')
                scr.pause_screen()
            else:
                break
        #Se continúan registrando los datos necesarios para los activos
        activo['nombre'] = input('Ingrese el nombre del activo: ')
        while True: #Verifica que el valor unitario sea un precio real
            try: 
                activo['valor und'] = float(input('Ingrese el valor unitario del activo: '))
                break
            except: 
                print('Por favor digite un valor válido')
                scr.pause_screen()
        while True:
            try:
                scr.clean_screen()
                activo['nro serial'] = int(input('Ingrese el número serial del activo: '))
                break
            except: 
                print('Número invalido, vuelva a intentarlo')
                scr.pause_screen()
        new_code = activo['codigo']
        filedata.update({new_code : activo}) #Actualiza el filedata con el contenido dado
        file.update_file('activos.json', filedata) #Actualiza el archivo json con el nuevo activo
        #Bucle para decidir si se agrega otro activo o no 
        while True:
            scr.clean_screen()
            yes_or_not = input('¿Desea registrar otro activo? s(sí) -- ENTER(no): ')
            if yes_or_not == ('s' or 'S'):
                break
            elif yes_or_not == '':
                is_add_active = False
                break

#Función para modificar el contenido del archivo de activos.json
def modifyActi():
    modify_running = True
    while modify_running:
        scr.clean_screen()
        file.check_file('activos.json') #Chequea si el archivo existe y si no lo crea
        filedata = file.read_file('activos.json') #Carga el archivo a una variable python
        if len(filedata) == 0: #Revisa si hay contenido o no dentro del archivo
            print('No se encuentra ningún activo registrado')
            break
        while True:
            scr.clean_screen()
            code_to_modify = input('Ingrese el codigo del activo que desea modificar (ENTER para salir): ').upper()
            
            if code_to_modify == '':
                modify_running = False
                return
            if code_to_modify in filedata.keys(): #Si el codigo está registrado empieza el proceso
                acti_dict = filedata[code_to_modify] 
                for key, value in acti_dict.items(): 
                    scr.clean_screen()
                    #Imprime los valores que se pueden modificar y quita algunos que no.
                    if (key != 'historial') and (key != 'codigo') and (key != 'estado') and (key != 'codCampus') and (key != 'tipo'):
                        print(f'{key} : {value}')
                        print('')
                        while True:
                            modify_or_not = str(input('¿Desea modificar esta información? s(sí) - n(no): ')).upper()
                            if modify_or_not == 'S':
                                if key != 'valor und':
                                    new_value = input(f'Ingrese la nueva información para "{key}": ')
                                    acti_dict[key] = new_value
                                    break  
                                elif key == 'valor und':
                                    while True:
                                        try:
                                            new_value = float(input(f'Ingrese la nueva información para "{key}": '))
                                            break
                                        except:
                                            print('Digite un valor unitario válido')
                                            scr.clean_screen()
                                    acti_dict[key] = new_value
                                    break
                            
                            elif modify_or_not == 'N':
                                break
                break                
            else:
                print('El codigo no se encuentra registrado')
                scr.pause_screen()  
        file.update_file('activos.json', filedata)  
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

#Función para borrar un activo
def delActi():
    isfind = True
    del_acti = True
    while del_acti:
        scr.clean_screen()
        file.check_file('activos.json')
        filedata = file.read_file('activos.json')  
        if len(filedata) == 0: #Si no hay activos registrados no entra al proceso de eliminación
            print('No hay activos registrados')
            scr.pause_screen()
            del_acti = False
            break
        while True:
            scr.clean_screen()   
            code_to_del = input('Ingrese el codigo del activo que desea eliminar (ENTER para salir): ').upper()
            if code_to_del == '':
                return  
            if code_to_del in filedata.keys():
                for key, value in filedata[code_to_del].items():
                    if filedata[code_to_del]['estado'] == '0':
                        if key == 'nombre' or key == 'tipo' or key == 'estado':
                            print(f'{key} : {value}')
                            isfind = False
                if isfind == True:
                    print('El activo no se puede eliminar porque se encuentra asignado')
                    scr.pause_screen()
                break
            else:
                print('El codigo ingresado no se encuentra registrado')
                scr.pause_screen() 
        if filedata[code_to_del]['estado'] == '0':   
            while True:
                print('')
                yes_or_not = input('Seguro que desea eliminar este activo? s(sí) - n(no): ').upper()
                if yes_or_not == 'S':
                    filedata.pop(code_to_del)
                    file.update_file('activos.json', filedata)
                    break
                elif yes_or_not == 'N':
                    break
        while True:
            scr.clean_screen()
            yes_or_not = input('¿Desea eliminar otro activo? s(sí) - n(no): ').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                del_acti = False
                break
                
#Función para buscar un activo especifico
def searchActi():
    search_running = True
    while search_running:
        scr.clean_screen()
        info = []
        kys = ['Codigo','Nombre','CodTransaccion','Formulario','Marca','Categoria','Tipo','Valor Unitario','Proveedor','Nro Serial','Resposable','Estado']
        file.check_file('activos.json')
        filedata = file.read_file('activos.json')
        while True:
            scr.clean_screen()
            code_to_search = input('Ingrese el codigo del activo a buscar (ENTER para salir): ').upper()
            if code_to_search == '':
                search_running = False
                return
            #Imprimir toda la información del codigo ingresado
            if code_to_search in filedata.keys(): #Si el codigo está registrado empieza el proceso
                for key, value in filedata[code_to_search].items(): 
                    if key != 'historial':
                        value = str(value)
                        info.append([value])
                print(tabulate([info], headers=kys, tablefmt='fancy_grid'))
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

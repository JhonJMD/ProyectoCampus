import jsonfiles as file



#Función para agregar el contenido al diccionario de activos en el archivo json 

def añadir_activo(): 

    is_add_active = True
    while is_add_active: 

        file.screen.clean_screen()

        file.check_file('activos.json')
        filedata = file.read_file('activos.json')
        activo =  {
                        'codCampus' : '',
                        'nombre' : '',
                        'codTrans' : '327',
                        'nroFormu' : '966217823',
                        'marca' : 'Compumax',
                        'categoria ' : 'Equipo de computo',
                        'tipo' : '',
                        'valor und' : 0.0,
                        'proveedor' : 'Compumax',
                        'nro serial' : '',
                        'empresaRes' : 'CampusLands',
                        'estado' : '0',
                        'histActivo' : {}
                        
        }

        codCampus = input('Ingrese el codigo del activo a registrar: ')
        
       
        if codCampus in filedata.keys():
            print('Este codigo ya se encuentra registrado, si desea editarlo vaya a la sección de editar activos')
            file.screen.pause_screen()
            
    
        else: 
                  
            activo['codCampus'] = codCampus
            activo['nombre'] = input('Ingrese el nombre del activo: ')
            activo['tipo'] = input('Ingrese el tipo de activo (cpu, mouse, teclado, monitor): ')
            while True: 
                try: 
                    activo['valor und'] = float(input('Ingrese el valor unitario del activo: '))
                    break
                except: 
                    print('Por favor digite un valor válido')
                    file.screen.pause_screen()


            activo['nro serial'] = input('Ingrese el número serial del activo: ')

            filedata.update({codCampus : activo})

            file.update_file('activos.json', filedata)
            

        while True:
            file.screen.clean_screen()
            yes_or_not = input('¿Desea registrar otro activo? s(sí) -- ENTER(no): ')
            if yes_or_not == ('s' or 'S'):
                break
            elif yes_or_not == '':
                is_add_active = False
                break
        



    


añadir_activo()







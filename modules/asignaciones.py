import modules.jsonfiles as file
import modules.screen as scr



#Función para crear asignaciones
def createAsig():
    dd = ''
    mm = ''
    yy = ''
    create_asig = True
    while create_asig:
        scr.clean_screen()
        file.check_file('asignaciones.json')
        asigdata = file.read_file('asignaciones.json')
        personadata = file.read_file('personal.json')
        activdata = file.read_file('activos.json')
        asignacion = {
            'nro asignacion' : '',
            'fecha asignacion' : (),
            'tipo asignacion' : '',
            'asignado a' : '',
            'activo/s asignado' : []
        }
        asignacion['nro asignacion'] = input('Ingrese el número de asignación (Enter para salir): ')
        if asignacion['nro asignacion'] == '':
            return
        print('A continuación va a agregar la fecha de asignacion')
        scr.pause_screen()
        while True:
            try:
                scr.clean_screen()
                dd = int(input('Ingrese el día de asignación: '))
                if dd in range(31):
                    break
                else:
                    print('Por favor ingrese un día válido')
                    scr.pause_screen()
            except:
                print('Por favor ingrese un día válido')
                scr.pause_screen()
        while True:
            try:
                scr.clean_screen()
                mm = int(input('Ingrese el mes de asignación: '))
                if mm in range(12):
                    break
                else:
                    print('Por favor ingrese un mes válido')
                    scr.pause_screen()
            except:
                print('Por favor ingrese un mes válido')
                scr.pause_screen()
        while True:
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
        asignacion['fecha asignación'] = f'{dd}/{mm}/{yy}'
        while True:
            scr.clean_screen()
            tipo = input('Ingrese "P" si el tipo de asignación es a persona o "Z" si es a una zona: ').upper()
            if tipo == 'P':
                asignacion['tipo asignacion'] = 'Persona'
                break
            elif tipo == 'Z':
                asignacion['tipo asignacion'] = 'Zona'
                break
            else:
                print('Por favor ingrese un dato válido ("P" o "Z")')
        if tipo == 'P':
            add_person = True
            while add_person:  
                id = input('Ingres el ID de la persona a la que se asigna el activo: ')

def searchAsig():
    pass

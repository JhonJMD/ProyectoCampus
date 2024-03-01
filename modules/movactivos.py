import modules.jsonfiles as file 
import modules.screen as scr


def returnActi():
    return_acti = True
    while return_acti:
        file.check_file('activos.json')
        acti_data = file.read_file('activos.json')
        persona_data = file.read_file('personal.json')
        asig_data = file.read_file('asignaciones.json')
        while True:
            scr.clean_screen()
            code_to_return = input('Ingrese el codigo del activo que desea retornar: ')
            state = acti_data[code_to_return]['estado'] 
            if code_to_return not in acti_data.keys():
                print('El activo no se encuentra registrado, por favor verifique en la sección de activos del menú principal') 
                scr.pause_screen()           
                break
            

        

def cancelActi():
    pass

def changeAsig():
    pass

def sendWarran():
    pass

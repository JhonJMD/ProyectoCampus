
import os 
import json

BASE = 'data/'


#Chequear si el archivo json existe y si no existe lo crea
#Recibe: el nombre del archivo

def check_file(file : str): 

    if not os.path.isfile(BASE+file):

        with open(BASE+file, 'w') as create_file:
            json.dump({}, create_file, indent = 2)
    
    else: 
        pass


#Lee el archivo y lo carga a una variable dada en otra función
#Recibe: Nombre del archivo
#Retorna: El contenido del archivo cargado
    
def read_file(file : str):
    with open(BASE+file, 'r') as read_file:
        return json.load(read_file)
    
#Actualiza el archivo con el contenido dado
#Recibe: Nombre del archivo, contenido a actualizar

def update_file(file : str, contenido):
    with open (BASE+file, 'w+') as update_file:
        json.dump(contenido, update_file, indent = 2)


#Función para preguntar si desea seguir la ejecución de una función o salir 
#Recibe: La pregunta que se desea hacer en forma de variable
#        el nombre del loop que desea terminar 
    
def quit_loop(pregunta : str, nombre_bucle : bool):
     while True:
        yes_or_not = input(pregunta).upper()
        if yes_or_not == 'S':
            break
        elif yes_or_not == 'N':
            nombre_bucle = False
            break
        

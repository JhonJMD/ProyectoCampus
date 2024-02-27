import os 
import sys 


#Limpiar pantalla según el sistema operativo

def clean_screen():
    if sys.platform == 'windows':
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')


#Pausar pantalla según el sistema operativo
        
def pause_screen():
    if sys.platform == 'windows':
        os.system('pause')

    elif sys.platform == 'linux':
        input('Presiona cualquier tecla para continuar...')

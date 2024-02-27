import os 
import sys 


#Limpiar pantalla según el sistema operativo

def clean_screen():
    if sys.system == 'Windows':
        os.system('cls')
    elif sys.system == 'Linux':
        os.system('clear')


#Pausar pantalla según el sistema operativo
        
def pause_screen():
    if sys.system == 'Windows':
        os.system('pause')

    elif sys.system == 'Linux':
        input('Presiona cualquier tecla para continuar...')


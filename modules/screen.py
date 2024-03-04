import os 
import sys 

#Limpiar pantalla según el sistema operativo
def clean_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

#Pausar pantalla según el sistema operativo        
def pause_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        input("Presione una tecla para continuar...")
    else:
        os.system("pause")

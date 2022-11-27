import sys
from collections import *

print("""
***************************************************
            ___  ___ _____  _   _  _   _
            |  \/  ||  ___|| \ | || | | |
            | .  . || |__  |  \| || | | |
            | |\/| ||  __| | . ` || | | |
            | |  | || |___ | |\  || |_| |
            \_|  |_/\____/ \_| \_/ \___/
***************************************************
        """)

persona = deque()
vehiculo = []
parqueos = []
servicioCompleto = ["Car Wash","Baño","Aspirado"]
servicios2 = ["Car Wash","Baño"]
servicios3 = ["Car Wash","Aspirado"]


N1 = {'Ubicacion':'Norte', 'capacidad de vehiculos':150, 'servicios incluidos': servicios2}
N2 = {'Ubicacion':'Norte', 'capacidad de vehiculos':620 , 'servicios incluidos': servicioCompleto}
N3 = {'Ubicacion':'Norte', 'capacidad de vehiculos':250, 'servicios incluidos': 'Car Wash'}
N4 = {'Ubicacion':'Norte', 'capacidad de vehiculos':75,'servicios incluidos': 'Baño' }

S1 = {'Ubicacion':'Sur','capacidad de vehiculos':250,'servicios incluidos': 'Car Wash' }
S2 = {'Ubicacion':'Sur','capacidad de vehiculos':400, 'servicios incluidos':servicioCompleto}
S3 = {'Ubicacion':'Sur','capacidad de vehiculos':300, 'servicios incluidos':servicios3}
S4 = {'Ubicacion':'Sur','capacidad de vehiculos':125,'servicios incluidos': 'Baño'}

E1 = {'Ubicacion':'Este','capacidad de vehiculos':510, 'servicios incluidos': servicios3}
E2 = {'Ubicacion':'Este','capacidad de vehiculos':600, 'servicios incluidos':servicioCompleto}
E3 = {'Ubicacion':'Este','capacidad de vehiculos':300, 'servicios incluidos': 'Car Wash'}
E4 = {'Ubicacion':'Este','capacidad de vehiculos':75, 'servicios incluidos':'Baño'}

O1 = {'Ubicacion':'Oeste','capacidad de vehiculos':140, 'servicios incluidos': 'Baño'}
O2 = {'Ubicacion':'Oeste','capacidad de vehiculos':200, 'servicios incluidos': 'Car Wash'}
O3 = {'Ubicacion':'Oeste','capacidad de vehiculos':450, 'servicios incluidos': servicios2}
O4 = {'Ubicacion':'Oeste','capacidad de vehiculos':600, 'servicios incluidos':servicioCompleto}

while True:
    print("""
****************************seleccione un accion
1..........................cargar data
2..........................iniciar aplicacion
3...........................Salir
************************************************""")
    opcion = int(input())
    if opcion == 1:
        print("cargando formulario:")
    elif opcion == 2:
        print("cargando aplicacion:")
        print(N1)
        print(S2)
        print(E3)
        print(O1)
    elif opcion == 3:
        print("Adios...")
        break;
    else: print("error: Comando desconocido")
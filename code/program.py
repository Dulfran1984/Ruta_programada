list_programacion = []
list_rutas = []
import os
def fnt_limpiar():
    os.system('cls')
    print('Nombre del programa: Gestión de rutas')
    print('Autor: Dulfran Montaño')
    print('Año: 2024 -1')
    print('Universidad Católica Luis Amigó\n')
def fnt_agregar_ruta():
    fnt_limpiar()
    print('\n<<< AGREGAR NUEVA RUTA >>>\n')
    cod = input('CÓDIGO:  ')
    nombre = input('NOMBRE:  ')
    descripcion = input('DESCRIPCIÓN:  ')
    r = cod + ' ' + nombre + ' ' + descripcion
    list_rutas.append(r)
    input('\nRuta registrada con éxito <ENTER>')
sw2 = True
def fnt_menu_rutas():
    global sw2
    while sw2 == True:
        fnt_limpiar()
        opcion_r = input('<< MENÚ RUTAS >>\n1. AGREGAR\n2. CONSULTAR\n3. SALIR\n-> ')
        if opcion_r == '1':
            fnt_agregar_ruta()
        if opcion_r == '3':
            sw2 = False
    
global sw
sw = True
while sw == True:
    fnt_limpiar()
    opcionStr = input('<< MENÚ PRINCIPAL >>\n1. RUTAS\n2. ENVÍOS\n3. SALIR\n-> ')
    if opcionStr == '1':
        fnt_menu_rutas()
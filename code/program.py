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
def fnt_consultar_rutas():
    fnt_limpiar()
    print('\n<<< CONSULTAR RUTAS >>>\n')
    if len(list_rutas) == 0:
        print('\nNo hay rutas registradas')
    else:
        for i in range(len(list_rutas)):
            print(list_rutas[i])
    input('\nFin del registro <ENTER>')
sw2 = True
def fnt_menu_rutas():
    global sw2
    while sw2 == True:
        fnt_limpiar()
        opcion_r = input('<< MENÚ RUTAS >>\n1. AGREGAR\n2. CONSULTAR\n3. SALIR\n-> ')
        if opcion_r == '1':
            fnt_agregar_ruta()
        if opcion_r == '2':
            fnt_consultar_rutas()
        if opcion_r == '3':
            sw2 = False
sw3 = True
def fnt_menu_envios():
    global sw3
    while sw3 == True:
        fnt_limpiar()
        opcion3 = input('<< MENÚ ENVÍOS >>\n1. AGREGAR\n2. CONSULTAR\n3. SALIR\n-> ')
        if opcion3 == '1':
            fnt_agregar_envio()
        if opcion3 == '2':
            fnt_consultar_envios()
        if opcion3 == '3':
            sw3 = False
def fnt_consultar_envios():
    fnt_limpiar()
    print('\n<<< CONSULTAR ENVÍOS >>>\n')
    if len(list_programacion) == 0:
        print('\nNo hay envíos registrados')
    else:
        for i in range(len(list_programacion)):
            print(list_programacion[i])
    input('\nFin del registro <ENTER>')
def fnt_agregar_envio():
    fnt_limpiar()
    print('<<< RUTAS DISPONIBLES >>>\n')
    for i in range(len(list_rutas)):
        print(list_rutas[i])
    print('\n<<< DATOS DEL ENVÍO >>>\n')
    n_envio = input('NÚMERO DE ENVÍO:  ')
    nombre = input('NOMBRE CLIENTE:  ')
    valor = input('VALOR $  ')
    peso  = input('PESO DE LA MERCANCÍA:  ')
    ruta = input('RUTA:  ')
    r = 'ENVIO No. ' + n_envio + ' - CLIENTE: ' + nombre + '- VALOR $  '+ valor +  '- PESO: ' + peso + ' - RUTA: ' + ruta
    list_programacion.append(r)
global sw
sw = True
while sw == True:
    fnt_limpiar()
    opcionStr = input('<< MENÚ PRINCIPAL >>\n1. RUTAS\n2. ENVÍOS\n3. SALIR\n-> ')
    if opcionStr == '1':
        fnt_menu_rutas()
    if opcionStr == '2':
        fnt_menu_envios()
    if opcionStr == '3':
        sw = False
        print('Fin del programa')
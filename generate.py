import csv
import uuid
from datetime import datetime, timedelta


datos = [['numeroControl', 'codigoGeneracion', 'fecEmi', 'horEmi', 'codigoGeneracionRecepcion', 'version', 'tipoDTE']]
dict_DTE = { '1' : { 'tipo': 'Factura', 'tipoDTE' : 1, 'version': 1 } }
filename_csv = 'datos.csv'
id_minimo = 0
id_maximo = 0
control  = 0


def menu():
    print('01 Factura')
    print('03 Comprobante Credito Fiscal')
    print('05 Nota de Credito')
    print('06 Nota de Debito')
    print('11 Factura de Exportación')
    print('14 Factura de Sujeto Excluido')


def tipo_DTE(opcion):
    
    
    if opcion == 1:
        version = 1
        tipoDTE = 1
    elif opcion == 3:
        version = 3
        tipoDTE = 3
    elif opcion == 5:
        version = 3
        tipoDTE = 5
    elif opcion == 6:
        version = 3
        tipoDTE = 6
    elif opcion == 11:
        version = 1
        tipoDTE = 11
    elif opcion == 6:
        version = 1
        tipoDTE = 14
    else:
        print("Ingrese un parametro correcto")
        exit()
  
    return version, tipoDTE


def fecha_actual():
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")    
    
    return fecha_formateada


def hora_actual_mas_cinco():
    hora_actual = datetime.now().time()
    hora_adelantada = (datetime.min + timedelta(hours=hora_actual.hour, minutes=hora_actual.minute + 5)).time()
    hora_formateada = hora_adelantada.strftime("%H:%M:%S")
    
    return hora_formateada


def generar_uuid():
    return str(uuid.uuid4())


def guardar_csv(archivo_csv):
    # Abrir el archivo CSV en modo escritura
    with open(archivo_csv, 'w', newline='') as archivo:
        # Crear un objeto escritor CSV
        escritor_csv = csv.writer(archivo)

        # Escribir los datos en el archivo CSV
        escritor_csv.writerows(datos)



menu()

opcion = int(input("Ingrese la opción: "))
control = int(input("Ingrese el número de control: "))
id_minimo = int(input("Limite mínimo del loop: "))
id_maximo  = int(input("Limite máximo del loop: "))



version, tipoDTE = tipo_DTE(opcion)
numero_control_parcial = "DTE-"+tipoDTE+"-20000000-000000000000"
fecha = fecha_actual()
hora = hora_actual_mas_cinco()


for item in range(id_minimo, id_maximo):
    numero_control = ""
    uuid_generado = generar_uuid().upper()
    uuid_generado_recepcion = generar_uuid().upper()
    control += 1
    numero_control = numero_control_parcial + str(control)
    datos.append([numero_control, uuid_generado, fecha, hora, uuid_generado_recepcion, version, tipoDTE])
    

guardar_csv(filename_csv)


print(f'Se ha creado el archivo CSV "{filename_csv}" con éxito.')   
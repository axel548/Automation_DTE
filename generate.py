import csv
import uuid
from datetime import datetime, timedelta


datos = [['numeroControl', 'codigoGeneracion', 'fecEmi', 'horEmi', 'codigoGeneracionRecepcion', 'version', 'tipoDTE']]
dict_DTE = { 
            1 : { 'no': 1, 'tipo': 'Factura', 'dte' : 1, 'version': 1 },
            3 : { 'no': 3, 'tipo': 'Comprobante Credito Fiscal', 'dte' : 3, 'version': 3 },
            5 : { 'no': 5, 'tipo': 'Nota de Credito', 'dte' : 5, 'version': 3 },
            6 : { 'no': 6, 'tipo': 'Nota de Debito', 'dte' : 6, 'version': 3 },
            11 : { 'no': 11, 'tipo': 'Factura de Exportación', 'dte' :11, 'version': 1 },
            14 : { 'no': 14, 'tipo': 'Factura de Sujeto Excluido', 'dte' : 14, 'version': 1 },
            }
filename_csv = 'datos.csv'
id_minimo = 0
id_maximo = 0
control  = 0

 
def menu(arreglo):
    for item in arreglo:
        print("%d %s" %(arreglo[item]['no'], arreglo[item]['tipo']))

    

def tipo_DTE(opcion):
    dte = dict_DTE[opcion]
    return dte['version'], dte['dte']


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



menu(dict_DTE)

opcion = int(input("Ingrese la opción: "))
control = int(input("Ingrese el número de control: "))
id_maximo  = int(input("Limite máximo del loop: "))


version, tipoDTE = tipo_DTE(opcion)
if len(str(tipoDTE)) > 2:
  tipoDTE = str(tipoDTE)
else:
  tipoDTE = "0" + str(tipoDTE)

numero_control_parcial = "DTE-"+tipoDTE+"-20000000-000000000000"
fecha = fecha_actual()
hora = hora_actual_mas_cinco()


for item in range(1, id_maximo):
    numero_control = ""
    uuid_generado = generar_uuid().upper()
    uuid_generado_recepcion = generar_uuid().upper()
    control += 1
    numero_control = numero_control_parcial + str(control)
    datos.append([numero_control, uuid_generado, fecha, hora, uuid_generado_recepcion, version, tipoDTE])
    

guardar_csv(filename_csv)


print(f'Se ha creado el archivo CSV "{filename_csv}" con éxito.')   
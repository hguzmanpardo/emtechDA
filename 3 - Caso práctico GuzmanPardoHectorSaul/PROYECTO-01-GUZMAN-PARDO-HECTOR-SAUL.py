#LIBRERIAS IMPORTADAS PARA FUNCIONES DE LIMPIEZA DE PANTALLA Y DE MANEJO DE ARCHIVOS CSV
import csv
import os
from collections import Counter

os.system("clear")
print("### Synergy Logistics ###")

### INICIO DEL PROGRAMA CON FUNCIÓN CÍCLICA QUE PERMITA CONTINUAR O TERMINARLO ###
while True:
######## FUNCIONES ########
  def filtrado():
    
### EJERCICIO DE CASO PRÁCTICO ###
    
    with open('synergy_logistics_database.csv','r',encoding='utf-8-sig') as archivo:
      lector = csv.reader(archivo)

## LISTAS CREADAS PARA AGRUPAR DATOS DE EXPORTACIÓN E IMPORTACIÓN ##
      grupoe=[]
      grupoi=[]

## BÚSQUEDA EN LISTA QUE SEPARAN LOS DATOS SEGUN SEA IMPORTACIÓN O EXPORTACIÓN ##
      for row in lector:
        if (row[1]=="Imports"):
          grupoi.append(row[2]+"-"+row[3])
        elif(row[1]=="Exports"):
          grupoe.append(row[2]+"-"+row[3])
          
## ALMACENAMIENTO DE ELEMENTOS ÚNICOS DE LOS REGISTROS ##        
      rutasi=Counter(grupoi).keys()
      rutase=Counter(grupoe).keys()

## LISTAS QUE CONTABILIZARÁN LAS RUTAS MAS UTILIZADAS DEL PROCESO ANTERIOR##
      cuentaRutasi=[]
      cuentaRutase=[]

## RECORRIDO Y GUARDADO DE LA LISTA DE RUTAS PARA CONTABILIZAR CUALES SON LAS RUTAS MAS UTILIZADAS DE IMPORTACIÓN Y EXPORTACIÓN ##
      for x in rutasi:
        numero=grupoi.count(x)
        cuentaRutasi.append([x, numero])
      for y in rutase:
        numero=grupoe.count(y)
        cuentaRutase.append([y, numero])
        
## ORDENAMIENTO DE RUTAS PARA LA IMPRESIÓN DE MAYOR A MENOR ## 
      cuentaRutasi= sorted(cuentaRutasi, key=lambda x: x[1], reverse=True)
      cuentaRutase= sorted(cuentaRutase, key=lambda x: x[1], reverse=True)

## IMPRESIÓN DE LAS 10 RUTAS MAS USADAS PARA IMPORTACIONES ##
      os.system("clear")
      print("### Synergy Logistics ###\n")
      print("RUTAS CON MAYOR CANTIDAD DE IMPORTACIONES:")
      for x in range(0,10):
        print(cuentaRutasi[x])

## IMPRESIÓN DE LAS 10 RUTAS MAS USADAS PARA EXPORTACIONES ##
      print("\n RUTAS CON MAYOR CANTIDAD DE EXPORTACIONES:")
      for x in range(0,10):
        print(cuentaRutase[x])



## LOGIN DEL PRGRAMA CON VALIDACION DE USUARIO Y CLAVE ###
  os.system("clear")
  u = input ("Ingrese usuario: ")
  p = input ("Ingrese contraseña: ")
  if u == "admin" and p == "123":
    print("Acceso correcto\n")
    
### FUNCION QUE MANDA LLAMAR AL CASO PRACTICO NUM 2 (FINAL) EN CASO DE SER ACEPTADAS LAS CREDENCIALES ###
    filtrado()

    
##VALIDACIÓN DE USUARIO INCORRECTO##      
  elif u != "admin":
      os.system("clear") # LIMPIA PANTALLA #
      print ("Usuario no existe")
    
##VALIDACIÓN DE CLAVE INCORRECTA##
  elif p != "123":
      os.system("clear") # LIMPIA PANTALLA #
      print ("Contraseña incorrecta")

##VALIDACIÓN PARA CONTINUAR O TERMINAR EL PROGRAMA    
  resp_terminar = input ("\nDesea terminar el programa: si/no: ")
  resp_terminar_mayus=resp_terminar.upper() # CONVIERTE LA RESPUESTA SIEMPRE A MAYUSCULA #
  if resp_terminar_mayus == "SI":
    os.system("clear") # LIMPIA PANTALLA #
    quit() # TERMINA EL PROGRAMA #
    
    
      
   

    
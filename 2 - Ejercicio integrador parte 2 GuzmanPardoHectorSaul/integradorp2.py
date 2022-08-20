import os
import csv

### FUNCIONES ###
def opcion1():
    os.system("clear")
    print("Opción 1 elegida: \n")
      
    with open("EjercicioIntegrador2DB.csv", "r",encoding='utf-8-sig') as archivo_csv:
        lector = csv.reader(archivo_csv)
               
        lista = []
        for reg in lector:
          if reg[3] == "Pasajeros":
            continue
          pasajeros = float(reg[3])
          lista.append([reg[0], reg[1], reg[2], pasajeros, reg[4]])

        lista_ordenada = sorted(lista, key=lambda pas: pas[3], reverse=True)
        i=0
        print("\n#### Los 5 aeropuertos que tienen mayor cantidad de pasajeros que desean viajar a Sinaloa son: ####\n")
        for i in range(0,5):
          print(lista_ordenada[i])
          i+=1
  
    input ("\nPresione Enter para continuar")
##############################################################


def opcion2():
    os.system("clear")
    print("Opción 2 elegida: \n")
    
    with open("EjercicioIntegrador2DB.csv", "r",encoding='utf-8-sig') as archivo_csv:
        lector = csv.reader(archivo_csv)
               
        lista = []
        cant_pasajeros = []
        cant_reg = 0
        for reg in lector:
          if reg[3] == "Pasajeros":
            continue
          pasajeros = float(reg[3])
          lista.append([reg[0], reg[1], reg[2], pasajeros, reg[4]])
          cant_pasajeros.append(pasajeros)
          total_pasajeros=sum(cant_pasajeros)
          cant_reg+=1
          
          
    print ("El total de registros son: ",cant_reg)
    print ("El total de pasajeros de todos los aeropuertos es: ",total_pasajeros)
    prom_pas  = total_pasajeros/cant_reg
    print ("\nEl promedio de pasajeros de todos los aeropuertos es: ",round(prom_pas,2))
    input ("\nPresione Enter para continuar")
#######################################################################
    


def opcion3():
    os.system("clear")
    print("Opción 3 elegida: \n")
    with open("EjercicioIntegrador2DB.csv", "r",encoding='utf-8-sig') as archivo_csv:
        lector = csv.reader(archivo_csv)
               
        lista = []
        for reg in lector:
          if reg[3] == "Pasajeros":
            continue
          pasajeros = float(reg[3])
          lista.append([reg[0], reg[1], reg[2], pasajeros, reg[4]])

        lista_ordenada = sorted(lista, key=lambda pas: pas[3], reverse=False)
        i=0
        print("Los 5 aeropuertos con menos vuelos hacia Sinaloa: \n")
        for i in range(0,5):
          print(lista_ordenada[i])
          i+=1
          
    input ("\nPresione Enter para continuar")
#######################################################################


def opcion4():
    os.system("clear")
    print("Opción 3 elegida: \n")
    print("Saliendo...\n\n")
    quit()
#######################################################################



while True:
    os.system("clear")
    print("\n### Bienvenido a FlyUs ###\n")
    #### MENU ####
    print("#### MENU ####\n")
    print(
        "1. Los 5 aeropuertos con mayor cantidad de pasajeros que desean viajar a Sinaloa"
    )
    print("2. Promedio de pasajeros de todos los aeropuertos")
    print("3. Los 5 aeropuertos con menos vuelos hacia Sinaloa")
    print("4. Salir")
    opcion = input("\nElija un número de las opciones anteriores: \n")
    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "4":
        opcion4()
#######################################################################
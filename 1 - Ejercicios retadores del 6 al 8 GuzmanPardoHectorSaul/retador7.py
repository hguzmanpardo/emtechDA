print("Bienvenido a FlyUs")
repetir = True
pasajeros=[]
dest1 = 0
dest2 = 0
dest3 = 0
suma_edad1=0
suma_edad2=0
suma_edad3=0
prom1=0
prom2=0
prom3=0
lista_clientes=0
lista_preferentes = 0
eleccion=[]

todos_clientes={}
clientes_preferentes={}

while repetir == True:

  ################MENÚ DE OPCIONES###########
  opcion = input("Elija una opción:\n(1) Añadir cliente\n(2) Listar todos los clientes\n(3) Listar clientes preferentes\n(4) Salir\n")
  if opcion == "1":
    id = input("ID del INE/IFE: ")
    nombre = input("Cual es su nombre: ")

    edad = input("Edad: ")
    edad=int(edad)
    destino = input("Tecleé Destino (|BJX|GDL|JAL|): ")
    destino_mayus = destino.upper()
    detalle_destino=[["BJX",dest1],["GDL",dest2],["JAL",dest3]]
    preferente = input("Cliente Preferente\n(si) SI\n(no) NO\n")
    prefer_mayus = preferente.upper()

    
    ######### GUARDA LOS CLIENTES PREFERENTES ##########
    if prefer_mayus == "SI":
      if lista_preferentes == "0":
        lista_preferentes+=1
        clientes_preferentes[lista_preferentes] = (id,nombre,edad,destino_mayus,prefer_mayus)
      else:
        lista_preferentes+=1
        clientes_preferentes[lista_clientes]= (id,nombre,edad,destino_mayus,prefer_mayus)

      
   ######## CONTABILIZA LOS DESTINOS SELECCIONADOS ######### 
    if destino_mayus == "BJX":
      dest1 += 1
      suma_edad1 += edad
      detalle_destino[0]=["BJX",dest1]
    elif destino_mayus == "GDL":
      dest2 += 1
      suma_edad2 += edad
      detalle_destino[1]=["GDL",dest2]
    elif destino_mayus == "JAL":
      dest3 += 1
      suma_edad3 += edad
      detalle_destino[2]=["JAL",dest3]
    else:
      print ("---Ingrese un destino válido---")



      
    ####### REGISTRA A TODOS LOS CLIENTES ##########
    if lista_clientes == "0":
      lista_clientes+=1
      todos_clientes[lista_clientes] = (id,nombre,edad,destino_mayus,prefer_mayus)
    else:
      lista_clientes+=1
      todos_clientes[lista_clientes]= (id,nombre,edad,destino_mayus,prefer_mayus)
   
    print("\n")
    repetir= True

    
  elif opcion == "2":
    print ("Clientes registrados: ")
    print (todos_clientes)
    print ()

  elif opcion == "3":
    print ("Clientes preferentes")
    print(clientes_preferentes)
    print("\n")
    
  elif opcion == "4":
    print("Saliendo...")
    quit()

   
    
if (suma_edad1!=0):
  prom1=suma_edad1/dest1
if (suma_edad2!=0):
  prom2=suma_edad2/dest2 
if (suma_edad3!=0):
  prom3=suma_edad3/dest3  
prom_edad=[["BJX",prom1],["GDL",prom2],["JAL",prom3]]
print ("\n Destinos y número de pasajeros: \n")
print (detalle_destino)
print ("\n Destinos y promedios de edad de pasajeros: \n")
print (prom_edad)


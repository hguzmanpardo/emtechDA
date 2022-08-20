print("Bienvenido a FlyUs")
nombre = True
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
eleccion=[]
while nombre == True:
  nombre = input("Cual es su nombre: ")
  if nombre == "x" or nombre == "X":
    nombre = False
  else:
    edad = input("Edad: ")
    edad=int(edad)
    destino = input("Tecleé Destino (|BJX|GDL|JAL|): ")
    detalle_destino=[["BJX",dest1],["GDL",dest2],["JAL",dest3]]
    if destino == "BJX":
      dest1 += 1
      suma_edad1 += edad
      detalle_destino[0]=["BJX",dest1]
    elif destino == "GDL":
      dest2 += 1
      suma_edad2 += edad
      detalle_destino[1]=["GDL",dest2]
    elif destino == "JAL":
      dest3 += 1
      suma_edad3 += edad
      detalle_destino[2]=["JAL",dest3]
    else:
      print ("---Ingrese un destino válido---")
    
    
    nombre = True
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


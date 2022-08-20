print("### Bienvenido a FlyUs ###\n")

### DICCIONARIO PREDEDIFINIDO ###
clientes = {
    45471: ["Luis Perez", 45, "BJX", "SI"],
    8944411: ["Fernanda Garcia", 25, "JAL", "SI"],
    15223: ["Alejandra Ortiz", 33, "JDL", "NO"]
}




### FUNCIONES ###
def agregarClientes():
    print("\n### Agregar cliente ###\n")
    ine = input("ID del INE/IFE: ")
    nombre = input("Cual es su nombre: ")
    edad = input("Edad: ")
    edad = int(edad)
    destino = input("Tecleé Destino (|BJX|GDL|JAL|): ")
    destino_mayus = destino.upper()
    preferente = input("Cliente Preferente\n(si) SI\n(no) NO\n")
    prefer_mayus = preferente.upper()
    ### LINEA QUE GUARDA LOS DATOS EN EL DICCIONARIO ###
    clientes[ine] = [nombre, edad, destino_mayus, prefer_mayus]
    print(clientes)


def mostrarClientesTodos():
    print("\n## Mostrar todos los clientes ##")
    print(clientes)
    print("\n")
  
def mostrarClientesPreferentes():
    lista = list(clientes.values())
    print("##Listado de clientes preferentes ##")
    for dato in lista:
      if (dato[3] == "SI"):
        print (dato)

def eliminarClienteid():
    print("\n## Eliminar cliente por ID/INE ##")
    delid = int(input("Escriba el INE del usuario que deseé eliminar: "))
    del clientes[delid]
    print("Usuario ", delid, "eliminado")
    print(clientes)
    print("\n")

def edadpromedioclientes():
  suma_edades = 0
  cont=0
  lst = list(clientes.values())
  for dato in lst:
    edadx = int(dato[1])
    suma_edades += edadx
    cont += 1
  prom_edades = suma_edades / cont
  print("\n## Promedio de edad de clientes: ##")
  print(prom_edades)
  print("\n")

def edadpromedioclientesprefer():
  suma_edades = 0
  cont=0
  lst = list(clientes.values())
  for dato in lst:
    if (dato[3] == "SI"):
      edadx = int(dato[1])
      suma_edades += edadx
      cont += 1
  prom_edades = suma_edades / cont
  print("\n## Promedio de edad de clientes preferentes: ##")
  print(prom_edades)
  print("\n")


#### MENU PRINCIPAL ####
while True:
    opcion = input(
        "Elija una opción:\n(1) Añadir nuevos clientes\n(2) Listar todos los clientes\n(3) Listar clientes preferentes\n(4) Eliminar un cliente mediante ID del INE\n(5) Edad promedio de clientes \n(6) Edad promedio de clientes preferentes\n(7) Salir\n"
    )

    if opcion == "1":
        agregarClientes()
    elif opcion == "2":
        mostrarClientesTodos()
    elif opcion == "3":
        mostrarClientesPreferentes()
    elif opcion == "4":
        eliminarClienteid()
    elif opcion == "5":
        edadpromedioclientes()
    elif opcion == "6":
        edadpromedioclientesprefer()
    elif opcion == "7":
        print("Saliendo...\n\n")
        quit()

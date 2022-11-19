from pymongo import MongoClient

def getConexion():
    MONGO_URL = 'mongodb://localhost' #La ubicación de la base de datos

    client = MongoClient(MONGO_URL)

    db = client['Pruebas'] #la base de datos

    collection =db['ciudades'] #La coleccion

    return collection

def menu():
    
    return int(input("""
    ======= Registro de ciudades =======
    ======= 1.Agregar ciudad
    ======= 2.Modificar ciudad
    ======= 3.Información sobre ciudades
    ======= 4.Eliminar ciudades
    ======= 5.Salir del registro de ciudades
    Opcion:"""))

def menuModificar():
    return int(input("""
    ======= Opciones de modificación =======
    ======= 1.Nombre 
    ======= 2.Población
    ======= 3.Clima
    Opcion:"""))

def menuVer():
    return int(input("""
    ======= Opciones de modificación =======
    ======= 1.Ver todas las ciudades
    ======= 2.Ver ciudad en especifico
    ======= 3.Salir
    Opcion:"""))

def getCiudades():

    ciudades = getConexion().find()

    return ciudades


def getCiudad(nombre):

    ciudades = getConexion().find_one({'ciudad':nombre})

    return ciudades

def setCiudad(nombre,habitantes,clima):

    ciudad = getConexion().insert_one({'ciudad':nombre, 'habitantes':habitantes, 'clima': clima})
        
    return ciudad.acknowledged

def updateCiudad(nombre, habitante, climas):

    update = getConexion().update_one({'ciudad':nombre},{'$set':{'habitantes':habitante,'clima':climas}})

    return update.acknowledged

def deleteCiudad(nombre):

    delete = getConexion().delete_one({'ciudad':nombre})

    return delete.acknowledged

def verCiudades():

    ciudades = getCiudades()
    
    for ciudad in ciudades:
        
        #print(ciudad)
        print("=========== {} =========== \n Habitantes: {} \n Clima: {}".format(ciudad['ciudad'],ciudad['habitantes'],ciudad['clima']))

def verCiudad():

    nombre = input("Ingresa la ciudad:")

    ciudad = getCiudad(nombre)
    
    print("=========== {} =========== \n Habitantes: {} \n Clima: {}".format(ciudad['ciudad'],ciudad['habitantes'],ciudad['clima']))

def ingresarCiudad():

    nombre = input("Ingresar el nombre de la ciudad:")
    cantidad_habitantes = int(input("Cantidad de habitantes:"))
    lista_clima = []
    while True:

        clima = str(input("Ingresar clima:"))
        lista_clima.append(clima)

        salir = input("Ingresar otra raza (S/N):")

        if salir.lower() == "n":
            break 
    if setCiudad(nombre,cantidad_habitantes,lista_clima):
        print("\n========== Ciudad agregada exitosamente ==========")
    else:
        print("\n========== Error ==========")  

def modificarCiudad():

    nombre = input("Ingresar el nombre de la ciudad:")
    cantidad_habitantes = int(input("Cantidad de habitantes:"))
    lista_clima = []
    while True:

        clima = str(input("Ingresar clima:"))
        lista_clima.append(clima)

        salir = input("Ingresar otro clima (S/N):")

        if salir.lower() == "n":
            break 
    if updateCiudad(nombre,cantidad_habitantes,lista_clima):
        print("\n========== Ciudad actualizada exitosamente ==========")
    else:
        print("\n========== Error ==========")  
    
def main():

    op = menu()
    while(op != 5):

        if(op == 1):
            ingresarCiudad()

        if(op == 2):
            modificarCiudad()

        if(op == 3):
            
            opVer = menuVer()

            while(opVer != 3):

                if(opVer == 1):
                    verCiudades()
                
                if(opVer == 2):
                    verCiudad()

                opVer = menuVer()

            print("\t=========== Ciudad visualizada ===========")

        if(op == 4):

            print("\nElimnar ciudad")

            ciudad = input("\nIngresar el nombre de la ciudad a eliminar:")

            if deleteCiudad(ciudad):
                print("\n ========== Ciudad elimnana exitosamente ==========")
            else:
                print("========== Error ==========")

        op = menu()

    print("\t=========== Programa finalizado ===========")


if __name__ == '__main__':
    main()
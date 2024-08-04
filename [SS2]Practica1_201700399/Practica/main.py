import dataBase as etl
import queries

def menu():
    conn = etl.conexionBD()
    if conn is not None:
        while True:
            print("\n---------------------------------")
            print("|            Menu               |")
            print("--------------------------------- ")
            print("a) Borrar modelo")
            print("b) Crear modelo")
            print("c) Extraer información")
            print("d) Cargar información")
            print("e) Realizar consultas")
            print("f) Salir")
            print("\nSeleccione una opción:")

            opcion = input(">> ").lower()

            print("\n------------------------------------")
            if opcion == 'a':
                etl.borrarModelo()
                
            elif opcion == 'b':
                etl.crearModelo()
                
            elif opcion == 'c':
                ruta = input("Ingrese la ruta del archivo CSV: ")
                etl.extraerInformacion(ruta,conn)
                
            elif opcion == 'd':
                etl.cargarInformacion(conn)
                
            elif opcion == 'e':
                menuConsultas()
                
            elif opcion == 'f':
                print("Adiós...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
    else:
        print("Error al conectar a la base de datos.")
        conn.close()
        
        
def menuConsultas():
    while True:
        print("\n-----------------------------------")
        print("|             Consultas           |")
        print("-----------------------------------")
        print("1. Consulta 1")
        print("2. Consulta 2")
        print("3. Consulta 3")
        print("4. Consulta 4")
        print("5. Consulta 5")
        print("6. Consulta 6")
        print("7. Consulta 7")
        print("8. Consulta 8")
        print("9. Consulta 9")
        print("10. Consulta 10")
        print("11. Volver al menú principal")
        print("\nSeleccione una opción:")
        consulta_opcion = input(">> ").lower()

        if consulta_opcion == '1':
            print("Ejecutando consulta 1...")
            
        elif consulta_opcion == '2':
            print("Ejecutando consulta 2...")
            
        elif consulta_opcion == '3':
            print("Ejecutando consulta 3...")
            # Llamar a la función para ejecutar la consulta 3
        elif consulta_opcion == '4':
            print("Ejecutando consulta 4...")
            # Llamar a la función para ejecutar la consulta 4
        elif consulta_opcion == '5':
            print("Ejecutando consulta 5...")
            # Llamar a la función para ejecutar la consulta 5
        elif consulta_opcion == '6':
            print("Ejecutando consulta 6...")
            # Llamar a la función para ejecutar la consulta 6
        elif consulta_opcion == '7':
            print("Ejecutando consulta 7...")
            # Llamar a la función para ejecutar la consulta 7
        elif consulta_opcion == '8':
            print("Ejecutando consulta 8...")
            # Llamar a la función para ejecutar la consulta 8
        elif consulta_opcion == '9':
            print("Ejecutando consulta 9...")
            # Llamar a la función para ejecutar la consulta 9
        elif consulta_opcion == '10':
            print("Ejecutando consulta 10...")
            # Llamar a la función para ejecutar la consulta 10
        elif consulta_opcion == '11':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
if __name__ == "__main__":
    menu()

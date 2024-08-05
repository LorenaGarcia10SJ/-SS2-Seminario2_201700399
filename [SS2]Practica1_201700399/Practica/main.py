import dataBase as etl
import os

def menu():
    conn = etl.conexionBD()
    if conn is not None:
        while True:
            
            print("---------------------------------")
            print("|            Menu               |")
            print("--------------------------------- ")
            print("a. Borrar modelo")
            print("b. Crear modelo")
            print("c. Extraer información")
            print("d. Cargar información")
            print("e. Realizar consultas")
            print("f. Salir")
            print("\nSeleccione una opción:")

            opcion = input(">> ").lower()

            print("\n----------------------------------")
            if opcion == 'a':
                etl.borrarModelo()
                os.system('cls')
                print("Modelo borrado con éxito...")
                
            elif opcion == 'b':
                etl.crearModelo()
                os.system('cls')
                print("Modelo creado con éxito...")
                
            elif opcion == 'c':
                ruta = input("Ingrese la ruta del archivo CSV: ")
                etl.extraerInformacion(ruta,conn)
                os.system('cls')
                print("Información extraida con éxito...")
                
            elif opcion == 'd':
                etl.cargarInformacion(conn)
                os.system('cls')
                print("Información cargada con éxito...")
                
            elif opcion == 'e':
                os.system('cls')
                menuConsultas(conn)
                
            elif opcion == 'f':
                print("Adiós...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    else:
        print("Error al conectar a la base de datos.")
        conn.close()
        
        
def menuConsultas(conn):
    if conn is not None:
        while True:
            print("\n-----------------------------------")
            print("|             Consultas           |")
            print("-----------------------------------")
            print("1.  Consulta 1")
            print("2.  Consulta 2")
            print("3.  Consulta 3")
            print("4.  Consulta 4")
            print("5.  Consulta 5")
            print("6.  Consulta 6")
            print("7.  Consulta 7")
            print("8.  Consulta 8")
            print("9.  Consulta 9")
            print("10. Consulta 10")
            print("11. Volver ")
            
            print("\nSeleccione una opción:")
            
            opcion = input(">> ").lower()

            if opcion == '1':
                print("Consulta 1")
                ##etl.consulta1(conn)
                os.system(r'sqlcmd -S LAPTOP-VUS22HJ1 -d ProcesoETL -i "C:\Users\logas\Desktop\USAC\SEGUNDO SEMESTRE 2024\Seminario 2\Lab\-SS2-Seminario2_201700399\[SS2]Practica1_201700399\Practica\consulta1.sql"')
                os.system(r'sqlcmd -S LAPTOP-VUS22HJ1 -d ProcesoETL -i "C:\Users\logas\Desktop\USAC\SEGUNDO SEMESTRE 2024\Seminario 2\Lab\-SS2-Seminario2_201700399\[SS2]Practica1_201700399\Practica\consulta1.sql" -o "C:\Users\logas\Desktop\USAC\SEGUNDO SEMESTRE 2024\Seminario 2\Lab\-SS2-Seminario2_201700399\[SS2]Practica1_201700399\Practica\consulta1.txt"')
            elif opcion == '2':
                print("Ejecutando consulta 2...")
                
            elif opcion == '3':
                print("Ejecutando consulta 3...")

            elif opcion == '4':
                print("Ejecutando consulta 4...")

            elif opcion == '5':
                print("Ejecutando consulta 5...")

            elif opcion == '6':
                print("Ejecutando consulta 6...")

            elif opcion == '7':
                print("Ejecutando consulta 7...")

            elif opcion == '8':
                print("Ejecutando consulta 8...")

            elif opcion == '9':
                print("Ejecutando consulta 9...")

            elif opcion == '10':
                print("Ejecutando consulta 10...")
                
            elif opcion == '11':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
    else:
        print("Error al conectar a la base de datos.")
        conn.close()

if __name__ == "__main__":
    menu()

def leer_opcion():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por tipo de plan")
        print("2. Búsqueda de planes por rango de precio")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar plan")
        print("6. Salir")
        print("====================================")
        try:
            opcion = int(input("Ingrese una opcion: "))
            return
        except ValueError:
            print("Debe seleccionar una opción válida.") 

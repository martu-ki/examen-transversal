def leer_opcion():
    try:
        opcion = int(input("Ingrese opción: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Debe seleccionar una opción válida")
            return
    except ValueError:
        print("Debe seleccionar una opción válida")
        return 

def cupos_tipo(tipo, planes, inscripciones):
    tipo_norm = tipo.strip().lower()
    total_cupos = 0
    for codigo, datos in planes.items():
        if datos[1].lower() == tipo_norm:
            if codigo in inscripciones:
                total_cupos += inscripciones[codigo][1]
    print(f"El total de cupos disponibles es: {total_cupos}")

def busqueda_precio(p_min, p_max, planes, inscripciones):
    resultados = []
    for codigo, datos_ins in inscripciones.items():
        precio = datos_ins[0]
        cupos = datos_ins[1]
        if p_min <= precio <= p_max and cupos > 0:
            if codigo in planes:
                nombre_plan = planes[codigo][0]
                resultados.append(f"{nombre_plan}--{codigo}")
    if not resultados:
        print("No hay planes en ese rango de precios.")
    else:
        resultados.sort()
        print(f"Los planes encontrados son: {resultados}")

def buscar_codigo(codigo, inscripciones):
    return codigo.upper() in inscripciones

def actualizar_precio(codigo, nuevo_precio, inscripciones):
    codigo_upper = codigo.upper()
    if buscar_codigo(codigo_upper, inscripciones):
        inscripciones[codigo_upper][0] = nuevo_precio
        return True
    return False

def validar_codigo(codigo, planes):
    cod = codigo.strip()
    if not cod:
        return False
    if cod.upper() in planes:
        return False
    return True

def validar_nombre(nombre):
    return bool(nombre.strip())

def validar_tipo(tipo):
    return tipo in ['mensual', 'trimestral', 'anual']

def validar_duracion(duracion):
    return duracion > 0

def validar_piscina(opcion):
    return opcion in ['s', 'n']

def validar_clases(opcion):
    return opcion in ['s', 'n']

def validar_horario(horario):
    return bool(horario.strip())

def validar_precio(precio):
    return precio > 0

def validar_cupos(cupos):
    return cupos >= 0

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, planes, inscripciones):
    codigo_upper = codigo.upper()
    if codigo_upper in planes or codigo_upper in inscripciones:
        return False
    piscina_bool = True if acceso_piscina == 's' else False
    clases_bool = True if incluye_clases == 's' else False
    planes[codigo_upper] = [nombre, tipo, duracion, piscina_bool, clases_bool, horario]
    inscripciones[codigo_upper] = [precio, cupos]
    return True

def eliminar_plan(codigo, planes, inscripciones):
    codigo_upper = codigo.upper()
    if buscar_codigo(codigo_upper, inscripciones):
        if codigo_upper in planes:
            del planes[codigo_upper]
        del inscripciones[codigo_upper]
        return True
    return False

def programa_principal():
    planes = {
        'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
        'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
        'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
        'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
        'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
        'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
    }
    inscripciones = {
        'F001': [14990, 30],
        'F002': [22990, 10],
        'F003': [39990, 0],
        'F004': [35990, 6],
        'F005': [159990, 2],
        'F006': [18990, 15]
    }
    
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por tipo de plan")
        print("2. Búsqueda de planes por rango de precio")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar plan")
        print("6. Salir")
        print("=====================================")
        
        opc = leer_opcion()
        if opc is None:
            continue
            
        if opc == 1:
            tipo = input("Ingrese tipo de plan a consultar: ")
            cupos_tipo(tipo, planes, inscripciones)
            
        elif opc == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, planes, inscripciones)
            
        elif opc == 3:
            while True:
                cod = input("Ingrese código del plan: ")
                try:
                    n_precio = int(input("Ingrese nuevo precio: "))
                    if n_precio > 0:
                        if actualizar_precio(cod, n_precio, inscripciones):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("El código no existe")
                except ValueError:
                    print("El código no existe")
                
                resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if resp == 'n':
                    break
                    
        elif opc == 4:
            cod = input("Ingrese código del plan: ")
            if not validar_codigo(cod, planes):
                print("El código ya existe")
                continue
            
            nom = input("Ingrese nombre del plan: ")
            if not validar_nombre(nom):
                continue
                
            tip = input("Ingrese tipo (mensual/trimestral/anual): ")
            if not validar_tipo(tip):
                continue
                
            try:
                dur = int(input("Ingrese duración (meses): "))
                if not validar_duracion(dur):
                    continue
            except ValueError:
                continue
                
            pisc = input("¿Incluye acceso a piscina? (s/n): ")
            if not validar_piscina(pisc):
                continue
                
            clas = input("¿Incluye clases grupales? (s/n): ")
            if not validar_clases(clas):
                continue
                
            hor = input("Ingrese horario: ")
            if not validar_horario(hor):
                continue
                
            try:
                prec = int(input("Ingrese precio: "))
                if not validar_precio(prec):
                    continue
            except ValueError:
                continue
                
            try:
                cup = int(input("Ingrese cupos: "))
                if not validar_cupos(cup):
                    continue
            except ValueError:
                continue
                
            if agregar_plan(cod, nom, tip, dur, pisc, clas, hor, prec, cup, planes, inscripciones):
                print("Plan agregado")
            else:
                print("El código ya existe")
                
        elif opc == 5:
            cod = input("Ingrese código del plan: ")
            if eliminar_plan(cod, planes, inscripciones):
                print("Plan eliminado")
            else:
                print("El código no existe")
                
        elif opc == 6:
            print("Programa finalizado.")
            break

programa_principal()
import json
from pelicula import Pelicula, Serie, Documental, Cortometraje


# Muestra el menú principal de opciones
def mostrar_menu():
    print("n\---Estudio de Cine ---")
    print("1. Añadir nueva obra")
    print("2. Mostrar todas las obras")
    print("3. Añadir premio a una obra")
    print("4. Ver informes del estudio")
    print("5. Salir")


# Añade una nueva obra audiovisual (película, serie, documental o cortometraje)
def añadir_obra():
    print("\nTipos disponibles: ")
    print("1. Película")
    print("2. Serie")
    print("3. Documental")
    print("4. Cortometraje")


    tipo = input("Selecciona un tipo (1-4): ")


    titulo = input("Título: ")
    try:
        duracion = int(input("Duración (en minutos): "))
    except ValueError:
        print("Duración no válida. Debe ser un número.")
        return
    genero = input("Género: ")
#Comprobación de duplicados por título
    for obra in peliculas:
        if obra.titulo.lower() == titulo.lower():
            print(f"Ya existe una obra con el título '{titulo}'. No se añadirá de nuevo.")
            return

    if tipo == "1":
        director = input("Director: ")
        nueva = Pelicula(titulo, duracion, genero, director)
    elif tipo == "2":
        try:
            temporadas = int(input("Número de temporadas: "))
        except ValueError:
            print("Número de temporadas no válido. Debe ser un número.")
            return
        nueva = Serie(titulo, duracion, genero, temporadas)
    elif tipo == "3":
        tema = input("Tema principal: ")
        nueva = Documental(titulo, duracion, genero, tema)
    elif tipo == "4":
        festival = input("Festival asocoiado: ")
        nueva = Cortometraje(titulo, duracion, genero, festival)
    else:
        print("Opción no válida.")
        return

    peliculas.append(nueva)
    print("Obra añadida correctamente.")

# Muestra la información de todas las obras registradas
def mostrar_todas():
    if not peliculas:
        print("No hay obras registradas.")
    else:
        for obra in peliculas:
            print("\n---")
            obra.mostrar_info()
            
# Añade un premio a una obra seleccionada por título
def premiar_obra():
    if not peliculas:
        print("No hay obras disponibles para premiar.")
        return
    titulo = input("Introduce el título de la obra a premiar: ")

    for obra in peliculas:
        if obra.titulo.lower() == titulo.lower():
            obra.añadir_premio()
            print(f"Premio añadido a '{obra.titulo}'. Ahora tiene {obra.premios} premio(s).")
            return

    print(f"No se encontró ninguna obra con el título '{titulo}'.")

# Bucle principal
# --- Código reorganizado abajo ---
# Bucle principal de la aplicación, gestiona la interacción con el usuario
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            añadir_obra()
        elif opcion == "2":
            mostrar_todas()
        elif opcion == "3":
            premiar_obra()
        elif opcion == "4":
            mostrar_informes()
        elif opcion == "5":
            guardar_obras("obras.json", peliculas)
            print("Obras guardadas correctamente. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


# Guarda la lista de obras en un archivo JSON
def guardar_obras(ruta,obras):
    with open(ruta, 'w') as f:
         json.dump([obra.to_dict() for obra in obras], f, indent=4)

# Carga la lista de obras desde un archivo JSON, si existe
def cargar_obras(ruta):
    obras = []
    try:
        with open(ruta, 'r') as f:
            datos = json.load(f)
            for item in datos:
                 tipo = item["tipo"]
                 if tipo == "Película":
                    nueva = Pelicula( item["titulo"], item ["duracion"],item["genero"], item["director"])
                 elif tipo == "Serie":
                     nueva = Serie(item["titulo"],item["duracion"], item["genero"], item["temporadas"])
                 elif tipo == "Documental":
                     nueva = Documental(item["titulo"], item["duracion"], item["genero"],item["tema"])
                 elif tipo == "Cortometraje":
                     nueva = Cortometraje(item["titulo"], item["duracion"], item["genero"], item["festival"])
                 else:
                   print("fTipo desconocido: {tipo}. Esta entrada se omitira.")
                   continue

                 nueva.premios = item["premios"]
                 obras.append(nueva)
    except FileNotFoundError:
         print("Archivo no encontrado, se iniciará una lista nueva.")

    return obras

peliculas = cargar_obras("obras.json")


# Genera y muestra informes estadísticos del estudio de cine
def mostrar_informes():
    if not peliculas:
        print("No hay datos para generar informes.")
        return
    tipos = {"Pelicula": 0, "Serie": 0, "Documental": 0, "Cortometraje": 0}
    duraciones = {"Pelicula": [], "Serie": [], "Documental": [], "Cortometraje": []}
    total_premios = 0
    obra_mas_premiada = None
    for obra in peliculas:
        tipo = obra.__class__.__name__
        if tipo in tipos:
            tipos[tipo] += 1
            duraciones[tipo].append(obra.duracion)
        total_premios += obra.premios
        if not obra_mas_premiada or obra.premios > obra_mas_premiada.premios:
            obra_mas_premiada = obra
    print("\n--- INFORMES DEL ESTUDIO ---")
    print("Cantidad de obras por tipo:")
    for tipo, cantidad in tipos.items():
        print(f"  {tipo}: {cantidad}")
    print("\nDuración media por tipo:")
    for tipo, lista in duraciones.items():
        if lista:
            promedio = sum(lista) / len(lista)
            print(f"  {tipo}: {promedio:.2f} min")
        else:
            print(f"  {tipo}: N/A")
    if obra_mas_premiada:
        print(f"\nObra con más premios: '{obra_mas_premiada.titulo}' con {obra_mas_premiada.premios} premio(s).")
    print(f"Total de premios otorgados: {total_premios}")

if __name__ == "__main__":
    main()

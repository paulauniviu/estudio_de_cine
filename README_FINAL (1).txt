# Estudio de Cine - Herramienta de Gestión por Consola

**He elegido: Opción 4 - Herramienta de gestión con menús y POO**

Este proyecto ha sido desarrollado como parte de la actividad de programación orientada a objetos en Python. 
Se trata de una herramienta de gestión para un estudio de cine, ejecutada desde consola y estructurada según 
los principios de modularización, reutilización y buenas prácticas de programación.

## Fichero de inicio

Para ejecutar el programa, abrir y ejecutar el archivo:

**main_ENTREGABLE_FINAL.py**

## Librerías utilizadas

- `json`: Para guardar y cargar datos en formato JSON.
- No he usado librerías externas, sólo estándar de Python.

## Estructura del proyecto

- `main_ENTREGABLE_FINAL.py`: contiene el menú, la lógica principal y la interacción con el usuario.
- `pelicula_FINAL.py`: contiene la clase base `ContenidoAudiovisual` y 4 clases hijas (`Pelicula`, `Serie`, `Documental`, `Cortometraje`).
- `README.txt`: este documento.

## Funcionalidades principales

- Añadir nuevas obras (películas, series, documentales, cortometrajes).
- Mostrar todas las obras registradas.
- Añadir premios a obras existentes.
- Generar informes estadísticos:
  - Total de obras por tipo
  - Duración media por tipo
  - Obra más premiada
  - Total de premios otorgados
- Guardar y cargar automáticamente las obras usando ficheros JSON.
- Gestión de errores de entrada del usuario y control de opciones no válidas.

## Requisitos cumplidos

Este proyecto cumple los puntos exigidos por la rúbrica de evaluación:
- Clases bien estructuradas, con atributos propios y métodos.
- DocStrings explicativos y comentarios funcionales.
- Interfaz por consola clara y funcional.
- Gestión de datos con colecciones y JSON.
- Informes generados automáticamente con cálculos.
- Control de errores implementado.

## Instrucciones de uso

1. Ejecutar el archivo `main_ENTREGABLE_FINAL.py`.
2. Seguir las instrucciones del menú por consola.
3. Los datos se guardan automáticamente en `obras.json` al salir del programa.

## Autora

[Paula Tomás Marco]

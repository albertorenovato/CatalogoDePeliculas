from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp
opcion = None

while opcion != 4:
   try:
    print('Opciones:')
    print('1. Agregar Pelicula')
    print('2. Listar Peliculas')
    print('3. Eliminar Catalogo Peliculas')
    print('4. Salir')
    opcion = int(input('Escribe tu opción (1-4):'))

    if opcion == 1:
        nombrePelicula = input('Proporciona el nombre de la pelicula: ')
        pelicula = Pelicula(nombrePelicula)
        cp.agregarPelicula(pelicula)

    elif opcion == 2:
        cp.listarPeliculas()

    elif opcion == 3:
        cp.eliminarPeliculas()

   except Exception as e:
       print(f'Ocurrio un error {e}')
       opcion = None
else:
    print('Salimos del programa...')
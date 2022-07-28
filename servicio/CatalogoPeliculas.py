import os
class CatalogoPeliculas:

    rutaArchivo = 'peliculas.txt'

    @classmethod
    def agregarPelicula(cls, pelicula):
        with open(cls.rutaArchivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.getNombre}\n')


    @classmethod
    def listarPeliculas(cls):
        with open(cls.rutaArchivo, 'r', encoding='utf8') as archivo:
            print('Catalogo de Peliculas'.center(50, '-'))
            print(archivo.read())


    @classmethod
    def eliminarPeliculas(cls):
        os.remove(cls.rutaArchivo)
        print(f'Archivo eliminado: {cls.rutaArchivo}')
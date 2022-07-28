class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre


    def __str__(self):
        return f'Pelicula:{self._nombre}'


    @property
    def getNombre(self):
        return self._nombre

    @getNombre.setter
    def setNombre(self,nuevoNombre):
        self._nombre =nuevoNombre

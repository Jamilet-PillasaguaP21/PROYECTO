#Joseph Paez
#Viviana Caice
#Alejandra Barrera
#Jamilet Pillasagua

from revista import Revista
from libro import Libro
from docente import Docente
from estudiante import Estudiante

class Pedido():
    def __init__(self, id, solicitante, lista_material, fecha_prestamo, fecha_devolucion):
        self._id = id
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion

    def __str__(self):
        return f'Pedido: {self.__dict__}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def solicitante(self):
        return self._solicitante

    @solicitante.setter
    def solicitante(self, nuevo_solicitante):
        self._solicitante = nuevo_solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, nueva_lista_material):
        self._lista_material = nueva_lista_material

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, nueva_fecha_prestamo):
        self._fecha_prestamo = nueva_fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, nueva_fecha_devolucion):
        self._fecha_devolucion = nueva_fecha_devolucion


if __name__ == '__main__':
    pedido1 = Pedido(id='0932548449', solicitante='Joseph Paez', lista_material='Compra domicilio',
                     fecha_prestamo='20/junio/2023', fecha_devolucion='28/Junio/2023')
    print(pedido1)
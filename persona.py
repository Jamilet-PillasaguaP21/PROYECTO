#Joseph Paez
#Viviana Caice
#Alejandra Barrera
#Jamilet Pillasagua

from abc import ABC ,abstractmethod

class Persona(ABC):
    def __init__(self ,cedula :str ,nombre :str ,apellido :str ,email :str ,telefono :str ,direccion :str
                 ,numero_libros :int ,activo :bool ,carrera :str):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera


    def __str__ (self):
        return f' Persona : {self.__dict__.__str__()}'


    @property
    def cedula (self):
        return self._cedula
    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def numero_libros(self):
        return self._numero_libros
    @numero_libros.setter
    def numero_libros(self, numero_libros):
        self._numero_libros = numero_libros

    @property
    def activo(self):
        return self._activo
    @activo.setter
    def activo(self, activo):
        self._activo = activo

    @property
    def carrera(self):
        return self._carrera
    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera

    @abstractmethod
    def pedir_libro(self) -> bool:
        pass

    @abstractmethod
    def devolver_libro(self) -> bool:
        pass



if __name__ == '__main__':
    pass
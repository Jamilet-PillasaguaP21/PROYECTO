#Joseph Paez
#Viviana Caice
#Alejandra Barrera
#Jamilet Pillasagua

from persona import Persona

class Docente(Persona):

    contador_docente = 0

    def __init__(self ,cedula :str ,nombre :str ,apellido :str ,email :str ,telefono :str ,direccion :str
                 ,numero_libros :int ,activo :bool ,carrera :str, titulo_3er_nivel :str ,titulo_4to_nivel :str):

        Docente.contador_docente +=1
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera
        self._id = Docente.contador_docente
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        super(Docente, self).__init__(cedula = cedula, nombre = nombre, apellido= apellido, email=email, telefono=telefono, direccion=direccion, numero_libros=numero_libros, activo=activo, carrera=carrera)


    def __str__ (self):
        return f' Docente : {self.__dict__.__str__()}'


    @property
    def id (self):
        return self._id


    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel
    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, titulo_3er_nivel):
        self._titulo_3er_nivel = titulo_3er_nivel

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel
    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, titulo_4to_nivel):
        self._titulo_4to_nivel = titulo_4to_nivel

    @classmethod
    def pedir_libro(self) -> bool:
        pass

    @classmethod
    def devolver_libro(self) -> bool:
        pass


if __name__ == '__main__':
    d1 = Docente(cedula='0900000080', nombre='DANIELA', apellido='COBOS', email='DANICOBO@gmail.com',
                 telefono='0980808080', direccion='manabi', numero_libros=0, activo=True, carrera='GIG',
                 titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')
    d2 = Docente(cedula='0912345678', nombre='LUIS', apellido='MACIAS', email='luismacias@gmail.com',
                 telefono='0970707070', direccion='pedro carbo', numero_libros=0, activo=True, carrera='GIG',
                 titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')

    print(d1)
    print(d2)
#Joseph Paez
#Viviana Caice
#Alejandra Barrera
#Jamilet Pillasagua

from material import Material

class Libro(Material):
    contador_libro = 0

    def __init__(self, codigo:str, autor:str, titulo:str, anio:int, editorial:str, disponible:bool, cantidad_disponible:int,tipo_pasta:str):
        Libro.contador_libro +=1
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo
        self._anio = anio
        self._editorial = editorial
        self._disponible = disponible
        self._cantidad_disponible = cantidad_disponible
        self._id = Libro.contador_libro
        self._tipo_pasta = tipo_pasta
        super(Libro, self).__init__(codigo=codigo, autor=autor, titulo=titulo, anio=anio, editorial=editorial, disponible=disponible, cantidad_disponible=cantidad_disponible)

    def __str__(self):
        return f' Pedido : {self.__dict__.__str__()}'


    @property
    def id(self):
        return self._id


    @property
    def tipo_pasta(self):
        return self._tipo_pasta
    @tipo_pasta.setter
    def tipo_pasta(self, tipo_pasta):
        self._tipo_pasta = tipo_pasta

    @classmethod
    def actualizar_disponibilidad(self)-> bool :
        pass


if __name__ == '__main__':
    libro9 = Libro(codigo='20', autor='Mercedes Ron', titulo='CULPA NUESTRA', anio=2018, editorial='MONTENA',
                   disponible=True, cantidad_disponible=40, tipo_pasta='NORMAL')
    print(libro9)
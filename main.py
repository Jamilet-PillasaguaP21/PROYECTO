#Joseph Paez
#Viviana Caice
#Alejandra Barrera
#Jamilet Pillasagua

from docente import Docente
from estudiante import Estudiante
from libro import Libro
from revista import Revista
from pedido import Pedido

d1 = Docente(cedula='0900000080', nombre='DANIELA', apellido='COBOS', email='DANICOBO@gmail.com',
             telefono='0980808080', direccion='manabi', numero_libros=0, activo=True, carrera='GIG',
             titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')
d2 = Docente(cedula='0912345678', nombre='LUIS', apellido='MACIAS', email='luismacias@gmail.com',
             telefono='0970707070', direccion='pedro carbo', numero_libros=0, activo=True, carrera='GIG',
             titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')

print(d1)
print(d2)

# Estudiantes
e1 = Estudiante(cedula='0932548449', nombre='joseph', apellido='paez', email='josephsamuelpaez@gmail.com',
                telefono='0984902300', direccion='mapasingue ', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)
e2 = Estudiante(cedula='0915459077', nombre='viviana', apellido='caice', email='vcaicezuniga1978@gmail.com',
                telefono='0979512906', direccion='centro sur', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)
e3 = Estudiante(cedula='0953509502', nombre='alejandra', apellido='barrera', email=' alejandrabarrera0207@gmail.com',
                telefono='0979262951', direccion='daule', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)
e4 = Estudiante(cedula='0952308245', nombre='jamilet', apellido='pillasagua', email='jamifernanda@gmail.com',
                telefono='0989475023', direccion='sauces', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)

print(e1)
print(e2)
print(e3)
print(e4)


libro9 = Libro(codigo='20', autor='Mercedes Ron', titulo='CULPA NUESTRA', anio=2018, editorial='MONTENA', disponible=True, cantidad_disponible=40,tipo_pasta='NORMAL')
print(libro9)

revista10 = Revista(codigo='300', autor='MATIAS', titulo='AUTO', anio=2010, editorial='MAZDA', disponible=True, cantidad_disponible=60,tipo='DIGITAL')
print(revista10)

pedido1 = Pedido(id='0932548449', solicitante='Joseph Paez', lista_material='Compra domicilio',
                 fecha_prestamo='20/junio/2023', fecha_devolucion='28/Junio/2023')
print(pedido1)
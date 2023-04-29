"""
DESARROLLO - Continuación del trabajo.
Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python, para comprender
las ventajas de la programación orientada a objetos.
En vista a nuestro sistema desarrollado anteriormente se solicita lo siguiente:
Agregar una nueva clase pertinente a la aplicación que están desarrollando e identificar en ella al
menos cuatro atributos (uno de ellos debe ser opcional). Agréguela al diagrama intuitivo que realizó en
la actividad anterior.

Se deberá crear métodos para cada uno de los usuarios. Piensen en diferentes acciones particulares
que pueda ejecutar cada una de sus clases. Desarrolle cuatro métodos por cada clase. Dos deben
incluir acciones que afecten números y dos que afecten strings. Al menos uno de estos métodos debe
aplicar los contenidos de ‘sobrecarga de métodos’.
También se solicita que existan condiciones para realizar las validaciones correspondientes.
"""
class Productos:
    def __init__(self, id, nombre, precio, precio_venta, stock, descuento=False):
        self.id = id
        self.color = nombre
        self.precio = precio
        self.precio_venta = precio_venta
        self.stock = stock
    
    def agregar(self):
        pass

    def eliminar(self):
        pass
    #Modificar producto (Precio,nombre)
    def modificar(self):
        pass

    def modificar_stock(self):
        pass

    def modificar_descuentos(self):
        pass
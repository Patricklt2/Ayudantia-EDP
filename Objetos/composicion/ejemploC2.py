"""
Escribe un programa en Python que modele una tienda en línea. La tienda debe tener productos disponibles para la venta,
 cada uno con un nombre, un precio y una cantidad en stock.
 Los clientes pueden agregar productos a su carrito de compras,
 ver el total de su carrito y realizar la compra.
 Implementa clases para representar la tienda, los productos y los carritos de compras.
 Asegúrate de usar la herencia cuando sea apropiado y proporciona métodos para agregar productos al carrito,
calcular el total de la compra y realizar la compra.
"""

# Paso 1 : definir la clase producto

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock -= cantidad

# Paso 2 : Definir la clase carrito

class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos:
            total += producto.precio * cantidad
        return total

# Paso 3 : definir la clase tienda + agregar interaccion al user

class TiendaEnLinea:
    def __init__(self):
        self.productos_disponibles = []

    def agregar_producto(self, producto):
        self.productos_disponibles.append(producto)

    def realizar_compra(self, carrito):
        for producto, cantidad in carrito.productos:
            if producto.stock < cantidad:
                print(f"No hay suficiente stock de {producto.nombre}")
                return
            producto.actualizar_stock(cantidad)
        print("Compra realizada con éxito. ¡Gracias por comprar!")

# ejemplo de uso de esta clase

producto1 = Producto("Camiseta", 20, 10)
producto2 = Producto("Pantalón", 30, 5)

tienda = TiendaEnLinea()
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

carrito = CarritoDeCompras()
carrito.agregar_producto(producto1, 2)
carrito.agregar_producto(producto2, 1)

print("Total de la compra:", carrito.calcular_total())
tienda.realizar_compra(carrito)

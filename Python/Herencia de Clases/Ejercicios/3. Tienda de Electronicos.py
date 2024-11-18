class Producto:
    def __init__(self, nombre, precio):
        """Modelo de un Producto"""
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_final(self):
        return self.precio * 1.19

    def __str__(self):
        return f"Nombre: {self.nombre}\nPrecio: {self.precio}"

#p = Producto("Barra de proteína 12g", 2000)
#print(p)

class Electrodomestico(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self.garantia = garantia

    def calcular_precio_final(self):
        precio_base = super().calcular_precio_final()
        if self.garantia > 1:
            precio_base += self.precio * 0.10
        return precio_base       

electrodomestico = Electrodomestico("Hervidor",20000,3)
producto = Producto("Barra de proteína 12g", 1500)

electrodomestico.calcular_precio_final()
producto.calcular_precio_final()

print(electrodomestico)
print(f"Precio final (IVA y garantía incluida): {electrodomestico.calcular_precio_final():.2f}")
print(producto)
print(f"Precio final (IVA incluido): {producto.calcular_precio_final():.2f}\n")
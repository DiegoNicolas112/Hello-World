#Clase de Autos

class Vehiculo:
    def __init__(self, modelo, vin, patente):
        self.modelo = modelo
        self.vin = vin
        self.patente = patente

    def __str__(self):
        return """
MODELO: {}
VIN: {}
PATENTE: {}""".format(self.modelo, self.vin, self.patente)

    #def mostrar_vehiculos(self):
    #    print("Modelo:", self.modelo, ",Vin:",self.vin, ",Patente:",self.patente)
vehiculo1 = Vehiculo("Audi A3", "X1", "XXYY-10")
print(vehiculo1)

class Combustible(Vehiculo):
    def __init__(self, modelo, vin, patente, combustible):
        super().__init__(modelo, vin, patente)
        # Agregamos el nuevo atributo específico de esta clase
        self.combustible = combustible

    def __str__(self):
        return """
MODELO: {}
VIN: {}
PATENTE: {}
COMBUSTIBLE: {}""".format(self.modelo, self.vin, self.patente, self.combustible)

com = Combustible("Audi A3", "X1", "XXYY-10","Gasolina 97")
print(com)
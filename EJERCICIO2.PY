class Telefono:
    def __init__(self, marca, modelo, color):
        self.marca = marca 
        self.modelo = modelo 
        self.color = color
        
samsungS24 = Telefono("samsung", "S24","azul-blanco")
samsungA22 = Telefono("samsung", "A22", "gris")
samsungA23 = Telefono("samsung", "A23", "black")



print(type(samsungS24))
print(type(samsungA22))
print(type(samsungA23))

print(samsungS24.marca,samsungS24.modelo, samsungS24.color )
print(samsungA22.marca, samsungA22.modelo, samsungA22.color)
print(samsungA23.marca, samsungA23.modelo, samsungA23.color)

class Vehiculo:
    def __init__(self, marca, modelo, velocidadmax):
        self.marca = marca 
        self.modelo = modelo 
        self.velocidadmax = velocidadmax
        
audi = Vehiculo("Audi", "A1","280k/h")
nissan = Vehiculo("Nissan", "X-trail", "300k/h")
ford = Vehiculo("Ford", "Fiesta", "200h/h")


print(type(audi))
print(type(nissan))
print(type(ford))


print(audi.marca, audi.modelo, audi.velocidadmax )
print(nissan.marca, nissan.modelo,nissan.velocidadmax)
print(ford.marca, ford.modelo, nissan.velocidadmax)
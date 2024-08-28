class Bicletas:
    def __init__(self, marca, modelo, color):
        self.marca = marca 
        self.modelo = modelo 
        self.color = color
        
trekMadone = Bicletas("Trek", "Madone","azul turquesa")
trek23 = Bicletas("Trek", "23", "verde azulado")


print(type(trekMadone))
print(type(trek23))


print(trekMadone.marca, trekMadone.modelo, trekMadone.color )
print(trek23.marca, trek23.modelo, trek23.color)


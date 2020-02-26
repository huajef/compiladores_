#herencia 
class Pokemon :
    pass

    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo = tipo
        
    def descrip(self) :
        return '{} es un pokemon de tipo {}'.format(self.nombre,self.tipo) 

class pikachu (Pokemon) :
    def ataque (self,tipoataque):
        return '{} tipo de ataque p:{}'.format(self.nombre,tipoataque)

class charmander (Pokemon):
     def ataque (self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre,tipoataque)


nuevo_pokemon = charmander ('yefer','electrico')
print(nuevo_pokemon.descrip())    
print(nuevo_pokemon.ataque('impacto trueno'))  


#hello cambio 
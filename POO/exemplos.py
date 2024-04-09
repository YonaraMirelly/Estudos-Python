from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('ligar')
    def desligar(self):
        print('desligar')
    @property
    def marca(self):
        return "LG"

class Ar(ControleRemoto):
    def ligar(self):
        print('ligando')
    def desligar(self):
        print('desligando')
    @property
    def marca(self):
        return "ARAR"
    
c = ControleTV()
c.ligar()
c.desligar()
print(c.marca)

c = Ar()
c.ligar()
print(c.marca)


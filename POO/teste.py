class Passaro:
    def voar(self):
        print('voando')


class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não voa')

class Aviao(Passaro):
    def voar(self):
        print('Decolando')

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
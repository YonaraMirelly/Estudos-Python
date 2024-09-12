class No():
    def __init__(self,dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class Fila():
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def isvazia(self):
        return self.inicio is None
        
    def inserir(self,dado):
        novo_no= No(dado)
        if self.isvazia():
            self.inicio = novo_no
            self.fim = novo_no
            self.tamanho =self.tamanho +1
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no
            self.tamanho = self.tamanho+1

    def remover(self):
            if self.isvazia():
                return 0
            elif self.tamanho == 1:
                self.inicio = None
                self.fim = None
                self.tamanho =self.tamanho - 1
                
            else:
                j = self.inicio
                self.inicio = self.inicio.proximo 
                self.inicio.anterior = None
                self.tamanho = self.tamanho - 1
                return j
    
    def imprimir(self):
         if self.isvazia():
             return 0
         return self.inicio.dado

def comparar (comando,lista):
    if comando[0] =='f':
        regular.inserir(comando[1])
    elif comando[0] =='p':
        preferencial.inserir(comando[1])
    elif comando[0] =='A':
        removido = regular.remover()
        if removido == 0:
            preferencial.remover()
    elif comando[0] =='B':
        removido = preferencial.remover()
        if removido == 0:
            regular.remover()
    elif comando[0] =='I':
        lista.append(f'{regular.imprimir()} {preferencial.imprimir()}')

cases = []

N = int(input())
for i in range(N):
    preferencial = Fila()
    regular = Fila()
    T =int(input())
    imprimir = []
    for i in range(T):
        comando = input().split()
        comparar(comando,imprimir)
    cases.append(imprimir)

for i in range(len(cases)):
    print(f'Caso {i+1}:')
    for j in cases[i]:
        print(f'{j}')
        



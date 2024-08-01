def exemplo(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(tamanho):
            if i != j and lista[i] == lista[j]: 
                return True
    return False
        
    
print(exemplo([1,2,3]))

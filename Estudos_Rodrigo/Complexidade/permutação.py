def permutacoes(lista):
  """
  Gera todas as permutações possíveis de uma lista.
  Args:
    lista: A lista de elementos a serem permutados.
  Returns:
    Uma lista de todas as permutações.
  """
  if len(lista) == 1:
    return [lista]
  result = []
  for i in range(len(lista)):
    # Escolhe o elemento i
    elemento = lista[i]
    # Gera as permutações do restante da lista
    restante = lista[:i] + lista[i+1:]
    # Gera as permutações do restante e combina com o elemento escolhido
    for p in permutacoes(restante):
      result.append([elemento] + p)
  return result
# Exemplo de uso:
lista_letras = ['a', 'b', 'c']
todas_permutacoes = permutacoes(lista_letras)
print(todas_permutacoes)
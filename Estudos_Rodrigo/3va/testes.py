def is_palindromo(palavra):
    if len(palavra) <= 2:
        return True
    if palavra[0] != palavra[-1]:
        return False
    else:
        return is_palindromo(palavra[1:-1])
    
print(is_palindromo('yonara'))
    
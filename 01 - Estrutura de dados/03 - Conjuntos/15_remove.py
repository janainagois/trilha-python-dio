#o método .remove() tem uma função parecida com o .discart(), porém se eu tento remover um número inexistente no conjunto, ele retorna um "keyerror" ex:

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros.remove(45)) 
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

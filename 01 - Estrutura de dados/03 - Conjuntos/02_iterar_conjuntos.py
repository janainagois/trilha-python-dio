#apesar de não poder acessar os elementos da função set() por índices, é possível ver estes índices a partir da estrutura for, ex:

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

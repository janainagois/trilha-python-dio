def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

#abaixo estão três formas de inserir valores aos argumentos das funções:
    
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
#desse modo ele atribui o valor ao argumento correspondente, mas se por algum motivo a ordem dos argumentos for trocada, as informações não serão mais correspondentes.

salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
#desse modo ele atribui o valor ao argumento informando um par de chave-valor, mas se por algum motivo o argumento que corresponde a chave for trocado, as informações não serão mais correspondentes.

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
#o exemplo acima é semelhante ao anterior, mas na forma de dicionário.

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):#quando eu coloco um argumento sem valor atribuído na função, eu sou obrigada a atribuir um valor no momento da execução desta função, senão me retorna um erro.
    print(f"Seja bem vindo(a) {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo(a) {nome}!")


exibir_mensagem()
exibir_mensagem_2("Janaína")#eu também posso colocar diretamente o valor
exibir_mensagem_3()
exibir_mensagem_3("Chappie")

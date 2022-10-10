nome = "Aline"
idade = 31

saldo = 45.435

dados = {"nome": "Aline", "idade": 31}

# Old Style %
print("Nome: %s Idade: %d" % (nome, idade))

# Método Formta
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

# Método f strings
print(f"Nome: {nome} Idade: {idade} saldo: {saldo:.2f}")


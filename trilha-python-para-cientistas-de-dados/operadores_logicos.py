# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

#Operador E

#print(True and True and True)
#print(True and False and True)
#print(False and False and False)

#Operador OU

#print(True or True or True)
#print(True or False or False)
#print(False or False or False)

#Exemplo

saldo = 1000
saque = 250
limite = 200
conta_especial = True

#exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

#print(exp_1)

#exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

#print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)


#Operador de negação


#Parênteses


# if


#MAIOR_IDADE = 18

#idade = int(input("Informe sua idade: "))

#if idade >= 18:
    #print("Maior de idade, pode tirar a CNH.")

#if idade < MAIOR_IDADE:
    #print("Ainda não pode tirar CNH.")


# if / else

#MAIOR_IDADE = 18

#idade = int(input("Informe sua idade: "))

#if idade >= 18:
    #print("Maior de idade, pode tirar a CNH.")

#else:
    #print("Ainda não pode tirar CNH.")


#MAIOR_IDADE = 18
#IDADE_ESPECIAL = 17

#idade = int(input("Informe sua idade: "))

#if idade >= MAIOR_IDADE:
        #print("Maior de idade, pode tirar a CNH.")

#elif idade == IDADE_ESPECIAL:
        #print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")

#else:
        #print("Ainda não pode tirar CNH.")

# Estrutura condicional aninhada (if aninhado)

#conta_normal = False
#conta_universitária = False
#conta_especial = True

#saldo = 2000
#saque = 1500
#cheque_especial = 450

#if conta_normal:

    #if saldo >= saque:
        #print("Saque realizado com sucesso!")

    #elif saque <= (saldo + cheque_especial):
        #print("Saque realizado com uso do cheque especial!")

    #else: 
        #print("Não foi possível realizar o saque, saldo insuficiente!")

#elif conta_universitária:

    #if saldo >= saque:
       # print("Saque realizado com sucesso!")

    #else:
       # print("Saldo insuficiente!")
    
#elif conta_especial:
        #print("Conta especial selecionada!")

#else:
    #print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente!")


# Estrutura condicional (if ternário)

saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
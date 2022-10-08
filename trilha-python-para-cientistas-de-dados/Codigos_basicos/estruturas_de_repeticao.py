#  Comando for 

#texto = input("Informe um texto: ")
#texto = ""
#VOGAIS = "AEIOU"



#for letra in texto:
    #if letra.upper() in VOGAIS:
        #print(letra, end="")

#else:
    #print() # adiciona uma quebra de linha
    #print("Executa no final do laço")

    
# range com for

#for numero in range(0, 51, 5):
    #print(numero, end=" ")


#exe: utilizando a função while

#opcao = -1

#while opcao != 0:
    #opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair\n: "))

    #if opcao == 1:
        #print("Sacando...")

    #elif opcao == 2:
        #print("Exibindo o extrato...")


#exe: utilizando a função while / else

#opcao = -1

#while opcao != 0:
    #opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair\n: "))

    #if opcao == 1:
        #print("Sacando...")

    #elif opcao == 2:
        #print("Exibindo o extrato...")
#else:
    #print("Obrigado por usar nosso sistema bancário, até logo!")

#Estruturas de repetição Comando Break



#while True:
#    numero = int(input("Informe um número: "))
    
#    if numero == 10:
#       break

 #   print(numero)

#for numero in range(100):

   # if numero == 15:
     ##   break

   # print(numero, end=" ")


#for numero in range(100):

    #if numero % 2 == 0:
        #continue

    #print(numero, end=" ")

#Estruturas de repetição Comando Break e Continue no while
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    if numero % 2 == 0:
        continue
     
    print(numero)
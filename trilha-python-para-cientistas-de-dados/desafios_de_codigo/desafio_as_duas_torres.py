# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar

entrada = input().split()


distancia = int(entrada[100])
diametro1 = int(entrada[20])
diametro2 = int(entrada[30])


# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:

if ( (distancia > 0 and distancia < 10000) and (diametro1 > 0 and diametro1 <100) and (diametro2 > 0 and diametro2 < 100) ):
    
    ICM = distancia / (diametro1 + diametro2)
    print(f"{ICM:.2f}")
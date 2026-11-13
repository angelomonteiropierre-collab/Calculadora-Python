#Planejamento: elaboração de uma calculadora simples que receba dois números do usuário e retorne o resultado da operação escolhida por ele

#Etapa 1: definimos as funções de cada operação

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtrair(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    return resultado
    
def dividir(numero1, numero2):
    resultado = numero1 / numero2
    return resultado

#Etapa 2: prever e retornar uma resposta caso ocorra uma entrada inválida. Nesse caso, o código trata uma digitação de um texto ao invés de números

#Lógica: tente digitar o primeiro número, o segundo número e a operação escolhida, se um dos números for um texto, retorne a mensagem: "Digite apenas números"
try:
    primeiro_número = float(input("Digite o primeiro número: "))
    segundo_número = float(input("Digite o segundo número: "))
    operacao_escolhida = input("Escolha a operação: ")

#Colocamos a operação dentro do try porque ela depende que a digitação dos números ocorra de maneira correta
#Fazemos uma lógica condicional para o programa executar uma determinada função de acordo com a operação escolhida pelo usuário
    if operacao_escolhida == "+":
        resultado = somar(primeiro_número, segundo_número)
        print(f"A soma desses números é: {resultado}")

    elif operacao_escolhida == "-":
        resultado = subtrair(primeiro_número, segundo_número)
        print(f"A subtração desses números é: {resultado}")

    elif operacao_escolhida == "/":
#Usamos try e except para se o usuário dividir um número por 0, o código retornar a mensagem "Não é possível dividir um número por 0"
        try:
            resultado = dividir(primeiro_número, segundo_número)
            print(f"A divisão entre esses números é: {resultado}")
        except ZeroDivisionError:
            print("Não é possível dividir um número por 0")   

    elif operacao_escolhida == "*":
        resultado = multiplicar(primeiro_número, segundo_número)
        print(f"A multiplicação entre esses números é: {resultado}")
#O código retorna uma mensagem caso o usuário digite um texto diferente das operações possíveis
    elif operacao_escolhida not in ["+", "-", "*", "/"]:
        print("Digite uma operação válida: + ou - ou * ou /")

except ValueError:
    print("Digite apenas números")











n1 = int(input("Digite um número: ")) #Convertendo de string para inteiro, colocando "int"
n2 = int(input("Digite outro número: "))

soma = n1 + n2
subtrair = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
resto = n1 % n2

print(f"O resultado da soma é {soma} o tipo da variavel é {type(soma)}")
print(f"O resultado da subtração é {subtrair} o tipo da variavel é {type(subtrair)}")
print(f"O resultado da multiplicação é {multiplicacao} o tipo da variavel é {type(multiplicacao)}")
print(f"O resultado da sdivisão é {divisao} o tipo da variavel é {type(divisao)}")
print(f"O resultado da resto é {resto} o tipo da variavel é {type(resto)}")
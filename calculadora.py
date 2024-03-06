print("Calculadora")
print(" ")

valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))

soma = valor1 + valor2
subtracao = valor1 - valor2
divisao = valor1 / valor2
multiplicacao = valor1 * valor2
divisao2 = valor1 // valor2
multiplicacao2 = valor1 ** valor2

print(f'''
Resultado da Soma = {soma}
Resultado da Subtração = {subtracao}
Resultado da Divisão = {divisao}
Resultado da Multiplicação = {multiplicacao}

Resultado da 2º Divisão = {divisao2}
Resultado da 2º Multiplicação = {multiplicacao2}
''')

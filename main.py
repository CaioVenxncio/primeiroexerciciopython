'''
# Ler os dois valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Verificar e imprimir o maior valor
if valor1 > valor2:
    print("O maior valor é:", valor1)
else:
    print("O maior valor é:", valor2)
'''
'''
# Ler a idade da pessoa
idade = int(input("Digite sua idade: "))

# Verificar se a pessoa pode votar este ano
if idade >= 16:
    print("Você pode votar este ano!")
else:
    print("Você não pode votar este ano.")
'''
'''
# Ler a senha fornecida pelo usuário
senha = input("Digite a senha: ")

# Verificar se a senha está correta e imprimir a mensagem apropriada
if senha == "1234":
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")
'''
'''
# Ler o número de maçãs compradas
numero_macas = int(input("Digite o número de maçãs compradas: "))

# Calcular o valor total da compra
if numero_macas < 12:
    valor_total = numero_macas * 0.30
else:
    valor_total = numero_macas * 0.25

# Imprimir o valor total da compra
print(f"O valor total da compra é: R$ {valor_total:.2f}") 
'''
'''
# Ler os três valores inteiros
num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = int(input("Digite o terceiro valor inteiro: "))

# Encontrar o menor, o do meio e o maior
if num1 < num2 < num3:
    menor, meio, maior = num1, num2, num3
elif num1 < num3 < num2:
    menor, meio, maior = num1, num3, num2
elif num2 < num1 < num3:
    menor, meio, maior = num2, num1, num3
elif num2 < num3 < num1:
    menor, meio, maior = num2, num3, num1
elif num3 < num1 < num2:
    menor, meio, maior = num3, num1, num2
else:
    menor, meio, maior = num3, num2, num1

# Imprimir os valores em ordem crescente
print(f"Em ordem crescente: {menor}, {meio}, {maior}")
'''
'''
# Ler a altura e o sexo da pessoa
altura = float(input("Digite a altura da pessoa em metros: "))
sexo = int(input("Digite o sexo da pessoa (1 para masculino, 2 para feminino): "))

# Calcular o peso ideal
if sexo == 1:
    peso_ideal = (72.7 * altura) - 58
    genero = "masculino"
elif sexo == 2:
    peso_ideal = (62.9 * altura) - 44.7
    genero = "feminino"
else:
    print("Código de sexo inválido. Use 1 para masculino e 2 para feminino.")
    exit()

# Imprimir o peso ideal
print(f"O peso ideal para uma pessoa {genero} com altura {altura} metros é: {peso_ideal:.2f} kg")
'''
'''
import math

# Ler o número de lados e a medida do lado do polígono
num_lados = int(input("Digite o número de lados do polígono regular: "))
medida_lado = float(input("Digite a medida do lado em cm: "))

# Calcular a área do polígono
if num_lados == 3:
    # Triângulo
    area = (medida_lado ** 2 * math.sqrt(3)) / 4
    nome_poligono = "TRIÂNGULO"
elif num_lados == 4:
    # Quadrado
    area = medida_lado ** 2
    nome_poligono = "QUADRADO"
elif num_lados == 5:
    # Pentágono
    apotema = medida_lado / (2 * math.tan(math.pi / 5))
    area = (5 * medida_lado * apotema) / 2
    nome_poligono = "PENTÁGONO"
else:
    print("Polígono com número de lados inválido. Use 3 para triângulo, 4 para quadrado e 5 para pentágono.")
    exit()

# Imprimir o nome do polígono e a área
print(f"O polígono é um {nome_poligono} e a área é: {area:.2f} cm²")
'''
'''
 import math

# Ler o número de lados e a medida do lado do polígono
num_lados = int(input("Digite o número de lados do polígono regular: "))
medida_lado = float(input("Digite a medida do lado em cm: "))

# Verificar o tipo de polígono e calcular a área
if num_lados < 3:
    print("Não é um polígono.")
elif num_lados == 3:
    # Triângulo
    area = (medida_lado ** 2 * math.sqrt(3)) / 4
    nome_poligono = "TRIÂNGULO"
elif num_lados == 4:
    # Quadrado
    area = medida_lado ** 2
    nome_poligono = "QUADRADO"
elif num_lados == 5:
    # Pentágono
    apotema = medida_lado / (2 * math.tan(math.pi / 5))
    area = (5 * medida_lado * apotema) / 2
    nome_poligono = "PENTÁGONO"
elif num_lados > 5:
    print("Polígono não identificado.")
    exit()

# Imprimir o nome do polígono e a área, se for um polígono identificado
if num_lados >= 3 and num_lados <= 5:
    print(f"O polígono é um {nome_poligono} e a área é: {area:.2f} cm²")
'''
'''
# Ler os três valores inteiros
valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

# Encontrar o maior valor
maior_valor = max(valor1, valor2, valor3)

# Imprimir o maior valor
print(f"O maior valor é: {maior_valor}")
'''
''' 
# Ler as medidas dos três lados do triângulo
lado1 = float(input("Digite a medida do primeiro lado: "))
lado2 = float(input("Digite a medida do segundo lado: "))
lado3 = float(input("Digite a medida do terceiro lado: "))

# Verificar o tipo de triângulo
if lado1 == lado2 == lado3:
    tipo_triangulo = "Equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo_triangulo = "Isósceles"
else:
    tipo_triangulo = "Escaleno"

# Imprimir o tipo de triângulo
print(f"O triângulo é {tipo_triangulo}.")
'''
'''
# Ler os três ângulos do triângulo
angulo1 = float(input("Digite o valor do primeiro ângulo: "))
angulo2 = float(input("Digite o valor do segundo ângulo: "))
angulo3 = float(input("Digite o valor do terceiro ângulo: "))

# Verificar o tipo de triângulo
if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    tipo_triangulo = "Retângulo"
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    tipo_triangulo = "Obtusângulo"
else:
    tipo_triangulo = "Acutângulo"

# Imprimir o tipo de triângulo
print(f"O triângulo é {tipo_triangulo}.")
'''

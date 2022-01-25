
nome = "Luiz"
idade = 32
altura = 1.80
peso = 80.5
ano_atual = 2021
ano_nasc = ano_atual - idade
imc = peso / altura ** 2

print("{} tem {} anos, {} de altura e pesa {}kg.".format(nome, idade, altura, peso))
print("O IMC de {} é {:.2f}.".format(nome, imc))
print("{} nasceu em {}".format(nome, ano_nasc))
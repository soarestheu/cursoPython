

nome = 'Luiz' #string
idade = 32 #int 
altura = 1.80 #float
e_maior = idade > 18 #bool
peso = 80 
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{2} tem {1} anos de idade e seu imc é {0}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))
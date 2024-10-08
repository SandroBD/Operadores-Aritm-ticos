d=int(input('Por qunatos dias foi alugado?  '))
k=float(input('Quantos Km foi percorrido? '))
valor = (60 * d) + ( k * 0.15)
print('Valor pago em {} dias de aluguel, com uma diária de R$60,00 e R$0,15 de Km excedente'
      ' - sendo que foi percorrido {:.2f}Km, será de R${:.2f}'.format(d, k, valor))

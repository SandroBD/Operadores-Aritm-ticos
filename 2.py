n1=int(input('Um valor: '))
n2=int(input('Outro valor: '))
s=n1 + n2
m=n1 * n2
sub=n1 - n2
e=n1 ** n2
d=n1 / n2
di=n1 // n2
r=n1 % n2
#print('A soma de {} e {} vale {}'.format(n1, n2, s))
print('A soma é {}, o produto é {},\n e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')

print('Divisão inteira {},\n potência {}'.format(di, e))



m = float(input())
a = float(input())
imc = m/(a**2)

print(f'{imc:.0f}')

if imc <= 18.5:
  print('Abaixo do peso')
elif imc <= 25 and imc > 18.5:
  print('Peso normal')
elif imc <= 30 and imc > 25:
  print('Sobrepeso')
elif imc < 35 and imc > 30:
  print('Obeso leve')
elif imc < 40 and imc >= 35:
  print('Obeso moderado')
else:
  print('Obeso Mórbido')
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

media = (n1+n2+n3+n4+n5)/5

print(f'{media:.2f}')

if n1 > media:
  print(f'{n1:.2f}')
if n2 > media:
  print(f'{n2:.2f}')
if n3 > media:
  print(f'{n3:.2f}')
if n4 > media:
  print(f'{n4:.2f}')
if n5 > media:
  print(f'{n5:.2f}')
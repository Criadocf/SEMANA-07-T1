# -*- coding: utf-8 -*-
"""SEMANA 07 T1.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14NeAtL9Htmzd85H7ctJMwzbDssuMizvi
"""



"""03) Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores
são diferentes. NÃO use as funções embutidas min() e max().
"""

def maior(n1,n2,n3,n4,n5):
  if n1 > n2 and n2 > n3 and n1 > n4 and n1 > n5:
    return n1
  elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    return n2
  elif n3 > n1 and n3 >n2 and n3 > n4 and n3 > n5:
    return n3
  elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    return n4
  else:
    return n5

def menor(nu1,nu2,nu3,nu4,nu5):
    if nu1 < nu2 and nu1 < nu3 and nu1 < nu4 and nu1 < nu5:
      return nu1
    elif nu2 < nu1 and nu2 < nu3 and nu2 < nu4 and nu2 < nu5:
      return nu2
    elif nu3 < nu1 and nu3 < nu2 and nu3 < nu4 and nu3 < nu5:
      return nu3
    elif nu4 < nu1 and nu4 < nu2 and nu4 < nu3 and nu4 < nu5:
      return nu4
    else:
      return nu5
    
num1 = int(input().strip())
num2 = int(input().strip())
num3 = int(input().strip())
num4 = int(input().strip())
num5 = int(input().strip())

ch1 = maior(num1, num2, num3, num4, num5)
ch2 = menor(num1, num2, num3, num4, num5)

print(ch1)
print(ch2)
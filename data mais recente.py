#Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras
#: dia, mês e ano) e escreva qual delas é a mais recente.

dia1 = int(input())
mes1 = int(input())
ano1 = int(input())

dia2 = int(input())
mes2 = int(input())
ano2 = int(input())

if ano1 > ano2:
    print(f'{dia1}/{mes1}/{ano1}')
elif mes1 > mes2:
    print(f'{dia1}/{mes1}/{ano1}')
elif dia1 > dia2:
    print(f'{dia1}/{mes1}/{ano1}')
else:
    print(f'{dia2}/{mes2}/{ano2}')
    


nota = int(input('Entre com uma nota: '))
while nota > 10:
    nota = int(input('[ERRO] \nNota inválida \nDigite a nota válida: '))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1): # a+1 serve ex. digitei numero 7 ele percorre 1 ao 6 +1 == 7
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)



# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a+1): # a+1 serve ex. digitei numero 7 ele percorre 1 ao 6 +1 == 7
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('O número {} não é primo'.format(a))

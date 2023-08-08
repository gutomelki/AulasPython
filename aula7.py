# # criamos um dicionário em Pyhton utilizando chaves{}
#
# # tabela = {'alface': 0.45, 'batata': 1.2, 'tomate': 2.3, 'feijão': 1.5}
# # print(tabela['feijão'])
#
carros = {'Nissan 370z': ['R$250.000,00', '2009'], 'BMW 320i': ['R$150.000,00', '2023'], 'Toyota Supra': ['R$1.200.000,00', '1998']}
# print(carros)
# print(carros['BMW 320i'])
#
# carros['BMW 320i'] = ['R$ 400.000,00', '2023']
# print(carros)
#
# del carros['Toyota Supra']
# print(carros)
#
# carros['Honda Fit'] = ['R$ 50.000,00', '2016']
# print(carros)
#
# print('Audi' in carros)
# print('BMW 320i' in carros)
#
# print(carros.keys())
# print(carros.values())
#
# carros['BMW 320i'][1] = 2019
# print(carros)



while True:
    produto = input('Digite o nome do carro ou fim para terminar:')
    if produto == 'fim.':
        break
    if produto in carros:
        print(f'Preço: R$ {carros[produto]:.2f}')
    else:
        print('Carro não encontrado.')

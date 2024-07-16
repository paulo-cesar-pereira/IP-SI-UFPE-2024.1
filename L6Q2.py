# Usos de dict comprehension.
# Uso de **kwargs para mesclar mais de dois dicionários.

def ganho(n):
  return n * 20 * (1 - 0.01 * (2 * (n > 1) + 3 * (n > 3) + 2 * (n > 5)))

fortuna = {'Priscila Senna': 10000, 'Eduarda': 9990, 'Academia da Berlinda': 9995, 'Martins': 9970, 'Igor de Carvalho': 9965}
N = int(input())
vendas = {x[0]: int(x[1]) for x in [input().split(' - ') for i in range(N)]}
add_fortuna = {x: fortuna[x] + ganho(vendas[x]) for x in vendas if x in fortuna}
new_fortuna = {x: ganho(vendas[x]) for x in vendas if x not in fortuna}

if add_fortuna:
  print('Estes artistas obtiveram aumento do lucro em relação à primeira semana:')
  for a in add_fortuna:
    print(f'{a} - Lucro em relação à primeira semana: {100*(add_fortuna[a]/fortuna[a] - 1):.2f}%')
else:
  print('Os artistas da primeira semana não tiveram aumento do lucro na segunda semana!')

fortuna = {**fortuna, **add_fortuna, **new_fortuna}
print('\nEsta é a fortuna atual dos artistas considerados:')
for a in fortuna:
  print(f'{a}: R$ {fortuna[a]:.2f}')

if new_fortuna:
  print('\nNa semana 2 tivemos vendas de novos artistas no mercado:')
  for a in new_fortuna:
    print(f'{a} - Discos vendidos: {vendas[a]}')
else:
  print('\nNa semana 2 não tivemos vendas de novos artistas no mercado!')

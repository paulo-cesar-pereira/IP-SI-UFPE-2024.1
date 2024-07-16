# Uso de join em dicionário. Uso de zip para somar listas.
# Uso de sorted() para criar uma lista ordenada de chaves de um dicionário, segundo determinado critério.

info_dis, info_art = {}, {input(): [0, 0], input(): [0, 0]}
print(f"Bem-vindo(a) à 'Sergio Bieber's Disco Shop'!\nE os artistas de hoje são {' e '.join(info_art)}!")
for a in info_art:
  disco = input()
  while disco != 'acabou':
    info_dis[disco] = [a, 1, float(input())]
    disco = input()

print('-----COMEÇO DO EXPEDIENTE!-----')
disco = input()
while disco != 'FIM':
  if disco in info_dis:
    print(f'{disco} vendido')
    a = info_dis[disco][0]
    info_art[a] = [x+y for x, y in zip(info_art[a], info_dis[disco][1:])]
    ap, ag = sorted(info_art, key=lambda x: info_art[x][0])
    if ((info_art[ag][0]-info_art[ap][0])%3 == 0) and (info_art[ag][0] > info_art[ap][0]):
      print(f'A diferença está ficando muito grande! AUMENTA R$4 DE {ag.upper()} E ABAIXA R$4 DE {ap.upper()}!')
      for d in info_dis:
        if info_dis[d][0] == ag:
          info_dis[d][2] += 4
        else:
          info_dis[d][2] = (info_dis[d][2] >= 5)*(info_dis[d][2] - 5) + 1
  else:
    print('Parece que não temos esse disco...')
  disco = input()
print('-----FIM DO EXPEDIENTE!-----')

ap, ag = sorted(info_art, key=lambda x: info_art[x][1])
print(f'O total de receita gerado foi de {info_art[ap][1]+info_art[ag][1]} e foram vendidos {info_art[ap][0]+info_art[ag][0]} discos.')
if info_art[ap][1]+info_art[ag][1] == 0:
  print('Que tristeza! Só artista péssimo...')
elif info_art[ap][1] == info_art[ag][1]:
  print('Difícil de escolher o melhor!')
else:
  print(f'O artista que mais gerou dinheiro para a loja foi {ag}, acumulando uma receita de {info_art[ag][1]} e vendendo {info_art[ag][0]} discos.')

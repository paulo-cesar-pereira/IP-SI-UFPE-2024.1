# Usos de update e get em dicionários.

pt_art = {'João Gomes':0, 'Zé Vaqueiro':0, 'Raphaela Santos':0, 'Alceu Valença':0, 'Priscila Senna':0}
mus_art = {a: ('', 0) for a in pt_art}

for i in range(int(input())):
  cidade, idade = input(), 2024 - int(input())
  if cidade == 'Recife':
    print('A veneza brasileira foi consultada nesta pesquisa!')
  elif cidade == 'Olinda':
    print('Uma honra ver que a primeira capital pernambucana foi consultada!')
  elif cidade == 'Petrolina':
    print('Ansioso para descobrir a opinião dos petrolinenses!')
    
  info = [input().split(' - ') for i in range(3)]
  mus_art.update({x[0]: (x[1], int(x[2])) for x in info if int(x[2]) > mus_art[x[0]][1]})
  pt_art.update({x[0]: pt_art[x[0]] + idade//(1+info.index(x)) + int(x[2]) for x in info})

vencedor = max(pt_art, key=pt_art.get)
if vencedor == 'João Gomes':
  print('Parabéns, João Gomes, o novo fenômeno da música pernambucana!')
elif vencedor == 'Zé Vaqueiro':
  print('Zé Vaqueiro, o astro do forró, agora brilha como o rei da música pernambucana!')
elif vencedor == 'Raphaela Santos':
  print('Raphaela Santos, a voz marcante, agora é a rainha da música pernambucana!')
elif vencedor == 'Alceu Valença':
  print('Alceu Valença, o ícone da MPB, agora é o gigante da música pernambucana!')
else:
  print('Priscila Senna, a rainha da sofrência, é a mais nova estrela da música pernambucana!')

print(f'O fenômeno é {vencedor}, que canta a música {mus_art[vencedor][0]}, já contando com mais de {mus_art[vencedor][1]} milhões de visualizações na internet.')

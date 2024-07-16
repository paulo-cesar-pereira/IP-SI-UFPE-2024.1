# Usos de pop, values, items e enumerate em dicionários.
# Usos de set e | para criar e unir conjuntos.

info_gen = {'Samba': ["Preciso Me Encontrar", "O Mundo É Um Moinho", "Trem Das Onze", "O Que É O Que É?", "Disritmia", "Timoneiro"],
            'Rock Nacional': ["Epitáfio", "Meu Novo Mundo", "À Sua Maneira", "Que País É Este", "Um Minuto Para O Fim Do Mundo", "Infinita Highway"],
            'Rock': ["Smells Like Teen Spirit", "In The End", "Californication", "Welcome To The Jungle", "Another Brick In The Wall", "Bohemian Rapsody", "Bring Me To Life", "Paint It, Black", "Stairway To Heaven"],
            'Pop': ["As It Was", "Viva La Vida", "Someone Like You", "Blinding Lights", "Maps", "Talking To The Moon", "Believer", "Ghost", "Wake Me Up", "Rude", "Perfect"],
            'MPB': ["O Descobridor Dos Sete Mares", "Anunciação", "Exagerado", "João E Maria", "Sujeito De Sorte", "Naquela Mesa", "Eduardo E Mônica", "Lanterna Dos Afogados", "Metamorfose Ambulante"],
            'Manguebeat': ["Da Lama Ao Caos", "A Praieira", "Maracatu Atômico", "Manguetown", "Um Sonho", "A Cidade"],
            'Indie Folk': ["Ends Of The Earth", "Welcome Home, Son", "Riptide", "Father And Son", "Ho Hey", "The Night We Met", "Budapest", "Atlantis"],
            'Forró': ["Xote Das Meninas", "Xote Da Alegria", "Deus Me Proteja", "Numa Sala De Reboco", "Meu Cenário", "Colo De Menina", "Riacho Do Navio"]}
n_gen, info_mus = {g: 0 for g in info_gen}, {m: g for g in info_gen for m in info_gen[g]}

mus_recom, nome, N =  [], input(), int(input())
if N:
  for i in range(N):
    n_gen[info_mus.pop(input())] += 1
  
  o_gen = {g: i for i, n in enumerate(reversed(sorted(set(n_gen.values())|{0})[1:])) for g in n_gen if n_gen[g]==n}
  for g, i in o_gen.items():
    mus_recom += [m for m in info_gen[g] if m in info_mus][:(2-i)*(i<3)+1]
  if mus_recom:
    print(f'{nome} escutou {N} música(s) e estas são as próximas recomendações:\n')
    for i, m in enumerate(mus_recom):
      print(f'{i+1}. {m}')
  else:
    gen = [g for g in n_gen if n_gen[g]>0]
    print(f"{nome} já escutou todas as músicas disponíveis no(s) gênero(s): {' e '.join([', '.join(gen[:-1])]*any(gen[:-1]) + gen[-1:])}. Infelizmente não sobrou nenhuma música disponível para recomendação.")
else:
  print(f'Parece que {nome} não escutou nenhuma música. Vamos recomendar algumas músicas de gêneros diferentes:\n')
  for i, g in enumerate(n_gen):
    print(f'{i+1}. {info_gen[g][0]}')

# Uso de zip() para criar uma iteração de tuplas a partir de listas

nomes = ['Abbey Road', 'The Dark Side of the Moon', 'Riot!', 'Fearless', 'Da Lama ao Caos', 'Gal Costa', 'Sim', 'As 20 Melhores', 'O Melhor de Dominguinhos', 'Alucinação', 'Samba Esquema Novo']
artistas = ['The Beatles', 'Pink Floyd', 'Paramore', 'Taylor Swift', 'Chico Science e Nação Zumbi', 'Gal Costa', 'Vanessa da Mata', 'Luiz Gonzaga', 'Dominguinhos', 'Belchior', 'Jorge Ben Jor']
anos = ['1969', '1973', '2007', '2008', '1994', '1969', '2007', '2004', '2013', '1976', '1963']
generos = ['Rock', 'Rock', 'Rock', 'Pop', 'Manguebeat', 'MPB', 'MPB', 'Forró', 'Forró', 'MPB', 'Samba']
lista_albuns = list(zip(nomes, artistas, anos, generos))

entrada = input()
while entrada != 'FIM':
  if entrada == 'CONSULTAR':
    consulta = input()
    albuns = [album for album in lista_albuns if consulta == album[3]]
    if albuns:
      print(f'Nessa galeria há {len(albuns)} albuns de {consulta}. Os albuns encontrados foram:')
      for album in albuns:
        print(f'- {album[0]} do/da artista/banda {album[1]} lançado em {album[2]}')
    else:
      print('Você vai precisar adicionar um novo álbum ao catálogo! Não encontramos nenhum álbum desse estilo musical!')
  else:
    lista_albuns += [(entrada, input(), input(), input())]
    print(f'Este foi o novo álbum adicionado:\n- {lista_albuns[-1][0]} do/da artista/banda {lista_albuns[-1][1]} lançado em {lista_albuns[-1][2]}')
    if not any(lista_albuns[-1][3] in album for album in lista_albuns[:-1]):
      print('Oba, você adicionou um novo estilo musical ao catálogo!')
  entrada = input()

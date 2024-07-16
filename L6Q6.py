# Uso de try/except para quando se tenta acessar uma chave que não está no dicionário.

pt_mus = {'sweetener': {"no tears left to cry": 0, "the light is coming": 0, "better off": 0, "everytime": 0},
          'thank u, next': {"NASA": 0, "thank u, next": 0, "break up with your girlfriend, i'm bored": 0, "bad idea": 0},
          'Positions': {"motive": 0, "safety net": 0, "nasty": 0, "pov": 0},
          'eternal sunshine': {"yes, and?": 0,"eternal sunshine": 0, "the boy is mine": 0, "we can't be friends": 0}}
pt_alb, info_mus = {a: 0 for a in pt_mus}, {m: a for a in pt_mus for m in pt_mus[a]}

def decifra(s):
  return chr(ord(s) - (3 - (ord(s.lower()) < ord('d'))*26)*s.isalpha())

limite = int(input())
while info_mus:
  try:
    mus, nyeahs = input().split(' - ')# Aqui pode ter ValueError
    mus = "".join(map(decifra, mus))
    print(f'O nome da música decifrada é: {mus}')
    
    alb = info_mus[mus]# Aqui pode ter KeyError
    print(f'Ótimo! A música está na discografia da nossa base de dados!\nO album da música decifrada é {alb}')
    
    nyeahs = int(nyeahs)
    if nyeahs <= 5:
      print('A diva do pop não se empolgou nessa e decepcionou os arianators.')
    elif nyeahs < 10:
      print('Ariana fez o dever de casa e entregou uma música na média para os seus fãs.')
    else:
      print('AVISA QUE ESSA JÁ É HIT NOS CHARTS!')
    
    pt_mus[alb][mus] += nyeahs
    pt_alb[alb] += nyeahs
    if pt_alb[alb] >= limite:
      print(f'Atenção! O limite de pontuação foi atingido pelo álbum {alb}!')
      info_mus = {}
  except KeyError:
    print('Poxa, essa música não está na discografia da base do nosso estúdio!')
  except ValueError:
    info_mus = {}

alb = max(pt_alb, key=pt_alb.get)
print(f'Fim da análise!\n\nO álbum da estrela Ariana Grande com a maior pontuação foi {alb}, com um total de {pt_alb[alb]} pontos!')
mus = max(pt_mus[alb], key=pt_mus[alb].get)
print(f'Entre todas as faixas desse álbum, a melhor pontuada foi {mus}, que obteve {pt_mus[alb][mus]} pontos')

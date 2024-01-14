# -*- coding: utf-8 -*-
# Desafio DIO.ipynb

# 1 - Desafio Classificador de nível de Herói 🎯

print("Bem vindo!")
print("--------------------------------")
NomeDeHeroi = input("Digite o nome do herói:")
print("Qual o nível de XP do herói? de 0 a 10000")
NivelXP = int(input("Digite o nível de XP do herói:"))
print("--------------------------------")


if NivelXP <= 1000:
    NivelXP = "Ferro"

elif 1001 == NivelXP >=2000:
    NivelXP = "Bronze"

elif 2001 == NivelXP >= 5000:
    NivelXP = "Prata"

elif  5001 == NivelXP >= 7000:
    NivelXP = "Ouro"

elif 7001 == NivelXP >= 8000:
  NivelXP = "Platina"

elif 8001 == NivelXP >= 9000:
    NivelXP = "Ascendente"

elif 9001 == NivelXP >= 10000:
  NivelXP = "Imortal"

elif NivelXP >= 10000:
    NivelXP = "Radiante"


print("O Herói de nome", NomeDeHeroi, "está no nível de ", NivelXP)



#  2 - Calculadora de partidas Rankeadas 🎯


print("Bem vindo!")
print("--------------------------------")
vitorias = int(input("Digite o número de vitórias:"))
derrotas = int(input("Digite o número de derrotas:"))
print("--------------------------------")

def saldoVitorias (vitorias, derrotas):
  return vitorias - derrotas

Nivel = saldoVitorias(vitorias, derrotas)

if vitorias < 10:
  vitorias = "Ferro"
elif 11 >= vitorias <= 20:
  vitorias = "Bronze"
elif  21 >= vitorias <=  50:
  vitorias =  "Prata"
elif 51 >= vitorias <= 80:
  vitorias =  "Ouro"
elif  81 >= vitorias <= 90:
  vitorias =  "Diamante"
elif 91 >= vitorias <=  100:
  vitorias =  "Lendário"
elif vitorias >= 101:
  vitorias = "Imortal"

print("O Herói tem de saldo de ", vitorias, " e está no nível ", Nivel)



# 3 - Escrevendo as classes de um Jogo 🎯

print("Bem vindo!")
print("--------------------------------")
nome = input("Digite o nome do herói: ")
idade = int(input("Digite a idade do herói: "))
print("Qual o tipo de herói? guerreiro, mago, monge ou ninja")
tipo = str(input("Digite o tipo do herói:"))
print("--------------------------------")

while(tipo != "guerreiro") and (tipo != "mago") and (tipo  != "monge") and (tipo  != "ninja"):
  print("Tipo de herói incorreto, por favor escolha entre as opções: guerreiro, mago, monge ou ninja")
  tipo = str(input("Digite o tipo do herói:"))

else:
  if   tipo == "guerreiro":
        ataque = "a espada"

  elif tipo == "mago":
      ataque = "magia"

  elif tipo == "monge":
        ataque = "artes marciais"

  elif tipo == "ninja":
        ataque =  "shuriken"


print( "O", tipo, "atacou usando", ataque)

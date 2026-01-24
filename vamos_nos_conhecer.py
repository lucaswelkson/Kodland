import random as r
resposta = 0
# Surpreenda seus colegas!
my_list = [
    "hobby = arte, assistir e jogar (estou começando no ramo de speedruns)",
    "jogo favorito = plants vs zombies",
    "idade = 14",
    "fini favorito = fini de bananaaa",
    "bebida favorita = água",
    "inicial de crush = j",
    "época favorita da vida = 2020",
    "filme favorito do studio ghibli = entregas da kiki",
    "quant. irmãos = 1",
    "amigos do coração = 6",
    "primeira platina de jogo = henry stickmin",
    "console favorito = xbox 360 (meu primeiro console)"
    
]

print("bem-vindo ao melhor (e mais interessante) cassino de fatos aleatórios sobre o programador, edição 4512!")
print("gire a roleta apertando o botão r do seu teclado")
resposta = input("vai logo, seu tonto")

while True:
    if resposta == "r":
        print(r.choice(my_list))
    else:
        print("aperta r, seu tonto!")
    resposta = input("vai logo, seu tonto")
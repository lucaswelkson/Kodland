meme_dict = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "STALKEAR": "Investigar a vida de alguém online",
    "SYBAU": "Mandar alguém grossamente se voltar a ficar em silêncio, o famoso 'cala a boca'"
    "GG": "'Bom jogo', ou 'boa jogada'"
    "RNG": "Random Number Generator (Gerador de Números Aleatórios)"
    "BL": "Eu só sei disso por causa de uma amiga dorameira, é um tipo de fanfic... só saiba disso mesmo."
    "TS": "As vezes pode ser 'essa coisa', outras 'essa *palavra feia*', mas se refere a algo"
    "🥀": "Significa perda, lamento, normalmente utilizado de forma irônica, mas também pode ser de forma genuína"
    "BFDI": "Battle For Dream Island, uma série inovadora de 2010 muito culturalmente importante para internet, principalmente pro nicho de fãs, a chamada Object Show Community"
    "Fandom": "'Fan' significa 'fã'. 'Dom' é uma abreviação para 'domínio', então um 'domínio de fãs', um grupo de fãs."
    "YT": "Significa na maioria 'Youtube'"
}

word = input("Digite uma palavra moderna que você não entende (em letras maiúsculas): ")

if word in meme_dict:
    print("Significado:", meme_dict[word])
else:
    print("Essa palavra não está no dicionário.")
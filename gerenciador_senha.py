print("=== Gerador de Senhas Infinito ===")

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print("Caracteres disponíveis para a senha:")
print(caracteres)

senhas_geradas = []

while True:
    print("")
    print("--- Gerar Nova Senha ---")
    print("")
    
    comprimento = input("Digite o comprimento da senha que deseja gerar: ")
    
    senha_gerada = ""
    import random
    
    comprimento_int = int(comprimento)
    
    for i in range(comprimento_int):
        caractere_aleatorio = random.choice(caracteres)
        senha_gerada = senha_gerada + caractere_aleatorio
    
    print("")
    print(f"✅ Senha gerada: {senha_gerada}")
    print(f"📏 Comprimento: {comprimento} caracteres")
    
    senhas_geradas.append(senha_gerada)
    
    print("")
    resposta = input("Digite True para ver todas as suas senhas ou False para continuar gerando: ")
    
    if resposta == "True":
        print("")
        print("=" * 50)
        print("📋 SUAS SENHAS GERADAS")
        print("=" * 50)
        print("")
        
        if len(senhas_geradas) == 0:
            print("Nenhuma senha foi gerada ainda.")
        else:
            print(f"Total de senhas geradas: {len(senhas_geradas)}")
            print("")
            print("-" * 40)
            
            for i, senha in enumerate(senhas_geradas, 1):
                print(f"🔐 SENHA {i}:")
                print(f"   {senha}")
                print(f"   Caracteres: {len(senha)}")
                print("-" * 40)
        
        print("")
        print("Voltando ao gerador...")
        print("")
    
    else:
        print("")
        print("Continuando a gerar senhas...")
        print("")
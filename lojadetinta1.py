print("=================")
print(" TINTAS M&N N&M")
print("=================")
print("[1] TINTAS DE GALÃO\n[2] TINTAS DE AMOSTRA\n[3] PAPEL DE PAREDE\n[4] SAIR ")

escolha = int(input("\nEscolha a opção que deseja entrar: "))
if escolha == 1:
    
    
    #Cores de tinta Vermelhas
    print("\n=================")
    print("CORES DISPONÍVEIS")
    print("=================")
    cores = int(input("\n[1]Vermelho\n[2]Azul\n[3]Amarelo\n[4]SAIR "))
    if cores == 1:
        print("\nOPÇÕES DISPONÍVEIS DE VERMELHO")
        print("[1]Coral\n[2]Vermelho Bebê\n[3]Vermelho Fogo\n[4] SAIR")
        escolha2 = int(input("\nEscolha a opção que deseja comprar: "))
        if escolha2 == 1:
            print("O Preço dessa cor é de R$ 50,00 o litro")
            litros_tinta= int(input("Quantos litros de tinta deseja?"))
            valor_tinta= litros_tinta * 50
            print(f"Sua compra deu o valor de {valor_tinta}R$")
            
        if escolha2 == 2:
            print("O Preço dessa cor é de R$ 50,00 o litro")
            litros_tinta= int(input("Quantos litros de tinta deseja?"))
            valor_tinta= litros_tinta * 50
            print(f"Sua compra deu o valor de {valor_tinta}R$")
        if escolha2 == 3:
            print("O Preço dessa cor é de R$ 50,00 o litro")
            litros_tinta= int(input("Quantos litros de tinta deseja?"))
            valor_tinta= litros_tinta * 50
            print(f"Sua compra deu o valor de {valor_tinta}R$")
        if escolha2 == 4:
            print("Obrigado por nos visitar, tenha um bom dia!!")

    #Cores de tinta Azuis
    
    if cores == 2:
        print("\nOPÇÕES DISPONÍVEIS DE AZUIS")
        print("[1]Azul Sideral\n[2]Azul Fantasma\n[3]Azul Paraíso Escondido\n[4] SAIR")
        escolha3 = int(input("\nEscolha a opção que deseja comprar: "))
        if escolha3 == 1:
            print("O Preço dessa cor é de R$ 50,00 o litro")
            litros_tinta= int(input("Quantos litros de tinta deseja?"))
            valor_tinta= litros_tinta * 50
            print(f"Sua compra deu o valor de {valor_tinta}R$")
        if escolha3 == 2:
            print("O Preço dessa cor é de R$ 50,00 o litro")
            litros_tinta= int(input("Quantos litros de tinta deseja?"))
            valor_tinta= litros_tinta * 50
            print(f"Sua compra deu o valor de {valor_tinta}R$")
        if escolha3 == 3:
            print("O Preço dessa cor é de R$ 50,00 o litro")
            litros_tinta= int(input("Quantos litros de tinta deseja?"))
            valor_tinta= litros_tinta * 50
            print(f"Sua compra deu o valor de {valor_tinta}R$")
        if escolha3 == 4:
            print("Obrigado por nos visitar, tenha um bom dia!!")  

    #Cores de tinta Amarelas
    if cores == 3:
        print("\nOPÇÕES DISPONÍVEIS DE AMAMRELO")
        print("[1]Amarelo Dandelion\n[2]Amarelo Blonde\n[3]Amarelo Fire\n[4] SAIR")
        escolha4 = int(input("\nEscolha a opção que deseja comprar: "))
        if escolha4 == 1:
            print("O Preço dessa cor é de R$ 50,00 o litro")
            litros_tinta= int(input("Quantos litros de tinta deseja?"))
            valor_tinta= litros_tinta * 50
            print(f"Sua compra deu o valor de {valor_tinta}R$")
        if escolha4 == 2:
            print("O Preço dessa cor é de R$ 50,00 o litro")
            litros_tinta= int(input("Quantos litros de tinta deseja?"))
            valor_tinta= litros_tinta * 50
            print(f"Sua compra deu o valor de {valor_tinta}R$")
        if escolha4 == 3:
            print("O Preço dessa cor é de R$ 50,00 o litro")
            litros_tinta= int(input("Quantos litros de tinta deseja?"))
            valor_tinta= litros_tinta * 50
            print(f"Sua compra deu o valor de {valor_tinta}R$")
        if escolha4 == 4:
            print("Obrigado por nos visitar, tenha um bom dia!!")

    if cores == 4:
         print("Obrigado por nos visitar, tenha um bom dia!!")

# tintas de amostras 
if escolha == 2:
    print("\nAMOSTRAS DE TINTAS\n")
    print("CORES DISPONÍVEIS: ")
    print("\n[1]Vermelho\n[2]Azul\n[3]Amarelo\n[4]Sair")
    cor_amostra= int(input("\nQual cor deseja? "))
    if cor_amostra == 4:
        print("Obrigado por nos visitar, tenha um bom dia!!")
    if cor_amostra == 1:
        print(f"Amostra vermelha, frete 10R$.")
    if cor_amostra == 2:
        print(f"Amostra azul, frete 10R$.")
    if cor_amostra == 3:
        print(f"Amostra amarelo, frete 10R$.")

#papeis de parede
if escolha ==3:
    print("\nPAPÉIS DE PAREDE\n")
    print("ESTAMPAS DISPONÍVEIS: ")
    print("\n[1]Listrado\n[2]Colorido\n[3]Geométricos\n[4]Relevo\n[5]Sair")
    papel_parede= int(input("\nQual estampa deseja comprar?"))
    if papel_parede == 1:
        metros_parede=int(input("\nQuantos metros de papel deseja? "))
        valor_parede= metros_parede * 35
        print(f"Estampa listrada, o valor de sua compra é de {valor_parede}R$.")
    if papel_parede == 2:
        metros_parede=int(input("\nQuantos metros de papel deseja? "))
        valor_parede= metros_parede * 35
        print(f"Estampa colorida, o valor de sua compra é de {valor_parede}R$.")
    if papel_parede == 3:
        metros_parede=int(input("\nQuantos metros de papel deseja? "))
        valor_parede= metros_parede * 35
        print(f"Estampa geométrica, o valor de sua compra é de {valor_parede}R$.")
    if papel_parede == 4:
        metros_parede=int(input("\nQuantos metros de papel deseja? "))
        valor_parede= metros_parede * 45
        print(f"Estampa de relevo, o valor de sua compra é de {valor_parede}R$.")
    if papel_parede == 5:
        print("Obrigado por nos visitar, tenha um bom dia!!")

if escolha == 4:
    print("Tenha um dia celestial!!")
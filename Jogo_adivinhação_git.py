import random 

def jogo_advinhacao (): 
    numero_secreto = random.randint(1,100)
    tentativas = 0

    print ("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")
    print("")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            print("")
            tentativas += 1

            if palpite < numero_secreto:
                print("O número que estou pensando é maior...")
                print("")
            elif palpite > numero_secreto:
                print("O número que estou pesando é menor...")
                print("")
            else:
                print( "Parabéns, Você adivinhou! ")
                print("")
                print( "O número era", numero_secreto, ".")
                print( "O número foi adivinhado em", tentativas, "tentativas.")
                break
        except ValueError:
            print("Por favor, digite um caracter válido.")
            print("Deve ser digitado um número entre 1 e 100.")
            print("")

if __name__ == "__main__":
    jogo_advinhacao()           
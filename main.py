import random

# Função para realizar a aposta
def fazer_aposta(dinheiro_disponivel):
    print("Bem-vindo ao jogo de apostas!")
    print("Dinheiro disponível: ${}".format(dinheiro_disponivel))

    # Obter a aposta do usuário
    aposta = float(input("Quanto você deseja apostar? $"))

    # Verificar se o valor da aposta é válido
    if aposta > dinheiro_disponivel or aposta <= 0:
        print("Aposta inválida. Tente novamente.")
        return dinheiro_disponivel

    # Escolher números da sorte
    numeros_da_sorte = [random.randint(1, 10) for _ in range(3)]

    print("Números da sorte:", numeros_da_sorte)

    # Sortear números
    numeros_sorteados = [random.randint(1, 10) for _ in range(3)]

    print("Números sorteados:", numeros_sorteados)

    # Verificar se o jogador ganhou
    if set(numeros_da_sorte) == set(numeros_sorteados):
        ganho = aposta * 3  # Se os números coincidirem, o jogador ganha três vezes a aposta
        print("Parabéns! Você ganhou ${}".format(ganho))
        dinheiro_disponivel += ganho
    else:
        print("Você perdeu ${}".format(aposta))
        dinheiro_disponivel -= aposta

    return dinheiro_disponivel

# Função principal
def main():
    dinheiro_disponivel = 100.0  # Dinheiro inicial
    continuar_jogando = True

    while continuar_jogando:
        dinheiro_disponivel = fazer_aposta(dinheiro_disponivel)

        # Verificar se o jogador quer continuar jogando
        resposta = input("Deseja fazer outra aposta? (s/n): ").lower()
        continuar_jogando = resposta == 's'

    print("Obrigado por jogar! Seu saldo final é: ${}".format(dinheiro_disponivel))

if __name__ == "__main__":
    main()
import random

# Função para realizar a aposta
def fazer_aposta(dinheiro_disponivel):
    print("Bem-vindo ao jogo de apostas!")
    print("Dinheiro disponível: ${}".format(dinheiro_disponivel))

    # Obter a aposta do usuário
    aposta = float(input("Quanto você deseja apostar? $"))

    # Verificar se o valor da aposta é válido
    if aposta > dinheiro_disponivel or aposta <= 0:
        print("Aposta inválida. Tente novamente.")
        return dinheiro_disponivel

    # Escolher números da sorte
    numeros_da_sorte = [random.randint(1, 10) for _ in range(3)]

    print("Números da sorte:", numeros_da_sorte)

    # Sortear números
    numeros_sorteados = [random.randint(1, 10) for _ in range(3)]

    print("Números sorteados:", numeros_sorteados)

    # Verificar se o jogador ganhou
    if set(numeros_da_sorte) == set(numeros_sorteados):
        ganho = aposta * 3  # Se os números coincidirem, o jogador ganha três vezes a aposta
        print("Parabéns! Você ganhou ${}".format(ganho))
        dinheiro_disponivel += ganho
    else:
        print("Você perdeu ${}".format(aposta))
        dinheiro_disponivel -= aposta

    return dinheiro_disponivel

# Função principal
def main():
    dinheiro_disponivel = 100.0  # Dinheiro inicial
    continuar_jogando = True

    while continuar_jogando:
        dinheiro_disponivel = fazer_aposta(dinheiro_disponivel)

        # Verificar se o jogador quer continuar jogando
        resposta = input("Deseja fazer outra aposta? (s/n): ").lower()
        continuar_jogando = resposta == 's'

    print("Obrigado por jogar! Seu saldo final é: ${}".format(dinheiro_disponivel))

if __name__ == "__main__":
    main()

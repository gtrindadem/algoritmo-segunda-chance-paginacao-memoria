# Guilherme Trindade Mendes
# RA: F045FB-0  Turma: CC6P12

# Robson Matheus G. Ferreira
# RA: F051AH-3  Turma: CC6P12

import random

tamanhoDaMemoria = 30 # Altere essa variavel para definir o tamanho da memoria a ser trabalhada
quantidadeDePaginasPossiveis = 50 # Altere essa variavel para definir a quantidade de páginas diferentes (ex. 4 -> Página 1, 2, 3 e 4)
quantidadeDeAlocacoesDaSimulacao = 100 # Altere essa variavel para definir o tamanho da simulação (já que é um processo infinito)

memoria = [[0, 0]] * tamanhoDaMemoria

def novaPagina():
    return [random.randrange(1, quantidadeDePaginasPossiveis + 1), 1];

def buscaNaMemoria(pagina):
    for i in range(len(memoria)):
        if memoria[i][0] == pagina[0]:
            if memoria[i][1] == 0:
                memoria[i][1] = 1
                print('ATUALIZOU BIT R')
            return True
    return False

def alocaNaMemoria(pagina):
    deuSegundaChance = verificaSegundaChance()
    if deuSegundaChance:
        alocaNaMemoria(pagina)
    else:
        memoria.append(pagina)

def verificaSegundaChance():
    if memoria[0][1] == 1:
        darSegundaChance()
        return True
    else:
        memoria.pop(0)
        return False

def darSegundaChance():
    pagina = memoria.pop(0)
    pagina[1] = 0
    memoria.append(pagina)
    print('DADA SEGUNDA CHANCE')
    print('MEMORIA', memoria)


if __name__ == "__main__" :
    print('## INICIO ##')
    print('MEMORIA', memoria)
    print('---------------------------------')

    for x in range(quantidadeDeAlocacoesDaSimulacao):
        pagina = novaPagina()
        print('NOVA PAGINA:', pagina)
        print('MEMORIA', memoria)

        bitR = buscaNaMemoria(pagina)
        if bitR:
            print('PAGINA JÁ EXISTENTE NA MEMORIA')
            print('-------------------------------------------------------------------------------')
            continue

        alocaNaMemoria(pagina)
        print('ALOCADA');
        print('MEMORIA FINAL', memoria)
        print('-------------------------------------------------------------------------------')

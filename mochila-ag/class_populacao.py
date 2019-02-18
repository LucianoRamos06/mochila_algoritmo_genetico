from class_item import Item
from class_cromossomo import Cromossomo
from random import *

class Populacao:
    cromossomos = []
    best = 0
    melhorValor = 0
    parada = 0
    qtdPopulacoes = 0
    taxaMutacao = 0.10
    tamanhoMochila = 20

    def addCromossomo(self, cromossomo):
        self.cromossomos.append(cromossomo)

    def getBest(self):
        return self.best

    def setBest(self):
        antigoBest = self.best 
        for i in range(self.getTamanhoPopulacao()):
            if(self.best == 0):
                self.best = self.cromossomos[i]
            else:    
                if(self.cromossomos[i].funcaoObjetivo() > self.best.funcaoObjetivo()):
                    self.best = self.cromossomos[i]

        if(self.best.funcaoObjetivo() > self.melhorValor):
            self.melhorValor = self.best.funcaoObjetivo()
            
        if(antigoBest != 0):
            if(antigoBest.funcaoObjetivo() == self.best.funcaoObjetivo()):
                self.parada += 1

    def getParada(self):
           return self.parada

    def gerarPopulcaoInicial(self, item1, item2, item3):
        print('Geracao da populacao inicial...')
        while self.getTamanhoPopulacao() < 4:
            cromossomoCriado = Cromossomo(item1, item2, item3)
            if(cromossomoCriado.restricao() <= 20):
                self.addCromossomo(cromossomoCriado)
            else:
                print('Cromossomo infactivel: ', cromossomoCriado.restricao())

        self.setBest()
        self.printPopulcao()

    def gerarNovaPopulacao(self):
        
        self.qtdPopulacoes += 1
        print('gerando populacao - ', self.qtdPopulacoes)

        melhores = []
        piores = []
        novaLista = []
        cromossomosAux = self.cromossomos
        metade = int(len(cromossomosAux) / 2)
        tudo = int(round(len(cromossomosAux)))

        novaLista.clear()
        melhores.clear()
        piores.clear()
        
        for i in range(tudo):
            for j in range(tudo):
                if(cromossomosAux[i].funcaoObjetivo() >  cromossomosAux[j].funcaoObjetivo()):
                    cromaux = cromossomosAux[i]
                    cromossomosAux[i] = cromossomosAux[j]
                    cromossomosAux[j] = cromaux

        for i in range(metade):
            melhores.append(cromossomosAux[i])

        cromossomosAux.reverse()
        for i in range(metade):
            piores.append(cromossomosAux[i])

        vencedorMelhor = self.determinarVencedor(melhores)
        vencedorPior = self.determinarVencedor(piores)
        
        filhos = self.fazerCrossover(vencedorMelhor, vencedorPior)

        mutacao = []
        for item  in filhos:
            mutacao.append(self.trocarPaiPorFilho(item[0], item[1]))

        self.fazerMutacao(mutacao[0], mutacao[1])

        self.setBest()

        self.printPopulcao()


        
    def fazerCrossover(self, vencedorMelhor, vencedorPior):
        print('-- iniciando crossover')
        print('entre cromossomo: {x} - cromossomo {y}'.format(x=vencedorMelhor.getGenes()[0][2], y=vencedorPior.getGenes()[0][2]))
        flag = 1
        filhoMelhor = 0
        filhoPior = 0

        while flag == 1:

            pMutacaoVencedorMelhor = (self.obterPosicaoMutacao(len(vencedorMelhor.getGenes())) - 1)
            pMutacaoVencedorPior = (self.obterPosicaoMutacao(len(vencedorPior.getGenes())) - 1)

            print('-- posicao troca melhor: ', pMutacaoVencedorMelhor)
            print('-- posicao troca pior: ', pMutacaoVencedorPior)

            filhoMelhor = vencedorMelhor
            filhoPior = vencedorPior

            if(pMutacaoVencedorMelhor == pMutacaoVencedorPior):
                valorAux = filhoMelhor.getGenes()[pMutacaoVencedorMelhor]
                filhoMelhor.getGenes()[pMutacaoVencedorMelhor] = filhoPior.getGenes()[pMutacaoVencedorMelhor]
                filhoPior.getGenes()[pMutacaoVencedorMelhor] = valorAux
            else:
                valorAux = filhoMelhor.getGenes()[pMutacaoVencedorMelhor]
                filhoMelhor.getGenes()[pMutacaoVencedorMelhor] = filhoPior.getGenes()[pMutacaoVencedorMelhor]
                filhoPior.getGenes()[pMutacaoVencedorMelhor] = valorAux

                valorAux = filhoPior.getGenes()[pMutacaoVencedorPior]
                filhoPior.getGenes()[pMutacaoVencedorPior] = filhoMelhor.getGenes()[pMutacaoVencedorPior]
                filhoMelhor.getGenes()[pMutacaoVencedorPior] = valorAux

            if(filhoMelhor.restricao() <= 20 and filhoPior.restricao() <= 20):
                flag = 0
            else:
                print('cromossomos infactives')

        return [[vencedorMelhor, filhoMelhor], [vencedorPior, filhoPior]]

    def fazerMutacao(self, cromossomoA, cromossomoB):
        print('-- iniciando Mutacao')
        percent = self.obterPoncentagem()
        flag = 1

        while flag == 1:
            if(percent <= self.taxaMutacao):
                print('Ocorre mutacao, taxa = ', percent)
                pVencedorMutacao = self.obterPosicaoMutacao(2)
                vencedorMutacao = 0
                
                if(pVencedorMutacao == 1):
                    vencedorMutacao = cromossomoA
                else:
                    vencedorMutacao = cromossomoB

                pMutacao = (self.obterPosicaoMutacao(len(vencedorMutacao.getGenes())) - 1)
                novoValor = int(round(randint(0, vencedorMutacao.getGenes()[pMutacao][0].qtd)))
                valorAnterior = vencedorMutacao.getGenes()[pMutacao][1]
                vencedorMutacao.setGene(pMutacao, novoValor)
                
                print("cromossomo vencedor: ", vencedorMutacao.getGenes()[0][2])
                print("posicao mutacao: ", pMutacao)
                print("valor mutacao: ", novoValor)
                
                if(vencedorMutacao.restricao() > self.tamanhoMochila):
                    print('mutacao gerou neuronio infactivel')
                    vencedorMutacao.setGene(pMutacao, valorAnterior)
                else:
                    flag = 0
            else:
                print('Nao ocorre mutacao, taxa = ', percent)
                flag = 0


    def getTamanhoPopulacao(self):
        return len(self.cromossomos)

    def obterPorcentagemValor(self, total, parcela):
        return (parcela / total)

    def obterPosicaoMutacao(self, qtd):
        percent = self.obterPoncentagem()
        percentItem = (100 / qtd) / 100

        for i in range(qtd):
            if(((i+1) * percentItem) >= percent ):
                return (i+1) 
        
    def obterPoncentagem(self):
        return (randint(0, 100) / 100)

    def determinarVencedor(self, lista):
        percent = self.obterPoncentagem()
        
        cromossomosPercent = []
        valor = 0
        valorPercent = 0
        
        for item in lista:
            valor += item.funcaoObjetivo()

        for item in lista:
            itemPercent = self.obterPorcentagemValor(valor, item.funcaoObjetivo())
            cromossomosPercent.append([item, 
            valorPercent, (itemPercent + valorPercent)])
            
            valorPercent += (itemPercent + 0.001)

        for item in cromossomosPercent:
            if(percent >= item[1] and percent <= item[2]):
                return item[0]


    def trocarPaiPorFilho(self, pai, filho):
        for idx, item in enumerate(self.cromossomos):
            if(pai == item):
                self.cromossomos[idx] = filho
                return self.cromossomos[idx]

    def printPopulcao(self):

        for item in self.cromossomos:
            item.printCromossomo()
        
        print("melhor valor atual: ", self.best.funcaoObjetivo())
        print("melhor valor: ", self.melhorValor)
        print("")

        
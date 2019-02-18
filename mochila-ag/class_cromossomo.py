from random import *

class Cromossomo:

    def __init__(self, item1, item2, item3):
        self.genes = []
        self.genes.clear()
        qtdItem = self.obterQuantidade(item1)
        self.genes.append([item1, qtdItem, randint(0, 10000)])
        qtdItem = self.obterQuantidade(item2)
        self.genes.append([item2, qtdItem, randint(0, 10000)])
        qtdItem = self.obterQuantidade(item3)
        self.genes.append([item3, qtdItem, randint(0, 10000)])

    def funcaoObjetivo(self):
        funObjetivo = 0
        for item in self.genes:
            funObjetivo += item[1] * item[0].valor
        
        return funObjetivo

    def restricao(self):
        restricao = 0
        for item in self.genes:
            restricao += item[1] * item[0].peso

        return restricao

    def getGenes(self):
        return self.genes

    def setGene(self, pos, valor):
        self.genes[pos][1] += ((-self.genes[pos][1]) + valor)

    #criar populacao inicial

    def obterPoncentagem(self):
        return (randint(0, 100) / 100)

    def obterQuantidade(self, item):
        percent = self.obterPoncentagem()
        percentItem = (100 / (item.qtd + 1)) / 100
        qtdItem = 0

        for i in range(item.qtd + 1):
            if(((qtdItem + 1) * percentItem) >= percent ):
                return qtdItem
            else:
                qtdItem = qtdItem + 1 

    def printCromossomo(self):
            texto = ""
            texto += 'index:  {index} |  '.format(index=self.genes[0][2])
            for item in self.genes:
                texto += 'nome:  {nome} |  '.format(nome=item[0].nome)
                texto += 'qtd: {qtd}  |  '.format(qtd=item[1])

            texto += 'restricao: {rest}  |  '.format(rest=self.restricao())
            texto += 'F.O. : {fo}   |  '.format(fo=self.funcaoObjetivo())

            print('----------------------------------------------------------')
            print(texto)

    
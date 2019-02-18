from random import *

class Item:
    def __init__(self, nome, qtd, valor, peso):
        self.nome = nome
        self.qtd = qtd
        self.valor = valor
        self.peso = peso
     
    def getNome(self):
        return self.nome
     
    def getQtd(self):
        return self.qtd
     
    def getValor(self):
        return self.valor
         
    def getPeso(self):
        return self.peso

    def obterQuantidadeAleatoria(self):
        percent = self.obterPoncentagem()
        percentItem = (100 / (self.qtd + 1)) / 100
        qtdItem = 0

        for i in range(self.qtd + 1):
            if(((qtdItem + 1) * percentItem) >= percent ):
                return qtdItem
            else:
                qtdItem = qtdItem + 1

    def obterPoncentagem(self):
        return (randint(0, 100) / 100) 
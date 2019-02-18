from class_item import Item
from class_populacao import Populacao

populacao = Populacao()
item1 = Item('item 1', 3, 40, 3)
item2 = Item('item 2', 2, 100, 2)
item3 = Item('item 3', 3, 50, 5)

#criando populacao inicial
populacao.gerarPopulcaoInicial(item1, item2, item3)

while populacao.getParada() < 50:
    populacao.gerarNovaPopulacao()

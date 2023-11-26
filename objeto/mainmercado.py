from classes import Carrinhodecompra,Produto


carrinho=Carrinhodecompra()

p1=Produto('iphone',15570)
p2=Produto('camisa',520)
p3=Produto('Creatina',10000)
p4=Produto('camisa social',17000)
p5=Produto('teclado game',72050)

carrinho.inserir_product(p1)
carrinho.inserir_product(p2)
carrinho.inserir_product(p3)
carrinho.inserir_product(p4)
carrinho.lista_produtos()
carrinho.deleteitem(p1)
# print(carrinho.soma_total())
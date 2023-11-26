
from banco2 import Banco
from pessoaaa import Pessoa

bn=Banco('brasil',2222)
p1=Pessoa('alice',26,'feminino',5621)
bn.depositar2(200)
bn.saque(100)
bn.versaldo()
bn.saque(100)
bn.versaldo()

bn.depositar2(100)
bn.versaldo()
print("======" *20)
p1.depositar2(100)
p1.versaldo()
p1.detalhes()
p1.saque(100)
p1.versaldo()
p1.detalhes()
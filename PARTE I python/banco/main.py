from cp  import ContaPoupanca
from contacorre  import ContaCorrente

cp=ContaPoupanca(1111,2222,0)

cp.depositar(1000)
print()
print()
cp.sacar(500)
print()
print()
cp.sacar(500)
print()
print()
cp.sacar(500)
print("#########################################")

cp1 = ContaCorrente(agencia=3331,conta= 22212,saldo=0,limite=500)

cp1.depositar(100)
print()
print()


cp1.sacar(250)





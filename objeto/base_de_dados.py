
 # metodos public,privat,protected

"""public = pode acessar tudo da variavel da class
   privat= ele priva a variavel  com o simbolo  _  (então não acesse)
   protected= protege contra qualquer mudança exe: variavel dados = __dados = protected
"""



class BaseDeDados:
    
    def __init__(self):
        self.dados={}
    

    def inserirclient(self,id,nome):
        if 'clientes' not in self.dados:
            self.dados['clientes']={id:nome}
        else:
            self.dados['clientes'].update({id:nome})    
    def list_client(self):
        for id,nome in self.dados['clientes'].items(): 
         print(id,nome)
    def deleteClient(self,id):
        del self.dados['clientes'][id]

bd=BaseDeDados()


bd.inserirclient(1,'Maria oliveira')
bd.inserirclient(2,'Maria joaquina')
bd.inserirclient(3,'Alice Maria')
bd.inserirclient(4,'Thaleson silva')
bd.inserirclient(5,'Aracy silva')
bd.inserirclient(6,'Oliveira de Carvalho')
bd.inserirclient(7,'Jõao Luiz')
bd.list_client()
bd.deleteClient(1)
bd.list_client()
bd.deleteClient(2)
bd.deleteClient(6)
bd.deleteClient(7)
bd.list_client()


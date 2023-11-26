class MinhaLista:
    def __init__(self) :
        self._itemns=[]
        self._index=0

        
    def add(self,valor):
        self._itemns.append(valor)


    def __iter__(self):
        return self 


    def __next__(self):

        try: 
           item=self._itemns[self._index]
           self._index +=1
           return item
        except IndexError:
            raise StopIteration
    

    def __str__(self) :
       return f'{self.__class__.__name__}({self._itemns})'
    

if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('alice')
    lista.add('aracy')
    lista.add('josi')

    for i in lista :
      print(i)

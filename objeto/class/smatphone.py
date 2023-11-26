from eletronicos import Eletronicos
from log import LogMixin

class Smarthphone(Eletronicos,LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            erro=f'{self._nome} não esta ligado'
            print(erro)
            self.log_error(erro)
            return

        if self._conectado:
            info = f'{self._nome} ja esta conectado'
            print(info)
            self.log_info(info)
            return
        
        info=f'{self._nome}  esta conectado'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            erro=f'{self._nome } não esta conectado'
            print(erro)
            self.log_error(erro)
            return
        
        info=f'{self._nome} foi desligado'
        print(info)
        self.log_info(info)
        self._conectado = False

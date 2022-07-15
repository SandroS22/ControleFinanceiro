from Controler.controlador_receita import ControladorReceita
from Controler.controlador_categoria import ControladorCategoria
from View.tela_sistema import TelaSistema
from Controler.controlador_carteira import ControladorCarteira
from Controler.controlador_despesa import ControladorDespesa


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_carteira = ControladorCarteira(self)
        self.__controlador_despesa = ControladorDespesa(self)
        self.__controlador_receita = ControladorReceita(self)
        self.__controlador_categoria = ControladorCategoria(self)

    def tela_opcoes(self):
        while True:
            op = self.__tela_sistema.tela_opcoes()
            if op == 1:
                self.__controlador_carteira.opcoes_carteira()
            elif op == 2:
                self.__controlador_receita.opcoes_receita()
            elif op == 3:
                self.__controlador_despesa.opcoes_despesa()
            elif op == 4:
                self.__controlador_categoria.opcoes_categoria()
            elif op == 0:
                break

    def iniciar(self):
        c = self.tela_opcoes()

from controlador_receita import ControladorReceita
from controlador_categoria import ControladorCategoria
from View.tela_sistema import TelaSistema
from controlador_carteira import ControladorCarteira
from controlador_despesa import ControladorDespesa


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_carteira = ControladorCarteira()
        self.__controlador_despesa = ControladorDespesa()
        self.__controlador_receita = ControladorReceita()
        self.__controlador_categoria = ControladorCategoria()

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
                return

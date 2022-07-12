from controlador_carteira import ControladorCarteira
from controlador_despesa import ControladorDespesa
from controlador_receita import ControladorReceita
from controlador_categoria import ControladorCategoria
from View.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_carteira = ControladorCarteira()
        self.__controlador_despesa = ControladorDespesa()
        self.__controlador_receita = ControladorReceita()
        self.__controlador_categoria = ControladorCategoria()

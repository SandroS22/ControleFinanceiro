from View.tela_carteira import TelaCarteira
from Model.carteira import Carteira
from controlador_sistema import ControladorSistema


class ControladorCarteira:
    def __init__(self):
        self.__controlador_sistema = ControladorSistema()
        self.__tela_carteira = TelaCarteira()
        self.__carteiras = []

    @property
    def carterias(self):
        return self.__carteiras

    def inclui_carteira(self):
        dados = self.__tela_carteira.nova_carteira()
        carteira = Carteira(dados['nome'], ['codigo'])
        self.__carteiras.append(carteira)

    def exclui_carteira(self):
        cod = self.__tela_carteira.selecionar()
        for i in self.__carteiras:
            if i.codigo == cod:
                self.__carteiras.remove(i)
            else:
                self.__tela_carteira.mostra_mensagem('Carteira inexistente')

    def listar_carteiras(self):
        if len(self.__carteiras) == 0:
            self.__tela_carteira.mostra_mensagem('Lista vazia')
        else:
            for i in self.__carteiras:
                self.__tela_carteira.mostra_mensagem(i.nome)

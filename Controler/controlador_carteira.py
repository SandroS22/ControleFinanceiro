from View.tela_carteira import TelaCarteira
from Model.carteira import Carteira


class ControladorCarteira:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_carteira = TelaCarteira()
        self.__carteiras = []

    def inclui_carteira(self):
        dados = self.__tela_carteira.pega_dados_carteira()
        carteira = Carteira(dados['nome'], ['codigo'])
        self.__carteiras.append(carteira)

    def exclui_carteira(self):
        nome = self.__tela_carteira.pega_dados_carteira()
        for i in self.__carteiras:
            if i.codigo == nome:
                self.__carteiras.remove(i)
            else:
                return 'Carteira inexistente'

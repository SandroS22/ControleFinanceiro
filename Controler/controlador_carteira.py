from View.tela_carteira import TelaCarteira
from Model.carteira import Carteira


class ControladorCarteira:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_carteira = TelaCarteira()
        self.__carteiras = []

    @property
    def carteiras(self):
        return self.__carteiras

    def inclui_carteira(self):
        dados = self.__tela_carteira.nova_carteira()
        carteira = Carteira(dados['nome'], dados['codigo'])
        self.__carteiras.append(carteira)

    def opcoes_carteira(self):
        while True:
            op = self.__tela_carteira.tela_opcoes()
            if op == 1:
                self.inclui_carteira()
            elif op == 2:
                self.exclui_carteira()
            elif op == 3:
                self.listar_carteiras()
            elif op == 0:
                break

    def exclui_carteira(self):
        if len(self.__carteiras) == 0:
            self.__tela_carteira.mostra_mensagem('Lista vazia')
        else:
            self.listar_carteiras()
            c = self.pega_carteira()
            for i in self.__carteiras:
                if i == c:
                    self.__carteiras.remove(i)

    def listar_carteiras(self):
        if len(self.__carteiras) == 0:
            self.__tela_carteira.mostra_mensagem('Lista vazia')
        else:
            for i in self.__carteiras:
                self.__tela_carteira.mostra_mensagem(i.nome + ' ' + str(i.codigo))
                self.__tela_carteira.mostra_mensagem('')

    def pega_carteira(self):
        x = self.__tela_carteira.selecionar()
        for i in self.__carteiras:
            if i.codigo == x:
                return i
            else:
                self.__tela_carteira.mostra_mensagem('Carteira inexistente')

from Model.receita import Receita
from View.tela_receita import TelaRceita


class ControladorReceita:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_receita = TelaRceita()

    def opcoes_receita(self):
        while True:
            x = self.__tela_receita.tela_opcoes()
            if x == 1:
                self.inclui_receita()
            elif x == 2:
                self.lista_receita()
            elif x == 0:
                break

    def inclui_receita(self):
        carteira = self.__controlador_sistema.controlador_carteira.pega_carteira()
        categoria = self.__controlador_sistema.controlador_categoria.pega_categoria()
        dados_receita = self.__tela_receita.pega_dados_receita()
        receita = Receita(carteira, dados_receita['valor'],
                          dados_receita['descricao'], categoria,
                          dados_receita['codigo'])
        carteira.receitas.append(receita)

    def lista_receita(self):
        self.__controlador_sistema.controlador_carteira.listar_carteiras()
        carteira = self.__controlador_sistema.controlador_carteira.pega_carteira()
        if len(carteira.despesas) == 0:
            self.__tela_receita.mostra_mensagem('Lista vazia')
        else:
            for i in carteira.despesas:
                self.__tela_receita.mostra_mensagem(i.descricao + ' ' + str(i.codigo))

    def total_receitas(self):
        carteira = self.__controlador_sistema.controlador_carteira.pega_carteira()
        total = 0
        for i in carteira.receitas:
            total += i.valor
        self.__tela_receita.mostra_mensagem(total)

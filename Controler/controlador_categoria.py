from Model.categoria import Categoria
from View.tela_categoria import TelaCategoria


class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__categorias = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_categoria = TelaCategoria()

    def inclui_categoria(self):
        nome = self.__tela_categoria.pega_dados_categoria()
        if isinstance(nome, str):
            if nome not in self.__categorias:
                c = Categoria(nome)
                self.__categorias.append(c)
            else:
                return 'Categoria já existente'

    def exclui_categoria(self):
        nome = self.__tela_categoria.pega_dados_categoria()
        for i in self.__categorias:
            if i == nome:
                self.__categorias.remove(i)
            else:
                return 'Categoria inexistente'

    def lista_categoria(self):
        if len(self.__categorias) == 0:
            self.__tela_categoria.mostra_mensagem('Lista vazia')
        else:
            for categoria in self.__categorias:
                self.__tela_categoria.mostra_categoria(categoria.nome)

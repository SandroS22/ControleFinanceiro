from Model.categoria import Categoria
from View.tela_categoria import TelaCategoria


class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__categorias = []
        self.__tela_categoria = TelaCategoria()
        self.__controlador_sistema = controlador_sistema

    def opcoes_categoria(self):
        while True:
            op = self.__tela_categoria.tela_opcoes()
            if op == 1:
                self.inclui_categoria()
            elif op == 2:
                self.altera_categoria()
            elif op == 3:
                self.lista_categoria()
            elif op == 4:
                self.exclui_categoria()
            elif op == 0:
                break

    def altera_categoria(self):
        # TODO: Pegar dado antigo e o novo para atualizar
        x = self.__tela_categoria.pega_dados_categoria()
        for i in self.__categorias:
            i.nome = x

    def inclui_categoria(self):
        nome = self.__tela_categoria.pega_dados_categoria()
        if isinstance(nome, str):
            for i in self.__categorias:
                if i.nome == nome:
                    self.__tela_categoria.mostra_mensagem('Categoria já existe')
            else:
                c = Categoria(nome)
                self.__categorias.append(c)

    def exclui_categoria(self):
        nome = self.__tela_categoria.pega_dados_categoria()
        for i in self.__categorias:
            if i.nome == nome:
                self.__categorias.remove(i)
        else:
            self.__tela_categoria.mostra_mensagem('Categoria inexistente')

    def lista_categoria(self):
        if len(self.__categorias) == 0:
            self.__tela_categoria.mostra_mensagem('Lista vazia')
        else:
            for categoria in self.__categorias:
                self.__tela_categoria.mostra_mensagem(categoria.nome)

    def pega_categoria(self):
        if len(self.__categorias) == 0:
            self.__tela_categoria.mostra_mensagem('Lista vazia')
        else:
            self.__tela_categoria.mostra_mensagem('Insira o nome da categoria')
            cat = self.__tela_categoria.pega_dados_categoria()
            for i in self.__categorias:
                if i.nome == cat:
                    return i

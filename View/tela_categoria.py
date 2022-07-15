from View.abstract_tela import AbstractTela


class TelaCategoria(AbstractTela):
    def tela_opcoes(self):
        print("-------- Categorias ----------")
        print("Escolha a opcao")
        print("1 - Incluir Categoria")
        print("2 - Alterar Categoria")
        print("3 - Listar Categorias")
        print("4 - Excluir Categoria")
        print("0 - Retornar")
        opcao = self.le_num_inteiro('Escolha a opcao: ', [1, 2, 3, 4, 0])
        return opcao

    def mostra_categoria(self, nome):
        print('Nome da categoria: ', nome.nome)

    def pega_dados_categoria(self):
        print('-------- DADOS CATEGORIA ----------')
        nome = input('Nome: ')
        return nome

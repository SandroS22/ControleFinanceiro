from abstract_tela import AbstractTela
from random import randint


class TelaDespesa(AbstractTela):
    def tela_opcoes(self):
        print("-------- DESPESAS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Despesa")
        print("2 - Total despesas")
        print("0 - Retornar")
        opcao = self.le_num_inteiro('Escolha a opcao: ', [1, 2, 0])
        return opcao

    def pega_dados_despesa(self):
        print('-------- DADOS DESPESA ----------')
        carteira = input(self.teste_carteira('Carteira: '))
        valor = input(self.numero('Valor: '))
        descricao = input('Descricao: ')
        categoria = input(self.teste_categoria('Categoria: '))
        codigo = randint(0, 1000)
        return {'carteira': carteira, 'valor': valor, 'descricao': descricao, 'categoria': categoria, 'codigo': codigo}


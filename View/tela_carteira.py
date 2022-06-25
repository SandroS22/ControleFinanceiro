from abstract_tela import AbstractTela
from random import randint


class TelaCarteira(AbstractTela):
    def tela_opcoes(self):
        print("-------- Carteira ----------")
        print("Escolha a opcao")
        print("1 - Despesas")
        print("2 - Receitas")
        print("3 - Nova Carteira")
        print("4 - Excluir Carteira")
        print("0 - Retornar")
        opcao = self.le_num_inteiro('Escolha a opcao: ', [1, 2, 0])
        return opcao

    def pega_dados_carteira(self):
        print('-------- DADOS CARTEIRA ----------')
        nome = input('Nome: ')
        codigo = randint(0, 1000)
        return {'nome': nome, 'codigo': codigo}

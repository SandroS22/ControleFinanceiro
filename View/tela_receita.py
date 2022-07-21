from View.abstract_tela import AbstractTela
from random import randint


class TelaRceita(AbstractTela):
    def tela_opcoes(self):
        print("-------- RECEITAS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Receita")
        print("2 - Total Receitas")
        print("0 - Retornar")
        opcao = self.le_num_inteiro('Escolha a opcao: ', [1, 2, 0])
        return opcao

    def pega_dados_receita(self):
        print('-------- DADOS RECEITA ----------')
        valor = self.numero(input('Valor: '))
        descricao = input('Descricao: ')
        codigo = randint(0, 1000)
        return {'valor': valor, 'descricao': descricao, 'codigo': codigo}

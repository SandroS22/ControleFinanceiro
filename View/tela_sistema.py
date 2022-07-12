from abstract_tela import AbstractTela


class TelaSistema(AbstractTela):
    def tela_opcoes(self):
        print("-------- Categorias ----------")
        print("Escolha a opcao")
        print("1 - Carteiras")
        print("2 - Receitas")
        print("3 - Despesas")
        print("4 - Categorias")
        print("0 - Sair")
        opcao = self.le_num_inteiro('Escolha a opcao: ', [1, 2, 3, 4, 0])
        return opcao

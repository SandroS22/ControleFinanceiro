from abc import ABC
from Model.categoria import Categoria
from Model.carteira import Carteira


class AbstractTela(ABC):
    def le_num_inteiro(self, mensagem: str = '', inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print('Valor incorreto: Digite um valor numerico inteiro válido')
                if inteiros_validos:
                    print('Valores válidos: ', inteiros_validos)

    def numero(self, valor):
        try:
            numero = float(valor)
            return numero
        except:
            self.mostra_mensagem("O valor digitado é inválido.")
            return None

    def teste_categoria(self, categoria):
        while True:
            if isinstance(categoria, Categoria):
                return categoria
            else:
                self.mostra_mensagem('Categoria inválida.')
                break

    def selecionar(self):
        codigo = self.numero(input('Codigo: '))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)

    def teste_carteira(self, carteira):
        if isinstance(carteira, Carteira):
            return carteira
        else:
            self.mostra_mensagem('Carteira inválida')
            return None

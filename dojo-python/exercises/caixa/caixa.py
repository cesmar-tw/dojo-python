#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CaixaEletronico:
    """
    * Entregar o menor número de notas;
    * E possível sacar o valor solicitado com as notas disponíveis;
    * Saldo do cliente infinito;
    * Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
    * Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
    """

    def __init__(self):
        pass

    def sacar(self, valor):
        pass

    def executarSaque(self, valor):
        """ Implemente aqui o comando de saque"""
        print("Sacando R$", valor)
        self.sacar(valor)


if __name__ == '__main__':
    caixaEletronico = CaixaEletronico()
    caixaEletronico.executarSaque(10)

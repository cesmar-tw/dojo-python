#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from caixa import CaixaEletronico


class CaixaEletronicoTest(unittest.TestCase):
    """
    * Entregar o menor número de notas;
    * É possível sacar o valor solicitado com as notas disponíveis;
    * Saldo do cliente infinito;
    * Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
    * Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
    """

    def setUp(self):
        self.caixaEletronico = CaixaEletronico()

    def testMenorNumeroNotas(self):
        self.assertEquals(len(self.caixaEletronico.sacar(60)), 2)
        self.assertEquals(len(self.caixaEletronico.sacar(50)), 1)
        self.assertEquals(len(self.caixaEletronico.sacar(90)), 3)
        self.assertEquals(len(self.caixaEletronico.sacar(100)), 1)
        self.assertEquals(len(self.caixaEletronico.sacar(40)), 2)

    def testNotasDisponiveis(self):
        self.assertEquals(len(self.caixaEletronico.sacar(102)), 0)
        self.assertEquals(len(self.caixaEletronico.sacar(11)), 0)
        self.assertEquals(len(self.caixaEletronico.sacar(23)), 0)

    def testSaldoInfinito(self):
        self.assertNotEquals(len(self.caixaEletronico.sacar(100000)), 0)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from calculadora import Calculadora


class Calculadora(unittest.TestCase):
    """
    * Calculadora receber dois números e aplica o cálculo desejado.
    * Operações disponíveis:
    * - somar
    * - subtrair
    * - multiplicar
    * - dividir
    """

    def setUp(self):
        self.calculadora = Calculadora()

    def test_soma(self):
        self.assertEquals(self.calculadora.somar(1, 1), 2)

    def test_subtrair(self):
        self.assertEquals(self.calculadora.subtrair(1, 1), 0)

    def test_multiplicar(self):
        self.assertEquals(self.calculadora.multiplicar(2, 2), 4)

    def test_dividir(self):
        self.assertEquals(self.calculadora.dividir(4, 2), 2)


if __name__ == '__main__':
    unittest.main()

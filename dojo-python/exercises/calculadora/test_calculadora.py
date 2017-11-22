#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from calculadora import Calculadora


class CalculadoraTest(unittest.TestCase):
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

    def testSomar(self):
        self.assertEquals(self.calculadora.somar(1, 1), 2)

    def testSubtrair(self):
        self.assertEquals(self.calculadora.subtrair(1, 1), 0)

    def testMultiplicar(self):
        self.assertEquals(self.calculadora.multiplicar(2, 2), 4)

    def testDividir(self):
        self.assertEquals(self.calculadora.dividir(4, 2), 2)


if __name__ == '__main__':
    unittest.main()

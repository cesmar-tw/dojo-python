#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from romanos import ConversorDeNumerosRomanos


class ConversorDeNumerosRomanosTest(unittest.TestCase):

    def setUp(self):
        self.conversorDeNumerosRomanos = ConversorDeNumerosRomanos()

    def testDecimalParaRomano(self):
        self.assertEquals(self.conversorDeNumerosRomanos.decimalParaRomano(0), '')
        self.assertEquals(self.conversorDeNumerosRomanos.decimalParaRomano(1), 'I')
        self.assertEquals(self.conversorDeNumerosRomanos.decimalParaRomano(60), 'LX')
        self.assertEquals(self.conversorDeNumerosRomanos.decimalParaRomano(4), 'IV')
        self.assertEquals(self.conversorDeNumerosRomanos.decimalParaRomano(99), 'XCIX')
        self.assertEquals(self.conversorDeNumerosRomanos.decimalParaRomano(44), 'XLIV')
        self.assertEquals(self.conversorDeNumerosRomanos.decimalParaRomano(994), 'CMXCIV')

    def testDecimalParaRomano(self):
        self.assertEquals(self.conversorDeNumerosRomanos.romanosParaDecimal(''), 0) 
        self.assertEquals(self.conversorDeNumerosRomanos.romanosParaDecimal('I'), 1)
        self.assertEquals(self.conversorDeNumerosRomanos.romanosParaDecimal('LX'), 60)
        self.assertEquals(self.conversorDeNumerosRomanos.romanosParaDecimal('IV'), 4)
        self.assertEquals(self.conversorDeNumerosRomanos.romanosParaDecimal('XCIC'), 99)
        self.assertEquals(self.conversorDeNumerosRomanos.romanosParaDecimal('XLIV'), 44)
        self.assertEquals(self.conversorDeNumerosRomanos.romanosParaDecimal('CMXCIV'), 994)


if __name__ == '__main__':
    unittest.main()

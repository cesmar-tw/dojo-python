#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ConversorDeNumerosRomanos():
    """
    * Converte números decimais para romanos e vice-versa. 
    * Exemplos: 
    *      1 --> I
    *      10 --> X 
    *      7 --> VII 
    *  
    * Por definição temos I=1, V=5, X=10, L=50, C=100, D=500 e M=1000 
    * Não faremos conversão de números maiores que 3000 (os romanos não sabiam contar além disso)
    """

    def romanosParaDecimal(self, numero):
         """ Implemente aqui o comando para converter de romano para decimal"""

    def decimalParaRomano(self, numero):
        """ Implemente aqui o comando para converter de decimal para romano"""


if __name__ == '__main__':
    conversorDeNumerosRomano = ConversorDeNumerosRomano()
    conversorDeNumerosRomano.romanosParaDecimal()
    conversorDeNumerosRomano.decimalParaRomano()

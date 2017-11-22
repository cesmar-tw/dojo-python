#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Calculadora:
    """
    * Calculadora receber dois números e aplica o cálculo desejado.
    * Operações disponíveis:
    * - somar
    * - subtrair
    * - multiplicar
    * - dividir
    """
    def __init__(self):
        pass

    def somar(self, valor1, valor2):
        """ Implemente aqui a função de soma """
        print("Somando os valores a: ", valor1, " e b: ", valor2)

    def subtrair(self, valor1, valor2):
        """ Implemente aqui a função de subtração """
        print("Subtraindo o valor a: ", valor1, " de b: ", valor2)

    def multiplicar(self, valor1, valor2):
        """ Implemente aqui a função de multiplicação """
        print("Multiplicando o valor a: ", valor1, " por b: ", valor2)

    def dividir(self, valor1, valor2):
        """ Implemente aqui a função de divisão """
        print("Dividindo o valor a: ", valor1, " por b: ", valor2)


if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.somar(1, 1)
    calculadora.subtrair(1, 1)
    calculadora.multiplicar(1, 1)
    calculadora.dividir(4, 2)

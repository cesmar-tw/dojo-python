#!/usr/bin/env python
# -*- coding: utf-8 -*-


class FizzBuzz:
    """
    * Retorne as strings Fizz, Buzz ou FizzBuzz dependendo do valor da entrada;
    * Se o valor da entrada for divisível por 3, diga Fizz;
    * Se o valor da entrada for divisível por 5, diga Buzz;
    * Se o valor da entrada for divisível por 3 e por 5, diga FizzBuzz;
    * O valor de entrada é qualquer número inteiro válido;
    """

    def __init__(self):
        pass

    def ehFizz(self, valor):
        pass

    def ehBuzz(self, valor):
        pass

    def ehFizzBuzz(self, valor):
        pass

    def executar(self, valor):
        """ Implemente aqui a logica do FizzBuzz"""
        print("Executando o FizzBuzz para o valor ", valor)
        self.ehFizzBuzz(valor)


if __name__ == '__main__':
    fizzBuzz = FizzBuzz()
    fizzBuzz.executar(15)
    fizzBuzz.ehFizz(15)

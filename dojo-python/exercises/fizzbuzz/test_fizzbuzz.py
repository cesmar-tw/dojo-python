#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def setUp(self):
        self.numeros = list(range(101))
        self.fizzBuzz = FizzBuzz()

    def test_fizz(self):
        """Se o número for divisível por 3, diga Fizz"""
        self.assertTrue(self.fizzBuzz.ehFizz(self.numeros[3]))
        self.assertTrue(self.fizzBuzz.ehFizz(self.numeros[33]))
        self.assertTrue(self.fizzBuzz.ehFizz(self.numeros[66]))
        self.assertFalse(self.fizzBuzz.ehFizz(self.numeros[5]))
        self.assertFalse(self.fizzBuzz.ehFizz(self.numeros[10]))

    def test_buzz(self):
        """Se o número for divisível por 5, diga Buzz"""
        self.assertTrue(self.fizzBuzz.ehBuzz(self.numeros[5]))
        self.assertTrue(self.fizzBuzz.ehBuzz(self.numeros[55]))
        self.assertTrue(self.fizzBuzz.ehBuzz(self.numeros[65]))
        self.assertFalse(self.fizzBuzz.ehBuzz(self.numeros[3]))
        self.assertFalse(self.fizzBuzz.ehBuzz(self.numeros[33]))
        self.assertFalse(self.fizzBuzz.ehBuzz(self.numeros[93]))

    def test_fizzBuzz(self):
        """Se o número for divisível por 3 e por 5, diga FizzBuzz"""
        self.assertTrue(self.fizzBuzz.ehFizzBuzz(self.numeros[15]))
        self.assertTrue(self.fizzBuzz.ehFizzBuzz(self.numeros[30]))
        self.assertTrue(self.fizzBuzz.ehFizzBuzz(self.numeros[60]))
        self.assertFalse(self.fizzBuzz.ehFizzBuzz(self.numeros[5]))
        self.assertFalse(self.fizzBuzz.ehFizzBuzz(self.numeros[10]))
        self.assertFalse(self.fizzBuzz.ehFizzBuzz(self.numeros[100]))


if __name__ == '__main__':
    unittest.main()

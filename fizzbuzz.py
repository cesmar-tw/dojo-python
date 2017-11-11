import unittest
from FizzBuzz import isFizz, isBuzz, isFizzBuzz

class FizzBuzz(unittest.TestCase):

    def setUp(self):
        self.numbers = list(range(100))

    def test_fizz(self):
        """if number is divisible by three, say Fizz"""
        self.assertTrue(isFizz(self.numbers[3]))
        self.assertTrue(isFizz(self.numbers[33]))
        self.assertTrue(isFizz(self.numbers[66]))
        self.assertFalse(isFizz(self.numbers[0]))
        self.assertFalse(isFizz(self.numbers[5]))
        self.assertFalse(isFizz(self.numbers[10]))

    def test_buzz(self):
        """if number is divisible by five, say “Buzz"""
        self.assertTrue(isBuzz(self.numbers[5]))
        self.assertTrue(isBuzz(self.numbers[55]))
        self.assertTrue(isBuzz(self.numbers[65]))
        self.assertFalse(isBuzz(self.numbers[3]))
        self.assertFalse(isBuzz(self.numbers[33]))
        self.assertFalse(isBuzz(self.numbers[93]))
        
    def test_fizzBuzz(self):
        """if number is divisible by three AND five say FizzBuzz"""
        self.assertTrue(isFizzBuzz(self.numbers[15]))
        self.assertTrue(isFizzBuzz(self.numbers[30]))
        self.assertTrue(isFizzBuzz(self.numbers[60]))
        self.assertFalse(isFizzBuzz(self.numbers[5]))
        self.assertFalse(isFizzBuzz(self.numbers[10]))
        self.assertFalse(isFizzBuzz(self.numbers[100]))

if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python3

import sys
import unittest

from hello_world import say_hi
from io import StringIO


target = __import__("hello_world")
say_hi2 = target.say_hi


class TestHelloWorld(unittest.TestCase):
    def test_say_hi(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        say_hi()
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "Hello World!\n", 'Should'
                         'be "Hello World!\\n"')

    def test_return_hi(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        result = say_hi()
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(result, {"Hello World!\n"}, 'Should be'
                         '"Hello World!\\n"')


if __name__ == '__main__':
    unittest.main()

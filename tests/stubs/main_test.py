import unittest
from unittest.mock import MagicMock

import main

class MainTest(unittest.TestCase):

    # A Unit Test
    def test_string_length():
        testStr = "1"
        result = str_len(testStr)
        assert result == 1
import unittest

from python.eval import get_output

class TestGetOutput(unittest.TestCase):
    def test_basic_print(self):
        code = """print 'foo'
"""
        result = get_output(code)
        expected = "foo\n"
        self.assertEqual(result, expected)

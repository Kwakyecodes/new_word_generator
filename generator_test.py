###############################################################################
# TESTING GENERATOR.PY USING PYTHON UNITTEST
###############################################################################

import unittest

from generator import make_prefixes, make_suffixes, generate

class GeneratorTest(unittest.TestCase):
    def test_make_prefixes_function(self):
        self.assertEqual(make_prefixes("apple"), ["a", "ap", "app", "appl", "apple"])
        
    def test_make_prefixes_function_with_empty_string(self):
        self.assertEqual(make_prefixes(""), [])
        
    def test_make_suffixes_function(self):
        self.assertEqual(make_suffixes("grapes"), ["s", "es", "pes", "apes", "rapes", "grapes"])
        
    def test_make_suffixes_function_with_empty_string(self):
        self.assertEqual(make_suffixes(""), [])
        
    def test_generate_function(self):
        self.assertEqual(generate("apple", "grapes"), ["as", "apes", "apples"])
        
    def test_generate_function_with_empty_string(self):
        self.assertEqual(generate("", "grapes"), [])
            
            
if __name__ == "__main__":
    unittest.main()
